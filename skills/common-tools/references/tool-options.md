# Tool Options Reference

Detailed options for each tool. Only read this when you need specific options not covered in SKILL.md.

---

## csv_query.py Options

### filter Command Options
```
--published true|false     Filter by publication status
--min-popularity N         Minimum popularity (1-10)
--max-popularity N         Maximum popularity
--min-quality N            Minimum quality score (0-100)
--max-quality N            Maximum quality score
--quality RANGE            Range: "50-75" or "85+" or "50"
--popularity RANGE         Range: "6-8" or "8+" or "8"
--category SLUG            Filter by category
--has-json true|false      Filter by JSON file existence
--dashboard                Show metrics table view
```

### Global Options (BEFORE command)
```
--json                     Output as JSON
--table                    Output as table (one per line)
--csv-path PATH            Custom CSV file path
```

### Batch Input Options
```
--from-file FILE           Read slugs from file (one per line)
--from-stdin               Read slugs from stdin
```

---

## csv_write.py Options

### Commands
```
set PROG SLUG FIELD VALUE        Set single field
update-score PROG SLUG SCORE     Set quality_score
update-post-id PROG SLUG ID      Set post_id
mark-json PROG SLUG              Set has_json=true
mark-reupload PROG SLUG          Set needs_reupload=true
bulk-set PROG FIELD slug=val...  Set field on multiple functions
bulk-score PROG slug=score...    Set scores on multiple functions
```

### Safety Options
```
--save                     REQUIRED to actually write (dry-run without)
--csv-path PATH            Custom CSV file path
```

---

## json_query.py Options

### Commands
```
get PROG SLUG [FIELD]      Get field value (all fields if omitted)
exists PROG SLUG           Check if JSON file exists
validate PROG SLUG         Quick validation
path PROG SLUG             Get file path
examples PROG SLUG         Get examples count/list
arguments PROG SLUG        Get arguments count/list
related PROG SLUG          Get related functions list
resources PROG SLUG        Get resources count/list
```

### Output Options
```
--json                     Output as JSON
--pretty                   Pretty-print JSON
```

---

## json_write.py Options

### Commands
```
set PROG SLUG FIELD "VALUE"                Set top-level field
set-nested PROG SLUG PATH VALUE            Set nested field (dot notation)
add-related PROG SLUG RELATED_SLUG         Add to related_functions
bulk-add-related PROG RELATED SLUG1 SLUG2  Add related to multiple
update-meta PROG SLUG FIELD "VALUE"        Update meta field
bulk-set PROG FIELD slug=val...            Set field on multiple
```

### Safety Options
```
--save                     REQUIRED to actually write
```

---

## validate_functions.py Options

```
--program PROGRAM          Program to validate (required)
--slugs SLUG1 SLUG2...     Specific slugs to validate
--from-file FILE           Read slugs from file
--from-stdin               Read slugs from stdin
--skip-relationships       Skip relationship validation (faster)
```

---

## smart_publish.py Options

```
--slug SLUG1 SLUG2...      Function slug(s) to publish
--category CATEGORY        Publish all in category
--from-file FILE           Read slugs from file
--from-stdin               Read slugs from stdin
--program PROGRAM          Program filter (for --category)
--dry-run                  Preview without publishing
--skip-validation          Skip validation (dangerous!)
```

---

## Column Names Reference

**CSV columns (for csv_write.py set command):**
```
program           excel, power-query, dax, google-sheets, n8n
slug              Function slug (e.g., average, sum-n8n)
function_name     Display name (AVERAGE, $json)
category          Category slug (statistical, array-functions)
post_id           WordPress post ID (integer)
quality_score     Overall quality 0-100
popularity        Usage frequency 1-10
difficulty        Technical complexity 1-5
usefulness        Impact on work 1-10
has_json          JSON file exists (TRUE/FALSE) ⚠️ NOT json_exists
needs_reupload    Needs re-publishing (TRUE/FALSE)
```

**Common mistake:** Using `json_exists` instead of `has_json`
