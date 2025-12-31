# Function Explainer System - Complete Workflow

This document shows how all 5 skills work together in the Function Explainer ecosystem.

## Skill Relationships

```
┌─────────────────────────────────────────────────────────────────┐
│                    Function Explainer System                    │
└─────────────────────────────────────────────────────────────────┘

program-status-checker                 function-explainer
        ↓                                      ↓
   (Overview of                          (1. Research)
    all programs)                              ↓
                                    function-researcher
                                               ↓
                                         (2. Create JSON)
                                               ↓
                                         (3. Validate)
                                               ↓
                                     function-validator
                                               ↓
                                         (4. Publish)
                                               ↓
                                     function-publisher
```

## Skill Purpose & When to Use

### 1. program-status-checker
**Purpose:** Get overview of program quality and identify what needs work

**When to use:**
- Check overall quality across programs (Excel, Power Query, DAX, etc.)
- Identify high-priority functions to create/improve
- Generate status reports

**What it provides:** Program quality dashboard, priority lists

---

### 2. function-researcher
**Purpose:** Deep research for function documentation from official sources

**When to use:**
- Need to research a new function
- Gathering syntax, arguments, examples, best practices
- Finding official documentation links

**What it provides:** Structured research findings with verified sources

**Used by:** function-explainer (research phase)

---

### 3. function-explainer
**Purpose:** Orchestrate complete lifecycle (research → create → validate → publish)

**When to use:**
- Create new Function Explainer posts
- Update existing posts to improve quality
- Complete category of functions
- Any end-to-end function work

**What it does:**
1. Research (invokes function-researcher if needed)
2. Create/update JSON content
3. Validate (invokes function-validator)
4. Publish (invokes function-publisher)

**This is the main orchestration skill** - use it for most function work

---

### 4. function-validator
**Purpose:** Validate JSON quality before publishing

**When to use:**
- Check if JSON meets requirements (0 issues needed to publish)
- Verify content quality (examples, Thai ratio, related functions)
- Fix validation issues

**What it checks:**
- Required fields, examples count (≥3)
- Official docs links, Thai language ratio (≥60%)
- Related functions, argument defaults
- JSON structure validity

**Used by:** function-explainer (validation step), function-publisher (pre-publish)

---

### 5. function-publisher
**Purpose:** Publish validated content to WordPress REST API

**When to use:**
- Publish validated Function Explainer JSON to WordPress
- Update existing published functions
- Batch publish multiple functions

**What it does:**
- Auto-detects CREATE vs UPDATE
- Prevents duplicate posts
- Updates CSV tracking
- Returns post ID and URL

**Used by:** function-explainer (final publishing step)

---

## Complete Workflow Example

**Scenario:** Create a new function explainer for Excel's XLOOKUP

```bash
# 1. Check program status (optional)
Invoke skill: program-status-checker
# See where XLOOKUP ranks in priority

# 2. Use main orchestration skill
Invoke skill: function-explainer
# This skill will automatically:
#   - Research XLOOKUP (may invoke function-researcher)
#   - Create JSON content (with related field)
#   - Validate (invokes function-validator internally)
#   - Publish (invokes function-publisher internally)
#   - Sync related pairs (batch, after all publishing)

# OR: Manual step-by-step (for advanced users)

# Step 1: Research
Invoke skill: function-researcher
# Gather official docs, examples, best practices

# Step 2: Create JSON
# (Manual content creation based on research)

# Step 3: Validate
Invoke skill: function-validator
# Ensure 0 issues before publishing

# Step 4: Publish
Invoke skill: function-publisher
# Publish to WordPress REST API
```

##  Recommended Approach

**For most tasks:** Use `function-explainer` (the orchestration skill)
- It handles the complete workflow
- Invokes other skills automatically
- Most efficient for end-to-end work

**For specific needs:** Invoke individual skills
- `program-status-checker` - Get overview only
- `function-researcher` - Research only
- `function-validator` - Validation only
- `function-publisher` - Publishing only

---

## Shared Resources

All skills use these shared resources:

1. **Data Tools** (csv_query, csv_write, json_query, json_write)
   - See: `/.claude/skills/common-tools/references/data-tools-quick-ref.md`
   - For complete docs: See function-publisher skill's references

2. **Master CSV Registry**
   - `functions/all_functions_reference.csv`
   - Single source of truth for all functions
   - Updated automatically by publisher

3. **Configuration**
   - `tools/config/taxonomy_map.json` - WordPress term IDs
   - `tools/config/master_program_categories.json` - Valid categories

---

## Avoiding Redundancy

To prevent duplication:

1. ✅ **Data tools documentation** → Shared in common-tools/references/
2. ✅ **Workflow overview** → This document (referenced by all skills)
3. ✅ **Validation rules** → Documented in function-validator only
4. ✅ **Publishing process** → Documented in function-publisher only
5. ✅ **Research sources** → Documented in function-researcher only

Each skill references these shared resources instead of duplicating content.
