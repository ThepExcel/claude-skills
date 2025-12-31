# Supporting Problem-Solving Techniques

Quick techniques to complement the main frameworks.

## Table of Contents

1. [Rubber Duck Debugging](#rubber-duck-debugging)
2. [Inversion (via Negativa)](#inversion)
3. [Decomposition](#decomposition)
4. [Analogical Thinking](#analogical-thinking)
5. [Constraints First](#constraints-first)
6. [Time Boxing](#time-boxing)
7. [Pre-Mortem](#pre-mortem)
8. [Reframing](#reframing)

---

## Rubber Duck Debugging

**Origin:** "The Pragmatic Programmer" (1999)

**Method:** Explain your problem step-by-step to an inanimate object (traditionally a rubber duck).

### Why It Works

1. Forces you to articulate the problem clearly
2. Slows down your thinking
3. Exposes gaps in logic
4. Triggers "aha!" moments when you say something that sounds wrong

### How to Apply

```
1. State the problem clearly
2. Explain what you expect to happen
3. Explain what actually happens
4. Walk through the logic step by step
5. Often: "Wait... that's not right..." → Solution found
```

### Variations

| Variant | Method |
|---------|--------|
| **Cardboard programmer** | Explain to imaginary colleague |
| **5-minute email** | Write email describing problem (don't send) |
| **ELI5** | Explain like I'm 5 years old |
| **Teaching** | Pretend you're teaching someone else |

---

## Inversion

**Origin:** Carl Jacobi (mathematician): "Invert, always invert"

**Principle:** Instead of asking "How do I achieve X?", ask "How would I guarantee failure?"

### Method

```
1. Define success
2. Brainstorm: "How could I make this fail completely?"
3. List all failure modes
4. Invert each: "Don't do that"
5. Result: Robust plan avoiding failure paths
```

### Example - Successful Project

**Direct approach:** "How do we succeed?"
- Good planning
- Clear goals
- Skilled team
(Generic, vague)

**Inverted approach:** "How do we guarantee failure?"
- No clear owner
- Scope creep
- Ignore stakeholder feedback
- No milestones
- Skip testing

**Invert to actions:**
- Assign single owner
- Lock scope
- Regular stakeholder check-ins
- Weekly milestones
- Test everything

### When Inversion Excels

- Risk management
- Avoiding obvious mistakes
- When "best practices" feel too generic
- Safety-critical systems

---

## Decomposition

**Principle:** Break big problems into smaller, solvable pieces.

### Strategies

| Strategy | When to Use | Example |
|----------|-------------|---------|
| **Functional** | System with distinct functions | Split by feature |
| **Temporal** | Process over time | Split by phase |
| **Hierarchical** | Nested components | Top-down breakdown |
| **By stakeholder** | Multiple users/owners | Split by persona |

### Work Breakdown Structure

```
Build Website
├── 1.0 Design
│   ├── 1.1 Wireframes
│   ├── 1.2 Visual design
│   └── 1.3 Prototype
├── 2.0 Development
│   ├── 2.1 Frontend
│   ├── 2.2 Backend
│   └── 2.3 Integration
├── 3.0 Content
│   ├── 3.1 Copy
│   └── 3.2 Images
└── 4.0 Launch
    ├── 4.1 Testing
    └── 4.2 Deployment
```

### Signs You Need Decomposition

- Problem feels overwhelming
- Don't know where to start
- Can't estimate effort
- Multiple people need to work on it

### Decomposition Pitfalls

- Over-decomposition (too granular)
- Missing dependencies between pieces
- Losing sight of the whole
- Analysis paralysis

---

## Analogical Thinking

**Principle:** Solutions from one domain often transfer to another.

### Method

```
1. Abstract your problem to its essence
   "I need to move X from A to B efficiently"

2. Find domains that solved similar abstract problem
   Nature, military, sports, other industries

3. Study their solutions

4. Adapt principles back to your domain
```

### Productive Analogies

| Domain | Insights For |
|--------|--------------|
| **Nature** | Efficiency, resilience, adaptation |
| **Military** | Strategy, logistics, rapid response |
| **Sports** | Team dynamics, performance, training |
| **Healthcare** | Diagnosis, triage, prevention |
| **Manufacturing** | Process, quality, scale |
| **Aviation** | Safety, checklists, redundancy |

### Example

**Problem:** Email inbox overwhelming

**Analogy:** Hospital emergency room triage

**Transfer:**
- Immediate (red): Reply now
- Urgent (yellow): Reply today
- Can wait (green): Reply this week
- Doesn't need me (black): Delete/delegate

### Analogy Pitfalls

- Surface similarity without structural match
- Forcing analogy that doesn't fit
- Over-relying on single analogy

---

## Constraints First

**Principle:** Understanding what you CAN'T do clarifies what you CAN do.

### Method

```
1. List ALL constraints explicitly:
   - Budget
   - Time
   - Resources (people, tools)
   - Technical limitations
   - Legal/regulatory
   - Dependencies

2. Categorize:
   - Hard constraints (cannot violate)
   - Soft constraints (prefer not to violate)

3. Define solution space:
   "Given these constraints, what options remain?"
```

### Constraint Types

| Type | Example | Typical Flexibility |
|------|---------|---------------------|
| **Physical** | Laws of physics | Zero |
| **Legal** | Regulations | Very low |
| **Contractual** | Agreements | Low |
| **Budget** | Money limits | Medium |
| **Time** | Deadlines | Medium |
| **Technical** | System limits | Medium-High |
| **Preference** | "We'd like..." | High |

### Constraints as Creativity

Paradox: More constraints often = more creative solutions

**Why?**
- Eliminates obvious/generic solutions
- Forces novel thinking
- Reduces decision paralysis
- Creates focus

**Example:** "Design a car with no constraints" → Overwhelming
**Better:** "Design a car for under $15K that gets 50 MPG" → Focused

---

## Time Boxing

**Principle:** Allocate fixed time, then stop—regardless of completion.

### Why It Works

1. Parkinson's Law: "Work expands to fill time available"
2. Forces prioritization
3. Prevents perfectionism
4. Creates urgency
5. Enables progress estimation

### Method

```
1. Estimate total time needed (be realistic)
2. Cut it by 20-30% (create urgency)
3. Set timer
4. Work with full focus
5. When timer ends: STOP
6. Assess: What got done? What didn't? Why?
```

### Time Box Guidelines

| Task Type | Suggested Box |
|-----------|---------------|
| Quick decision | 5-10 min |
| Research | 25-45 min |
| Planning | 30-60 min |
| Deep work | 90-120 min |
| Brainstorming | 15-30 min |

### Pomodoro Technique

Popular time boxing method:
- 25 min work
- 5 min break
- Repeat 4x
- 15-30 min longer break

---

## Pre-Mortem

**Origin:** Gary Klein, cognitive psychologist

**Principle:** Imagine project has failed, then work backwards to identify what went wrong.

### Method

```
1. Assemble team
2. Brief: "Imagine it's [future date]. The project has failed completely."
3. Each person writes: "What went wrong?"
4. Share all failure modes
5. Prioritize: Which are most likely? Most damaging?
6. Create prevention plan for top risks
```

### Why Pre-Mortem > Risk Assessment

| Traditional Risk | Pre-Mortem |
|------------------|------------|
| "What could go wrong?" | "What DID go wrong?" |
| Feels hypothetical | Feels real |
| Optimism bias present | Optimism removed |
| Misses creative risks | Surfaces hidden concerns |

### Example Outputs

**Project: Launch new product**

Pre-mortem failures identified:
- "Marketing and product weren't aligned on messaging"
- "We underestimated competitive response"
- "Key engineer left mid-project"
- "Legal review took 3 weeks longer than planned"

**Prevention actions:**
- Weekly marketing-product sync
- Competitive intelligence sprint before launch
- Document all critical knowledge
- Start legal review 1 month earlier

---

## Reframing

**Principle:** How you define the problem determines what solutions you can find.

### Reframing Techniques

| Technique | Example |
|-----------|---------|
| **Zoom out** | "Reduce email" → "Communicate better" |
| **Zoom in** | "Improve culture" → "Improve Monday meetings" |
| **Change subject** | "How do we hire?" → "How do people want to be hired?" |
| **Flip the relationship** | "How to sell more?" → "Why would someone want to buy?" |
| **Remove constraints** | "Given our budget..." → "If budget weren't an issue..." |
| **Add constraints** | "Any solution" → "Solution a child could use" |

### "How Might We" (HMW)

IDEO's reframing format:

```
"How might we [action verb] for [user] so that [outcome]?"
```

**Examples:**
- "How might we make waiting enjoyable for customers so that they feel valued?"
- "How might we simplify onboarding for new users so that they succeed in day one?"

### Reframing Red Flags

Signs you're solving the wrong problem:
- Solution doesn't address root frustration
- Stakeholders keep changing requirements
- Similar problems keep recurring
- "Yes, but..." responses to solutions

### Ladder of Abstraction

Move up (abstract) or down (concrete) to find better framing:

```
Abstract: "Be happy"
    ↑
    "Have fulfilling work"
    ↑
    "Get promoted"
    ↑
    "Deliver successful project"
    ↑
Concrete: "Fix the bug in module X"
```

Different levels = different solution spaces
