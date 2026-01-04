# Workflow Patterns

Use these patterns when skills need multi-step processes with quality controls.

## Sequential Workflows

Break complex tasks into clear, sequential steps with a checklist Claude can track:

```markdown
## PDF form filling workflow

Copy this checklist and track your progress:

```
Task Progress:
- [ ] Step 1: Analyze the form (run analyze_form.py)
- [ ] Step 2: Create field mapping (edit fields.json)
- [ ] Step 3: Validate mapping (run validate_fields.py)
- [ ] Step 4: Fill the form (run fill_form.py)
- [ ] Step 5: Verify output (run verify_output.py)
```

**Step 1: Analyze the form**
Run: `python scripts/analyze_form.py input.pdf`
This extracts form fields and saves to `fields.json`.

**Step 2: Create field mapping**
Edit `fields.json` to add values for each field.

**Step 3: Validate mapping**
Run: `python scripts/validate_fields.py fields.json`
Fix any validation errors before continuing.

**Step 4: Fill the form**
Run: `python scripts/fill_form.py input.pdf fields.json output.pdf`

**Step 5: Verify output**
Run: `python scripts/verify_output.py output.pdf`
If verification fails, return to Step 2.
```

Clear steps with checklists help both Claude and users track progress.

## Conditional Workflows

For tasks with branching logic, guide Claude through decision points:

```markdown
## Document modification workflow

1. Determine the modification type:

   **Creating new content?** → Follow "Creation workflow" below
   **Editing existing content?** → Follow "Editing workflow" below

2. Creation workflow:
   - Use docx-js library
   - Build document from scratch
   - Export to .docx format

3. Editing workflow:
   - Unpack existing document
   - Modify XML directly
   - Validate after each change
   - Repack when complete
```

**Tip**: If workflows become large, push them into separate files and tell Claude to read the appropriate file based on the task.

## Feedback Loops

**Common pattern**: Run validator → fix errors → repeat

This pattern greatly improves output quality.

### Example 1: Style Guide Compliance (No Code)

```markdown
## Content review process

1. Draft your content following the guidelines in STYLE_GUIDE.md
2. Review against the checklist:
   - Check terminology consistency
   - Verify examples follow the standard format
   - Confirm all required sections are present
3. If issues found:
   - Note each issue with specific section reference
   - Revise the content
   - Review the checklist again
4. Only proceed when all requirements are met
5. Finalize and save the document
```

### Example 2: Document Editing (With Code)

```markdown
## Document editing process

1. Make your edits to `word/document.xml`
2. **Validate immediately**: `python scripts/validate.py unpacked_dir/`
3. If validation fails:
   - Review the error message carefully
   - Fix the issues in the XML
   - Run validation again
4. **Only proceed when validation passes**
5. Rebuild: `python scripts/pack.py unpacked_dir/ output.docx`
6. Test the output document
```

The validation loop catches errors early.

## Research Synthesis Workflow (No Code)

For skills without executable code:

```markdown
## Research synthesis workflow

Copy this checklist and track your progress:

```
Research Progress:
- [ ] Step 1: Read all source documents
- [ ] Step 2: Identify key themes
- [ ] Step 3: Cross-reference claims
- [ ] Step 4: Create structured summary
- [ ] Step 5: Verify citations
```

**Step 1: Read all source documents**
Review each document in `sources/`. Note main arguments and evidence.

**Step 2: Identify key themes**
Look for patterns across sources. What themes appear repeatedly?

**Step 3: Cross-reference claims**
For each major claim, verify it appears in source material.

**Step 4: Create structured summary**
Organize findings by theme:
- Main claim
- Supporting evidence
- Conflicting viewpoints (if any)

**Step 5: Verify citations**
Check every claim references the correct source. If incomplete, return to Step 3.
```

## Verifiable Intermediate Outputs

For complex tasks, create plan files that get validated before execution:

**Problem**: Asking Claude to update 50 form fields based on a spreadsheet without validation could result in referencing non-existent fields, conflicting values, or missed required fields.

**Solution**: Create `changes.json` → validate → execute

```markdown
## Batch update workflow

1. Analyze source data and target document
2. Create `changes.json` with planned modifications:
   ```json
   {
     "field_name": "new_value",
     "another_field": "another_value"
   }
   ```
3. Run: `python scripts/validate_changes.py changes.json`
4. If validation fails, fix `changes.json` and re-validate
5. Only when validation passes: `python scripts/apply_changes.py`
```

**Why this works:**
- **Catches errors early** — Validation finds problems before changes apply
- **Machine-verifiable** — Scripts provide objective verification
- **Reversible planning** — Claude can iterate on plan without touching originals
- **Clear debugging** — Error messages point to specific problems

**When to use**: Batch operations, destructive changes, complex validation rules, high-stakes operations.

**Implementation tip**: Make validation scripts verbose:
```
Field 'signature_date' not found.
Available fields: customer_name, order_total, signature_date_signed
```
