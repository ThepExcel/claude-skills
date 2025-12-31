# AI Creativity Methodology

Research-backed guidance for AI-augmented ideation.

## Table of Contents

1. [Research Insights](#research-insights)
2. [AI-Optimized Protocols](#ai-optimized-protocols)
3. [Persona Bank](#persona-bank)
4. [Constraint Types](#constraint-types)
5. [TRIZ Principles](#triz-principles)

---

## Research Insights

### What Works (High Confidence)

| Finding | Implication |
|---------|-------------|
| Incubation breaks prevent AI self-anchoring | Pause between idea bursts |
| Parallel personas > sequential > single | Use Multi-Persona Parallel |
| Mild constraints boost novelty (Goldilocks) | Use Constraint Injection |
| Combinatorial framework +7-10% novelty | Use for breakthrough tasks |
| Human steering required for analogies | Don't let AI run alone |
| Combining 2+ techniques > single | Stack techniques |

### Risks to Mitigate

| Risk | Mitigation |
|------|------------|
| **Fixation amplification** - AI strengthens biases if used too early | Use AI AFTER initial human ideation |
| **Collective homogenization** - Individual ↑ but group diversity ↓ | Use Divergence Guard |
| **Over-early AI use** - Weakens deep thinking | Human ideates first, then AI expands |
| **Authorship erosion** - Loss of ownership feeling | Balance AI contribution |

### Optimal AI Role

- **Best as:** Exploration partner, constraint enforcer, analogy finder
- **Avoid:** Sole ideation source, final decision maker
- **Timing:** After initial human ideation, not before

### LLM Creativity Ceiling

Research suggests LLMs max out at "little-c" creativity (amateur level). For "Pro-c" (professional/expert), human guidance is essential. AI is a tool, not a replacement.

**Sources:**
- [HBR 2025](https://hbr.org/2025/12/research-when-used-correctly-llms-can-unlock-more-creative-ideas)
- [arXiv 2024 - Combinatorial](https://arxiv.org/abs/2412.14141)
- [Science Advances 2024](https://www.science.org/doi/10.1126/sciadv.adn5290)
- [PMC 2024 - Homogenization](https://pmc.ncbi.nlm.nih.gov/articles/PMC11244532/)

---

## AI-Optimized Protocols

### Incubation Cycling

**Problem:** LLMs anchor to their own outputs → convergence.

**Protocol:**
1. Generate first burst (5-10 ideas)
2. **STOP** — user does unrelated task 2-5 min
3. Fresh context (don't show previous ideas)
4. Generate second burst from scratch
5. Compare and combine both sets

**Variations:**
- Overnight gap for major challenges
- Work on different problem during break
- Return as different persona for second burst

### Multi-Persona Parallel

**Problem:** Sequential personas anchor to earlier outputs.

**Parallel prompt (maximum diversity):**
```
Solve [problem] from 4 perspectives simultaneously:
1. Skeptical engineer (feasibility)
2. Customer experience designer (delight)
3. Cost-optimizer (efficiency)
4. 10-year-old child (fun)

Give each 2-3 distinct ideas.
```

**Sequential evolution (when parallel not possible):**
1. Persona A generates → 2. Persona B critiques → 3. Persona C adds different angle → 4. Synthesize

### Constraint Injection

**Problem:** Without constraints, AI converges to same "optimal" solutions.

**Protocol:**
1. Generate 5 ideas unconstrained
2. Pick random constraint (see table below)
3. Generate 5 MORE ideas with constraint
4. Compare — constrained set often more creative
5. Apply constraint insights to unconstrained ideas

### Divergence Guard

**Problem:** AI ideas become too similar across users.

**5-Step Protocol:**
1. **Similarity check** — After 3+ ideas, review for patterns
2. **Force opposite** — "Generate OPPOSITE of above"
3. **Domain shift** — "What would [random field] do?"
4. **Constraint swap** — Remove assumed constraint, add random new one
5. **Absurdity injection** — "Most ridiculous solution?"

### Combinatorial Creativity Engine

**Systematic breakthrough (+7-10% novelty):**

1. **ABSTRACT** — Strip problem to core function
   - "Move people" not "better bus"
2. **RETRIEVE** — Find solutions from 3+ distant domains
   - Nature, military, sports, healthcare, entertainment
3. **GENERALIZE** — Extract transferable principles
   - "Leave trails" not "pheromones"
4. **COMBINE** — Create novel configurations
   - Principle A + B applied to problem
5. **INSTANTIATE** — Make concrete for context

### TRIZ-AI Quick Method

**For technical/engineering problems:**

1. State problem as contradiction: "I want X but it causes Y"
2. Identify 2-3 relevant principles (see below)
3. Prompt: "Apply TRIZ principle [X] to solve: [problem]"
4. Iterate with different principles

---

## Persona Bank

| Category | Options |
|----------|---------|
| **Role** | Engineer, Designer, Marketer, CFO, Support, CEO, Intern |
| **Attitude** | Skeptic, Optimist, Pragmatist, Dreamer, Devil's Advocate |
| **Domain** | Healthcare, Military, Entertainment, Education, Nature, Finance |
| **Age** | Child (5), Teen (15), Adult (35), Elder (75) |
| **Constraint** | No budget, Unlimited budget, No time, 10 years, Hostile environment |

---

## Constraint Types

| Type | Examples |
|------|----------|
| **Resource** | "$0 budget", "$1M budget", "1 person only" |
| **Time** | "24 hours", "10 years", "real-time" |
| **Anti-feature** | "No software", "No internet", "No employees" |
| **Stakeholder** | "For a 5-year-old", "For an expert", "For your enemy" |
| **Technical** | "Using only paper", "Voice-only", "No electricity" |
| **Scale** | "For 1 person", "For 1 million users", "For 1 country" |
| **Location** | "In rural Africa", "In space", "Underwater" |
| **Inversion** | "Users pay us → We pay users", "We deliver → They come to us" |

---

## TRIZ Principles

**Top 10 for AI ideation:**

| # | Principle | Description |
|---|-----------|-------------|
| 1 | Segmentation | Divide into independent parts |
| 2 | Taking out | Separate interfering part |
| 3 | Local quality | Different parts do different things |
| 4 | Asymmetry | Replace symmetry with asymmetry |
| 5 | Merging | Bring closer, combine in time |
| 6 | Universality | One part performs multiple functions |
| 7 | Nesting | Place one inside another |
| 13 | The other way around | Invert the action |
| 15 | Dynamics | Allow characteristics to change |
| 19 | Periodic action | Use pulses instead of continuous |

**Full 40 principles:** See [techniques.md](techniques.md#triz-ai-quick-method) for complete list.

**Prompt pattern:** `"Apply TRIZ principle [segmentation] to solve: [problem]"`
