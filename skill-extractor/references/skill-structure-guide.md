# Skill Structure Design Guide

## Overview

This guide helps organize extracted expertise into well-structured, usable Claude skills. It covers architecture patterns, file organization, and quality guidelines.

## Skill Architecture Patterns

### Pattern 1: Simple Knowledge Base

**Use when**:
- Straightforward reference material
- No complex workflows
- Self-contained knowledge

**Structure**:
```
skill-name/
├── SKILL.md (all content in one file)
└── (optional) README.md
```

**SKILL.md contains**:
- Overview
- Key concepts
- Best practices
- Examples

**Example domains**: glossaries, checklists, quick references

---

### Pattern 2: Workflow Skill

**Use when**:
- Clear step-by-step process
- Decision points and criteria
- Some complexity but manageable

**Structure**:
```
skill-name/
├── SKILL.md (overview + workflow)
├── references/
│   ├── detailed-guide.md (deep dives)
│   └── examples.md (use cases)
└── (optional) README.md
```

**SKILL.md contains**:
- Overview and scope
- High-level workflow (phases/steps)
- Key principles
- When to use each reference

**References contain**:
- Detailed explanations
- Extended examples
- Alternative approaches

**Example domains**: data cleaning workflows, design processes, troubleshooting guides

---

### Pattern 3: Coaching Skill

**Use when**:
- Interactive problem-solving
- Asks questions and provides guidance
- Adapts to user situation
- Has a persona/character

**Structure**:
```
skill-name/
├── SKILL.md (persona + workflow)
├── references/
│   ├── conversation-patterns.md (how to interact)
│   ├── knowledge-base.md (domain knowledge)
│   └── examples.md (sample conversations)
└── (optional) README.md
```

**SKILL.md contains**:
- Persona definition (name, personality, style)
- Workflow/phases of interaction
- Core principles
- Conversation guidelines

**References contain**:
- Question techniques
- Response patterns
- Deep domain knowledge
- Example dialogues

**Example domains**: learning amplifier, code review coach, career advisor

---

### Pattern 4: Hybrid Skill

**Use when**:
- Combines multiple patterns
- Complex domain with multiple facets
- Needs both workflow AND coaching AND reference

**Structure**:
```
skill-name/
├── SKILL.md (overview + orchestration)
├── references/
│   ├── workflow-guide.md
│   ├── knowledge-base.md
│   ├── conversation-patterns.md
│   ├── best-practices.md
│   └── examples/
│       ├── scenario-1.md
│       └── scenario-2.md
└── (optional) README.md
```

**Example domains**: comprehensive consulting skills, full-stack development guides

---

## Designing SKILL.md

### Metadata Section (Required)

```markdown
---
name: skill-name
description: Brief, clear description of what the skill does and when to use it. Should be scannable in skill list.
---
```

**Description guidelines**:
- 1-2 sentences
- Mention primary use case
- Include key capabilities
- Avoid jargon

**Examples**:
```yaml
# Good
description: Extract expertise from domain experts and transform it into working Claude skills through structured conversations.

# Too vague
description: Helps create skills.

# Too detailed  
description: This skill provides a comprehensive framework for conducting interviews with subject matter experts in order to capture their tacit and explicit knowledge, which is then organized into a structured format suitable for creating Claude skills with proper documentation and examples.
```

---

### Overview Section

**Purpose**: Quick orientation for users

**Include**:
- What the skill does
- Who it's for
- What problems it solves
- What outputs it produces

**Keep it brief**: 3-5 paragraphs max

---

### Persona Section (for Coaching Skills)

**Define**:
- Name and identity
- Personality traits
- Communication style
- Tone and energy
- Customization options

**Important**: Always allow persona customization!

**Example**:
```markdown
**Default character: น้องฟ้า**

[Character description]

**Customization**: Users can request different personas by simply asking.
```

---

### Workflow Section

**For simple skills**: Describe process directly

**For complex skills**: Break into phases

**Each phase should include**:
- Phase name and goal
- Key activities
- Important considerations
- Transition to next phase

**Use clear headings**:
```markdown
### Phase 1: Discovery (15-20 min)
**Goal**: Understand domain and scope
**Activities**: ...
```

---

### Key Principles Section

**Include**:
- Core guidelines
- Important mindsets
- Things to remember
- Non-negotiables

**Keep it**:
- Short (5-10 principles max)
- Clear and actionable
- Prioritized (most important first)

---

### Conversation Guidelines (for Coaching Skills)

**Include**:
- How to open conversations
- Tone and style
- Question techniques
- How to handle different situations
- How to close/transition

**Be specific**: Provide example phrases and dialogues

---

### References Section

**List all reference files** with brief descriptions:
```markdown
## References

**Read before [action]:**
- `references/file-name.md` - What it contains and when to use it

**Read when [situation]:**
- `references/another-file.md` - Purpose and content
```

---

### Quality Standards Section (Optional)

For skills where output quality matters, define:
- Completeness criteria
- Clarity standards
- Usability requirements
- Accuracy expectations

---

## Designing Reference Files

### When to Create Reference Files

**Create separate reference when**:
- Content is >500 words
- Detailed technical knowledge
- Reference material that doesn't fit flow of main SKILL.md
- Optional/conditional information
- Extended examples

**Keep in main SKILL.md when**:
- Critical to workflow
- Quick reference
- Needs to be seen immediately

---

### Common Reference File Types

**1. conversation-patterns.md**
- Question techniques
- Response patterns
- Example dialogues
- Handling different situations

**2. knowledge-base.md** or **[domain]-guide.md**
- Deep technical content
- Detailed explanations
- Comprehensive coverage

**3. best-practices.md**
- Proven patterns
- Common mistakes
- Quality guidelines
- Optimization techniques

**4. examples.md** or **examples/** folder
- Real scenarios
- Case studies
- Before/after comparisons
- Sample outputs

---

### Reference File Structure

Each reference should have:

**1. Overview** - What it contains, when to use it

**2. Organized sections** - Clear headers, logical flow

**3. Concrete content** - Examples, not just theory

**4. Scannable format** - Headers, lists, code blocks

**Example structure**:
```markdown
# [Reference Name]

## Overview
What this reference covers and when to use it.

## Section 1: [Topic]
Content with examples

## Section 2: [Topic]
Content with examples

...
```

---

## File Organization Best Practices

### Naming Conventions

**Files**:
- Lowercase with hyphens: `knowledge-base.md`
- Descriptive: `power-query-patterns.md` not `patterns.md`
- Avoid version numbers in names

**Folders**:
- Plural for collections: `examples/`, `references/`
- Singular for single purpose: `template/`

### Folder Structure

**Keep it flat** (1-2 levels max):
```
✅ Good
skill-name/
├── SKILL.md
├── references/
│   ├── guide-1.md
│   └── guide-2.md
└── examples/
    ├── example-1.md
    └── example-2.md

❌ Too nested
skill-name/
├── SKILL.md
└── references/
    ├── core/
    │   └── concepts/
    │       └── basics.md
    └── advanced/
        └── techniques/
            └── optimization.md
```

---

## Content Quality Guidelines

### Clarity

**Use clear language**:
- ✅ "Connect to your data source"
- ❌ "Establish a connection to the underlying data repository"

**Define jargon**:
- First use: "Power Query (a data transformation tool in Excel)"
- After: "Power Query"

**Use examples**:
- Don't just describe, show
- Use realistic scenarios
- Include before/after when relevant

### Completeness

**Cover the essentials**:
- Core concepts
- Main workflows
- Important edge cases
- Common mistakes

**But avoid**:
- Exhaustive documentation
- Rare edge cases
- Excessive detail
- Information overload

### Actionability

**Make it practical**:
- Clear next steps
- Specific guidance
- Concrete examples
- Usable immediately

**Avoid**:
- Pure theory
- Vague advice
- "It depends" without criteria

### Scannability

**Use formatting**:
- ## and ### for sections
- **Bold** for key terms
- `code` for technical terms
- > Blockquotes for important notes
- Lists for enumeration
- Code blocks for examples

**Keep paragraphs short**: 3-5 sentences max

**Use white space**: Don't wall of text

---

## Specific Skill Type Guidelines

### For Workflow Skills

**Focus on**:
- Clear sequence of steps
- Decision criteria at each point
- Prerequisites and preparation
- Expected outputs

**Structure**:
1. Overview of full workflow
2. Detailed breakdown of each step
3. Common variations
4. Troubleshooting

**Example domains**: data preparation, design processes, troubleshooting

---

### For Coaching Skills

**Focus on**:
- How to interact (persona, tone)
- Question techniques
- Response patterns
- Handling different user situations

**Structure**:
1. Persona definition
2. Conversation phases/workflow
3. Detailed interaction patterns
4. Examples of good conversations

**Example domains**: learning coaches, problem-solving guides, advisory roles

---

### For Knowledge Base Skills

**Focus on**:
- Organized reference information
- Quick access to specific topics
- Clear explanations with examples
- Comprehensive coverage

**Structure**:
1. Overview and scope
2. Core concepts
3. Detailed topics (alphabetical or logical order)
4. Cross-references

**Example domains**: technical references, best practices guides, concept libraries

---

## Sub-Skills: When and How

### When to Reference Sub-Skills

**Reference existing skills when**:
- Expert mentions needing capabilities from another domain
- Clear dependency on external expertise
- Standard skill exists that fits the need

**Example from Power Query Coach**:
- Main skill: Power Query workflow
- Sub-skills needed: 
  - Data analysis skill (understanding data patterns)
  - Excel skill (file handling)
  - Visualization skill (showing transformations)

**How to reference**:
```markdown
## Sub-Skills

This skill may benefit from:
- **xlsx skill**: For advanced Excel file manipulation
- **data-analysis skill**: For pattern recognition in datasets
- **visualization skill**: For showing data transformation results

These are optional but recommended for best results.
```

### When to Create Custom Sub-Content

**Create within your skill when**:
- Specific to your domain
- Not complex enough to be separate skill
- Tightly integrated with main workflow

**How to organize**:
- Put in references/ folder
- Link from main SKILL.md
- Keep focused on your domain

---

## Testing Your Skill Structure

### Structural Check

- [ ] Clear metadata with good description
- [ ] Scannable overview
- [ ] Logical workflow or organization
- [ ] Appropriate use of references
- [ ] Examples where helpful

### Content Check

- [ ] All key concepts covered
- [ ] Sufficient detail to be useful
- [ ] Not overwhelming with information
- [ ] Actionable guidance
- [ ] Clear language

### Usability Check

- [ ] Easy to navigate
- [ ] Can find information quickly
- [ ] Examples are realistic
- [ ] Appropriate for target users

---

## Common Structural Mistakes

### ❌ Mistake 1: Everything in One File

**Problem**: SKILL.md becomes 3000+ lines, hard to navigate

**Solution**: Split into logical references

**When it's OK**: Simple skills with <500 words total

---

### ❌ Mistake 2: Too Many Small Files

**Problem**: Information scattered across 20 tiny files

**Solution**: Consolidate related content

**Rule of thumb**: Each file should have >200 words of substance

---

### ❌ Mistake 3: Unclear File Purposes

**Problem**: `guide.md`, `info.md`, `details.md` - what's what?

**Solution**: Descriptive names: `conversation-patterns.md`, `technical-reference.md`

---

### ❌ Mistake 4: Missing Context

**Problem**: References don't explain when/why to read them

**Solution**: Add clear descriptions in main SKILL.md

---

### ❌ Mistake 5: No Examples

**Problem**: All theory, no concrete examples

**Solution**: Add examples inline or in examples/ folder

---

## Iteration and Refinement

### After Creating First Version

**Test it**:
- Use the skill for real task
- Have someone else use it
- Note what's confusing or missing

**Common issues**:
- Missing prerequisites
- Unclear decision points
- Not enough examples
- Too much/too little detail

**Refine**:
- Add missing information
- Clarify confusing parts
- Add examples
- Reorganize if needed

### Version Management

**Don't**:
- Put version numbers in filenames
- Keep old versions around
- Add "v2" sections

**Do**:
- Update in place
- Note major changes in commits/notes
- Consider backward compatibility

---

## Final Checklist

Before considering a skill complete:

**Structure**:
- [ ] Clear, logical organization
- [ ] Appropriate file separation
- [ ] Easy to navigate
- [ ] Descriptive filenames

**Content**:
- [ ] All key topics covered
- [ ] Sufficient examples
- [ ] Clear, actionable guidance
- [ ] Right level of detail

**Quality**:
- [ ] Clear language
- [ ] Scannable formatting
- [ ] Accurate information
- [ ] Expert-validated

**Usability**:
- [ ] Works for target users
- [ ] Easy to find information
- [ ] Practical and actionable
- [ ] Ready to use immediately

---

## Examples of Good Structure

### Example 1: Learning Amplifier (Coaching Skill)
```
learning-amplifier/
├── SKILL.md
│   ├── Persona (น้องฟ้า)
│   ├── Workflow (3 phases)
│   ├── Principles
│   └── References
├── references/
│   ├── conversation-patterns.md (how to interact)
│   └── article-structure.md (output templates)
```

**Why it works**:
- Clear persona in main file
- Workflow is scannable
- Detailed patterns in references
- Output guidance separate

---

### Example 2: Power Query Coach (Workflow + Coaching)
```
power-query-coach/
├── SKILL.md
│   ├── Persona
│   ├── Main workflow (4 phases)
│   ├── Key principles
│   └── References
├── references/
│   ├── data-quality-patterns.md (domain knowledge)
│   ├── power-query-techniques.md (technical reference)
│   ├── coaching-questions.md (how to coach)
│   └── examples/
│       ├── wide-to-long.md
│       ├── date-locale-fix.md
│       └── append-vs-merge.md
```

**Why it works**:
- Separates coaching from technical knowledge
- Examples organized by topic
- Clear workflow in main file
- Domain knowledge easily accessible

---

## Remember

**Good structure**:
- Makes information easy to find
- Separates concerns appropriately
- Scales with complexity
- Helps users succeed quickly

**The goal**: Create skills that work beautifully and help users effectively! 🎯✨
