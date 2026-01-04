# Advanced TRIZ Tools

Reference for Su-Field Analysis, 76 Standard Solutions, ARIZ, and Evolution Trends.

## Table of Contents

1. [Su-Field Analysis](#su-field-analysis)
2. [76 Standard Solutions](#76-standard-solutions)
3. [ARIZ Algorithm](#ariz-algorithm)
4. [Evolution Trends](#evolution-trends)

---

## Su-Field Analysis

### Overview

Su-Field (Substance-Field) Analysis models technical systems as interactions between substances and fields.

### Basic Structure

A minimal working system requires 3 elements:

```
     F (Field)
       ↓
S1 ←—————→ S2
(Tool)    (Object)
```

- **S1**: Tool (the acting substance)
- **S2**: Object (the substance being acted upon)
- **F**: Field (the energy/means of interaction)

### Types of Fields

| Field Type | Examples |
|------------|----------|
| Mechanical | Force, pressure, vibration, acoustic |
| Thermal | Heat, cold |
| Chemical | Reactions, catalysis |
| Electrical | Current, charge |
| Magnetic | Magnetism, electromagnetic |
| Optical | Light, laser |
| Gravitational | Weight, centrifugal |

### Problem Models

| Model Type | Description | Solution Direction |
|------------|-------------|-------------------|
| **Incomplete** | Missing S1, S2, or F | Add missing element |
| **Insufficient** | System works poorly | Improve/modify elements |
| **Harmful** | Unwanted interaction | Block/eliminate harm |

### Incomplete Su-Field

Problem: System has only 1-2 elements.

```
Missing F:   S1 .... S2    → Add a field
Missing S:   F → S1        → Add a tool substance
```

**Solution**: Complete the Su-Field by adding missing element.

### Insufficient Su-Field

Problem: Interaction is weak or ineffective.

**Solutions**:
1. Replace F with stronger field
2. Add another field (F2)
3. Modify S1 or S2
4. Add ferromagnetic particles + magnetic field

### Harmful Su-Field

Problem: Unwanted harmful effect exists.

```
     F (harmful)
       ↓
S1 ←——×——→ S2
```

**Solutions**:
1. Insert S3 between S1 and S2
2. Add F2 to counteract harmful F
3. Modify S1 or S2 to be unaffected
4. Eliminate source of harm

---

## 76 Standard Solutions

### Overview

The 76 Standard Solutions are organized into 5 classes based on problem type.

### Class Structure

| Class | Purpose | # of Standards |
|-------|---------|---------------|
| 1 | Building/destroying Su-Fields | 13 |
| 2 | Improving Su-Fields | 23 |
| 3 | System transitions | 6 |
| 4 | Detection and measurement | 17 |
| 5 | Helpers (simplification) | 17 |

### Class 1: Building/Destroying Su-Fields (13 standards)

**1.1 Building Su-Fields**
- 1.1.1: If object is hard to change, add easily-changed substance
- 1.1.2: If system needs internal additive, use existing internal resources
- 1.1.3: If external additive needed, use existing external resources
- 1.1.4: Use environmental resources
- 1.1.5: Add temporary additives
- 1.1.6: Use large quantity of cheap substance
- 1.1.7: Use field instead of substance
- 1.1.8: Use combination of fields

**1.2 Destroying Su-Fields**
- 1.2.1: Eliminate harmful effect by adding S3
- 1.2.2: Eliminate harmful effect by modifying S1 or S2
- 1.2.3: Counteract harmful field with opposite field
- 1.2.4: Turn harmful action into useful
- 1.2.5: De-activate harmful field by using another field

### Class 2: Improving Su-Fields (23 standards)

**2.1 Transition to complex Su-Fields**
- Add chain of substances
- Add parallel substances

**2.2 Increasing field effectiveness**
- Use ferromagnetic particles + magnetic field
- Use capillary/porous structures
- Increase segmentation

**2.3 Rhythmic coordination**
- Match rhythms/frequencies of actions
- Use resonance

**2.4 Use of ferromagnetic materials**
- Replace ordinary substance with ferromagnetic
- Use magnetic fluid

### Class 3: System Transitions (6 standards)

- Transition to bi-system or poly-system
- Develop links between systems
- Transition to micro-level
- Add empty space (voids)
- Use phase transitions
- Use physical/chemical effects

### Class 4: Detection and Measurement (17 standards)

**4.1 Indirect methods**
- Measure copies/images instead of object
- Measure related parameters

**4.2 Adding elements**
- Add easily-detectable substances
- Use markers

**4.3 Improving measurements**
- Use field changes for detection
- Use resonance phenomena

### Class 5: Helpers/Simplification (17 standards)

**5.1 Using derivatives**
- Use by-products
- Use fields from object

**5.2 Introducing voids**
- Inflatable/porous structures
- Use negative space

**5.3 Phase/state changes**
- Use dual-state substances
- Exploit transition phenomena

---

## ARIZ Algorithm

### Overview

ARIZ (Algorithm of Inventive Problem Solving) is the most powerful TRIZ tool for complex problems. Current version: ARIZ-85C.

### When to Use

- 85% of problems can be solved with simpler tools
- Use ARIZ for remaining 15% (most complex problems)
- Use when Contradiction Matrix doesn't provide solution

### The 9 Parts of ARIZ

#### Part 1: Problem Analysis
1. Define the mini-problem
2. Identify conflicting elements
3. Make graphical models
4. Choose a conflict (if multiple)

#### Part 2: Problem Model Analysis
1. Identify operational zone
2. Identify operational time
3. Define substance-field resources

#### Part 3: Ideal Final Result (IFR)
1. Formulate IFR: "X-element, without complicating the system, eliminates [harm] while maintaining [useful action]"
2. Intensify the formulation
3. Define physical contradiction

#### Part 4: Mobilizing Resources
1. List resources in operational zone
2. Model with Su-Field analysis
3. Consider system, supersystem, environment resources

#### Part 5: Apply Knowledge Base
1. Use physical effects database
2. Apply 76 Standard Solutions
3. Use Contradiction Matrix
4. Consider analogous problems

#### Part 6: Change or Reformulate Problem
1. If stuck, reformulate problem
2. Consider dual problem
3. Return to Part 1 with new formulation

#### Part 7: Analyze Solution Method
1. Evaluate solution quality
2. Compare to IFR
3. Check for new contradictions

#### Part 8: Apply Solution
1. Determine implementation requirements
2. Analyze subsystem changes
3. Analyze supersystem changes

#### Part 9: Analyze Problem-Solving Process
1. Compare actual path to ideal
2. Document lessons learned
3. Update knowledge base

### Key ARIZ Concepts

**Mini-Problem**: Simplify by keeping existing system, just eliminate deficiency.

**Physical Contradiction Intensification**:
- Must be [Property] to do X
- Must be [Opposite Property] to do Y
- Make properties as extreme as possible

**Separation Principles**:
- In time
- In space
- In condition
- In scale/level

---

## Evolution Trends

### Overview

Technical systems evolve following predictable patterns. Use these to forecast and guide innovation.

### The 8 Laws of Technical System Evolution

#### 1. S-Curve Stages

All technologies follow 4 stages:

```
Performance
    ↑
    |           ╭────── Maturity/Decline
    |         ╱
    |       ╱   Growth
    |     ╱
    |   ╱
    | ╱ Infancy
    +─────────────────→ Time
```

| Stage | Characteristics | Strategy |
|-------|-----------------|----------|
| Infancy | Low performance, high invention rate | Invest in R&D |
| Growth | Rapid improvement | Scale up |
| Maturity | Plateau, optimization | Efficiency focus |
| Decline | New tech emerges | Transition/exit |

#### 2. Increasing Ideality

Systems evolve toward higher ideality:

`Ideality = (Sum of Benefits) / (Sum of Cost + Harm)`

Ultimate: Ideal system doesn't exist, but function is delivered.

#### 3. Non-Uniform Development of Parts

Different parts evolve at different rates. Weakest parts limit system performance.

**Action**: Identify and improve limiting subsystems.

#### 4. Increasing Dynamism and Controllability

Evolution path:
```
Rigid → Jointed → Flexible → Fluid → Field-based
```

**Examples**:
- Solid → hinged → bendable → liquid → electromagnetic
- Manual → semi-auto → automatic → AI-controlled

#### 5. Increasing Complexity Then Simplification

```
Simple → Complex → Simplified (integrated)
```

First: add functions/parts
Then: integrate, trim, optimize

#### 6. Matching and Mismatching Parts

Parts must match for efficient energy transfer.
Deliberately mismatch for new effects.

#### 7. Transition to Micro-Level

```
Macro → Micro → Nano → Field
```

**Examples**:
- Mechanical switches → transistors → molecular switches
- Bulk materials → particles → molecules → fields

#### 8. Increasing Human Involvement Then Reduction

```
Manual → Tool-aided → Mechanized → Automated → Autonomous
```

### Additional Evolution Trends

| Trend | From → To |
|-------|-----------|
| Segmentation | Monolithic → Segmented → Powder → Field |
| Surface | Flat → 3D texture → Active surface |
| Symmetry | Symmetric → Asymmetric → Optimized |
| Nesting | Single → Nested → Multi-nested |
| Coordination | Uncoordinated → Resonant → Optimized |
| Action | Continuous → Periodic → Optimized pattern |
| Control | Open loop → Feedback → Feedforward |

### Using Evolution Trends

1. **Locate current position** on evolution curves
2. **Identify next step** from trends
3. **Generate ideas** using suggested direction
4. **Combine trends** for breakthrough innovation

### Example: Mobile Phone Evolution

| Trend | Past | Present | Future |
|-------|------|---------|--------|
| Dynamism | Fixed → Portable | Flexible screens | Rollable/foldable |
| Micro-level | Analog → Digital | Nano processors | Quantum? |
| Ideality | Multiple devices | Smartphone | Wearable/invisible |
| Segmentation | One device | Modular | Cloud-distributed |

---

## Choosing the Right Tool

| Problem Complexity | Tool |
|-------------------|------|
| Simple contradiction | Contradiction Matrix |
| Need quick ideas | 40 Principles browsing |
| System improvement | Su-Field + Standards |
| Forecast future | Evolution Trends |
| Very complex | ARIZ |
| Multiple contradictions | ARIZ |
