# QUEST Matrix: Systematic Query Generation

A framework for generating comprehensive search queries that cover all angles of a topic.

## Overview

**QUEST** = **Q**uestions + **U**niverses + **E**xpansions + **S**copes + **T**ypes

| Dimension | Purpose | Output |
|-----------|---------|--------|
| **Q** - Questions | Ensure question completeness | 5W1H decomposition |
| **U** - Universes | Multi-stakeholder coverage | Perspective-based queries |
| **E** - Expansions | Semantic breadth | Synonym/related term queries |
| **S** - Scopes | Boundary exploration | Geographic/temporal/scale queries |
| **T** - Types | Source diversity | Queries targeting different source types |

**Goal:** Generate 15-25 queries that ensure no major angle is missed.

---

## Step 1: Questions (5W1H Decomposition)

For any topic, decompose into fundamental questions:

| Question | Focus | Example Queries |
|----------|-------|-----------------|
| **Who** | Actors, affected parties, experts, authorities | "[topic] experts", "[topic] stakeholders" |
| **What** | Definition, components, variations, examples | "[topic] definition", "[topic] types" |
| **When** | Timeline, evolution, milestones, current state | "[topic] history", "[topic] 2025" |
| **Where** | Geography, contexts, platforms, industries | "[topic] by country", "[topic] use cases" |
| **Why** | Causes, motivations, drivers, purpose | "[topic] benefits", "[topic] reasons" |
| **How** | Mechanisms, processes, methods, implementation | "[topic] how it works", "[topic] implementation" |

### Template

```markdown
## 5W1H for "[TOPIC]"

- **Who:** [List actors, experts, affected parties]
- **What:** [Define, list components/variations]
- **When:** [Timeline, milestones, current state]
- **Where:** [Contexts, platforms, industries, regions]
- **Why:** [Drivers, motivations, benefits sought]
- **How:** [Mechanisms, processes, implementation methods]
```

---

## Step 2: Universes (Stakeholder Perspectives)

Different stakeholders care about different aspects. Generate queries from each viewpoint:

| Stakeholder | Key Concerns | Query Pattern |
|-------------|--------------|---------------|
| **End Users** | Pain points, benefits, experience | "[topic] user experience reviews" |
| **Providers/Vendors** | Challenges, opportunities, differentiation | "[topic] implementation challenges" |
| **Regulators** | Compliance, risks, policy | "[topic] regulation policy 2025" |
| **Competitors** | Benchmarks, alternatives | "[topic] vs [alternative] comparison" |
| **Experts/Researchers** | Best practices, innovations, studies | "[topic] research paper" |
| **Critics/Skeptics** | Limitations, failures, risks | "[topic] criticism problems limitations" |

### Template

```markdown
## Stakeholder Queries for "[TOPIC]"

| Stakeholder | Question They'd Ask | Search Query |
|-------------|---------------------|--------------|
| End Users | "Is this worth it for me?" | "[topic] user reviews pros cons" |
| Providers | "How do I implement this well?" | "[topic] best practices implementation" |
| Regulators | "What are the risks?" | "[topic] risks compliance" |
| Competitors | "How does this compare?" | "[topic] vs alternatives comparison" |
| Experts | "What does research say?" | "[topic] research study findings" |
| Critics | "What could go wrong?" | "[topic] failures problems criticism" |
```

---

## Step 3: Expansions (Semantic Breadth)

Expand terminology to catch content using different words:

| Expansion Type | Method | Example |
|----------------|--------|---------|
| **Synonyms** | Alternative words for same concept | "AI assistant" → "AI copilot", "AI helper" |
| **Related Terms** | Adjacent concepts | "AI coding" → "code generation", "autocomplete" |
| **Domain Jargon** | Industry-specific terminology | "productivity" → "developer velocity", "DORA metrics" |
| **Alternative Framings** | Different perspectives on same thing | "AI replacing jobs" → "AI augmenting work" |

### Template

```markdown
## Semantic Expansion for "[TOPIC]"

| Core Term | Synonyms | Related Terms | Domain Jargon |
|-----------|----------|---------------|---------------|
| [Main term] | [List 2-3] | [List 2-3] | [List 2-3] |
| [Sub-term 1] | [List] | [List] | [List] |
| [Sub-term 2] | [List] | [List] | [List] |
```

---

## Step 4: Scopes (Boundary Exploration)

Explore different boundaries and contexts:

| Scope | Dimensions | Query Examples |
|-------|------------|----------------|
| **Geographic** | Local vs Global vs Regional | "[topic] Thailand", "[topic] Asia", "[topic] global trends" |
| **Temporal** | Past vs Present vs Future | "[topic] history evolution", "[topic] 2025", "[topic] future predictions" |
| **Scale** | Micro vs Meso vs Macro | "[topic] individual", "[topic] enterprise", "[topic] industry-wide" |
| **Context** | Different application domains | "[topic] in healthcare", "[topic] in finance", "[topic] for startups" |

### Template

```markdown
## Scope Variations for "[TOPIC]"

**Geographic:**
- Local: "[topic] [country/region]"
- Global: "[topic] global trends worldwide"

**Temporal:**
- Historical: "[topic] history evolution"
- Current: "[topic] 2025 state of the art"
- Future: "[topic] future trends predictions"

**Scale:**
- Individual: "[topic] for individuals personal"
- Organization: "[topic] enterprise business"
- Industry: "[topic] industry impact"
```

---

## Step 5: Types (Source Diversity)

Target different source types for balanced information:

| Source Type | Characteristics | Query Modifier |
|-------------|-----------------|----------------|
| **Academic** | Peer-reviewed, rigorous, may be dated | "[topic] research paper arxiv" |
| **Industry** | Practical, current, may be biased | "[topic] industry report gartner" |
| **News** | Current, accessible, may lack depth | "[topic] news 2025" |
| **Official** | Authoritative, formal | "[topic] official government" |
| **User-Generated** | Real experiences, varied quality | "[topic] reddit forum discussion" |
| **Expert Opinion** | Informed views, may be subjective | "[topic] expert analysis opinion" |

### Template

```markdown
## Source Type Queries for "[TOPIC]"

| Type | Query |
|------|-------|
| Academic | "[topic] research study peer-reviewed" |
| Industry | "[topic] industry report analysis" |
| News | "[topic] news latest 2025" |
| Official | "[topic] official guidelines" |
| User | "[topic] reddit user experience" |
| Expert | "[topic] expert interview opinion" |
```

---

## Complete QUEST Workflow

### Phase 2: PLAN - Query Generation Checklist

Before searching, complete this checklist:

```markdown
## QUEST Query Generation for "[TOPIC]"

### Q - Questions (5W1H)
- [ ] Who queries generated (2+ queries)
- [ ] What queries generated (2+ queries)
- [ ] Why/How queries generated (2+ queries)

### U - Universes (Stakeholders)
- [ ] User perspective query
- [ ] Provider/expert perspective query
- [ ] Critic/skeptic perspective query

### E - Expansions (Semantics)
- [ ] At least 2 synonym variations used
- [ ] Domain-specific terms included

### S - Scopes (Boundaries)
- [ ] Temporal scope addressed (current year included)
- [ ] Geographic scope if relevant

### T - Types (Sources)
- [ ] Academic/research query included
- [ ] Practical/industry query included
- [ ] User experience query included

**Total Queries:** [Count] (Target: 15-25)
**Coverage Score:** [X/12 checklist items]
```

---

## Example: "AI Coding Assistants 2025"

### QUEST Application

**Q - Questions:**
- Who: "AI coding assistant developers users", "GitHub Copilot creators"
- What: "AI coding assistant features capabilities", "code completion vs generation"
- When: "AI coding assistants 2025", "GitHub Copilot evolution history"
- Why: "AI coding assistant benefits productivity", "why developers use AI coding"
- How: "how AI code generation works LLM", "AI coding assistant integration IDE"

**U - Universes:**
- Users: "AI coding assistant developer experience review"
- Providers: "AI coding assistant enterprise deployment challenges"
- Regulators: "AI generated code licensing intellectual property"
- Critics: "AI coding assistant limitations accuracy problems"

**E - Expansions:**
- Synonyms: "AI copilot", "code generation AI", "AI pair programmer"
- Related: "autocomplete", "code suggestions", "intelligent code completion"

**S - Scopes:**
- Temporal: "AI coding 2024 vs 2025", "future of AI coding"
- Scale: "AI coding individual developer", "AI coding enterprise adoption"

**T - Types:**
- Academic: "AI code generation research arxiv"
- Industry: "AI coding assistant market report"
- User: "GitHub Copilot reddit review"

**Total: 22 queries across all dimensions**

---

## Integration with Standard Mode

**When to use:** Phase 2: PLAN, after hypotheses are formed

**Minimum requirements by tier:**
| Tier | Min Queries | Min Dimensions |
|------|-------------|----------------|
| Quick | 8-10 | 3 (Q, U, T) |
| Standard | 15-20 | 4 (Q, U, E, T) |
| Deep | 20-25 | 5 (all) |
| Exhaustive | 25+ | 5 (all, with depth) |

**Output:** List of queries ready for parallel WebSearch execution in Phase 3: RETRIEVE
