# TRIZ + AI Prompt Templates

AI-enhanced prompts for systematic innovation using Large Language Models.

Based on research from: [AutoTRIZ](https://arxiv.org/html/2403.13002v2), [TRIZ-GPT](https://arxiv.org/html/2408.05897v1), [TRIZ Agents](https://arxiv.org/html/2506.18783v1), [ccTOPP Project](https://www.triz-consulting.de), and [TRIZ+AI V3.0](https://www.triz-consulting.de/wp-content/uploads/2024/04/TRIZ_and_Generative_AI-V3.0.pdf).

---

## Table of Contents

1. [Level 1 Prompts](#level-1-prompts) - Basic TRIZ Tools
2. [Level 2 Prompts](#level-2-prompts) - Intermediate Tools
3. [Level 3 Prompts](#level-3-prompts) - Advanced Tools
4. [Creative Mode Prompts](#creative-mode-prompts) - Cross-Industry Innovation
5. [Prompt Engineering Tips](#prompt-engineering-tips)

---

## Level 1 Prompts

### 1.1 Ideal Final Result (IFR)

**Purpose:** Define the perfect solution before problem-solving.

```markdown
## IFR Prompt Template

[Context] The Ideal Final Result (IFR) in TRIZ describes a system that delivers its main function without existing and without any harmful side effects. Ideality = Benefits / (Costs + Harm).

[Examples]
- The ideal lawn mower cuts grass to desired length without existing and without harmful side effects.
- The ideal car key opens/closes/starts/stops the car without existing and without harmful side effects.

[Instruction]
Step 1: Describe your technical system: [USER INPUT]
Step 2: Formulate the IFR using this template:
"The ideal [system] [performs main function] WITHOUT [costs/complexity/harm]"

Step 3: Identify what prevents achieving this IFR.
Step 4: List any systems that already achieve something similar.
```

---

### 1.2 Contradiction Analysis + 40 Principles

**Purpose:** Identify contradictions and find inventive principles to resolve them.

```markdown
## Contradiction Analysis Prompt (Chain-of-Thought)

You are a TRIZ Specialist. Help me analyze a technical problem using the Contradiction Matrix.

[Problem Description]
{Describe your problem here}

[Step-by-Step Analysis]

**Step 1: Identify the Improvement Goal**
What parameter do you want to IMPROVE?
(Refer to the 39 TRIZ parameters: Speed, Strength, Weight, Reliability, etc.)

**Step 2: Identify the Worsening Effect**
When you try to improve the above, what parameter gets WORSE?
(This creates the technical contradiction)

**Step 3: Map to TRIZ Parameters**
- Improving Parameter: #__ [Name]
- Worsening Parameter: #__ [Name]

**Step 4: Look Up Principles**
Based on the Contradiction Matrix, the suggested principles are: [#, #, #, #]

**Step 5: Generate Solutions**
For each principle, describe how it could apply to this specific problem:

| Principle | How to Apply | Specific Idea |
|-----------|--------------|---------------|
| #__ [Name] | | |

**Step 6: Evaluate and Select**
Rate each idea on: Feasibility, Impact, Novelty
```

---

### 1.3 Physical Contradiction + Separation Principles

**Purpose:** Resolve contradictions where one element needs opposite properties.

```markdown
## Physical Contradiction Prompt

[Context] A physical contradiction occurs when the same element must have OPPOSITE properties simultaneously.

[Template]
"[Element] must be [Property A] to achieve [Goal X]
AND must be [Opposite of Property A] to achieve [Goal Y]"

[Example]
"Coffee must be HOT to taste good AND COLD to drink quickly"

[Instruction]
Step 1: State your physical contradiction using the template above.

Step 2: Apply Separation Principles:

| Separation | Question | Your Solution |
|------------|----------|---------------|
| **In Time** | Can the property change at different times? | |
| **In Space** | Can different parts have different properties? | |
| **In Condition** | Can the property depend on external conditions? | |
| **In Scale** | Can it be different at micro vs macro level? | |

Step 3: Generate at least one concrete solution for each separation principle.
```

---

### 1.4 9-Screen System Operator

**Purpose:** Analyze a system across time and levels for comprehensive understanding.

```markdown
## 9-Screen Analysis Prompt

[Context] The 9-Screen (System Operator) analyzes a system across:
- **Levels:** Supersystem → System → Subsystem
- **Time:** Past → Present → Future

[Instruction]
Describe your system: [USER INPUT]

Generate a 9-screen analysis:

| Level/Time | PAST | PRESENT | FUTURE |
|------------|------|---------|--------|
| **Supersystem** | Components that interact with past system | Components interacting with current system | Predicted supersystem evolution |
| **System** | Predecessor system | Current system to analyze | Future system based on trends |
| **Subsystem** | Components of past system | Current components | Predicted component evolution |

[Rules]
- Identify at least 3 components for each supersystem/subsystem cell
- Consider TRIZ Evolution Trends for the Future column
- Summarize the key insight about system evolution
```

---

### 1.5 Root Cause Analysis (TRIZ-Enhanced)

**Purpose:** Find root causes of problems using TRIZ perspective.

```markdown
## Root Cause Analysis Prompt

You are a TRIZ Consultant analyzing a technical problem.

[Problem]: {Describe the problem}

[Step-by-Step Process]

**Step 1: Define the Undesired Effect**
What is the negative result you observe?

**Step 2: Ask "Why?" Chain (5 Whys + TRIZ)**
For each cause, also consider:
- What FIELD is involved? (Mechanical, Thermal, Chemical, Electrical, Magnetic, etc.)
- What SUBSTANCES are interacting?
- What RESOURCES are being used/wasted?

| Why Level | Cause | Field/Substance Involved |
|-----------|-------|--------------------------|
| Why 1 | | |
| Why 2 | | |
| Why 3 | | |
| Why 4 | | |
| Why 5 (Root) | | |

**Step 3: Identify Controllable vs Uncontrollable Factors**

**Step 4: Formulate as TRIZ Contradiction**
"If we [action], then [improvement] BUT [worsening]"

**Step 5: Suggest Inventive Principles for Resolution**
```

---

## Level 2 Prompts

### 2.1 Su-Field Analysis

**Purpose:** Model problems as Substance-Field interactions.

```markdown
## Su-Field Analysis Prompt

[Context] Su-Field (Substance-Field) analysis models technical systems as:
- **S1**: Tool (acting substance)
- **S2**: Object (substance being acted upon)
- **F**: Field (energy/means of interaction)

Fields include: Mechanical, Thermal, Chemical, Electrical, Magnetic, Optical, Gravitational

[Instruction]
Step 1: Describe your technical system problem.

Step 2: Identify the Su-Field elements:
- S1 (Tool): ___
- S2 (Object): ___
- F (Field): ___

Step 3: Classify the problem type:

| Type | Description | Check |
|------|-------------|-------|
| **Incomplete** | Missing S1, S2, or F | [ ] |
| **Insufficient** | Interaction too weak | [ ] |
| **Harmful** | Unwanted negative effect | [ ] |

Step 4: Apply the appropriate solution pattern:

**For Incomplete:**
→ Add the missing element

**For Insufficient:**
→ Add another field (F2)
→ Modify S1 or S2
→ Add ferromagnetic particles + magnetic field

**For Harmful:**
→ Insert S3 between S1 and S2
→ Add F2 to counteract harmful F
→ Modify S1/S2 to be unaffected

Step 5: Generate at least 2 concrete solutions using this pattern.
```

---

### 2.2 76 Standard Solutions

**Purpose:** Apply standardized solutions based on Su-Field patterns.

```markdown
## 76 Standards Quick Reference Prompt

Based on your Su-Field analysis, select the appropriate class:

| Class | Problem Type | # Solutions |
|-------|-------------|-------------|
| 1 | Build/Destroy Su-Fields | 13 |
| 2 | Improve Su-Fields | 23 |
| 3 | System Transitions | 6 |
| 4 | Detection/Measurement | 17 |
| 5 | Simplification | 17 |

[Instruction]
Given problem type: [incomplete/insufficient/harmful/measurement/simplification]

Suggest relevant standards from the appropriate class and explain how each could apply to the specific problem.

Format your response as:
| Standard # | Description | Application to Problem |
|-----------|-------------|------------------------|
```

---

### 2.3 Trimming

**Purpose:** Simplify systems by removing components while preserving function.

```markdown
## Trimming Analysis Prompt

[Context] Trimming removes system components while maintaining useful functions by:
1. Transferring functions to remaining components
2. Using resources already available
3. Making functions unnecessary

[Rules for Trimming]
- A component CAN be trimmed if its function is performed by another component
- A component CAN be trimmed if its function becomes unnecessary
- A component CAN be trimmed if the object of its function is eliminated

[Instruction]
Step 1: List all components of your system with their functions.

| Component | Main Function | Function Object |
|-----------|---------------|-----------------|
| | | |

Step 2: For each component, evaluate trimming possibility:

| Component | Can Another Do This? | Is It Necessary? | Can Object Be Eliminated? |
|-----------|---------------------|------------------|---------------------------|
| | | | |

Step 3: Identify trimming candidates and propose how to redistribute their functions.

Step 4: Describe the trimmed system and calculate ideality improvement.
```

---

### 2.4 Feature Transfer

**Purpose:** Transfer beneficial features from alternative systems.

```markdown
## Feature Transfer Prompt

[Context] Feature Transfer identifies useful features in alternative systems and adapts them to your system.

[Instruction]
Step 1: Define your system and its main function.

Step 2: Identify 3-5 alternative systems that perform similar functions.

| Alternative System | Industry/Domain | Key Feature |
|--------------------|-----------------|-------------|
| | | |

Step 3: For each feature, analyze transferability:

| Feature | What makes it work? | How to adapt for your system? | Barriers? |
|---------|---------------------|-------------------------------|-----------|
| | | | |

Step 4: Generate concrete transfer ideas with implementation sketches.
```

---

## Level 3 Prompts

### 3.1 ARIZ (Algorithm of Inventive Problem Solving)

**Purpose:** Systematic algorithm for the most complex problems.

```markdown
## ARIZ-Lite Prompt (Simplified 9-Part Process)

[Context] ARIZ is the most powerful TRIZ tool for complex problems that resist simpler methods. This is a streamlined version.

[Instruction] Follow each part step-by-step:

**Part 1: Problem Analysis**
- State the mini-problem (keep existing system, eliminate ONE deficiency)
- Identify conflicting elements
- Draw the operational zone (where conflict occurs)

**Part 2: Problem Model**
- Operational Zone (WHERE): ___
- Operational Time (WHEN): ___
- Available Resources: ___

**Part 3: Ideal Final Result**
"The X-element, WITHOUT complicating the system, eliminates [harmful action] WHILE maintaining [useful action] during [operational time] within [operational zone]"

**Part 4: Physical Contradiction**
"[Element] must be [Property] to [do X] AND [Opposite] to [do Y]"
Intensify: Make properties as EXTREME as possible.

**Part 5: Apply Separation Principles**
- In Time
- In Space
- In Condition
- In Scale

**Part 6: Apply Knowledge Base**
- Physical effects that might help
- Similar solved problems
- 40 Inventive Principles

**Part 7: Evaluate Solution**
- Does it approach IFR?
- Any new contradictions created?
- Is it implementable?

**Part 8: Apply Solution**
- What changes to subsystems?
- What changes to supersystem?

**Part 9: Document Learning**
- What pattern can be reused?
- Update your knowledge base
```

---

### 3.2 Evolution Trends (TESE)

**Purpose:** Predict technology evolution and generate innovation directions.

```markdown
## Evolution Trends Analysis Prompt

[Context] Technical systems evolve following predictable patterns. Use these to forecast and guide innovation.

[The 8 Laws of Technical System Evolution]

1. **S-Curve Stages:** Infancy → Growth → Maturity → Decline
2. **Increasing Ideality:** Benefits / (Cost + Harm) → Maximum
3. **Non-Uniform Development:** Weakest part limits system
4. **Increasing Dynamism:** Rigid → Jointed → Flexible → Fluid → Field
5. **Complexity Then Simplification:** Simple → Complex → Integrated
6. **Matching/Mismatching:** Parts must match OR deliberately mismatch
7. **Transition to Micro-Level:** Macro → Micro → Nano → Field
8. **Increasing Automation:** Manual → Mechanized → Automated → Autonomous

[Instruction]
Analyze your system: [USER INPUT]

| Trend | Current Position | Next Evolution Step | Innovation Idea |
|-------|-----------------|---------------------|-----------------|
| S-Curve | | | |
| Dynamism | | | |
| Micro-Level | | | |
| Automation | | | |

Generate 3-5 innovation concepts based on the next evolution steps.
```

---

### 3.3 Function Oriented Search (FOS)

**Purpose:** Find solutions by searching for the same function in other industries.

```markdown
## Function Oriented Search (FOS) Prompt

[Context] FOS finds innovative solutions by identifying how OTHER industries solve the SAME function.

[4-Step FOS Process]

**Step 1: Identify Core Function**
What is the fundamental function your system must perform?
Format: [Action Verb] + [Object]
Example: "Remove ice" not "De-ice airplane wings"

**Step 2: Generalize the Function**
Abstract to a broader level:
- Remove ice → Remove solid deposit → Remove unwanted material → Separate materials

**Step 3: Search Analogous Domains**
"Find 5-7 industries that perform the function: [generalized function]"

| Industry | System/Technology | How It Works | Key Mechanism |
|----------|-------------------|--------------|---------------|
| | | | |

**Step 4: Transfer and Adapt**
For each analog, evaluate:
- What makes this solution work?
- What's the underlying principle?
- How to adapt to my system?
- What are the barriers?

**Step 5: Generate Concrete Solutions**
Develop at least 3 specific solutions based on the most promising analogs.
```

---

### 3.4 Method Oriented Search (MOS)

**Purpose:** Search for systems that use a specific method or principle.

```markdown
## Method Oriented Search (MOS) Prompt

[Context] MOS finds applications for a known method/principle in new domains.

[Process]
**Step 1: Define the Method/Principle**
What method or physical principle are you interested in applying?
Example: "Ultrasonic vibration", "Shape memory alloy", "Magnetic levitation"

**Step 2: Identify Current Applications**
Where is this method currently used?

| Current Application | Industry | How It's Used |
|---------------------|----------|---------------|
| | | |

**Step 3: Abstract the Method's Key Benefit**
What fundamental advantage does this method provide?
(e.g., "contactless manipulation", "reversible deformation", "no friction")

**Step 4: Brainstorm New Applications**
"What problems could benefit from [key benefit]?"

| Problem Domain | Current Solution | How Method Could Help |
|----------------|------------------|----------------------|
| | | |

**Step 5: Feasibility Analysis**
For the most promising applications, analyze:
- Technical feasibility
- Economic viability
- Implementation barriers
```

---

### 3.5 Resources Analysis

**Purpose:** Identify hidden resources in and around the system.

```markdown
## Resources Analysis Prompt

[Context] Every system contains underutilized resources. Finding and using these resources increases ideality.

[Resource Categories]

| Category | Examples | In Your System? |
|----------|----------|-----------------|
| **Substance** | Materials, waste, byproducts | |
| **Field/Energy** | Heat, vibration, gravity, magnetic | |
| **Space** | Empty volumes, surfaces, interfaces | |
| **Time** | Idle time, parallel processing, pre/post | |
| **Information** | Signals, data, patterns | |
| **Functional** | Unused capabilities of components | |

[Instruction]
Step 1: Map all resources available in:
- The system itself
- The supersystem (environment)
- The subsystems (components)
- Waste/byproducts

Step 2: For each resource, ask:
- Can this be used instead of adding something new?
- Can this perform a missing function?
- Can this solve the contradiction?

Step 3: Generate resource-based solutions that don't add cost or complexity.
```

---

## Creative Mode Prompts

### Cross-Industry Innovation (FOS + Creativity)

**Purpose:** Combine TRIZ with creative thinking for breakthrough innovation.

```markdown
## Cross-Industry Innovation Prompt

[Process: Abstract → Map → Search → Generalize → Apply]

**Step 1: ABSTRACT**
Define the core function in the most general terms possible.
[Your System] → [Core Function] → [Most Abstract Function]

Example:
Airplane de-icing → Remove ice → Remove unwanted solid → Separate materials → Change state

**Step 2: MAP Analogous Domains**
List 5-7 completely different industries/domains that perform this abstract function:

| Domain | System | How It Works |
|--------|--------|--------------|
| Nature (Biomimicry) | | |
| Medicine | | |
| Food Industry | | |
| Construction | | |
| Entertainment | | |

**Step 3: SEARCH for Surprising Solutions**
For each domain, find the most innovative or unusual approach.

**Step 4: GENERALIZE Principles**
What transferable principles emerge from these analogs?

| Analog | Underlying Principle | Could Apply Because... |
|--------|---------------------|------------------------|
| | | |

**Step 5: APPLY to Original Problem**
Generate 3-5 breakthrough concepts by combining principles with your original problem.

Format each concept as:
- **Concept Name:**
- **Principle Used:**
- **How It Works:**
- **Key Advantage:**
- **Challenge to Solve:**
```

---

### SCAMPER + TRIZ Hybrid

**Purpose:** Combine SCAMPER's intuitive brainstorming with TRIZ's systematic approach.

```markdown
## SCAMPER-TRIZ Hybrid Prompt

[Context] SCAMPER provides quick ideation triggers. TRIZ provides deep problem-solving rigor.

**Step 1: SCAMPER Brainstorm**
Apply each SCAMPER trigger to your system:

| Letter | Trigger | Ideas |
|--------|---------|-------|
| S | Substitute: What can be replaced? | |
| C | Combine: What can be merged? | |
| A | Adapt: What can be borrowed from elsewhere? | |
| M | Modify: What can be changed (size, shape, color)? | |
| P | Put to other use: New applications? | |
| E | Eliminate: What can be removed? | |
| R | Reverse: What can be flipped/inverted? | |

**Step 2: TRIZ Analysis**
For each promising SCAMPER idea:
1. What contradiction does this create?
2. Which 40 Principles could resolve it?
3. What resources are needed vs available?

**Step 3: Refined Solutions**
Combine SCAMPER intuition with TRIZ rigor to generate implementable solutions.
```

---

## Prompt Engineering Tips

### Best Practices for TRIZ + LLM

1. **Use Chain-of-Thought (CoT)**
   - Break complex reasoning into explicit steps
   - "Let's solve this step by step..."

2. **Use Role Prompting**
   - "You are a TRIZ Master Consultant..."
   - "Act as an innovation expert using TRIZ methodology..."

3. **Use Few-Shot Examples**
   - Provide 1-2 solved examples before your problem
   - Show the expected output format

4. **Be Specific About Output Format**
   - Request tables, numbered lists, or structured formats
   - Specify required sections

5. **Iterate and Refine**
   - First prompt: Get broad analysis
   - Follow-up: Drill into specific principles
   - Final: Request concrete implementations

### Prompt Structure Template

```markdown
[ROLE] You are a [specific TRIZ expertise]

[CONTEXT] Brief background on the methodology being used

[TASK] Clear instruction of what to do

[INPUT] The specific problem/system to analyze

[FORMAT] How to structure the output

[CONSTRAINTS] Any limitations or requirements
```

---

## References

- [AutoTRIZ Paper (2024)](https://arxiv.org/html/2403.13002v2)
- [TRIZ-GPT Paper (2024)](https://arxiv.org/html/2408.05897v1)
- [TRIZ Agents Paper (2025)](https://arxiv.org/html/2506.18783v1)
- [TRIZ+AI V3.0 (Tanasak/Adunka)](https://www.triz-consulting.de/wp-content/uploads/2024/04/TRIZ_and_Generative_AI-V3.0.pdf)
- [GitHub: triz-prompt-engineering](https://github.com/jenson500/triz-prompt-engineering)
- [ccTOPP Project](https://www.triz-consulting.de/about-triz/artificial-intelligence-and-triz-a-synergy-for-innovation/?lang=en)
