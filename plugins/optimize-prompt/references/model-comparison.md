# Model-Specific Optimization Guide

## Overview

Each Claude model has different characteristics that affect prompt optimization:

| Model | Speed | Depth | Prompt Style |
|-------|-------|-------|--------------|
| **Opus** | Slow | Deep, nuanced | Can handle complexity |
| **Sonnet** | Balanced | Good balance | Standard prompts |
| **Haiku** | Fast | Surface-level | Needs more guidance |

---

## Claude Opus 4.5

### Strengths
- Handles complex, multi-step reasoning
- Excellent at nuanced analysis
- Can work with detailed instructions
- Strong at creative problem-solving

### Known Issues
- **Over-engineering tendency**: Will add features, abstractions, and "improvements" beyond what was asked
- Expensive for simple tasks
- Can be verbose

### Required Prompt Additions

Always include for Opus:

```markdown
## Simplicity Clause

Avoid over-engineering. Only make changes that are directly requested or clearly necessary.
Keep solutions simple and focused.

- Don't add features, refactor code, or make "improvements" beyond what was asked
- A bug fix doesn't need surrounding code cleaned up
- A simple feature doesn't need extra configurability
- Don't add error handling for scenarios that can't happen
- Don't create helpers or abstractions for one-time operations
```

### Best Use Cases
- Code reviews
- Architecture decisions
- Complex refactoring
- Research and analysis

---

## Claude Sonnet 4

### Strengths
- Good balance of speed and quality
- Reliable instruction following
- Cost-effective for most tasks

### Prompt Guidelines
- Standard, clear prompts work well
- Use as baseline for prompt testing
- No special anti-patterns to address

### Best Use Cases
- Daily development work
- Content generation
- Most general tasks

---

## Claude Haiku 3.5

### Strengths
- Very fast
- Cost-effective
- Good for simple, focused tasks

### Known Issues
- **Context limitations**: Forgets details in long sessions
- **Shallow responses**: May miss nuance
- **Needs more guidance**: What Opus infers, Haiku needs explicit

### Required Prompt Additions

For Haiku, provide more structure:

```markdown
## Task Breakdown

Complete these steps in order:
1. [Specific step 1]
2. [Specific step 2]
3. [Specific step 3]

Do not skip steps. Confirm each step before proceeding.
```

### Example Enhancement

Haiku benefits more from examples than other models:

| Examples | Haiku Accuracy | Opus Accuracy |
|----------|----------------|---------------|
| 0 | 11% | 70% |
| 3 | 75% | 85% |
| 5 | 80% | 87% |

Always provide 3-5 examples for Haiku on complex tasks.

### Best Use Cases
- Quick sub-tasks
- Simple transformations
- High-volume, low-complexity work
- Agent sub-agents

---

## Hybrid Workflows

### Recommended Pattern

Use models in sequence based on task complexity:

```
1. Haiku: Setup, simple transforms
2. Sonnet: Main implementation
3. Opus: Review, complex decisions
```

### Example Workflow

```markdown
## Multi-Model Workflow

1. **Planning (Opus)**: Generate detailed plan with architecture decisions
2. **Implementation (Sonnet)**: Execute plan step-by-step
3. **Quick Tasks (Haiku)**: Handle simple sub-tasks during implementation
4. **Review (Opus)**: Final code review and quality check
```

---

## Extended Thinking

### Model Behavior

| Model | Default Thinking | Token Budget |
|-------|------------------|--------------|
| Opus | Summary returned | Start 1024, increase as needed |
| Sonnet 3.7 | Full raw CoT returned | Similar |
| Haiku | Not recommended | N/A |

### Prompting for Thinking

For Opus/Sonnet with extended thinking:

```markdown
Think deeply about this problem. Consider multiple approaches.
Try different methods if your first approach doesn't work.
Before finishing, verify with test cases and fix any issues.
```

**Avoid** over-prescriptive thinking steps — Claude's creativity often exceeds human-prescribed patterns.
