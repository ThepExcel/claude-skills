# Problem-Solving Frameworks - Detailed Guide

## Table of Contents

1. [Polya's 4 Steps](#polyas-4-steps)
2. [First Principles Thinking](#first-principles-thinking)
3. [OODA Loop](#ooda-loop)
4. [Shannon Thinking](#shannon-thinking)
5. [Root Cause Analysis](#root-cause-analysis)
6. [Decision Matrix](#decision-matrix)

---

## Polya's 4 Steps

**Origin:** George Pólya, "How to Solve It" (1945) - sold 1M+ copies, 21 languages

### Step 1: Understand the Problem

**Questions to ask:**
- What is the unknown? What are we trying to find/solve?
- What is the data? What information do we have?
- What is the condition? What constraints exist?
- Is it possible to satisfy the condition?
- Is the condition sufficient/redundant/contradictory?

**Actions:**
- Restate the problem in your own words
- Draw a figure/diagram if possible
- Introduce suitable notation
- Separate the various parts of the condition

**Red flag:** If you can't explain the problem clearly, you don't understand it.

### Step 2: Devise a Plan

**Strategy selection:**

| Strategy | When to Use |
|----------|-------------|
| **Work backwards** | Clear end state, unclear path |
| **Find a pattern** | Repeating elements, sequences |
| **Divide and conquer** | Large problem, separable parts |
| **Simplify first** | Complex problem, simpler version helps |
| **Use analogy** | Similar problems exist |
| **Draw a diagram** | Spatial/relational problem |
| **Make a table** | Multiple cases to compare |
| **Guess and check** | Limited possibilities |
| **Process of elimination** | Known constraints |

**Connection questions:**
- Have I seen this before? In different form?
- Do I know a related problem with useful technique?
- Can I use part of the solution method?
- Can I solve a simpler related problem first?
- Can I change the unknown? The data? Both?

### Step 3: Carry Out the Plan

**Execution principles:**
- Check each step: "Can I see clearly that the step is correct?"
- If stuck, return to Step 2 and try different strategy
- Maintain patience and persistence
- Document as you go

**Common pitfalls:**
- Skipping steps → errors compound
- Not checking intermediate results
- Abandoning too early
- Not keeping notes

### Step 4: Look Back

**Reflection questions:**
- Can I check the result? The argument?
- Can I derive the result differently?
- Can I see it at a glance?
- Can I use the result, or method, for another problem?

**Benefits of reflection:**
- Consolidates knowledge
- Discovers shortcuts
- Builds problem-solving repertoire
- Prevents same mistakes

---

## First Principles Thinking

**Origin:** Aristotle (first principle = "the first basis from which a thing is known")
**Modern popularizer:** Elon Musk

> "I tend to approach things from a physics framework. Physics teaches you to reason from first principles rather than by analogy."

### The 3-Step Framework

#### Step 1: Identify and Challenge Assumptions

**Questions:**
- What do I "know" about this?
- Why do I believe this?
- Who told me this? Are they reliable?
- What if the opposite were true?
- What would I do if I knew nothing about how it's "normally" done?

**Example - SpaceX rockets:**
```
Assumption: "Rockets cost $65M because that's what aerospace companies charge"
Challenge: "Is $65M the fundamental cost, or the market price?"
```

#### Step 2: Break Down to Fundamental Truths

**Method: 5 Whys to fundamentals**

```
Why are rockets expensive? → Aerospace industry pricing
Why aerospace pricing? → Limited suppliers, high margins
Why high margins? → Assumed market, not questioned
What ARE rockets made of? → Aluminum, titanium, copper, carbon fiber
What do those materials cost? → ~2% of rocket price
```

**Fundamental truth:** Rocket material cost ≠ Rocket price

#### Step 3: Rebuild from Fundamentals

**Questions:**
- Given only the fundamental truths, what's possible?
- What would a solution look like if starting fresh?
- What can I build without the old constraints?

**SpaceX result:** Built rockets for 10% of traditional cost

### When to Use First Principles

| Good Fit | Poor Fit |
|----------|----------|
| Need breakthrough innovation | Incremental improvement |
| Industry stuck in old ways | Well-optimized domain |
| High stakes justify deep analysis | Quick decision needed |
| Challenging "impossible" problems | Standard problem with known solution |

### First Principles Pitfalls

- **Analysis paralysis:** Don't break down forever
- **Ignoring valid knowledge:** Some conventions exist for good reasons
- **Time cost:** Only use when stakes justify investment

---

## OODA Loop

**Origin:** Colonel John Boyd, USAF (1970s)
**Context:** Air combat maneuvering → business strategy

> Boyd earned nickname "Forty-Second Boyd" - could beat any opponent in under 40 seconds

### The 4 Phases

#### Observe

**Purpose:** Gather raw information about current situation

**Actions:**
- Collect data from environment
- Notice changes and anomalies
- Identify what's actually happening (vs. assumptions)
- Use multiple information sources

**Key insight:** Observe WHAT IS, not what you expect

#### Orient

**Purpose:** Make sense of observations in context

**Factors affecting orientation:**
- Previous experiences
- Cultural traditions
- Genetic heritage
- New information
- Analysis and synthesis

**This is the critical phase.** Boyd: "Orientation shapes the way we observe, the way we decide, the way we act."

**Questions:**
- What does this mean in context?
- What biases might I have?
- What patterns do I recognize?
- How does this fit with my mental models?

#### Decide

**Purpose:** Choose course of action

**Based on:**
- Oriented understanding
- Available options
- Resource constraints
- Risk tolerance

**Key:** Decision isn't final - it's hypothesis to test

#### Act

**Purpose:** Execute the decision

**Then:** Loop back to Observe to see results

### Speed as Advantage

> "The ability to operate at a faster tempo or rhythm than an adversary enables one to fold the adversary back inside himself so that he can neither appreciate nor keep up with what's going on."

**Business application:** Faster OODA loops → competitive advantage

### OODA in Practice

**Startup vs. Enterprise:**
```
Startup: Observe market → Orient quickly → Decide → Act → Learn
Enterprise: Long planning cycles, slow orientation, delayed action
```

**Agile development is OODA:**
- Sprint = one OODA cycle
- Retrospective = improved Orientation
- Demo = Observe results

---

## Shannon Thinking

**Origin:** Claude Shannon, "father of information theory"

> "Strip the problem to its fundamental elements and proceed from there."

### The 5-Step Process

#### Step 1: Define

**Goal:** State problem in simplest possible terms

**Shannon's method:**
- Remove all unnecessary complexity
- Get to the core of what you're trying to solve
- Write it in one clear sentence

**Example:**
```
Vague: "Our communication system has issues"
Defined: "How do we transmit a message accurately over a noisy channel?"
```

#### Step 2: Identify Constraints

**Categories:**

| Type | Examples |
|------|----------|
| Physical | Speed of light, energy limits |
| Resource | Budget, time, people |
| Technical | Hardware capabilities, protocols |
| Business | Regulations, contracts, policies |
| Human | Skills, attention, adoption |

**Shannon's insight:** Constraints define the solution space. Know them precisely.

#### Step 3: Model

**Purpose:** Create abstract representation of the system

**Shannon's approach:**
- Reduce to essential components
- Identify relationships mathematically if possible
- Find patterns and invariants

**Example - Information theory:**
```
Source → Encoder → Channel (+ Noise) → Decoder → Destination
```

**Key:** Model should be simple enough to analyze, accurate enough to be useful

#### Step 4: Validate

**Two approaches:**

| Formal Proof | Experimental Test |
|--------------|-------------------|
| Mathematical rigor | Empirical evidence |
| Works for abstract | Works for practical |
| Guarantees bounds | Reveals real behavior |

**Shannon used both:** Proved theorems, then built machines

#### Step 5: Implement

**Bridge from theory to practice:**
- Design practical solution
- Account for real-world complications
- Test incrementally
- Iterate based on results

### When Shannon Thinking Excels

- Complex systems with many interacting parts
- Problems that benefit from mathematical modeling
- Situations where constraints are hard but known
- Need to prove optimality or bounds

---

## Root Cause Analysis

### The 5 Whys Method

**Origin:** Taiichi Ohno, Toyota Production System

**Principle:** Surface problems have deeper causes. Ask "Why?" repeatedly to find the root.

### How to Apply

```
Problem: Production stopped

Why? → Machine failed
Why? → Bearing seized
Why? → Insufficient lubrication
Why? → Pump not working properly
Why? → Pump shaft worn from debris
Why? → No filter on pump intake
ROOT CAUSE: Missing filter specification in maintenance procedure
```

### 5 Whys Best Practices

**Do:**
- Ask "Why?" to the ANSWER, not the original problem
- Stop when you reach something actionable and within your control
- Look for process/system failures, not just people failures
- Document the chain

**Don't:**
- Accept "human error" as root cause (ask why the error was possible)
- Stop at symptoms
- Skip levels
- Guess at answers

### Common Stopping Points

| Level | Type | Example |
|-------|------|---------|
| 1-2 | Symptom | "Server crashed" |
| 3-4 | Proximate cause | "Memory leak in code" |
| 5+ | Root cause | "No memory profiling in CI/CD" |

### Beyond 5 Whys: Fishbone Diagram

For complex problems with multiple potential causes:

```
                    ┌─ Methods ──────┐
                    │                │
┌─ Materials ──────┐│                │┌── Machines ────┐
│                  ││                ││                │
└──────────────────┼┼────────────────┼┼────────────────┘
                   ││   [PROBLEM]    ││
┌──────────────────┼┼────────────────┼┼────────────────┐
│                  ││                ││                │
└─ Measurement ────┘│                │└── Manpower ────┘
                    │                │
                    └─ Mother Nature─┘
```

**Categories (6M):**
- Methods (processes)
- Machines (equipment)
- Manpower (people)
- Materials (inputs)
- Measurement (data quality)
- Mother Nature (environment)

---

## Decision Matrix

### When to Use

- Multiple options with multiple criteria
- Need to justify decision to others
- Want to reduce emotional bias
- Complex trade-offs to balance

### Building the Matrix

#### Step 1: List Options (Columns)

Brainstorm all viable alternatives. Include:
- Status quo
- Conservative option
- Aggressive option
- Creative alternatives

#### Step 2: Define Criteria (Rows)

**Common criteria:**

| Category | Examples |
|----------|----------|
| Cost | Initial, ongoing, total ownership |
| Time | Development, deployment, payback |
| Quality | Performance, reliability, UX |
| Risk | Technical, market, operational |
| Strategic fit | Vision alignment, scalability |

#### Step 3: Weight Criteria

Distribute 100% across criteria based on importance:

```
Cost: 25%
Time: 20%
Quality: 30%
Risk: 15%
Strategic: 10%
Total: 100%
```

**Method:** Pair comparison or stakeholder voting

#### Step 4: Score Options

Rate each option on each criterion (1-10):

| Criteria (Weight) | Option A | Option B | Option C |
|-------------------|----------|----------|----------|
| Cost (25%) | 8 | 5 | 3 |
| Time (20%) | 6 | 9 | 7 |
| Quality (30%) | 7 | 6 | 9 |
| Risk (15%) | 5 | 7 | 6 |
| Strategic (10%) | 8 | 5 | 7 |

#### Step 5: Calculate Weighted Scores

```
Option A: (8×0.25) + (6×0.20) + (7×0.30) + (5×0.15) + (8×0.10)
        = 2.0 + 1.2 + 2.1 + 0.75 + 0.8
        = 6.85

Option B: (5×0.25) + (9×0.20) + (6×0.30) + (7×0.15) + (5×0.10)
        = 1.25 + 1.8 + 1.8 + 1.05 + 0.5
        = 6.40

Option C: (3×0.25) + (7×0.20) + (9×0.30) + (6×0.15) + (7×0.10)
        = 0.75 + 1.4 + 2.7 + 0.9 + 0.7
        = 6.45
```

**Winner: Option A (6.85)**

### Sensitivity Analysis

After calculating, ask:
- If weights changed slightly, would winner change?
- Are any criteria scored incorrectly?
- Are we missing important criteria?

This validates the robustness of the decision.
