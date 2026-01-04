# TRIZ + AI Methodology

How to effectively combine TRIZ with Large Language Models for systematic innovation.

---

## Overview

TRIZ (Theory of Inventive Problem Solving) provides structured frameworks for innovation.
LLMs provide vast knowledge and reasoning capabilities.
Together, they create a powerful human-AI collaboration for problem-solving.

---

## The TRIZ-AI Synergy Model

```
                    ┌─────────────────┐
                    │   Human Expert  │
                    │   (Direction)   │
                    └────────┬────────┘
                             │
              ┌──────────────┼──────────────┐
              ▼              ▼              ▼
        ┌─────────┐    ┌─────────┐    ┌─────────┐
        │  TRIZ   │    │   LLM   │    │ Domain  │
        │Framework│    │Knowledge│    │Expertise│
        └────┬────┘    └────┬────┘    └────┬────┘
              │              │              │
              └──────────────┼──────────────┘
                             ▼
                    ┌─────────────────┐
                    │   Innovative    │
                    │    Solutions    │
                    └─────────────────┘
```

### Role Distribution

| Role | Human | LLM |
|------|-------|-----|
| Problem definition | Lead | Support |
| Contradiction identification | Collaborate | Suggest |
| Knowledge search | Direct | Execute |
| Solution generation | Evaluate | Generate |
| Feasibility assessment | Lead | Support |
| Implementation planning | Lead | Support |

---

## Prompt Engineering Techniques for TRIZ

### 1. Chain-of-Thought (CoT) Prompting

**What:** Ask LLM to reason step-by-step through TRIZ methodology.

**Why:** TRIZ is inherently sequential. CoT ensures each step is properly completed before moving to the next.

**Example:**
```
Let's solve this problem step-by-step using TRIZ:

Step 1: First, identify the main function of the system...
Step 2: Now, what parameter are you trying to improve?
Step 3: When you improve that, what gets worse?
Step 4: Let's map these to TRIZ's 39 parameters...
Step 5: Looking at the contradiction matrix, the suggested principles are...
Step 6: Now let's apply each principle to your specific problem...
```

**Research Finding:** TRIZ-GPT found CoT achieved 0.691 recall for contradiction analysis, outperforming basic prompts.

---

### 2. Role Prompting

**What:** Assign a specific TRIZ expert persona to the LLM.

**Why:** Primes the model to access TRIZ-relevant knowledge and reasoning patterns.

**Example Roles:**

| Role | Use When |
|------|----------|
| "TRIZ Master Consultant" | Complex problems requiring full methodology |
| "Contradiction Analyst" | Focus on identifying and mapping contradictions |
| "Evolution Trends Specialist" | Technology forecasting and roadmapping |
| "Su-Field Expert" | System modeling and interaction analysis |
| "Innovation Facilitator" | Workshop-style guided ideation |

**Template:**
```
You are a TRIZ Master Consultant with 20+ years of experience applying
TRIZ methodology across industries. You have deep knowledge of the
40 Inventive Principles, Contradiction Matrix, ARIZ algorithm, and
Evolution Trends. Guide the user through systematic problem-solving.
```

---

### 3. Few-Shot Prompting

**What:** Provide 1-3 solved examples before the actual problem.

**Why:** Shows the expected reasoning pattern and output format.

**Example:**
```
Here's how TRIZ contradiction analysis works:

EXAMPLE 1:
Problem: Car needs to be faster but engine gets heavier
Improving: Speed (#9)
Worsening: Weight of moving object (#1)
Matrix suggests: Principles 8, 15, 29, 34

EXAMPLE 2:
Problem: Phone needs longer battery but should be thinner
Improving: Duration of action (#15)
Worsening: Length of moving object (#3)
Matrix suggests: Principles 3, 35, 39, 2

NOW ANALYZE:
Problem: [User's problem]
```

**Research Finding:** Few-shot prompting showed superior token efficiency for solution generation in TRIZ-GPT.

---

### 4. Retrieval-Augmented Generation (RAG)

**What:** Supply specific TRIZ knowledge based on the problem context.

**Why:** LLMs may have general TRIZ knowledge but need precise definitions and matrix data.

**What to Retrieve:**

| Problem Stage | Retrieve |
|---------------|----------|
| Parameter mapping | 39 parameters definitions |
| Principle selection | Matrix cell + relevant principles |
| Solution generation | Principle descriptions + examples |
| Evolution analysis | Relevant evolution trends |

**Example (AutoTRIZ approach):**
```
Based on your contradiction:
- Improving: #9 Speed
- Worsening: #27 Reliability

The Contradiction Matrix recommends Principles: 21, 35, 11, 28

Here are the detailed descriptions:
[Inject principle 21 description]
[Inject principle 35 description]
...
```

---

### 5. Multi-Agent Collaboration

**What:** Use multiple specialized AI agents that collaborate on TRIZ problems.

**Why:** Complex problems benefit from diverse perspectives and specialized tools.

**Agent Team Structure (from TRIZ Agents research):**

| Agent | Role | Tools |
|-------|------|-------|
| Project Manager | Workflow coordination | Task delegation |
| TRIZ Specialist | Methodology application | Matrix lookup, principle retrieval |
| Domain Engineers | Technical validation | Domain knowledge |
| Documentation | Report generation | Template formatting |

**Workflow:**
```
1. Project Manager receives problem
2. Domain Engineers identify system components
3. TRIZ Specialist runs contradiction analysis
4. Multiple agents brainstorm solutions
5. Domain Engineers evaluate feasibility
6. Documentation compiles final report
```

---

## TRIZ + AI Workflow Models

### Model 1: AutoTRIZ (Fully Automated)

```
User Problem → [LLM: Extract Parameters] → [Lookup: Contradiction Matrix]
→ [LLM: Generate Solutions] → Solution Report
```

**Best for:** Quick ideation, users with limited TRIZ knowledge
**Limitation:** May miss nuanced problem aspects

---

### Model 2: TRIZ-GPT (LLM-Augmented)

```
User Problem → [LLM: Guided Analysis] → [Human: Validate]
→ [LLM: Principle Application] → [Human: Evaluate] → Solutions
```

**Best for:** Balanced automation and human judgment
**Advantage:** Reduces cognitive load while maintaining quality control

---

### Model 3: Human-Led with AI Support

```
Human Analysis → [AI: Knowledge Retrieval] → Human Synthesis
→ [AI: Expand Ideas] → Human Selection → [AI: Detail Solutions]
```

**Best for:** Expert users, complex/novel problems
**Advantage:** Maximum control and depth of analysis

---

## Quality Assurance

### Validation Checklist

Before accepting AI-generated TRIZ analysis:

- [ ] Is the contradiction correctly identified?
- [ ] Do parameters accurately map to TRIZ's 39 parameters?
- [ ] Are suggested principles from the actual matrix?
- [ ] Do generated solutions actually apply the principles?
- [ ] Are solutions technically feasible?
- [ ] Have multiple principles been explored?

### Common AI Errors in TRIZ

| Error | Detection | Correction |
|-------|-----------|------------|
| Wrong parameter mapping | Compare to 39 parameter definitions | Re-prompt with definitions |
| Made-up principles | Verify against 40 principles list | Constrain to known principles |
| Generic solutions | Check if principle is specifically applied | Ask "How does principle X specifically apply?" |
| Missing contradictions | Look for trade-offs in the problem | Probe "What gets worse when you improve X?" |
| Over-simplified analysis | Check if problem complexity is captured | Break into sub-problems |

---

## Integration with Other Methodologies

### TRIZ + Design Thinking

```
Design Thinking: Empathize → Define → Ideate → Prototype → Test
                     ↓         ↓        ↓
TRIZ Integration: [User study] [IFR] [40 Principles] [Feasibility] [Validate]
```

### TRIZ + Six Sigma DMAIC

| DMAIC Phase | TRIZ Tool |
|-------------|-----------|
| Define | Ideal Final Result |
| Measure | 9-Screen, Function Analysis |
| Analyze | Contradiction Matrix, Root Cause |
| Improve | 40 Principles, Su-Field |
| Control | Evolution Trends |

### TRIZ + Biomimicry

```
1. Abstract problem to function
2. Ask: "How does nature solve [function]?"
3. Apply TRIZ principles to biological analog
4. Transfer back to technical domain
```

---

## Prompt Templates by Use Case

### Quick Ideation (5 min)
```
I have a technical problem: [problem]
What are the top 3 TRIZ principles that might help?
For each, give me one concrete solution idea.
```

### Deep Analysis (30 min)
```
Act as a TRIZ Master. Guide me through full analysis:
1. Help me define the Ideal Final Result
2. Identify the technical contradiction
3. Map to 39 parameters
4. Find principles from the matrix
5. Generate 5+ solutions per principle
6. Evaluate each solution's feasibility
```

### Innovation Workshop
```
We're running a TRIZ innovation workshop on [topic].

Phase 1: Help participants identify contradictions in their systems
Phase 2: For each contradiction, provide the matrix principles
Phase 3: Facilitate ideation using the principles
Phase 4: Help evaluate and prioritize solutions
Phase 5: Create an action plan for top 3 ideas

Format each phase as interactive exercises.
```

---

## Performance Benchmarks

From published research:

| Metric | AutoTRIZ | TRIZ-GPT | Human Expert |
|--------|----------|----------|--------------|
| Speed | Fast (minutes) | Medium (guided) | Slow (hours) |
| Accuracy | Good (validated) | High (with CoT) | Highest |
| Creativity | Broad | Targeted | Deep |
| Feasibility | Variable | Good | Highest |
| Learning curve | None | Low | Years |

**Recommendation:** Use LLM for breadth and speed, human expert for depth and validation.

---

## Tools and Resources

### GitHub Repositories
- [jenson500/triz-prompt-engineering](https://github.com/jenson500/triz-prompt-engineering) - XML prompts (MIT)

### Research Papers
- AutoTRIZ (arXiv:2403.13002)
- TRIZ-GPT (arXiv:2408.05897)
- TRIZ Agents (arXiv:2506.18783)

### Organizations
- [MATRIZ](https://matriz.org) - International TRIZ Association
- [ccTOPP](https://www.triz-consulting.de) - Collaborative TRIZ Prompt Project

### Conferences
- TRAI2025 (Paris-Saclay, Nov 2025) - TRIZ + AI Conference

---

## Summary: When to Use AI with TRIZ

| Scenario | AI Role | Human Role |
|----------|---------|------------|
| Learning TRIZ | Tutor, explain concepts | Practice, ask questions |
| Quick brainstorm | Generate many ideas fast | Filter and develop best ones |
| Knowledge gap | Provide examples from other domains | Apply to specific context |
| Complex problem | Handle parallel analysis | Synthesize and decide |
| Documentation | Format and structure | Review and validate |
| Workshop | Facilitate, provide data | Lead, make decisions |
