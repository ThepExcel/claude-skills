# Prompt Optimization Checklist

## Universal Criteria (All Platforms)

### Structure (20 points)
- [ ] Clear section headers or XML tags
- [ ] Logical flow: context → instructions → examples
- [ ] No mixed formatting (pick one style)
- [ ] References linked appropriately for platform

### Specificity (20 points)
- [ ] Instructions use numbered steps
- [ ] Success criteria explicit
- [ ] Concrete examples, not abstract
- [ ] Edge cases addressed

### Examples (20 points)
- [ ] 3-5 diverse examples present
- [ ] Examples relevant to actual tasks
- [ ] Include edge cases
- [ ] Show good AND bad examples

### Conciseness (15 points)
- [ ] No redundant explanations
- [ ] Trusts model knows basics
- [ ] Essential info only
- [ ] Tables over paragraphs where appropriate

### Model Awareness (15 points)
- [ ] Model-specific clauses added
- [ ] Appropriate guidance level for target model
- [ ] No over-explaining for smart models

### System/User Separation (10 points)
- [ ] Persistent behavior in system prompt
- [ ] Task-specific in user prompt
- [ ] No confusion between roles

---

## Platform-Specific Checks

### Claude API
- [ ] Uses XML tags for structure
- [ ] Tools in API `tools` field (not prompt)
- [ ] Opus: Has anti-over-engineering clause
- [ ] Haiku: Has sufficient examples (3-5)
- [ ] Avoids "think" word if extended thinking disabled

### OpenAI API
- [ ] Uses message roles correctly
- [ ] Model version pinned for production
- [ ] Tools in `tools` parameter
- [ ] Verbosity controlled explicitly

### Gemini API
- [ ] Single format (XML OR Markdown)
- [ ] Critical instructions at END for long context
- [ ] Temperature not modified (keep 1.0)
- [ ] Knowledge cutoff mentioned if relevant
- [ ] Grounding clause if using context

### CLAUDE.md
- [ ] Content inline (not progressive disclosure)
- [ ] Under 200 instructions
- [ ] Includes: context, principles, workflows
- [ ] Excludes: API docs, rarely-used details

### ChatGPT Custom Instructions
- [ ] Under 1500 characters per field
- [ ] Clear "About me" section
- [ ] Clear "How to respond" section
- [ ] Works with Memory feature

### n8n / Workflow Tools
- [ ] Dynamic variables for dates/context
- [ ] Tools named clearly
- [ ] Memory node configured
- [ ] Explicit boundaries defined

---

## Anti-Pattern Check

| Pattern | Present? | Fixed? |
|---------|----------|--------|
| Vague instructions | [ ] | [ ] |
| Everything is CRITICAL | [ ] | [ ] |
| No examples | [ ] | [ ] |
| Explaining basics | [ ] | [ ] |
| Wrong format for platform | [ ] | [ ] |
| System/User mixed up | [ ] | [ ] |
| Hardcoded dynamic data | [ ] | [ ] |
| Tools in prompt (not API) | [ ] | [ ] |

---

## Scoring

| Category | Score |
|----------|-------|
| Structure | ___ / 20 |
| Specificity | ___ / 20 |
| Examples | ___ / 20 |
| Conciseness | ___ / 15 |
| Model Awareness | ___ / 15 |
| System/User Separation | ___ / 10 |
| **Total** | **___ / 100** |

### Interpretation

| Score | Quality | Action |
|-------|---------|--------|
| 90-100 | Excellent | Ready to use |
| 70-89 | Good | Minor improvements |
| 50-69 | Needs work | Address major gaps |
| <50 | Poor | Significant rewrite |
