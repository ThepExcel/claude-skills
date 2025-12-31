#!/usr/bin/env python3
"""
Research Report Validator
Ensures reports meet quality standards before delivery.
No external dependencies - uses Python stdlib only.

Usage:
    python validate_report.py --report path/to/report.md
    python validate_report.py --report report.md --strict
"""

import argparse
import re
import sys
from pathlib import Path
from typing import List


class ReportValidator:
    """Validates research report quality"""

    def __init__(self, report_path: Path, strict: bool = False):
        self.report_path = report_path
        self.strict = strict
        self.content = self._read_report()
        self.errors: List[str] = []
        self.warnings: List[str] = []

    def _read_report(self) -> str:
        """Read report file"""
        try:
            with open(self.report_path, 'r', encoding='utf-8') as f:
                return f.read()
        except Exception as e:
            print(f"ERROR: Cannot read report: {e}")
            sys.exit(1)

    def validate(self) -> bool:
        """Run all validation checks"""
        print(f"\n{'='*60}")
        print(f"VALIDATING: {self.report_path.name}")
        print(f"{'='*60}\n")

        checks = [
            ("Executive Summary", self._check_executive_summary),
            ("Required Sections", self._check_required_sections),
            ("Citations", self._check_citations),
            ("Bibliography", self._check_bibliography),
            ("Placeholder Text", self._check_placeholders),
            ("Content Truncation", self._check_truncation),
            ("Word Count", self._check_word_count),
            ("Source Count", self._check_source_count),
            ("Broken References", self._check_broken_references),
        ]

        for check_name, check_func in checks:
            print(f"Checking: {check_name}...", end=" ")
            passed = check_func()
            print("PASS" if passed else "FAIL")

        self._print_summary()
        return len(self.errors) == 0

    def _check_executive_summary(self) -> bool:
        """Check executive summary exists and is 50-250 words"""
        # Match both English and Thai headers
        patterns = [
            r'##\s*(Executive Summary|สรุปผู้บริหาร|สรุป)(.*?)(?=##|\Z)'
        ]

        for pattern in patterns:
            match = re.search(pattern, self.content, re.DOTALL | re.IGNORECASE)
            if match:
                summary = match.group(2).strip()
                word_count = len(summary.split())

                if word_count > 250:
                    self.warnings.append(f"Executive summary too long: {word_count} words (max 250)")
                if word_count < 50:
                    self.warnings.append(f"Executive summary too short: {word_count} words (min 50)")
                return True

        self.errors.append("Missing Executive Summary section")
        return False

    def _check_required_sections(self) -> bool:
        """Check all required sections are present"""
        # Support both English and Thai section headers
        required = [
            (r'(Executive Summary|สรุปผู้บริหาร|สรุป)', 'Executive Summary'),
            (r'(Introduction|บทนำ)', 'Introduction'),
            (r'(Analysis|การวิเคราะห์|Finding)', 'Main Analysis'),
            (r'(Synthesis|สังเคราะห์|ข้อมูลเชิงลึก)', 'Synthesis'),
            (r'(Limitation|ข้อจำกัด|ข้อควรระวัง)', 'Limitations'),
            (r'(Recommendation|ข้อเสนอแนะ)', 'Recommendations'),
            (r'(Bibliography|บรรณานุกรม|Sources)', 'Bibliography'),
        ]

        missing = []
        for pattern, name in required:
            if not re.search(rf'##.*{pattern}', self.content, re.IGNORECASE):
                missing.append(name)

        if missing:
            self.errors.append(f"Missing sections: {', '.join(missing)}")
            return False

        return True

    def _check_citations(self) -> bool:
        """Check citation format and presence"""
        citations = re.findall(r'\[(\d+)\]', self.content)

        if not citations:
            self.errors.append("No citations [N] found in report")
            return False

        unique = set(int(c) for c in citations)

        if len(unique) < 5:
            self.warnings.append(f"Only {len(unique)} unique sources (recommended: 10+)")

        # Check for consecutive numbers
        if unique:
            max_num = max(unique)
            expected = set(range(1, max_num + 1))
            missing = expected - unique
            if missing:
                self.warnings.append(f"Non-consecutive citations, missing: {sorted(missing)}")

        return True

    def _check_bibliography(self) -> bool:
        """Check bibliography completeness"""
        pattern = r'##\s*(Bibliography|บรรณานุกรม)(.*?)(?=##|\Z)'
        match = re.search(pattern, self.content, re.DOTALL | re.IGNORECASE)

        if not match:
            self.errors.append("Missing Bibliography section")
            return False

        bib_section = match.group(2)

        # Check for truncation placeholders (CRITICAL)
        truncation_patterns = [
            (r'\[\d+-\d+\]', 'Citation range (e.g., [8-75])'),
            (r'Additional.*citations', '"Additional citations"'),
            (r'\[Continue with', '"[Continue with"'),
            (r'\[\.\.\.', '"[..."'),
            (r'etc\.(?!\w)', 'Standalone "etc."'),
        ]

        for pattern_re, description in truncation_patterns:
            if re.search(pattern_re, bib_section, re.IGNORECASE):
                self.errors.append(f"CRITICAL: Bibliography truncation: {description}")
                return False

        # Count bibliography entries
        bib_entries = set(re.findall(r'^\[(\d+)\]', bib_section, re.MULTILINE))

        if not bib_entries:
            self.errors.append("Bibliography has no entries")
            return False

        # Find citations in text (excluding bibliography)
        text_before_bib = self.content[:match.start()]
        text_citations = set(re.findall(r'\[(\d+)\]', text_before_bib))

        # Check all citations have bibliography entries
        missing_in_bib = text_citations - bib_entries
        if missing_in_bib:
            self.errors.append(f"Citations missing from bibliography: {sorted(int(x) for x in missing_in_bib)}")
            return False

        return True

    def _check_placeholders(self) -> bool:
        """Check for placeholder text"""
        placeholders = [
            'TBD', 'TODO', 'FIXME', 'XXX',
            '[citation needed]', '[needs citation]',
            '[placeholder]', '[TODO]', '[TBD]'
        ]

        found = [p for p in placeholders if p in self.content]

        if found:
            self.errors.append(f"Found placeholder text: {', '.join(found)}")
            return False

        return True

    def _check_truncation(self) -> bool:
        """Check for content truncation patterns"""
        patterns = [
            (r'Content continues', '"Content continues"'),
            (r'Due to length', '"Due to length"'),
            (r'would continue', '"would continue"'),
            (r'\[Sections \d+-\d+', '"[Sections X-Y"'),
            (r'Additional sections', '"Additional sections"'),
        ]

        for pattern_re, description in patterns:
            if re.search(pattern_re, self.content, re.IGNORECASE):
                self.errors.append(f"CRITICAL: Content truncation: {description}")
                return False

        return True

    def _check_word_count(self) -> bool:
        """Check overall report length"""
        word_count = len(self.content.split())

        if word_count < 500:
            self.warnings.append(f"Report very short: {word_count} words")

        return True

    def _check_source_count(self) -> bool:
        """Check minimum source count"""
        pattern = r'##\s*(Bibliography|บรรณานุกรม)(.*?)(?=##|\Z)'
        match = re.search(pattern, self.content, re.DOTALL | re.IGNORECASE)

        if not match:
            return True  # Already caught in bibliography check

        bib_entries = set(re.findall(r'^\[(\d+)\]', match.group(2), re.MULTILINE))

        if len(bib_entries) < 5:
            self.warnings.append(f"Only {len(bib_entries)} sources (recommended: 10+)")

        return True

    def _check_broken_references(self) -> bool:
        """Check for broken internal references"""
        internal_links = re.findall(r'\[.*?\]\((\.\/.*?)\)', self.content)

        broken = []
        for link in internal_links:
            link_path = link.split('#')[0]
            full_path = self.report_path.parent / link_path
            if not full_path.exists():
                broken.append(link)

        if broken:
            self.warnings.append(f"Broken internal links: {', '.join(broken)}")

        return True  # Don't fail on this

    def _print_summary(self):
        """Print validation summary"""
        print(f"\n{'='*60}")
        print("VALIDATION SUMMARY")
        print(f"{'='*60}\n")

        if self.errors:
            print(f"ERRORS ({len(self.errors)}):")
            for error in self.errors:
                print(f"  - {error}")
            print()

        if self.warnings:
            print(f"WARNINGS ({len(self.warnings)}):")
            for warning in self.warnings:
                print(f"  - {warning}")
            print()

        if not self.errors and not self.warnings:
            print("ALL CHECKS PASSED\n")
        elif not self.errors:
            print("VALIDATION PASSED (with warnings)\n")
        else:
            print("VALIDATION FAILED - fix errors before delivery\n")


def main():
    parser = argparse.ArgumentParser(
        description="Validate research report quality",
        epilog="Example: python validate_report.py --report report.md"
    )

    parser.add_argument('--report', '-r', required=True, help='Path to report markdown')
    parser.add_argument('--strict', action='store_true', help='Treat warnings as errors')

    args = parser.parse_args()

    report_path = Path(args.report)
    if not report_path.exists():
        print(f"ERROR: Report file not found: {report_path}")
        sys.exit(1)

    validator = ReportValidator(report_path, strict=args.strict)
    passed = validator.validate()

    if args.strict and validator.warnings:
        passed = False

    sys.exit(0 if passed else 1)


if __name__ == '__main__':
    main()
