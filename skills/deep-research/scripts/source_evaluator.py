#!/usr/bin/env python3
"""
Source Credibility Evaluator
Assesses source quality, credibility, and potential biases.
No external dependencies - uses Python stdlib only.

Usage:
    python source_evaluator.py --url "https://example.com" --title "Article Title"
    python source_evaluator.py --url "https://arxiv.org/abs/2401.12345" --title "Research Paper" --date "2024-01-15"
"""

from dataclasses import dataclass
from typing import Dict, Optional
from urllib.parse import urlparse
from datetime import datetime, timedelta
import argparse
import re
import json


@dataclass
class CredibilityScore:
    """Represents source credibility assessment"""
    overall_score: float  # 0-100
    domain_authority: float
    recency: float
    expertise: float
    bias_score: float  # higher = more neutral
    factors: Dict[str, str]
    recommendation: str  # high_trust, moderate_trust, low_trust, verify


class SourceEvaluator:
    """Evaluates source credibility and quality"""

    # Domain reputation tiers
    HIGH_AUTHORITY_DOMAINS = {
        # Academic & Research
        'arxiv.org', 'nature.com', 'science.org', 'cell.com', 'nejm.org',
        'ieee.org', 'acm.org', 'pubmed.ncbi.nlm.nih.gov', 'scholar.google.com',

        # Government & International
        'nih.gov', 'cdc.gov', 'who.int', 'fda.gov', 'nasa.gov',
        'gov.uk', 'europa.eu', 'un.org',

        # Official Documentation
        'docs.python.org', 'developer.mozilla.org', 'docs.microsoft.com',
        'cloud.google.com', 'aws.amazon.com', 'kubernetes.io',
        'docs.anthropic.com', 'platform.openai.com',

        # Reputable News (fact-check verified)
        'reuters.com', 'apnews.com', 'bbc.com', 'economist.com',
    }

    MODERATE_AUTHORITY_DOMAINS = {
        # Tech News & Analysis
        'techcrunch.com', 'theverge.com', 'arstechnica.com', 'wired.com',
        'zdnet.com', 'cnet.com', 'thenextweb.com',

        # Industry Publications
        'forbes.com', 'bloomberg.com', 'wsj.com', 'ft.com',

        # Educational
        'wikipedia.org', 'britannica.com', 'khanacademy.org',

        # Tech Community (established)
        'medium.com', 'dev.to', 'stackoverflow.com', 'github.com',
        'hackernews.com', 'lobste.rs',
    }

    LOW_AUTHORITY_INDICATORS = [
        'blogspot.com', 'wordpress.com', 'wix.com', 'substack.com',
        'tumblr.com', 'weebly.com', 'squarespace.com',
    ]

    def evaluate_source(
        self,
        url: str,
        title: str,
        content: Optional[str] = None,
        publication_date: Optional[str] = None,
        author: Optional[str] = None
    ) -> CredibilityScore:
        """Evaluate source credibility"""
        domain = self._extract_domain(url)

        # Calculate component scores
        domain_score = self._evaluate_domain_authority(domain)
        recency_score = self._evaluate_recency(publication_date)
        expertise_score = self._evaluate_expertise(domain, title, author)
        bias_score = self._evaluate_bias(domain, title, content)

        # Weighted average
        overall = (
            domain_score * 0.35 +
            recency_score * 0.20 +
            expertise_score * 0.25 +
            bias_score * 0.20
        )

        factors = self._identify_factors(
            domain, domain_score, recency_score, expertise_score, bias_score
        )
        recommendation = self._generate_recommendation(overall)

        return CredibilityScore(
            overall_score=round(overall, 2),
            domain_authority=round(domain_score, 2),
            recency=round(recency_score, 2),
            expertise=round(expertise_score, 2),
            bias_score=round(bias_score, 2),
            factors=factors,
            recommendation=recommendation
        )

    def _extract_domain(self, url: str) -> str:
        """Extract domain from URL"""
        parsed = urlparse(url)
        domain = parsed.netloc.lower().replace('www.', '')
        return domain

    def _evaluate_domain_authority(self, domain: str) -> float:
        """Evaluate domain authority (0-100)"""
        if domain in self.HIGH_AUTHORITY_DOMAINS:
            return 90.0
        if domain in self.MODERATE_AUTHORITY_DOMAINS:
            return 70.0
        if any(ind in domain for ind in self.LOW_AUTHORITY_INDICATORS):
            return 40.0
        # Unknown domain - moderate skepticism
        return 55.0

    def _evaluate_recency(self, publication_date: Optional[str]) -> float:
        """Evaluate information recency (0-100)"""
        if not publication_date:
            return 50.0  # Unknown date

        try:
            # Handle various date formats
            for fmt in ['%Y-%m-%d', '%Y-%m', '%Y', '%d/%m/%Y', '%m/%d/%Y']:
                try:
                    pub_date = datetime.strptime(publication_date, fmt)
                    break
                except ValueError:
                    continue
            else:
                return 50.0

            age = datetime.now() - pub_date

            if age < timedelta(days=90):  # < 3 months
                return 100.0
            elif age < timedelta(days=365):  # < 1 year
                return 85.0
            elif age < timedelta(days=730):  # < 2 years
                return 70.0
            elif age < timedelta(days=1825):  # < 5 years
                return 50.0
            else:
                return 30.0
        except Exception:
            return 50.0

    def _evaluate_expertise(
        self,
        domain: str,
        title: str,
        author: Optional[str]
    ) -> float:
        """Evaluate source expertise (0-100)"""
        score = 50.0

        # Academic/research domains
        if any(d in domain for d in ['arxiv', 'nature', 'science', 'ieee', 'acm']):
            score += 30

        # Government/official sources
        if '.gov' in domain or 'who.int' in domain:
            score += 25

        # Technical documentation
        if 'docs.' in domain or 'documentation' in title.lower():
            score += 20

        # Author credentials
        if author:
            if any(cred in author.lower() for cred in ['dr.', 'phd', 'professor', 'prof.']):
                score += 15

        return min(score, 100.0)

    def _evaluate_bias(
        self,
        domain: str,
        title: str,
        content: Optional[str]
    ) -> float:
        """Evaluate potential bias (0-100, higher = more neutral)"""
        score = 70.0

        # Sensationalism indicators in title
        sensational = [
            '!', 'shocking', 'unbelievable', "you won't believe",
            'secret', "they don't want you to know", 'breaking',
            'exclusive', 'urgent', 'must read'
        ]
        title_lower = title.lower()
        if any(ind in title_lower for ind in sensational):
            score -= 20

        # Academic sources are typically less biased
        if any(d in domain for d in ['arxiv', 'nature', 'science', 'ieee']):
            score += 20

        # Balanced language in content
        if content:
            balanced = ['however', 'although', 'on the other hand', 'critics argue', 'alternatively']
            if any(ind in content.lower() for ind in balanced):
                score += 10

        return min(max(score, 0), 100.0)

    def _identify_factors(
        self,
        domain: str,
        domain_score: float,
        recency_score: float,
        expertise_score: float,
        bias_score: float
    ) -> Dict[str, str]:
        """Identify key credibility factors"""
        factors = {}

        if domain_score >= 85:
            factors['domain'] = "High authority domain"
        elif domain_score <= 45:
            factors['domain'] = "Low authority - verify claims"

        if recency_score >= 85:
            factors['recency'] = "Recent information"
        elif recency_score <= 40:
            factors['recency'] = "Outdated - verify currency"

        if expertise_score >= 80:
            factors['expertise'] = "Expert source"
        elif expertise_score <= 45:
            factors['expertise'] = "Limited expertise indicators"

        if bias_score >= 80:
            factors['bias'] = "Balanced perspective"
        elif bias_score <= 50:
            factors['bias'] = "Potential bias detected"

        return factors

    def _generate_recommendation(self, overall_score: float) -> str:
        """Generate trust recommendation"""
        if overall_score >= 80:
            return "high_trust"
        elif overall_score >= 60:
            return "moderate_trust"
        elif overall_score >= 40:
            return "low_trust"
        else:
            return "verify"


def main():
    parser = argparse.ArgumentParser(
        description="Evaluate source credibility",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python source_evaluator.py --url "https://arxiv.org/abs/2401.12345" --title "AI Research"
  python source_evaluator.py --url "https://blog.example.com/post" --title "Blog Post" --date "2024-01-15"
        """
    )

    parser.add_argument('--url', '-u', required=True, help='Source URL')
    parser.add_argument('--title', '-t', required=True, help='Source title')
    parser.add_argument('--date', '-d', help='Publication date (YYYY-MM-DD)')
    parser.add_argument('--author', '-a', help='Author name')
    parser.add_argument('--json', action='store_true', help='Output as JSON')

    args = parser.parse_args()

    evaluator = SourceEvaluator()
    score = evaluator.evaluate_source(
        url=args.url,
        title=args.title,
        publication_date=args.date,
        author=args.author
    )

    if args.json:
        result = {
            'overall_score': score.overall_score,
            'domain_authority': score.domain_authority,
            'recency': score.recency,
            'expertise': score.expertise,
            'bias_score': score.bias_score,
            'recommendation': score.recommendation,
            'factors': score.factors
        }
        print(json.dumps(result, indent=2))
    else:
        print(f"\nSource: {args.title}")
        print(f"URL: {args.url}")
        print(f"\nOverall Score: {score.overall_score}/100")
        print(f"  Domain Authority: {score.domain_authority}")
        print(f"  Recency: {score.recency}")
        print(f"  Expertise: {score.expertise}")
        print(f"  Bias Score: {score.bias_score}")
        print(f"\nRecommendation: {score.recommendation.upper()}")
        if score.factors:
            print(f"Factors: {score.factors}")


if __name__ == '__main__':
    main()
