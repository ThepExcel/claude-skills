# Agent Templates for Deep Research

Reusable agent prompts for spawning specialized research sub-tasks.

## Contents
- [Generate Agent](#generate-agent)
- [Verification Agent](#verification-agent)
- [Contradiction Resolver](#contradiction-resolver)
- [Red Team Agent](#red-team-agent)
- [Self-Critique Agent](#self-critique-agent)
- [Creative Mode Agent](#creative-mode-agent)

---

## Generate Agent

**Purpose:** Explore a specific angle of the research topic.

```
Task: "GoT Generate - [Topic] - [Angle]"
Goal: Explore [ANGLE] for [TOPIC].

Rules:
- Use WebSearch for 5-10 candidates
- Score candidates (authority, rigor, relevance, independence)
- WebFetch top 2-3
- Output structured findings + claim entries

Return:
1) Key Findings
2) Sources (date, author/org, title)
3) Claims (type C1/C2/C3, evidence quote, confidence)
4) Contradictions/Gaps
5) Next Queries
```

---

## Verification Agent

**Purpose:** Verify C1 claims with independent sources.

```
Task: "Verifier - C1 Claims - [Subtopic]"
Input: List of C1 claims + their current sources.

Goal:
- For each C1 claim:
  - Find corroboration from 2+ independent sources
  - Assign confidence High/Med/Low
  - Identify independence_group_id
  - Flag contradictions

Return:
- For each claim: Verified/Partially/Unverified + confidence + sources
```

---

## Contradiction Resolver

**Purpose:** Resolve conflicting information between sources.

```
Task: "Resolver - [Conflict ID]"

Sources disagree on: "[CONFLICTING CLAIM]"

Source A: [CLAIM_A] (Quality: [RATING])
Source B: [CLAIM_B] (Quality: [RATING])

1. CLASSIFY conflict type (data/interpretation/methodological/paradigm)
2. INVESTIGATE: Find primary source, check methodology
3. DOCUMENT: Evidence each side, confidence assessment

Return:
{
  "conflict_type": "data/interpretation/methodological/paradigm",
  "resolution": "...",
  "confidence": 0.XX,
  "remaining_uncertainty": "...",
  "user_decision_needed": true/false
}
```

---

## Red Team Agent

**Purpose:** Find counter-evidence to main conclusions.

```
Task: "Red Team - [Topic]"

Current conclusions:
"[AGGREGATED_FINDINGS]"

Mission: Find evidence AGAINST these conclusions.

Search for:
1. Data that contradicts main findings
2. Case studies where approach FAILED
3. Expert opinions that DISAGREE with consensus
4. Methodological weaknesses in cited studies
5. Edge cases where conclusions don't hold
6. Alternative explanations for same data

Present counterarguments at their STRONGEST.
Do NOT try to disprove them.

Return:
{
  "counterarguments": [
    {
      "claim": "[Counter-claim]",
      "evidence": "[Supporting evidence]",
      "source": "[Citation]",
      "strength": "strong/moderate/weak"
    }
  ],
  "methodological_concerns": [...],
  "alternative_explanations": [...],
  "remaining_uncertainties": [...]
}
```

---

## Self-Critique Agent

**Purpose:** Review draft report for quality issues.

```
Task: "Self-Critique - [Topic] Report"

Input: [DRAFT_REPORT]

Review for:
1. Citation accuracy - every claim has source?
2. Logic gaps - evidence → conclusion valid?
3. Confidence calibration - levels match evidence?
4. Missing perspectives - what's not addressed?
5. Clarity issues - jargon, undefined terms?

Return:
{
  "issues_found": [
    {
      "location": "[Section/claim]",
      "issue_type": "overclaiming/logic_gap/missing_nuance/stale_citation/vague_recommendation",
      "current": "[Current text]",
      "suggested": "[Improved text]",
      "priority": "high/medium/low"
    }
  ],
  "overall_quality": "A/B/C/D",
  "revision_needed": true/false
}
```

---

## Creative Mode Agent

**Purpose:** Execute full creative mode research.

```
Task: "Creative Mode - [TOPIC]"

Phase C1 - ABSTRACT:
Original topic: "[TOPIC]"
Abstracted function: "[To be determined]"

Phase C2 - MAP:
Identify 3-5 domains that excel at [abstracted function]

Phase C3 - SEARCH:
For each domain, search 2-3 queries about how they achieve [abstracted function]
[Execute ALL searches in parallel]

Phase C4 - GENERALIZE:
For each domain finding, extract:
- Observable practice
- Underlying mechanism
- Transferable principle

Phase C5 - SYNTHESIZE:
Apply each principle to [TOPIC]:
- Specific implementation
- Expected outcome
- Effort/Impact assessment

Return:
{
  "abstracted_function": "...",
  "domain_insights": [
    {
      "domain": "Gaming",
      "finding": "...",
      "source": "...",
      "principle": "...",
      "mechanism": "..."
    }
  ],
  "applications": [
    {
      "principle": "...",
      "implementation": "...",
      "expected_outcome": "...",
      "effort": "Low/Med/High",
      "impact": "Low/Med/High"
    }
  ],
  "quick_wins": ["High impact + Low effort items"],
  "bold_bets": ["High impact + High effort items"]
}
```

---

## Usage Notes

**Spawning agents:**
```
Task(agent): "[Agent Template Name]"
```

**Parallel execution:**
Launch multiple agents in single message when they're independent.

**Model selection:**
- Use **Haiku** for verification, simple searches
- Use **Sonnet** for synthesis, complex reasoning
- Use **Opus** for Red Team, creative mode (high stakes)
