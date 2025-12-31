---
name: common-tools
description: |
  SQL-based tools for Function Explainer data operations. Use when querying functions (SELECT), updating CSV (UPDATE), or syncing state (WordPress/JSON). Standard SQL syntax - no custom CLI.
---

# Common Tools: SQL Interface

**Use SQL for all data operations.** No custom CLI syntax to learn.

## Table of Contents

1. [Core Tools](#core-tools)
2. [sql_query.py](#sql_querypy---read-data)
3. [sql_write.py](#sql_writepy---update-data)
4. [sync_registry.py](#sync_registrypy---sync-state)
5. [Complete Workflows](#complete-workflows)
6. [Table Schema](#table-schema)
7. [Quick Reference](#quick-reference)

---

## Core Tools

| Tool | Purpose | Example |
|------|---------|---------|
| `sql_query.py` | SELECT (read) | `"SELECT * FROM functions WHERE ..."` |
| `sql_write.py` | UPDATE | `"UPDATE functions SET x=y WHERE ..."` |
| `sync_registry.py` | Sync from WordPress/JSON | `sync_registry.py wordpress --save` |

---

## sql_query.py - Read Data

```bash
python3 tools/sql_query.py "YOUR SQL QUERY"
```

### Common Queries

| Query | Command |
|-------|---------|
| Top N unpublished by popularity | `"SELECT slug, popularity FROM functions WHERE program='n8n' AND post_id IS NULL ORDER BY popularity DESC LIMIT 10"` |
| Top N unpublished with JSON | `"SELECT slug, quality_score FROM functions WHERE program='n8n' AND post_id IS NULL AND has_json=true ORDER BY quality_score DESC LIMIT 10"` |
| Get slugs for piping | `--slugs "SELECT slug FROM functions WHERE program='n8n' AND post_id IS NULL LIMIT 10"` |
| Count by program | `"SELECT program, COUNT(*) as cnt FROM functions GROUP BY program"` |
| Find specific function | `"SELECT * FROM functions WHERE slug='average' AND program='excel'"` |

### Output Formats

| Flag | Output |
|------|--------|
| (default) | Pretty table |
| `--json` | JSON array |
| `--csv` | CSV format |
| `--slugs` | Just slugs (for piping) |

---

## sql_write.py - Update Data

```bash
# Dry-run (preview)
python3 tools/sql_write.py "UPDATE functions SET field=value WHERE condition"

# Actually save
python3 tools/sql_write.py --save "UPDATE functions SET field=value WHERE condition"
```

### Common Updates

| Task | Command |
|------|---------|
| Update quality score | `--save "UPDATE functions SET quality_score=95.5 WHERE slug='average' AND program='excel'"` |
| Update post_id | `--save "UPDATE functions SET post_id=12345 WHERE slug='sum-n8n' AND program='n8n'"` |
| Mark for reupload | `--save "UPDATE functions SET needs_reupload=true WHERE slug='average' AND program='excel'"` |
| Bulk update | `--save "UPDATE functions SET needs_reupload=true WHERE program='n8n' AND quality_score < 70"` |

### Safety Features

- **Dry-run by default** - shows what would change
- **WHERE required** - prevents accidental bulk updates
- **Auto backup** - saves `.csv.backup` before writing

---

## sync_registry.py - Sync State

```bash
python3 tools/sync_registry.py wordpress --save  # Sync post IDs
python3 tools/sync_registry.py json --save       # Sync JSON status
python3 tools/sync_registry.py all --save        # Sync both
python3 tools/sync_registry.py status            # Check current state
```

---

## Complete Workflows

### Publish Top 10 Unpublished

```bash
# 1. Find candidates
python3 tools/sql_query.py "SELECT slug, quality_score FROM functions WHERE program='n8n' AND post_id IS NULL AND has_json=true ORDER BY quality_score DESC LIMIT 10"

# 2. Get slugs → validate → publish
python3 tools/sql_query.py --slugs "..." > /tmp/to_publish.txt
cat /tmp/to_publish.txt | xargs python3 tools/validate_functions.py --program n8n --slugs
python3 tools/smart_publish.py --slug slug1 slug2 slug3 ...
```

### Fix Low Quality Functions

```bash
# Find
python3 tools/sql_query.py "SELECT slug, quality_score FROM functions WHERE program='excel' AND post_id IS NOT NULL AND quality_score < 70"

# After fix, mark for reupload
python3 tools/sql_write.py --save "UPDATE functions SET needs_reupload=true WHERE slug='function-slug' AND program='excel'"
```

---

## Table Schema

**Table:** `functions` → `functions/all_functions_reference.csv`

| Column | Type | Description |
|--------|------|-------------|
| program | string | excel, power-query, dax, google-sheets, n8n |
| slug | string | URL-friendly function name |
| name | string | Display name |
| category | string | Function category |
| post_id | int/null | WordPress post ID (null = unpublished) |
| popularity | int | 1-10 popularity score |
| difficulty | int | 1-10 difficulty score |
| usefulness | int | 1-10 usefulness score |
| **Content Metrics** | | (Extracted from JSON) |
| quality_score | int | 0-100 calculated quality score |
| example_count | int | Number of examples |
| faq_count | int | Number of FAQ items |
| has_json | bool | Has JSON data file |
| needs_reupload | bool | Needs republishing |

**Quality Score:** Content (40) + Examples (20) + FAQs (15) + Related (15) + Resources (10)

**Update scores:** `python3 tools/extract_json_metrics.py --program all --update-csv`

---

## Quick Reference

| Task | Tool | Example |
|------|------|---------|
| Read data | sql_query | `"SELECT slug FROM functions WHERE ..."` |
| Update 1-10 rows | sql_write --save | `"UPDATE functions SET ..."` |
| Update 10+ rows | batch_sql_execute --save | `-e "UPDATE..." -e "UPDATE..."` |
| Sync WordPress | sync_registry | `wordpress --save` |
| Sync JSON status | sync_registry | `json --save` |
