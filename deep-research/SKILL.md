---
name: deep-research
description: Comprehensive web research with 8-phase Graph-of-Thoughts pipeline for fast-changing topics (AI, tech, tools, pricing, benchmarks). Use when user requests research, analysis, investigation, or comparison requiring current information. Features hypothesis testing, source triangulation, claim verification, Red Team challenge, and anti-hallucination protocols. Supports Quick/Standard/Deep/Exhaustive intensity tiers. **Creative Mode** enables cross-industry research using Combinatorial Creativity Engine for innovation and novel approaches.
---

# Deep Research

Research engine with Graph-of-Thoughts for topics where training data is outdated.

## Quick Start

### Standard Mode
1. **CLASSIFY** → Type A/B/C/D
2. **SCOPE** → Boundaries + success criteria
3. **HYPOTHESIZE** → 3-5 testable hypotheses
4. **PLAN** → Search queries + source strategy
5. **RETRIEVE** → Parallel execution (ALL searches in ONE message)
6. **TRIANGULATE** → Cross-verify, assign C1/C2/C3 claims
7. **SYNTHESIZE** → Insights + SO WHAT/NOW WHAT
8. **RED TEAM** → Counter-evidence (depth 3+)
9. **PACKAGE** → Report with citations

### Creative Mode
1. **ABSTRACT** → Topic to core function
2. **MAP** → 3-5 analogous domains
3. **SEARCH** → Cross-industry parallel
4. **GENERALIZE** → Transferable principles
5. **SYNTHESIZE** → Apply to original topic

**Trigger:** "creative mode", "cross-industry", "what do others do", innovation needed

## Phase 0: Fast-Path Routing

| Type | Characteristics | Process |
|------|-----------------|---------|
| A (LOOKUP) | Single fact | WebSearch → Answer |
| B (SYNTHESIS) | Multi-fact aggregation | 3 phases |
| C (ANALYSIS) | Judgment needed | 6 phases |
| D (INVESTIGATION) | Novel/conflicting | Full 8 phases + Red Team |

**Classify BEFORE proceeding.**

## Intensity Tiers

| Tier | Sources | When |
|------|---------|------|
| Quick | 5-10 | Known answer, single source |
| Standard | 10-20 | Multi-faceted, moderate |
| Deep | 20-30 | Novel, high stakes |
| Exhaustive | 30+ | Critical decision |
| Creative | 15-25 | Cross-industry innovation |

## Parallel Search (MANDATORY)

**WRONG:** `WebSearch #1 → wait → WebSearch #2 → wait`

**CORRECT (single message):**
```
WebSearch: "AI coding tools December 2025"
WebSearch: "Claude Code vs Cursor comparison"
WebSearch: "[topic] limitations challenges"
Task(agent): Academic paper analysis
```

## Claim Types

| Type | Requirements |
|------|--------------|
| **C1 Critical** | Quote + citation + 2+ independent sources + confidence |
| **C2 Supporting** | Citation required |
| **C3 Context** | Cite if contested |

**Independence Rule:** 5 articles citing same report = ONE source.

## Confidence Levels

| Level | Criteria |
|-------|----------|
| HIGH (90%+) | 3+ A/B sources, n>1000, replicated |
| MEDIUM (60-90%) | Single strong OR multiple weaker |
| LOW (30-60%) | Preliminary, expert opinion |
| SPECULATIVE (<30%) | Single weak, theoretical |

## Anti-Hallucination

- Every C1 MUST cite [N] immediately
- Use "According to [1]..." format
- Never "research suggests..." without citation
- Admit: "No sources found for X"

## Quality Gates

| Gate | Requirement |
|------|-------------|
| Source count | Per intensity tier |
| Independence | C1 claims in 2+ independent sources |
| Recency | < 3 months for AI/tech |
| Citation coverage | Every C1 has [N] + confidence |
| Implications | Every finding has SO WHAT/NOW WHAT |

## Termination

Stop when **any 2** are true:
1. Each subquestion meets source minimums
2. Last 5 queries yield <10% new info
3. All C1 claims meet independence rule
4. Budget caps hit

## Autonomy

**Default: Proceed autonomously.** Only ask if query is incomprehensible or contradictory.

## Resources

| Resource | Purpose |
|----------|---------|
| [methodology.md](./references/methodology.md) | Full 8-phase details, Creative Mode, agent templates |
| [report_template.md](./assets/report_template.md) | Thai report structure + output format |
| `source_evaluator.py` | Credibility scoring (0-100) |
| `validate_report.py` | 9-check quality validation |

## Related Skills (Optional)

| When | Suggest |
|------|---------|
| Cross-industry innovation | `/generate-creative-ideas` - Combinatorial Engine |
| Technical contradiction found | `/triz` - systematic innovation |
| Need to explain findings | `/explain-concepts` - teach concepts |
| Strategic analysis needed | `/manage-business-strategy` - SWOT, Porter's |
| Business model research | `/design-business-model` - BMC, Lean Canvas |

**Note:** These skills are optional. Deep-research works standalone for fact-finding.
