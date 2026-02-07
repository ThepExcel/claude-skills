# Integration Patterns

How to merge research findings into a skill. Each pattern specifies: what to change, where, and how.

## Pattern 1: Add Missing Workflow

**When:** Research reveals a procedure the skill doesn't cover.

**Steps:**
1. Identify where in the skill this workflow belongs (new section? extension of existing?)
2. Write the workflow as numbered steps with decision points
3. Add a concrete example showing input → steps → output
4. If workflow is long (>30 lines), put it in `references/` and link from SKILL.md

**Example:**
```
FINDING: "Experts always validate data schema before transformation"
→ ACTION: Add "Schema Validation" step before "Transform" in workflow
→ WHERE: Between Step 2 and Step 3 of main workflow
→ HOW: Add checklist with 3 validation checks + error handling
```

## Pattern 2: Deepen Decision Framework

**When:** Research reveals nuanced trade-offs the skill treats as simple.

**Steps:**
1. Identify the current oversimplified guidance
2. Create a decision table: situation → factors → recommendation
3. Add anti-patterns (what NOT to do and why)

**Example:**
```
BEFORE: "Use caching for performance"
AFTER: Decision table:
| Data changes | Read frequency | Recommendation |
|-------------|---------------|----------------|
| Rarely      | High          | Aggressive cache (TTL: hours) |
| Often       | High          | Short cache (TTL: seconds) |
| Often       | Low           | No cache |
```

## Pattern 3: Add Anti-Patterns

**When:** Research reveals common mistakes practitioners make.

**Steps:**
1. Describe the anti-pattern concisely
2. Explain WHY it's wrong (not just that it is)
3. Show the correct alternative

**Format:**
```
❌ Anti-pattern: [what people do wrong]
   Why: [root cause of the mistake]
✅ Instead: [correct approach]
```

## Pattern 4: Upgrade Examples

**When:** Existing examples are abstract or insufficient.

**Steps:**
1. Replace "e.g." with actual concrete values
2. Show full input → process → output
3. Include at least one edge case example

## Pattern 5: Extract to Reference

**When:** New content would push SKILL.md over 500 lines.

**Steps:**
1. Identify the heaviest section in SKILL.md
2. Move detailed content to `references/[topic].md`
3. Leave a summary + link in SKILL.md
4. Add grep patterns if reference file is >100 lines

## Merge Checklist

Before merging research into a skill:

```
□ Does this finding ADD value Claude doesn't already have?
□ Is it actionable (not just interesting trivia)?
□ Does it conflict with existing guidance? (If yes, which is correct?)
□ Where does it belong? (SKILL.md body / references / examples)
□ Will SKILL.md stay under 500 lines after adding this?
□ Is terminology consistent with rest of skill?
```
