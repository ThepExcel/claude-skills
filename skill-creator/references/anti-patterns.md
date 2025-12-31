# Anti-Patterns to Avoid

Common mistakes that reduce skill effectiveness.

## Path and File Issues

### Windows-Style Paths

Always use forward slashes, even on Windows:

| Good | Bad |
|------|-----|
| `scripts/helper.py` | `scripts\helper.py` |
| `reference/guide.md` | `reference\guide.md` |

Unix-style paths work across all platforms.

### Deeply Nested References

Claude may partially read files when they're referenced from other referenced files.

**Bad — Too deep:**
```markdown
# SKILL.md
See [advanced.md](advanced.md)...

# advanced.md
See [details.md](details.md)...

# details.md
Here's the actual information...
```

**Good — One level deep:**
```markdown
# SKILL.md
**Basic usage**: [instructions here]
**Advanced features**: See [advanced.md](advanced.md)
**API reference**: See [reference.md](reference.md)
**Examples**: See [examples.md](examples.md)
```

## Code and Scripts

### Punting to Claude

Scripts should handle errors, not punt to Claude:

**Bad — Punt to Claude:**
```python
def process_file(path):
    # Just fail and let Claude figure it out
    return open(path).read()
```

**Good — Handle errors:**
```python
def process_file(path):
    """Process a file, creating it if it doesn't exist."""
    try:
        with open(path) as f:
            return f.read()
    except FileNotFoundError:
        print(f"File {path} not found, creating default")
        with open(path, 'w') as f:
            f.write('')
        return ''
    except PermissionError:
        print(f"Cannot access {path}, using default")
        return ''
```

### Magic Constants (Voodoo Numbers)

Every configuration value needs justification:

**Bad — Magic numbers:**
```python
TIMEOUT = 47  # Why 47?
RETRIES = 5   # Why 5?
```

**Good — Self-documenting:**
```python
# HTTP requests typically complete within 30 seconds
# Longer timeout accounts for slow connections
REQUEST_TIMEOUT = 30

# Three retries balances reliability vs speed
# Most intermittent failures resolve by second retry
MAX_RETRIES = 3
```

### Assuming Tools Are Installed

Don't assume packages are available:

**Bad:**
```markdown
Use the pdf library to process the file.
```

**Good:**
```markdown
Install required package: `pip install pypdf`

Then use it:
```python
from pypdf import PdfReader
reader = PdfReader("file.pdf")
```
```

## Content Issues

### Too Many Options

Don't present multiple approaches unless necessary:

**Bad — Confusing:**
```markdown
You can use pypdf, or pdfplumber, or PyMuPDF, or pdf2image, or...
```

**Good — Provide default with escape hatch:**
```markdown
Use pdfplumber for text extraction:
```python
import pdfplumber
```

For scanned PDFs requiring OCR, use pdf2image with pytesseract instead.
```

### Time-Sensitive Information

Don't include info that becomes outdated:

**Bad:**
```markdown
If you're doing this before August 2025, use the old API.
After August 2025, use the new API.
```

**Good — Use "old patterns" section:**
```markdown
## Current method
Use the v2 API endpoint: `api.example.com/v2/messages`

## Old patterns
<details>
<summary>Legacy v1 API (deprecated 2025-08)</summary>
The v1 API used: `api.example.com/v1/messages`
This endpoint is no longer supported.
</details>
```

### Inconsistent Terminology

Choose one term and stick with it:

| Good (consistent) | Bad (inconsistent) |
|-------------------|-------------------|
| Always "endpoint" | Mix "endpoint", "URL", "route", "path" |
| Always "field" | Mix "field", "box", "element", "control" |
| Always "extract" | Mix "extract", "pull", "get", "retrieve" |

### Verbose Explanations

Claude is already smart. Don't over-explain:

**Bad — Too verbose (~150 tokens):**
```markdown
## Extract PDF text

PDF (Portable Document Format) files are a common file format that contains
text, images, and other content. To extract text from a PDF, you'll need to
use a library. There are many libraries available for PDF processing, but we
recommend pdfplumber because it's easy to use and handles most cases well.
First, you'll need to install it using pip. Then you can use the code below...
```

**Good — Concise (~50 tokens):**
```markdown
## Extract PDF text

Use pdfplumber for text extraction:

```python
import pdfplumber

with pdfplumber.open("file.pdf") as pdf:
    text = pdf.pages[0].extract_text()
```
```

## Structure Issues

### "When to Use" in Body

Claude only sees the description when deciding to trigger. "When to Use This Skill" sections in the body are useless.

**Bad:**
```markdown
---
name: pdf-processing
description: Processes PDF files.
---

# PDF Processing

## When to Use This Skill
Use this skill when working with PDF files...
```

**Good — Put triggers in description:**
```yaml
description: Extract text and tables from PDF files, fill forms, merge documents. Use when working with PDF files or when the user mentions PDFs, forms, or document extraction.
```

### Wrong Point of View in Description

Descriptions are injected into the system prompt. Inconsistent POV causes discovery problems.

| Good (third person) | Bad |
|---------------------|-----|
| "Processes Excel files and generates reports" | "I can help you process Excel files" |
| "Extracts data from spreadsheets" | "You can use this to extract data" |

## MCP Tool References

If using MCP tools, always use fully qualified names:

**Format**: `ServerName:tool_name`

**Good:**
```markdown
Use the BigQuery:bigquery_schema tool to retrieve table schemas.
Use the GitHub:create_issue tool to create issues.
```

**Bad:**
```markdown
Use the bigquery_schema tool...  # May fail if multiple servers available
```
