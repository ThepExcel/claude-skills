# Evaluation and Iteration

## Build Evaluations First

**Create evaluations BEFORE writing extensive documentation.** This ensures your skill solves real problems rather than documenting imagined ones.

### Evaluation-Driven Development

1. **Identify gaps** — Run Claude on representative tasks without a skill. Document specific failures or missing context
2. **Create evaluations** — Build three scenarios that test these gaps
3. **Establish baseline** — Measure Claude's performance without the skill
4. **Write minimal instructions** — Create just enough content to address gaps and pass evaluations
5. **Iterate** — Execute evaluations, compare against baseline, refine

This approach ensures you're solving actual problems rather than anticipating requirements that may never materialize.

### Evaluation Structure

```json
{
  "skills": ["pdf-processing"],
  "query": "Extract all text from this PDF file and save it to output.txt",
  "files": ["test-files/document.pdf"],
  "expected_behavior": [
    "Successfully reads the PDF file using an appropriate library",
    "Extracts text content from all pages without missing any",
    "Saves extracted text to output.txt in clear, readable format"
  ]
}
```

Create your own evaluation system. Evaluations are your source of truth for measuring skill effectiveness.

## The Claude A/B Iteration Pattern

The most effective skill development process involves Claude itself:
- **Claude A** — Helps you design and refine the skill
- **Claude B** — Tests the skill in real tasks (fresh instance with skill loaded)

### Creating a New Skill

**1. Complete a task without a skill**

Work through a problem with Claude A using normal prompting. Notice what information you repeatedly provide: context, preferences, procedural knowledge.

**2. Identify the reusable pattern**

After completing the task, identify what context would be useful for similar future tasks.

*Example*: For BigQuery analysis, you might have provided table names, field definitions, filtering rules ("always exclude test accounts"), and common query patterns.

**3. Ask Claude A to create a skill**

> "Create a skill that captures this BigQuery analysis pattern we just used. Include the table schemas, naming conventions, and the rule about filtering test accounts."

Claude models understand the skill format natively. No special prompts needed.

**4. Review for conciseness**

Check that Claude A hasn't added unnecessary explanations:

> "Remove the explanation about what win rate means — Claude already knows that."

**5. Improve information architecture**

Ask Claude A to organize content more effectively:

> "Organize this so the table schema is in a separate reference file. We might add more tables later."

**6. Test on similar tasks**

Use the skill with Claude B (fresh instance with skill loaded) on related use cases. Observe:
- Does Claude B find the right information?
- Does it apply rules correctly?
- Does it handle the task successfully?

**7. Iterate based on observation**

If Claude B struggles, return to Claude A with specifics:

> "When Claude used this skill, it forgot to filter by date for Q4. Should we add a section about date filtering patterns?"

### Iterating on Existing Skills

Continue alternating between:
- **Working with Claude A** — Refine the skill
- **Testing with Claude B** — Perform real work
- **Observing behavior** — Bring insights back to Claude A

**Workflow:**
1. Use the skill in real workflows (not test scenarios)
2. Note where Claude B struggles, succeeds, or makes unexpected choices
3. Share observations with Claude A: "Claude B forgot to filter test accounts when I asked for a regional report. The skill mentions filtering, but maybe it's not prominent enough?"
4. Review Claude A's suggestions (reorganize, stronger language, restructure)
5. Update and test again

### Gathering Team Feedback

1. Share skills with teammates and observe their usage
2. Ask: Does the skill activate when expected? Are instructions clear? What's missing?
3. Incorporate feedback to address blind spots

**Why this works**: Claude A understands agent needs, you provide domain expertise, Claude B reveals gaps through real usage, and iterative refinement improves skills based on observed behavior rather than assumptions.

## Observe How Claude Navigates Skills

Watch for:

| Observation | Meaning |
|-------------|---------|
| Unexpected exploration paths | Structure isn't intuitive |
| Missed connections | Links need to be more explicit |
| Overreliance on certain sections | Consider moving that content to SKILL.md |
| Ignored content | File might be unnecessary or poorly signaled |

The `name` and `description` in metadata are critical — Claude uses these when deciding whether to trigger the skill.

## Minimum Three Evaluations

Before sharing any skill, create at least three evaluation scenarios:

1. **Basic case** — The most common use case
2. **Edge case** — A tricky or unusual scenario
3. **Error case** — What happens when input is invalid or unexpected

Example for a PDF processing skill:

```json
[
  {
    "name": "basic_extraction",
    "query": "Extract text from this PDF",
    "expected": "Returns all text content correctly"
  },
  {
    "name": "scanned_document",
    "query": "Extract text from this scanned PDF",
    "expected": "Uses OCR or reports that document is image-based"
  },
  {
    "name": "corrupted_file",
    "query": "Extract text from this corrupted PDF",
    "expected": "Reports error gracefully, doesn't crash"
  }
]
```
