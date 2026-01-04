# Progressive Disclosure Patterns

Keep SKILL.md body to the essentials and under 500 lines. Split content into separate files when approaching this limit.

**Key principle:** When a skill supports multiple variations, frameworks, or options, keep only the core workflow and selection guidance in SKILL.md. Move variant-specific details into separate reference files.

## Pattern 1: High-Level Guide with References

```markdown
# PDF Processing

## Quick start

Extract text with pdfplumber:
```python
import pdfplumber
with pdfplumber.open("file.pdf") as pdf:
    text = pdf.pages[0].extract_text()
```

## Advanced features

- **Form filling**: See [FORMS.md](FORMS.md) for complete guide
- **API reference**: See [REFERENCE.md](REFERENCE.md) for all methods
- **Examples**: See [EXAMPLES.md](EXAMPLES.md) for common patterns
```

Claude loads FORMS.md, REFERENCE.md, or EXAMPLES.md only when needed.

## Pattern 2: Domain-Specific Organization

For skills with multiple domains, organize content by domain:

```
bigquery-skill/
├── SKILL.md (overview and navigation)
└── reference/
    ├── finance.md (revenue, billing metrics)
    ├── sales.md (opportunities, pipeline)
    ├── product.md (API usage, features)
    └── marketing.md (campaigns, attribution)
```

**SKILL.md example:**

```markdown
# BigQuery Data Analysis

## Available datasets

**Finance**: Revenue, ARR, billing → See [reference/finance.md](reference/finance.md)
**Sales**: Opportunities, pipeline, accounts → See [reference/sales.md](reference/sales.md)
**Product**: API usage, features, adoption → See [reference/product.md](reference/product.md)
**Marketing**: Campaigns, attribution, email → See [reference/marketing.md](reference/marketing.md)

## Quick search

Find specific metrics using grep:
```bash
grep -i "revenue" reference/finance.md
grep -i "pipeline" reference/sales.md
```
```

When user asks about sales metrics, Claude only reads `sales.md`.

Similarly, for skills supporting multiple frameworks:

```
cloud-deploy/
├── SKILL.md (workflow + provider selection)
└── references/
    ├── aws.md (AWS deployment patterns)
    ├── gcp.md (GCP deployment patterns)
    └── azure.md (Azure deployment patterns)
```

When user chooses AWS, Claude only reads `aws.md`.

## Pattern 3: Conditional Details

Show basic content, link to advanced content:

```markdown
# DOCX Processing

## Creating documents

Use docx-js for new documents. See [DOCX-JS.md](DOCX-JS.md).

## Editing documents

For simple edits, modify the XML directly.

**For tracked changes**: See [REDLINING.md](REDLINING.md)
**For OOXML details**: See [OOXML.md](OOXML.md)
```

Claude reads REDLINING.md or OOXML.md only when user needs those features.

## Important Guidelines

### Keep References One Level Deep

**Bad — Too deep:**
```
SKILL.md → advanced.md → details.md → actual_info.md
```

**Good — Direct links:**
```
SKILL.md → advanced.md
SKILL.md → reference.md
SKILL.md → examples.md
```

### Structure Longer Reference Files

For files longer than 100 lines, include a table of contents at the top:

```markdown
# API Reference

## Contents
- Authentication and setup
- Core methods (create, read, update, delete)
- Advanced features (batch operations, webhooks)
- Error handling patterns
- Code examples

## Authentication and setup
...

## Core methods
...
```

Claude can then read the complete file or jump to specific sections as needed.

### Signal File References Clearly

When referencing files from SKILL.md, make it clear when Claude should read them:

```markdown
## Form filling

For basic form filling, use the template in `assets/form-template.pdf`.

**For complex forms with validation**: Read [references/form-validation.md](references/form-validation.md) before proceeding.
```
