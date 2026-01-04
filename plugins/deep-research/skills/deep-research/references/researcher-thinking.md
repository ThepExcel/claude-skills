# THINK Protocol: Researcher Metacognition

Explicit thinking phases that mirror how skilled researchers approach problems.

## Overview

**THINK** = **T**ake Stock + **H**unt Direction + **I**nspect Gaps + **N**otice Assumptions + **K**now Limits

| Step | Core Question | When to Use |
|------|---------------|-------------|
| **T** | "What do I already know?" | Phase 1: SCOPE |
| **H** | "What do I need to find out?" | Phase 2: PLAN |
| **I** | "What am I still missing?" | Phase 3.5: GAP ANALYSIS |
| **N** | "What assumptions am I making?" | Phase 5: SYNTHESIZE |
| **K** | "What could I be wrong about?" | Phase 6: RED TEAM |

**Purpose:** Make implicit thinking explicit, reducing blind spots and improving rigor.

---

## T - Take Stock (Prior Knowledge Activation)

**When:** At SCOPE phase, before any searching

**Purpose:** Clarify what you already know vs. what you need to find out. Prevents wasted searches on known information and surfaces hidden assumptions.

### Prompts

```markdown
## Prior Knowledge Assessment

### What I Know with Confidence
Things I believe to be true and can rely on:
1. [Fact/belief] — Source: [training/user context/common knowledge]
2. [Fact/belief] — Source: [...]
3. [Fact/belief] — Source: [...]

### What I Think I Know (Needs Verification)
Beliefs that might be outdated or uncertain:
1. [Uncertain belief] — Why uncertain: [...]
2. [Uncertain belief] — Why uncertain: [...]

### What I Know I Don't Know
Explicit gaps in my knowledge:
1. [Unknown] — Why it matters: [...]
2. [Unknown] — Why it matters: [...]
3. [Unknown] — Why it matters: [...]

### What I Might Not Know I Don't Know
Potential blind spots:
1. [Possible blind spot area]
2. [Possible blind spot area]
```

### Example: Researching "Remote Work Productivity 2025"

```markdown
## Prior Knowledge Assessment

### What I Know with Confidence
1. Remote work expanded dramatically during COVID-19 (2020-2021) — Common knowledge
2. Major tech companies have various remote/hybrid policies — Training data
3. Productivity measurement is complex and debated — Training data

### What I Think I Know (Needs Verification)
1. "Most companies have settled on hybrid models" — May be outdated for 2025
2. "Remote work is here to stay" — Might have shifted

### What I Know I Don't Know
1. Current 2025 data on remote work adoption rates
2. Latest research on productivity outcomes
3. New tools/technologies affecting remote work

### What I Might Not Know I Don't Know
1. Regional variations I'm not aware of
2. Industry-specific patterns outside tech
3. Recent policy changes or regulations
```

---

## H - Hunt Direction (Question Decomposition)

**When:** At PLAN phase, after hypotheses are formed

**Purpose:** Break the core question into searchable sub-questions with clear priorities and dependencies.

### Prompts

```markdown
## Question Decomposition

### Core Question
[State the main research question]

### Sub-Questions by Type

**Factual Questions (What is?):**
1. [Question] — Priority: [High/Medium/Low]
2. [Question] — Priority: [...]

**Causal Questions (Why?):**
1. [Question] — Priority: [...]
2. [Question] — Priority: [...]

**Evaluative Questions (How good/bad?):**
1. [Question] — Priority: [...]
2. [Question] — Priority: [...]

**Predictive Questions (What will?):**
1. [Question] — Priority: [...]
2. [Question] — Priority: [...]

### Dependencies
- [Question A] must be answered before [Question B] because [...]
- [Question C] depends on [Question D]

### Priority Ranking
1. [Most critical question] — Must answer
2. [Second priority] — Should answer
3. [Third priority] — Nice to answer
```

### Example: "Is AI Coding Worth It for My Team?"

```markdown
## Question Decomposition

### Core Question
Should our development team adopt AI coding assistants?

### Sub-Questions by Type

**Factual Questions:**
1. What AI coding tools are available in 2025? — Priority: High
2. What do they cost? — Priority: High
3. What features do they offer? — Priority: Medium

**Causal Questions:**
1. Why do some teams report productivity gains? — Priority: High
2. Why do some developers resist AI tools? — Priority: Medium

**Evaluative Questions:**
1. How accurate are AI code suggestions? — Priority: High
2. What are the security implications? — Priority: High
3. How does code quality compare? — Priority: Medium

**Predictive Questions:**
1. Will AI coding become standard practice? — Priority: Low
2. How will AI coding evolve in 2-3 years? — Priority: Low

### Dependencies
- "What tools exist" must come before "which is best for us"
- "Productivity evidence" needed before "ROI calculation"

### Priority Ranking
1. Current tool landscape and capabilities
2. Productivity and quality evidence
3. Cost and implementation requirements
```

---

## I - Inspect Gaps (Mid-Research Reflection)

**When:** At GAP ANALYSIS phase, after initial retrieval

**Purpose:** Pause to assess what's been found vs. what's still needed. Prevents premature conclusions.

### Prompts

```markdown
## Gap Inspection

### Information Inventory
What I've gathered so far:
- [Finding 1] — Confidence: [High/Medium/Low]
- [Finding 2] — Confidence: [...]
- [Finding 3] — Confidence: [...]

### Coverage Check
- [ ] Sufficient data to answer core question?
- [ ] All major perspectives represented?
- [ ] Contradictions identified and understood?
- [ ] Confidence levels justified?

### Contradictions Found
1. [Source A] says [X], but [Source B] says [Y]
   - Possible explanation: [...]
   - Resolution: [Need more data / Acknowledge both / One is outdated]

### What Remains Unclear
1. [Unclear point] — Why it matters: [...]
2. [Unclear point] — Why it matters: [...]

### Most Concerning Gap
- Gap: [Description]
- Why it matters: [Impact on conclusions]
- How to address: [Specific follow-up action]

### Follow-Up Needed
Specific queries to fill gaps:
1. "[Follow-up query]" — Addresses: [gap]
2. "[Follow-up query]" — Addresses: [gap]
```

### Example: Mid-Research on AI Coding

```markdown
## Gap Inspection

### Information Inventory
- AI coding tools improve productivity 20-50% for routine tasks — Confidence: Medium
- Security concerns exist around code suggestions — Confidence: High
- Enterprise adoption growing but varies by industry — Confidence: Medium

### Coverage Check
- [x] Sufficient data to answer core question? Partially
- [x] All major perspectives represented? Missing skeptics
- [ ] Contradictions identified? Found one
- [x] Confidence levels justified? Yes

### Contradictions Found
1. GitHub claims 55% productivity boost, but academic study shows 10-20%
   - Possible explanation: Different measurement methods, different tasks
   - Resolution: Need to understand methodology differences

### Most Concerning Gap
- Gap: No data on long-term effects (>1 year usage)
- Why it matters: Short-term gains might not persist
- How to address: Search for longitudinal studies

### Follow-Up Needed
1. "AI coding productivity longitudinal study" — Addresses: long-term gap
2. "GitHub Copilot criticism developer" — Addresses: skeptic perspective
```

---

## N - Notice Assumptions (Assumption Surfacing)

**When:** At SYNTHESIZE phase, before drawing conclusions

**Purpose:** Surface hidden assumptions that could invalidate conclusions. Essential for intellectual honesty.

### Prompts

```markdown
## Assumption Audit

### My Hidden Assumptions
Beliefs underlying my analysis that I haven't questioned:

1. **Assumption:** [Statement]
   - Evidence for: [...]
   - Evidence against: [...]
   - If wrong: [Impact on conclusions]

2. **Assumption:** [Statement]
   - Evidence for: [...]
   - Evidence against: [...]
   - If wrong: [Impact on conclusions]

3. **Assumption:** [Statement]
   - Evidence for: [...]
   - Evidence against: [...]
   - If wrong: [Impact on conclusions]

### Source Assumptions
What my sources assume:
1. [Source] assumes [assumption] — Valid? [Yes/No/Unclear]
2. [Source] assumes [assumption] — Valid? [Yes/No/Unclear]

### Missing Perspectives
Whose voice is absent from my sources?
1. [Group] — Why it matters: [...]
2. [Group] — Why it matters: [...]

### Assumption Validity Matrix

| Assumption | Evidence For | Evidence Against | Risk if Wrong |
|------------|--------------|------------------|---------------|
| [A1] | [Evidence] | [Evidence] | [Impact] |
| [A2] | [Evidence] | [Evidence] | [Impact] |
| [A3] | [Evidence] | [Evidence] | [Impact] |
```

### Example: Assumptions in AI Coding Research

```markdown
## Assumption Audit

### My Hidden Assumptions

1. **Assumption:** Productivity gains translate to business value
   - Evidence for: Logic suggests faster = cheaper
   - Evidence against: Could produce more bugs, technical debt
   - If wrong: ROI case falls apart

2. **Assumption:** Current capabilities represent long-term trajectory
   - Evidence for: AI improving rapidly
   - Evidence against: Could hit capability ceiling
   - If wrong: Predictions about future adoption invalid

3. **Assumption:** Developer self-reports are accurate
   - Evidence for: They know their own work
   - Evidence against: Bias, placebo effect, social desirability
   - If wrong: Productivity claims overstated

### Source Assumptions
1. Vendor studies assume their tool is representative — Valid? No
2. Academic studies assume lab conditions generalize — Valid? Unclear

### Missing Perspectives
1. Junior developers — May have different experience than seniors
2. Non-English speakers — Most studies in English contexts
```

---

## K - Know Limits (Epistemic Humility)

**When:** At RED TEAM and SELF-CRITIQUE phases, before packaging

**Purpose:** Explicitly acknowledge uncertainty and conditions under which conclusions might be wrong.

### Prompts

```markdown
## Epistemic Humility Check

### What I Could Be Wrong About
Claims most likely to be incorrect:

1. **Claim:** [Statement]
   - Why I might be wrong: [...]
   - What would disprove this: [...]

2. **Claim:** [Statement]
   - Why I might be wrong: [...]
   - What would disprove this: [...]

3. **Claim:** [Statement]
   - Why I might be wrong: [...]
   - What would disprove this: [...]

### Evidence That Would Change My Mind
For each major conclusion, what would reverse it?

| Conclusion | Would Reconsider If... |
|------------|------------------------|
| [Conclusion 1] | [Evidence that would change mind] |
| [Conclusion 2] | [Evidence that would change mind] |
| [Recommendation] | [Condition where recommendation is wrong] |

### Honest Confidence Assessment

**Overall Confidence:** [HIGH / MEDIUM / LOW]

**Most Certain About:**
- [Claim] — Because: [strong evidence, multiple sources, clear logic]

**Least Certain About:**
- [Claim] — Because: [limited data, conflicting sources, assumptions]

**To Increase Confidence, Would Need:**
- [More/better data on X]
- [Expert validation of Y]
- [Real-world testing of Z]

### Limitations Statement
For the final report:
"This analysis has the following limitations:
1. [Limitation] — Impact: [...]
2. [Limitation] — Impact: [...]
3. [Limitation] — Impact: [...]"
```

### Example: Limits in AI Coding Research

```markdown
## Epistemic Humility Check

### What I Could Be Wrong About

1. **Claim:** AI coding saves 20-40% time on average
   - Why I might be wrong: Studies mostly short-term, self-reported
   - What would disprove this: Longitudinal study showing no sustained gains

2. **Claim:** Security risks are manageable with proper review
   - Why I might be wrong: Unknown vulnerabilities, evolving threats
   - What would disprove this: Major security breach traced to AI-generated code

### Evidence That Would Change My Mind

| Conclusion | Would Reconsider If... |
|------------|------------------------|
| AI coding worth adopting | Studies show >20% increase in bugs |
| Start with junior devs | Evidence juniors form bad habits |
| GitHub Copilot best option | Significant capability gap closes |

### Honest Confidence Assessment

**Overall Confidence:** MEDIUM

**Most Certain About:**
- AI coding tools exist and are improving — Clear market evidence

**Least Certain About:**
- Long-term productivity impact — Insufficient longitudinal data

**To Increase Confidence, Would Need:**
- 12+ month studies on same teams
- Data from non-tech industries
- Security audit outcomes
```

---

## Integration Summary

| Phase | THINK Step | Output |
|-------|------------|--------|
| SCOPE | **T** - Take Stock | Prior knowledge inventory |
| PLAN | **H** - Hunt Direction | Prioritized question list |
| GAP ANALYSIS | **I** - Inspect Gaps | Gap assessment + follow-ups |
| SYNTHESIZE | **N** - Notice Assumptions | Assumption audit |
| RED TEAM | **K** - Know Limits | Limitations + confidence |

**Minimum Application by Tier:**
| Tier | Required Steps |
|------|----------------|
| Quick | H only |
| Standard | T, H, I |
| Deep | T, H, I, N, K |
| Exhaustive | All steps, documented |
