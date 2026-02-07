# Skill Quality Audit Rubric

Score each dimension 1-5. Total determines quality tier.

## Dimensions

### 1. Coverage (What domain knowledge is included?)

| Score | Criteria |
|-------|----------|
| 1 | Major domain areas missing, skill handles only basic cases |
| 2 | Covers common cases but misses important edge cases or sub-domains |
| 3 | Covers most domain areas, some gaps in specialized knowledge |
| 4 | Comprehensive coverage, only niche gaps remain |
| 5 | Expert-level coverage, handles edge cases and rare scenarios |

**Check:** List all tasks the skill should handle. How many does it actually cover?

### 2. Depth (Surface-level or expert-level?)

| Score | Criteria |
|-------|----------|
| 1 | Generic advice anyone could give, no domain-specific insight |
| 2 | Some domain knowledge but lacks professional-level detail |
| 3 | Solid practitioner-level knowledge, follows known best practices |
| 4 | Expert-level with nuanced decision frameworks and trade-offs |
| 5 | Master-level with mental models, anti-patterns, and contextual judgment |

**Check:** Would a domain expert find this useful, or would they say "I already know all this"?

### 3. Structure (Does it follow skill-creator best practices?)

| Score | Criteria |
|-------|----------|
| 1 | Wall of text, no clear organization |
| 2 | Some headings but inconsistent, hard to navigate |
| 3 | Clear sections, follows basic skill-creator patterns |
| 4 | Well-organized with progressive disclosure, consistent terminology |
| 5 | Optimal structure: SKILL.md < 500 lines, heavy content in references/, clear navigation |

**Check:** Can Claude find what it needs in < 3 seconds of scanning?

### 4. Actionability (Can Claude execute without guessing?)

| Score | Criteria |
|-------|----------|
| 1 | Vague guidelines, Claude must guess implementation details |
| 2 | Some procedures but key steps are ambiguous |
| 3 | Clear workflows for common cases, some ambiguity in complex cases |
| 4 | Step-by-step procedures with decision points and fallbacks |
| 5 | Precise workflows with concrete examples, error handling, and validation steps |

**Check:** Give Claude a task using this skill. Does it ask clarifying questions it shouldn't need to?

### 5. Examples (Concrete or abstract?)

| Score | Criteria |
|-------|----------|
| 1 | No examples |
| 2 | Abstract examples ("e.g., do something like X") |
| 3 | A few concrete examples for common cases |
| 4 | Concrete examples for common + edge cases, with expected outputs |
| 5 | Rich examples showing input → process → output for each workflow |

**Check:** Could a new Claude instance understand the skill purely from examples?

## Scoring

| Total | Tier | Action |
|-------|------|--------|
| 5-10 | Draft | Major rewrite needed |
| 11-15 | Working | Significant gaps to fill |
| 16-20 | Solid | Targeted improvements |
| 21-25 | Production | Minor polish only |

## Quick Assessment Template

```
SKILL: [name]
SCORES: Coverage [?] | Depth [?] | Structure [?] | Actionability [?] | Examples [?]
TOTAL: [?]/25 → [Tier]

LOWEST DIMENSIONS: [which scored lowest — prioritize these]
```
