# Advanced Problem-Solving Frameworks

Deep guides for frameworks added from cross-domain research.

## Table of Contents

1. [Cynefin Framework](#cynefin-framework)
2. [Computational Thinking](#computational-thinking)
3. [Double Diamond](#double-diamond)
4. [Meadows' 12 Leverage Points](#meadows-12-leverage-points)
5. [A3 Thinking](#a3-thinking)
6. [DMAIC (Six Sigma)](#dmaic-six-sigma)
7. [Kepner-Tregoe](#kepner-tregoe)
8. [Wicked Problems](#wicked-problems)
9. [Theory of Constraints](#theory-of-constraints)
10. [Graph of Thoughts](#graph-of-thoughts)

---

## Cynefin Framework

**Origin:** Dave Snowden, IBM (1999)
**Purpose:** Classify problem before choosing approach

### The Five Domains

#### 1. Clear (Simple/Obvious)
- Cause-effect is obvious to everyone
- Best practices exist
- **Approach:** Sense → Categorize → Respond
- **Example:** Following a recipe, standard procedures

#### 2. Complicated
- Cause-effect requires analysis or expertise
- Multiple right answers exist
- **Approach:** Sense → Analyze → Respond
- **Example:** Repairing a car engine, tax planning

#### 3. Complex
- Cause-effect only understood in retrospect
- No "right" answers, only emergent patterns
- **Approach:** Probe → Sense → Respond
- **Example:** Market dynamics, organizational culture change

#### 4. Chaotic
- No cause-effect relationships discernible
- Immediate action required to establish order
- **Approach:** Act → Sense → Respond
- **Example:** Crisis management, emergency response

#### 5. Confused (Disorder)
- Don't know which domain applies
- **Approach:** Break into parts, classify each

### Domain Transitions

```
Clear → Complacent → Falls into Chaos (if ignored)
Complex → Patterns emerge → May become Complicated
Chaotic → Establish order → Becomes Complex
```

### Critical Mistake

Using **Complicated** tools on **Complex** problems:
- Detailed analysis won't help when cause-effect is unknowable
- Instead: Run small experiments, learn from feedback

---

## Computational Thinking

**Origin:** Jeannette Wing (2006), Communications of ACM
**Purpose:** Formulate problems so solutions can be computed

### The Four Pillars

#### 1. Decomposition
Break complex problems into smaller, manageable parts.

**Questions:**
- Can I divide this into independent sub-problems?
- What's the smallest piece I can solve?
- Are there natural boundaries?

**Example:**
```
Problem: Build a website
├── Frontend (UI/UX)
│   ├── Homepage
│   ├── Navigation
│   └── Forms
├── Backend (API)
│   ├── Authentication
│   ├── Database
│   └── Business logic
└── Deployment
    ├── Hosting
    └── CI/CD
```

#### 2. Pattern Recognition
Identify similarities among and within problems.

**Questions:**
- Have I seen this before?
- What's common across these sub-problems?
- Can I reuse a solution?

**Patterns to look for:**
- Recurring structures
- Similar inputs/outputs
- Analogous problems in other domains

#### 3. Abstraction
Focus on essential information, ignore irrelevant details.

**Questions:**
- What information is necessary?
- What can I safely ignore?
- What's the core mechanism?

**Example:**
```
Concrete: "User clicks blue button, form validates, sends POST to /api/submit"
Abstract: "User action → Validation → Data submission"
```

#### 4. Algorithm Design
Create step-by-step solution procedure.

**Considerations:**
- Correctness: Does it solve the problem?
- Efficiency: Is it fast enough?
- Clarity: Can others understand it?

---

## Double Diamond

**Origin:** British Design Council (2005)
**Purpose:** Separate problem-finding from solution-finding

### The Two Diamonds

```
        DIAMOND 1                    DIAMOND 2
    (Right Problem)              (Right Solution)

    ╱‾‾‾‾‾‾‾‾‾‾‾‾╲              ╱‾‾‾‾‾‾‾‾‾‾‾‾╲
   ╱              ╲            ╱              ╲
  ╱   DISCOVER     ╲          ╱   DEVELOP      ╲
 ╱    (diverge)     ╲        ╱   (diverge)     ╲
 ╲                  ╱        ╲                  ╱
  ╲   DEFINE       ╱          ╲   DELIVER      ╱
   ╲  (converge)  ╱            ╲  (converge)  ╱
    ╲____________╱              ╲____________╱
         │                           │
    Problem                     Solution
    Statement                   Launch
```

### Phase Details

#### Discover (Diverge)
- Research, observe, gather data
- Talk to stakeholders
- Explore problem space without judgment
- Quantity over quality

#### Define (Converge)
- Synthesize findings
- Create problem statement
- "How Might We..." formulation
- Prioritize and focus

#### Develop (Diverge)
- Brainstorm solutions
- Prototype rapidly
- Explore many options
- Defer judgment

#### Deliver (Converge)
- Test and iterate
- Select best solution
- Refine and implement
- Launch and learn

### Key Insight

**Diverge before you converge.** Most failures come from:
- Converging on problem too fast (solving wrong problem)
- Converging on solution too fast (missing better options)

---

## Meadows' 12 Leverage Points

**Origin:** Donella Meadows, "Thinking in Systems" (1997, 2008)
**Purpose:** Find where small changes create big impact

### The 12 Points (Weakest to Strongest)

| # | Leverage Point | Effectiveness |
|---|----------------|---------------|
| 12 | Constants, parameters (taxes, standards) | Weakest |
| 11 | Buffer sizes (stabilizing stocks) | ↓ |
| 10 | Stock-flow structure (physical structure) | ↓ |
| 9 | Delays (relative to system change) | ↓ |
| 8 | Negative feedback strength | ↓ |
| 7 | Positive feedback gain | ↓ |
| 6 | Information flows | ↓ |
| 5 | System rules (incentives, constraints) | ↓ |
| 4 | Self-organization power | ↓ |
| 3 | System goals | ↓ |
| 2 | Paradigm (mindset) | ↓ |
| 1 | Transcending paradigms | Strongest |

### Grouped by Category (Abson 2017)

| Category | Points | Impact |
|----------|--------|--------|
| **Intent** | 1-3 (Paradigms, Goals) | Highest |
| **Design** | 4-5 (Self-org, Rules) | High |
| **Feedbacks** | 6-8 (Info, Feedback loops) | Medium |
| **Parameters** | 9-12 (Numbers, Delays) | Lowest |

### Key Insight

> "Leverage points are not intuitive. Or if they are, we intuitively use them backward, systematically worsening whatever problems we are trying to solve."

**Common mistake:** Pushing on parameters (subsidies, taxes) when paradigm shift is needed.

---

## A3 Thinking

**Origin:** Toyota (1960s)
**Purpose:** Force clarity through constraint (one page)

### The A3 Template

```
┌─────────────────────────────────────────────────────────────┐
│ TITLE: [Problem Statement]                     Date:        │
├─────────────────────────────┬───────────────────────────────┤
│ 1. BACKGROUND/CONTEXT       │ 5. COUNTERMEASURES            │
│ • Why is this important?    │ • What will we do?            │
│ • Business impact?          │ • How does each address       │
│ • Stakeholders affected?    │   root causes?                │
├─────────────────────────────┼───────────────────────────────┤
│ 2. CURRENT CONDITION        │ 6. IMPLEMENTATION PLAN        │
│ • What's happening now?     │ • Who / What / When           │
│ • Data and facts            │ • Resources needed            │
│ • Gap from ideal            │ • Milestones                  │
├─────────────────────────────┼───────────────────────────────┤
│ 3. TARGET CONDITION         │ 7. FOLLOW-UP                  │
│ • What should happen?       │ • How will we know it worked? │
│ • Measurable goals          │ • Check dates                 │
│ • Success criteria          │ • Sustain plan                │
├─────────────────────────────┴───────────────────────────────┤
│ 4. ROOT CAUSE ANALYSIS                                      │
│ [5 Whys or Fishbone Diagram]                                │
│                                                             │
│ Why? → Why? → Why? → Why? → Why? → ROOT CAUSE               │
└─────────────────────────────────────────────────────────────┘
```

### Three Meanings of "A3"

1. **Paper Size:** Physical constraint forces clarity
2. **Thinking Process:** PDCA-based problem solving
3. **Coaching Tool:** Dialog between mentor and author

### A3 Rules

- Must fit on ONE page (A3 or 11x17")
- Left side = problem, Right side = solution
- Read like a story (top-to-bottom, left-to-right)
- Visual > Text (diagrams, charts)
- Living document (iterate, don't finalize)

---

## DMAIC (Six Sigma)

**Origin:** Motorola (1986), popularized by GE
**Purpose:** Data-driven process improvement

### The Five Phases

#### D - Define
- Project charter
- Problem statement (SMART)
- Voice of Customer (VOC)
- Scope boundaries

**Deliverables:** Charter, SIPOC diagram, CTQ tree

#### M - Measure
- Identify metrics
- Validate measurement system
- Collect baseline data
- Process capability

**Deliverables:** Data collection plan, baseline metrics

#### A - Analyze
- Root cause analysis
- Hypothesis testing
- Process analysis
- Failure modes

**Tools:** Pareto, Fishbone, Regression, FMEA

#### I - Improve
- Generate solutions
- Pilot test
- Implement changes
- Measure improvement

**Deliverables:** Pilot results, implementation plan

#### C - Control
- Standardize process
- Create control plan
- Document procedures
- Hand off to process owner

**Deliverables:** Control charts, SOPs, training

### When to Use DMAIC

| Use DMAIC | Don't Use DMAIC |
|-----------|-----------------|
| Process exists but underperforms | No process exists (use DMADV) |
| Root cause unknown | Root cause is obvious |
| Data can be collected | Problem is political/cultural |
| Improvement is measurable | Quick fix is acceptable |

---

## Kepner-Tregoe

**Origin:** Charles Kepner & Benjamin Tregoe (1965)
**Purpose:** Separate different types of thinking

### The Four Processes

#### 1. Situation Appraisal (SA)
- Clarify concerns
- Set priorities
- Determine next steps

**Questions:**
- What's going on?
- What's most urgent?
- What needs analysis vs. decision?

#### 2. Problem Analysis (PA)
- Describe deviation (IS vs. IS NOT)
- Identify possible causes
- Test most probable cause

**IS/IS NOT Matrix:**
| Dimension | IS | IS NOT |
|-----------|----|----|
| What | Affected objects | Not affected |
| Where | Location of problem | Where it doesn't occur |
| When | Timing of occurrence | When it doesn't occur |
| Extent | Scope of impact | What's not impacted |

#### 3. Decision Analysis (DA)
- State decision purpose
- Develop objectives (MUSTs vs. WANTs)
- Evaluate alternatives
- Assess risks

#### 4. Potential Problem/Opportunity Analysis (PPA/POA)
- Identify what could go wrong (or right)
- Determine likely causes
- Develop preventive/promoting actions
- Create contingency plans

---

## Wicked Problems

**Origin:** Rittel & Webber (1973)
**Purpose:** Recognize when traditional methods won't work

### The 10 Characteristics

1. **No definitive formulation** - Problem definition depends on solution idea
2. **No stopping rule** - Can always improve further
3. **Not true-or-false** - Solutions are better or worse, not right or wrong
4. **No immediate test** - Consequences unfold over time
5. **Every solution is "one-shot"** - Can't experiment without real impact
6. **No enumerable solutions** - Infinite possible approaches
7. **Essentially unique** - No same problem twice
8. **Symptom of another problem** - Layers of problems
9. **Causes explained many ways** - Depends on worldview
10. **Planner has no right to be wrong** - Accountability for consequences

### Examples of Wicked Problems

- Climate change
- Poverty
- Healthcare system design
- Urban planning
- Organizational culture

### How to Approach

Since traditional problem-solving fails:
- Use iterative, participatory approaches
- Accept "clumsy solutions" (good enough)
- Engage diverse stakeholders
- Embrace continuous adaptation
- Use Design Thinking/Double Diamond

---

## Theory of Constraints

**Origin:** Eliyahu Goldratt, "The Goal" (1984)
**Purpose:** Focus on the constraint that limits the whole system

### The Five Focusing Steps

```
1. IDENTIFY    → Find the constraint (bottleneck)
2. EXPLOIT     → Get maximum from constraint as-is
3. SUBORDINATE → Align everything else to constraint
4. ELEVATE     → Invest to remove constraint
5. REPEAT      → Find new constraint, loop back
```

### The Thinking Processes (TP)

| Tool | Purpose | Question Answered |
|------|---------|-------------------|
| Current Reality Tree | Diagnose | What to change? |
| Evaporating Cloud | Resolve conflict | What's the core conflict? |
| Future Reality Tree | Validate solution | Will this fix it without new problems? |
| Prerequisite Tree | Plan obstacles | What blocks implementation? |
| Transition Tree | Implementation | How to make change step-by-step? |

### Evaporating Cloud (Conflict Resolution)

```
        ┌─────────────┐
        │  OBJECTIVE  │
        │  (Goal)     │
        └──────┬──────┘
               │
      ┌────────┴────────┐
      │                 │
┌─────▼─────┐     ┌─────▼─────┐
│ REQUIRE-  │     │ REQUIRE-  │
│ MENT A    │     │ MENT B    │
└─────┬─────┘     └─────┬─────┘
      │                 │
      │                 │
┌─────▼─────┐     ┌─────▼─────┐
│ PREREQ A  │◄───►│ PREREQ B  │
│           │CLASH│           │
└───────────┘     └───────────┘

SOLUTION: Challenge assumptions connecting
Requirements to Prerequisites
```

---

## Graph of Thoughts

**Origin:** ETH Zurich (2023)
**Purpose:** AI reasoning beyond linear chains

### Evolution of AI Reasoning

| Structure | Description | Limitation |
|-----------|-------------|------------|
| **Chain of Thought** | Linear A → B → C | Can't backtrack |
| **Tree of Thoughts** | Branching exploration | Can't merge paths |
| **Graph of Thoughts** | Full graph with cycles | Most flexible |

### Graph of Thoughts Principles

- **Thoughts as nodes** - Each reasoning step is a vertex
- **Dependencies as edges** - Connections show relationships
- **Merge operations** - Combine multiple thoughts into one
- **Loop operations** - Refine thoughts with feedback

### Benefits

- Can combine thoughts from different branches
- Supports iterative refinement
- Models non-linear human thinking
- 62% quality improvement over ToT on sorting tasks

### Application to Problem Solving

```
        ┌─────────┐
        │ Problem │
        └────┬────┘
             │
     ┌───────┼───────┐
     ▼       ▼       ▼
  [Idea1] [Idea2] [Idea3]
     │       │       │
     └───┬───┴───┬───┘
         │       │
         ▼       ▼
    [Merged1] [Merged2]
         │       │
         └───┬───┘
             ▼
      [Refined Solution]
             │
         ◄───┴───► (feedback loop)
```

Use Graph of Thoughts when:
- Multiple valid perspectives exist
- Ideas need to be combined
- Iterative refinement helps
- Linear thinking gets stuck
