# Standard Mode: Enhanced Research Pipeline

## Contents
- [Phase 0: CLASSIFY](#phase-0-classify)
- [Phase 0.5: DISCOVERY](#phase-05-discovery)
- [Phase 1: SCOPE](#phase-1-scope)
- [Phase 1.5: HYPOTHESIZE](#phase-15-hypothesize)
- [Phase 2: PLAN](#phase-2-plan)
- [Phase 2.5: PLAN PREVIEW](#phase-25-plan-preview)
- [Phase 3: RETRIEVE](#phase-3-retrieve)
- [Phase 3.5: GAP ANALYSIS](#phase-35-gap-analysis)
- [Phase 4: TRIANGULATE](#phase-4-triangulate)
- [Phase 5: SYNTHESIZE](#phase-5-synthesize)
- [Phase 6: RED TEAM](#phase-6-red-team)
- [Phase 6.5: SELF-CRITIQUE](#phase-65-self-critique)
- [Phase 7: PACKAGE](#phase-7-package)
- [Quality Checklist](#quality-checklist)

---

## Phase 0: CLASSIFY

**Objective:** Route questions to appropriate process intensity

| Type | Characteristics | Process |
|------|-----------------|---------|
| **A: LOOKUP** | Single fact, known source | WebSearch → Answer. 1-2 min. |
| **B: SYNTHESIS** | Multi-fact aggregation | 3 phases. 10 min. |
| **C: ANALYSIS** | Judgment needed | 6 phases. 20-30 min. |
| **D: INVESTIGATION** | Novel/conflicting | Full pipeline + Red Team. 45-60 min. |

**Gate**: Classification explicit before proceeding.

---

## Phase 0.5: LANDSCAPE SCAN

**Objective:** Map the full landscape BEFORE diving into specifics. Discover what exists.

**Rationale:** You cannot research what you don't know exists. Claude's training data has a cutoff. For fast-changing fields (AI, crypto, tech), new entities exist that Claude doesn't know about. Scanning the landscape FIRST prevents blind spots.

### CRITICAL RULE: No Known Names in Scan Queries

```
❌ WRONG: "DeepSeek Qwen performance comparison 2025"
   → You're only searching things you already know!

✅ RIGHT: "China open source LLM models list 2025"
   → You're discovering what's out there
```

### When to Apply
**ALL research types** — MANDATORY before SCOPE:

| Type | Scan Intensity |
|------|----------------|
| A (Lookup) | 1 landscape search |
| B (Synthesis) | 2 landscape searches |
| C (Analysis) | 2-3 landscape searches |
| D (Investigation) | 3-4 landscape searches + full entity extraction |

### Process

1. **Landscape Search** (parallel, NO known entity names, use current year):
   ```
   WebSearch: "[topic] landscape overview [current year]"
   WebSearch: "top [topic] list [current year]"
   WebSearch: "[topic] ecosystem all players [current year]"
   WebSearch: "complete list [topic] [current year]"
   ```

2. **Extract ALL Entities from Results:**
   ```markdown
   **Discovered (NOT in my training data):**
   - [Entity 1]: Brief description from search
   - [Entity 2]: Brief description from search

   **Confirmed (matches my knowledge but updated):**
   - [Entity A]: What's new
   - [Entity B]: Still relevant
   ```

3. **Build Complete Picture:**
   - Count total entities found
   - Note which are new vs known
   - Use discovered names in SCOPE and PLAN queries
   - Flag unknown entities for deeper investigation

### Example

**Topic:** "Chinese open-source AI models"

**Landscape Scan Queries (CORRECT):**
```
"China open source AI models complete list 2025"
"Chinese AI ecosystem all players 2025"
"top Chinese LLM image video models 2025"
```

**NOT This (WRONG - uses known names):**
```
"DeepSeek vs Qwen comparison 2025" ← Skip this until AFTER scan!
```

**After Landscape Scan:**
```
Discovered: Wan 2.1, Kolors 2.1, MiniCPM4, Qwen3,
           DeepSeek-V3.2, HunyuanVideo-I2V, Step-2, Emu3
Confirmed: DeepSeek, Qwen, Yi, Baichuan, GLM
```

→ NOW you have complete picture for SCOPE

### Anti-Patterns

| Wrong | Right |
|-------|-------|
| Use known entity names in scan queries | Search for "list", "all", "ecosystem" |
| Skip scan, assume knowledge is current | Always scan landscape first |
| Search for specific comparisons first | Map the territory before drilling down |
| Ignore unfamiliar names in results | Extract and list every entity |

**Gate**: Complete entity list extracted; landscape mapped before SCOPE.

---

## Phase 1: SCOPE

**Objective:** Define research boundaries and success criteria

| Input | Description |
|-------|-------------|
| **Core question** | One-sentence research question |
| **Decision/use-case** | What will this inform? |
| **Audience** | Executive / Technical / Mixed |
| **Scope** | Geography, timeframe, in/out of scope |
| **Constraints** | Banned sources, required sources |
| **Definition of Done** | Measurable completion criteria |

### THINK Step: Take Stock (T)

Before searching, clarify prior knowledge. See [researcher-thinking.md](./researcher-thinking.md).

```markdown
- What I know with confidence: [List]
- What I think I know (needs verification): [List]
- What I know I don't know: [List]
```

**Gate**: Scope + definition of done explicit.

---

## Phase 1.5: HYPOTHESIZE

**Objective:** Transform research into hypothesis testing

1. Generate 3-5 testable hypotheses
2. Assign prior probability: High (70-90%) / Medium (40-70%) / Low (10-40%)
3. Design research to CONFIRM or DISCONFIRM each
4. Track probability shifts as evidence accumulates

**Requirements:**
- At least 3 hypotheses before Phase 2
- Include at least one contrarian hypothesis
- Track probability shifts in final report

**Gate**: 3+ hypotheses generated.

---

## Phase 2: PLAN

**Objective:** Create intelligent research roadmap

1. Identify 5-10 primary sources
2. List 5-10 secondary/backup sources
3. Create 15-25 search query variations using QUEST Matrix
4. Plan triangulation approach

### QUEST Matrix: Systematic Query Generation

Use [query-framework.md](./query-framework.md) for comprehensive query coverage.

| Dimension | Purpose | Min Queries |
|-----------|---------|-------------|
| **Q** - Questions (5W1H) | Ensure completeness | 4-6 |
| **U** - Universes (Stakeholders) | Multi-viewpoint | 3-4 |
| **E** - Expansions (Synonyms) | Semantic breadth | 2-3 |
| **S** - Scopes (Geo/Time/Scale) | Boundary exploration | 2-3 |
| **T** - Types (Source types) | Source diversity | 3-4 |

### THINK Step: Hunt Direction (H)

Decompose the core question into prioritized sub-questions:

```markdown
- Factual questions (What is?): [List with priority]
- Causal questions (Why?): [List with priority]
- Evaluative questions (How good?): [List with priority]
- Dependencies: [Which questions must come first?]
```

**Gate**: Each subquestion has 3+ queries and 2+ source classes. QUEST checklist ≥80% complete.

---

## Phase 2.5: PLAN PREVIEW

**Objective:** User validation before executing (Deep+ tier only)

Present plan and ask: **"ต้องการปรับแผนก่อนเริ่มไหมคะ?"**

| User Response | Action |
|---------------|--------|
| "proceed" / "ไปเลย" | Execute as planned |
| Adds/removes subquestion | Adjust plan |
| No response (30s) | Proceed with original |

**Gate**: User confirms OR timeout.

---

## Phase 3: RETRIEVE

**Objective:** Collect information using PARALLEL execution

### Parallel Execution (MANDATORY)

```
[Single message with multiple tool calls]
WebSearch: "[topic] 2025 state of the art"
WebSearch: "[topic] limitations challenges"
WebSearch: "[topic] vs alternatives comparison"
Task(agent): Academic paper analysis
```

### Backtrack Protocol

**When:** 3+ consecutive searches yield <10% new info

```
1. STOP current path
2. LOG: "⚠️ Dead-end: [query] → [reason]"
3. PIVOT: Alternative angle/terminology
4. RESUME with new queries
```

### URL Fetching

**Primary:** `WebFetch` tool

**Fallback (if 403/blocked):** Jina AI Reader
```bash
curl -s --max-time 60 "https://r.jina.ai/https://example.com/page"
```

**Gate**: Each subquestion has ≥3 sources and ≥1 high-quality.

---

## Phase 3.5: GAP ANALYSIS

**Objective:** Identify gaps, generate refined queries

After initial retrieval, assess:
- ✅ Questions answered
- ⚠️ Questions partially answered
- ❌ Questions unanswered
- Claims needing more evidence

### COMPASS Checklist: Perspective Coverage Audit

Use [perspective-checklist.md](./perspective-checklist.md) to verify comprehensive coverage.

| Category | Check | Status |
|----------|-------|--------|
| **C** - Contrast | Pro/Con, Benefits/Risks | [ ] |
| **O** - Outlook | Past/Present/Future | [ ] |
| **M** - Modes | Theory vs Practice | [ ] |
| **P** - Perspectives | Mainstream vs Alternative | [ ] |
| **A** - Arena | Local vs Global | [ ] |
| **S** - Scale | Individual/Org/Systemic | [ ] |
| **S** - Sources | Primary/Secondary/Diverse | [ ] |

**Min Coverage:** Quick 3/7, Standard 4/7, Deep 5/7, Exhaustive 6/7

### THINK Step: Inspect Gaps (I)

Reflect on what's still missing:

```markdown
- Information gathered so far: [Summary]
- Contradictions found: [List with resolution approach]
- Most concerning gap: [What + Why it matters + How to address]
- Follow-up queries: [Specific queries to fill gaps]
```

**Iteration Rules:**
- Quick tier: 0-1 iterations
- Standard: 1-2 iterations
- Deep: 2-3 iterations
- Exhaustive: Until diminishing returns

**Gate**: Gap analysis + COMPASS audit completed; follow-up queries executed.

---

## Phase 4: TRIANGULATE

**Objective:** Validate information, assign claim types

### Claim Taxonomy

| Type | Requirements |
|------|--------------|
| **C1 Critical** | Quote + 2+ independent sources + confidence + reasoning |
| **C2 Supporting** | Citation required |
| **C3 Context** | Cite if contested |

### Confidence Reasoning (Required for C1)

```markdown
**Claim:** [Statement]
**Confidence:** HIGH/MEDIUM/LOW/SPECULATIVE
**Reason:** [Why this level]
**What would raise/lower:** [Evidence needed]
**Sources:** [1][2][3]
```

### Confidence Levels

| Level | Criteria |
|-------|----------|
| **HIGH (90%+)** | 3+ sources agree, large samples, replicated |
| **MEDIUM (60-90%)** | Single strong OR multiple weaker |
| **LOW (30-60%)** | Preliminary, expert opinion |
| **SPECULATIVE (<30%)** | Single weak, theoretical |

**Gate**: All C1 claims verified or marked unverified.

---

## Phase 5: SYNTHESIZE

**Objective:** Generate insights with Implications Engine

For every major finding, answer:

| Question | Purpose |
|----------|---------|
| **SO WHAT?** | Why does this matter? |
| **NOW WHAT?** | What action to take? |
| **WHAT IF?** | If trend continues/reverses? |

**Output format:**
```markdown
**ผลกระทบ (Implications):**
- **แล้วยังไง:** [Significance]
- **แล้วต้องทำอะไร:** [Action]
- **ถ้าเป็นอย่างนี้ต่อ:** [Scenario]
```

### THINK Step: Notice Assumptions (N)

Before drawing conclusions, surface hidden assumptions. See [researcher-thinking.md](./researcher-thinking.md).

```markdown
- My hidden assumptions: [List with "if wrong" impact]
- Source assumptions: [What my sources assume]
- Missing perspectives: [Whose voice is absent?]
```

| Assumption | Evidence For | Evidence Against | Risk if Wrong |
|------------|--------------|------------------|---------------|
| [A1] | | | |
| [A2] | | | |

**Gate**: Every recommendation links to C1/C2 claims. Assumptions surfaced.

---

## Phase 6: RED TEAM

**Objective:** Find counter-evidence (Devil's Advocate)

**Deploy when:** Type D investigation OR user requests

Search for:
1. Data contradicting main findings
2. Case studies where approach FAILED
3. Expert opinions that DISAGREE
4. Methodological weaknesses
5. Edge cases where conclusions don't hold

**Requirements:**
- Present counterarguments at their STRONGEST
- Include "What would change our mind" triggers
- Section title: "ข้อจำกัดและหลักฐานที่ขัดแย้ง"

### THINK Step: Know Limits (K)

Practice epistemic humility. See [researcher-thinking.md](./researcher-thinking.md).

```markdown
- What I could be wrong about: [Top 3 claims + why might be wrong]
- Evidence that would change my mind: [For each conclusion]
- Honest confidence: Overall [HIGH/MEDIUM/LOW]
  - Most certain: [Claim]
  - Least certain: [Claim]
```

**Limitations Statement (for final report):**
"This analysis has the following limitations: [List 2-3 key limitations and their impact]"

---

## Phase 6.5: SELF-CRITIQUE

**Objective:** Review quality before packaging

### Checklist

- [ ] Every C1 has citation + confidence
- [ ] Quotes are verbatim
- [ ] Evidence supports conclusions
- [ ] HIGH claims have 3+ sources
- [ ] All hypotheses have outcomes
- [ ] Red Team section present

### Common Issues

| Issue | Fix |
|-------|-----|
| Overclaiming | Add qualifiers, lower confidence |
| Missing nuance | Add "however" or "in some cases" |
| Stale citation | Flag or find newer source |
| Vague recommendation | Make actionable with details |

**Gate**: High-priority issues resolved.

---

## Phase 7: PACKAGE

**Objective:** Deliver professional research report

### Progressive Assembly

1. Executive Summary → Write
2. Hypothesis Results → Append
3. Introduction → Append
4. Findings (each with implications) → Append
5. Red Team / Limitations → Append
6. Recommendations → Append
7. Bibliography (ALL entries) → Append

### Anti-Truncation Rules

**FORBIDDEN:**
- "Content continues..."
- "Due to length..."
- Bibliography ranges "[8-75]"

**REQUIRED:**
- Complete each section fully
- Every citation [N] has full entry

---

## Quality Checklist

Before delivery:
- [ ] Every C1 has citation + confidence + reasoning
- [ ] C1 claims have 2+ independent sources
- [ ] Contradictions acknowledged
- [ ] Sources recent (<3 months for AI/tech)
- [ ] No unsupported claims
- [ ] Implications for each finding
- [ ] Red Team section included
- [ ] Self-critique completed
- [ ] Gap analysis performed
- [ ] Hypothesis outcomes reported
