---
name: deep-research
description: Web research with Graph-of-Thoughts for fast-changing topics. Use when user requests research, analysis, investigation, or comparison requiring current information. Features hypothesis testing, source triangulation, claim verification, Red Team, self-critique, and gap analysis. Supports Quick/Standard/Deep/Exhaustive tiers. Creative Mode for cross-industry innovation.
---

# Deep Research

Enhanced research engine for topics where training data is outdated.

## Quick Start

### Standard Mode
```
CLASSIFY → SCOPE → HYPOTHESIZE → PLAN → [PLAN PREVIEW*] → RETRIEVE
→ GAP ANALYSIS → TRIANGULATE → SYNTHESIZE → RED TEAM → SELF-CRITIQUE → PACKAGE
```
*Deep+ tier only

### Creative Mode
```
ABSTRACT → MAP (3-5 domains) → SEARCH → GENERALIZE → SYNTHESIZE
```
**Trigger:** "creative mode", "cross-industry", "what do others do"

## Classification

| Type | When | Process |
|------|------|---------|
| A | Single fact | WebSearch → Answer |
| B | Multi-fact | 3 phases |
| C | Judgment needed | 6 phases |
| D | Novel/conflicting | Full + Red Team |

## Intensity Tiers

| Tier | Sources | When |
|------|---------|------|
| Quick | 5-10 | Simple question |
| Standard | 10-20 | Multi-faceted |
| Deep | 20-30 | Novel, high stakes |
| Exhaustive | 30+ | Critical decision |

## Core Rules

### Parallel Search (MANDATORY)
```
[Single message]
WebSearch: "[topic] 2025"
WebSearch: "[topic] limitations"
WebSearch: "[topic] vs alternatives"
```

### Claim Types

| Type | Requirements |
|------|--------------|
| **C1** | Quote + 2+ sources + confidence + reasoning |
| **C2** | Citation required |
| **C3** | Cite if contested |

### Confidence Format (C1 claims)
```
**Claim:** [Statement]
**Confidence:** HIGH/MEDIUM/LOW
**Reason:** [Why]
**Sources:** [1][2]
```

### Anti-Hallucination
- Every C1 cites [N] immediately
- Use "According to [1]..."
- Admit: "No sources found for X"

## URL Fallback

If WebFetch returns 403:
```bash
curl -s --max-time 60 "https://r.jina.ai/https://example.com"
```

## Finding Details in References

| Topic | File | Grep Pattern |
|-------|------|--------------|
| Phase details | [standard-mode.md](./references/standard-mode.md) | `grep -n "^## Phase"` |
| Creative mode | [creative-mode.md](./references/creative-mode.md) | `grep -n "^## Phase C"` |
| Agent prompts | [agent-templates.md](./references/agent-templates.md) | `grep -n "^## "` |
| Progress/recovery | [progress-recovery.md](./references/progress-recovery.md) | — |
| Report template | [report_template.md](./assets/report_template.md) | — |

## Scripts

| Script | Purpose |
|--------|---------|
| `scripts/validate_report.py` | 9-check quality validation |

## Related Skills

| When | Skill |
|------|-------|
| Cross-industry innovation | `/generate-creative-ideas` |
| Technical contradiction | `/triz` |
| Explain findings | `/explain-concepts` |
| Strategic analysis | `/manage-business-strategy` |
