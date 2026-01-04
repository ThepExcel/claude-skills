# Creative Mode: Cross-Industry Innovation Research

**Purpose:** Find innovative solutions by researching how other industries solve analogous problems.

**Trigger:** "creative mode", "cross-industry", "what do others do", innovation needed

**Based on:** Combinatorial Creativity Engine (+7-10% novelty)

## Contents
- [Phase C1: ABSTRACT](#phase-c1-abstract)
- [Phase C2: MAP](#phase-c2-map)
- [Phase C3: SEARCH](#phase-c3-search)
- [Phase C4: GENERALIZE](#phase-c4-generalize)
- [Phase C5: SYNTHESIZE](#phase-c5-synthesize)
- [Output Format](#output-format)
- [Quality Checklist](#quality-checklist)

---

## Phase C1: ABSTRACT

**Objective:** Strip topic to core function for cross-domain mapping

**Process:**
1. State original topic/question
2. Remove industry-specific terms
3. Identify the FUNCTION being performed
4. Express as: "[Verb]-ing [what] for [whom]"

**Examples:**

| Specific Topic | Abstracted Function |
|----------------|---------------------|
| "Improve Excel training completion" | "Maintain engagement through learning journey" |
| "Better error messages in Power Query" | "Help users recover from mistakes gracefully" |
| "Increase course sales conversion" | "Move prospects from awareness to action" |
| "Reduce customer support tickets" | "Enable self-service problem resolution" |

**Prompt:**
```
Original topic: "[TOPIC]"

1. What's the CORE FUNCTION? (ignore industry)
2. What VERB describes action? (guide, accelerate, maintain, reduce, enable)
3. What is being acted upon? (users, information, decisions)
4. Who benefits? (learners, users, customers)

Abstracted form: "[VERB]-ing [WHAT] for [WHOM]"
```

---

## Phase C2: MAP

**Objective:** Identify 3-5 distant domains that solve the abstracted function

**Selection Criteria:**
1. **Distant enough** — Different industry, not obvious connection
2. **Mature solutions** — Domain has solved the problem well
3. **Accessible knowledge** — Information available online
4. **Transferable** — Not dependent on unique domain features

**Domain Mapping Matrix:**

| Abstracted Function | High-Potential Domains |
|---------------------|----------------------|
| Maintain engagement | Gaming, Fitness apps, TV series, Theme parks |
| Accelerate learning | Military, Sports, Music education, Medical training |
| Help recover from errors | Aviation (CRM), Healthcare, Nuclear operations |
| Move to action | E-commerce, Political campaigns, Charity fundraising |
| Enable self-service | Banking ATMs, Airline check-in, IKEA furniture |
| Translate data to decisions | Military command, Emergency response, Sports analytics |
| Reduce cognitive load | Cockpit design, Surgical checklists, Traffic signs |
| Build trust quickly | Luxury retail, Healthcare providers, Financial advisors |
| Personalize at scale | Netflix, Spotify, Amazon recommendations |

---

## Phase C3: SEARCH

**Objective:** Research how each domain solves the abstracted function

**Parallel Search Pattern:**
```
[ALL searches in single message]

WebSearch: "[domain1] best practices [abstracted function]"
WebSearch: "[domain1] approach to [challenge] case study"
WebSearch: "[domain2] methodology [abstracted function]"
WebSearch: "[domain3] [abstracted function] principles"
WebSearch: "lessons from [domain3] applied to [other field]"
```

**Example: "Maintain engagement through learning journey"**
```
WebSearch: "video game player retention design principles"
WebSearch: "Duolingo gamification streak engagement"
WebSearch: "Netflix binge watching design psychology"
WebSearch: "fitness app habit formation methodology"
```

**Source Evaluation:**
- **Prioritize:** Case studies, design docs, academic research
- **Accept:** Industry blogs, conference talks, practitioner guides
- **Avoid:** Generic "5 tips" articles, outdated practices

---

## Phase C4: GENERALIZE

**Objective:** Extract transferable principles from domain findings

**Rules:**
1. Remove domain-specific terminology
2. Express as universal principle
3. Identify the mechanism (WHY it works)
4. Test if principle applies outside original domain

**Template:**
```
Domain Finding: "[DOMAIN] does [SPECIFIC PRACTICE]"

1. WHAT is happening? (observable behavior)
2. WHY does it work? (underlying mechanism)
3. PRINCIPLE: "[Abstract rule]"
4. TRANSFER TEST: Applies outside [DOMAIN]? [Yes/No + example]
```

**Examples:**

| Domain Finding | Principle | Mechanism |
|----------------|-----------|-----------|
| "Games show XP bar filling" | "Make progress visible and continuous" | Progress visibility motivates completion |
| "Pilots use pre-flight checklists" | "Externalize memory for critical sequences" | Reduces cognitive load |
| "Netflix auto-plays next episode" | "Remove friction from continuation" | Momentum maintained by eliminating choice |
| "Surgeons do timeouts before procedures" | "Force pause before irreversible actions" | Interruption allows error detection |

---

## Phase C5: SYNTHESIZE

**Objective:** Apply generalized principles back to original topic

**Process:**
1. Take each principle
2. Translate to original domain terms
3. Design specific implementation
4. Assess feasibility (effort vs. impact)

**Template:**
```
Principle: "[PRINCIPLE]"
Original Topic: "[TOPIC]"

1. What would this look like in [TOPIC DOMAIN]?
2. Specific implementation: [CONCRETE ACTION]
3. Expected outcome: [MEASURABLE RESULT]
4. Effort: Low / Medium / High
5. Impact: Low / Medium / High
```

**Prioritization:**
- **Quick Wins:** High Impact + Low Effort → Do first
- **Bold Bets:** High Impact + High Effort → Plan carefully

---

## Output Format

```markdown
## [Topic] — Creative Mode Research (ข้อมูล ณ [เดือน ปี])

### ปัญหาที่ Abstract แล้ว (Abstracted Problem)
**โจทย์เดิม:** "[Original topic]"
**Core Function:** "[Verb]-ing [what] for [whom]"

### Cross-Industry Insights

#### 1. จาก [Domain]: [Key Finding]
**แหล่งที่มา:** [Source] ([URL])
**สิ่งที่พวกเขาทำ:** [Observable practice]
**หลักการที่ถอดได้:** [Transferable principle]
**กลไกที่ทำให้ได้ผล:** [Why it works]

### หลักการที่สังเคราะห์ได้ (Synthesized Principles)

| # | หลักการ | ที่มา | กลไก |
|---|---------|-------|------|
| 1 | [Principle] | [Domain] | [Mechanism] |

### การประยุกต์ใช้กับโจทย์เดิม (Applications)

| หลักการ | Implementation | ผลลัพธ์ที่คาด | Effort | Impact |
|---------|----------------|---------------|--------|--------|
| [P1] | [Specific action] | [Outcome] | Low/Med/High | Low/Med/High |

### Quick Wins (ทำได้เลย)
- [High Impact + Low Effort items]

### Bold Bets (ลงทุนมาก แต่ผลตอบแทนสูง)
- [High Impact + High Effort items]

### แหล่งข้อมูลข้ามอุตสาหกรรม
[1] [Domain] - "Title" - URL [Quality: A/B/C]
```

---

## Quality Checklist

Before delivery:
- [ ] Abstraction is function-based, not solution-based
- [ ] 3-5 distant domains explored (not obvious competitors)
- [ ] Each domain has specific finding with source
- [ ] Principles are transferable (mechanism identified)
- [ ] Applications are concrete and actionable
- [ ] Quick Wins vs Bold Bets clearly separated
- [ ] All cross-industry sources cited
