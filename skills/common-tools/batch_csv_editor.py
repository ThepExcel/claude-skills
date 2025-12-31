#!/usr/bin/env python3
"""
Batch CSV Editor - Efficient bulk updates to all_functions_reference.csv

FEATURES:
- Update specific columns (post_id, has_json, quality_score, etc.)
- Batch operations: update multiple functions at once
- Dry-run mode: preview changes before applying
- Filter by program, category, slug patterns
- Atomic operations: write all-or-nothing

USAGE:
  # Update post_id for a single function
  python3 batch_csv_editor.py --set post_id=37434 --where slug=record-field --program power-query --dry-run

  # Mark all functions in a category as having JSON
  python3 batch_csv_editor.py --set has_json=True --where category=list-functions --program power-query --dry-run

  # Update quality score for functions matching pattern
  python3 batch_csv_editor.py --set quality_score=85.5 --where-regex "^Record\." --program power-query --dry-run

  # Flag functions for re-upload
  python3 batch_csv_editor.py --set needs_reupload=True --where post_id="" --program excel --dry-run

  # Batch update multiple columns
  python3 batch_csv_editor.py --set has_json=True quality_score=90 --where slug=sum --program excel --dry-run

  # Commit changes (remove --dry-run)
  python3 batch_csv_editor.py --set post_id=37434 --where slug=record-field --program power-query --commit
"""

import csv
import sys
import re
import argparse
from pathlib import Path
from typing import Dict, List, Optional, Tuple
from datetime import datetime
import shutil


class BatchCSVEditor:
    """Batch update tool for functions registry CSV."""

    def __init__(self, csv_path: str = None):
        """Initialize CSV editor."""
        if csv_path is None:
            csv_path = Path(__file__).parent.parent / "functions" / "all_functions_reference.csv"

        self.csv_path = Path(csv_path)
        self.rows = []
        self.headers = []

        if not self.csv_path.exists():
            raise FileNotFoundError(f"CSV not found: {self.csv_path}")

        self._load_csv()

    def _load_csv(self):
        """Load CSV into memory."""
        with open(self.csv_path, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            self.headers = reader.fieldnames
            self.rows = list(reader)

    def _backup_csv(self) -> Path:
        """Create backup of CSV before writing."""
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        backup_path = self.csv_path.parent / f"{self.csv_path.stem}_backup_{timestamp}{self.csv_path.suffix}"
        shutil.copy2(self.csv_path, backup_path)
        return backup_path

    def _parse_where_clause(self, where_str: str, is_regex: bool = False) -> Tuple[str, str]:
        """Parse where clause like 'slug=record-field'."""
        if '=' not in where_str:
            raise ValueError(f"Invalid where clause: {where_str}. Use format: column=value")

        column, value = where_str.split('=', 1)
        column = column.strip()
        value = value.strip()

        if column not in self.headers:
            raise ValueError(f"Unknown column: {column}. Available: {', '.join(self.headers)}")

        return column, value

    def _matches_filter(self, row: Dict, filters: Dict, regex_filters: Dict) -> bool:
        """Check if row matches all filters."""
        for column, value in filters.items():
            if row.get(column, '').strip() != value:
                return False

        for column, pattern in regex_filters.items():
            if not re.search(pattern, row.get(column, ''), re.IGNORECASE):
                return False

        return True

    def _parse_set_clause(self, set_args: List[str]) -> Dict[str, str]:
        """Parse set clauses like ['post_id=37434', 'has_json=True']."""
        updates = {}

        for arg in set_args:
            if '=' not in arg:
                raise ValueError(f"Invalid set clause: {arg}. Use format: column=value")

            column, value = arg.split('=', 1)
            column = column.strip()
            value = value.strip()

            if column not in self.headers:
                raise ValueError(f"Unknown column: {column}. Available: {', '.join(self.headers)}")

            updates[column] = value

        return updates

    def batch_update(
        self,
        updates: Dict[str, str],
        where_filters: Dict[str, str],
        where_regex_filters: Dict[str, str],
        program_filter: Optional[str] = None,
        category_filter: Optional[str] = None,
        dry_run: bool = True
    ) -> Dict:
        """Perform batch update with filters."""

        # Add program filter if specified
        if program_filter:
            program_filter = program_filter.strip().lower()
            where_filters['program'] = program_filter

        if category_filter:
            category_filter = category_filter.strip().lower()
            where_filters['category'] = category_filter

        # Find matching rows
        matching_rows = []
        for idx, row in enumerate(self.rows):
            if self._matches_filter(row, where_filters, where_regex_filters):
                matching_rows.append(idx)

        if not matching_rows:
            return {
                'status': 'no_matches',
                'matched': 0,
                'updated': 0,
                'changes': []
            }

        # Build changes
        changes = []
        for idx in matching_rows:
            row_changes = {}
            for column, value in updates.items():
                old_value = self.rows[idx].get(column, '')
                if old_value != value:
                    row_changes[column] = {
                        'old': old_value,
                        'new': value
                    }

            if row_changes:
                changes.append({
                    'row_index': idx,
                    'slug': self.rows[idx].get('slug', 'UNKNOWN'),
                    'changes': row_changes
                })

        # Apply changes if not dry-run
        if not dry_run and changes:
            for change in changes:
                idx = change['row_index']
                for column, new_value in updates.items():
                    self.rows[idx][column] = new_value

            # Write back to CSV
            backup = self._backup_csv()
            with open(self.csv_path, 'w', newline='', encoding='utf-8') as f:
                writer = csv.DictWriter(f, fieldnames=self.headers)
                writer.writeheader()
                writer.writerows(self.rows)

        return {
            'status': 'success',
            'matched': len(matching_rows),
            'updated': len(changes),
            'changes': changes,
            'dry_run': dry_run,
            'backup': str(self._backup_csv()) if not dry_run and changes else None
        }

    def get_column_stats(self, column: str, program: Optional[str] = None) -> Dict:
        """Get statistics for a column."""
        if column not in self.headers:
            raise ValueError(f"Unknown column: {column}")

        values = {}
        for row in self.rows:
            if program:
                if row.get('program', '').strip().lower() != program.strip().lower():
                    continue

            value = row.get(column, '').strip()
            if value not in values:
                values[value] = 0
            values[value] += 1

        return {
            'column': column,
            'total_rows': len(self.rows) if not program else sum(1 for r in self.rows if r.get('program', '').strip().lower() == program.strip().lower()),
            'unique_values': len(values),
            'value_counts': dict(sorted(values.items(), key=lambda x: x[1], reverse=True))
        }


def main():
    """CLI interface for batch CSV editor."""
    parser = argparse.ArgumentParser(
        description='Batch update all_functions_reference.csv',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog='''
Examples:
  # Dry-run: update post_id
  python3 batch_csv_editor.py --set post_id=37434 --where slug=record-field --program power-query --dry-run

  # Commit: mark functions as having JSON
  python3 batch_csv_editor.py --set has_json=True --where category=list-functions --program power-query --commit

  # Update multiple columns
  python3 batch_csv_editor.py --set has_json=True quality_score=90 --where slug=sum --program excel --dry-run

  # Find all empty post_ids
  python3 batch_csv_editor.py --stats post_id --program excel

  # Flag unpublished functions
  python3 batch_csv_editor.py --set needs_reupload=True --where post_id= --program dax --dry-run
        '''
    )

    parser.add_argument(
        '--set',
        nargs='+',
        help='Columns to set (e.g., post_id=37434 has_json=True)'
    )

    parser.add_argument(
        '--where',
        help='Filter condition (e.g., slug=record-field)'
    )

    parser.add_argument(
        '--where-regex',
        help='Regex filter condition (e.g., "^Record\.")'
    )

    parser.add_argument(
        '--program',
        help='Filter by program (excel, power-query, dax, google-sheets)'
    )

    parser.add_argument(
        '--category',
        help='Filter by category'
    )

    parser.add_argument(
        '--dry-run',
        action='store_true',
        default=False,
        help='Preview changes without applying (default)'
    )

    parser.add_argument(
        '--commit',
        action='store_true',
        help='Apply changes (requires explicit flag)'
    )

    parser.add_argument(
        '--stats',
        help='Show statistics for a column'
    )

    parser.add_argument(
        '--csv-path',
        default=None,
        help='Custom path to CSV file'
    )

    args = parser.parse_args()

    try:
        editor = BatchCSVEditor(args.csv_path)
    except FileNotFoundError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

    # Stats mode
    if args.stats:
        try:
            stats = editor.get_column_stats(args.stats, args.program)
            print(f"\nColumn: {stats['column']}")
            print(f"Total rows: {stats['total_rows']}")
            print(f"Unique values: {stats['unique_values']}")
            print("\nValue counts:")
            for value, count in stats['value_counts'].items():
                if value == '':
                    value = '(empty)'
                print(f"  {value}: {count}")
        except ValueError as e:
            print(f"Error: {e}", file=sys.stderr)
            sys.exit(1)
        sys.exit(0)

    # Batch update mode
    if not args.set:
        parser.print_help()
        sys.exit(0)

    # Parse filters
    where_filters = {}
    where_regex_filters = {}

    if args.where:
        try:
            column, value = editor._parse_where_clause(args.where)
            where_filters[column] = value
        except ValueError as e:
            print(f"Error: {e}", file=sys.stderr)
            sys.exit(1)

    if args.where_regex:
        # Parse regex filter: format is "column~pattern"
        if '~' not in args.where_regex and '=' in args.where_regex:
            # Allow format "column=pattern" for regex
            column, pattern = args.where_regex.split('=', 1)
            column = column.strip()
        else:
            parts = args.where_regex.split('~')
            if len(parts) != 2:
                print("Error: Regex format should be 'column=pattern'", file=sys.stderr)
                sys.exit(1)
            column, pattern = parts

        if column not in editor.headers:
            print(f"Error: Unknown column: {column}", file=sys.stderr)
            sys.exit(1)

        where_regex_filters[column] = pattern

    # Parse set clauses
    try:
        updates = editor._parse_set_clause(args.set)
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

    # Perform update
    dry_run = not args.commit
    try:
        result = editor.batch_update(
            updates=updates,
            where_filters=where_filters,
            where_regex_filters=where_regex_filters,
            program_filter=args.program,
            category_filter=args.category,
            dry_run=dry_run
        )
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

    # Print results
    print()
    if result['status'] == 'no_matches':
        print("No matching rows found.")
    else:
        print(f"Matched: {result['matched']} functions")
        print(f"Changes: {result['updated']} functions would be updated")

        if result['changes']:
            print("\nPreview of changes:")
            for change in result['changes'][:10]:  # Show first 10
                print(f"\n  {change['slug']}:")
                for column, values in change['changes'].items():
                    print(f"    {column}: {values['old']!r} -> {values['new']!r}")

            if len(result['changes']) > 10:
                print(f"\n  ... and {len(result['changes']) - 10} more")

        if dry_run:
            print("\n⚠️  DRY-RUN MODE - No changes applied")
            print("Run with --commit flag to apply changes")
        else:
            print(f"\n✅ Changes committed! Backup: {result['backup']}")

    print()


if __name__ == '__main__':
    main()
