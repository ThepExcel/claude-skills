# Program-Specific Syntax Patterns

**CRITICAL: Each program has unique syntax. Using wrong patterns = incorrect content.**

---

## Excel

### Reference Style in Documentation vs Examples

**Documentation (syntax):** Show cell references to teach the pattern
```
=FUNCTION(range)
=FUNCTION(lookup_value, table_array, col_index, [match_type])
```

**Examples (must be self-explanatory WITHOUT screenshots):**
```
// BAD - Reader doesn't know what's in A1:A10
=SUM(A1:A10)

// GOOD - Literal values, reader understands immediately
=SUM(10, 20, 30, 40, 50)

// GOOD - Inline array with clear data
=SUM({100, 200, 300, 400})

// GOOD - Descriptive table reference
=SUM(SalesTable[Amount])
```

### Example Patterns for Function Explainer JSON

```json
// BAD - meaningless without screenshot
{
  "example_formula": "=VLOOKUP(A1, B:D, 2, FALSE)",
  "example_result": "Apple",
  "example_explanation": "..."
}

// GOOD - self-explanatory
{
  "example_formula": "=VLOOKUP(\"B001\", {\"B001\",\"Apple\",500; \"B002\",\"Banana\",300}, 2, FALSE)",
  "example_result": "Apple",
  "example_explanation": "ค้นหา \"B001\" ในคอลัมน์แรก พบแล้วคืนค่าคอลัมน์ที่ 2 คือ \"Apple\""
}

// GOOD - simple with clear values
{
  "example_formula": "=IF(85>=60, \"ผ่าน\", \"ไม่ผ่าน\")",
  "example_result": "ผ่าน",
  "example_explanation": "85 มากกว่า 60 จึงได้ผลลัพธ์ \"ผ่าน\""
}
```

### Techniques for Self-Explanatory Examples

1. **Literal values:** `=SUM(10, 20, 30)` - Reader sees actual data
2. **Inline arrays:** `=MAX({85, 92, 78, 95})` - Data visible in formula
3. **Structured table refs:** `=SUM(SalesTable[Amount])` - Name explains meaning
4. **Named ranges:** `=AVERAGE(StudentScores)` - Name is self-documenting
5. **Explain in description:** If must use A1, add "สมมติ A1 มีค่า 100"

**Priority:** Literal > Inline Array > Structured Ref > Named Range > Cell Ref + Explanation

### Key Characteristics
- Starts with `=`
- Inline arrays use `{}` with `;` for rows, `,` for columns
- Optional arguments in `[brackets]` in documentation
- Examples should work standalone without seeing spreadsheet

---

## Google Sheets

### Same Rule: Examples Must Be Self-Explanatory

**Documentation (syntax):** Show cell references
```
=FUNCTION(range)
=ARRAYFORMULA(expression)
```

**Examples (self-explanatory without screenshots):**
```
// BAD
=ARRAYFORMULA(B2:B100*C2:C100)

// GOOD - clear what's happening
=ARRAYFORMULA({10;20;30} * {2;2;2})
// Result: {20;40;60}

// GOOD - inline data
=QUERY({1,"John",85; 2,"Jane",92; 3,"Bob",78}, "SELECT Col2, Col3 WHERE Col3 > 80")
```

### Key Differences from Excel
| Feature | Excel | Google Sheets |
|---------|-------|---------------|
| Array formulas | Ctrl+Shift+Enter or spill | ARRAYFORMULA() wrapper |
| Query language | Power Query | QUERY() with SQL-like syntax |
| Import data | Power Query | IMPORTRANGE(), IMPORTDATA() |

### Example Patterns for Function Explainer JSON

```json
// GOOD - self-explanatory QUERY
{
  "example_formula": "=QUERY({\"John\",85; \"Jane\",92; \"Bob\",78}, \"SELECT * WHERE Col2 >= 80\")",
  "example_result": "John, 85 / Jane, 92",
  "example_explanation": "กรองเฉพาะแถวที่คะแนน (Col2) >= 80"
}

// GOOD - clear FILTER
{
  "example_formula": "=FILTER({\"A\",1; \"B\",2; \"C\",3}, {1;2;3} > 1)",
  "example_result": "{\"B\",2; \"C\",3}",
  "example_explanation": "กรองแถวที่ค่าในคอลัมน์ที่สองมากกว่า 1"
}
```

### Google Sheets Unique Functions
- `QUERY()` - SQL-like queries on data
- `ARRAYFORMULA()` - Apply formula to range
- `IMPORTRANGE()` - Import from other sheets
- `GOOGLETRANSLATE()` - Translation
- `IMAGE()` - Insert image from URL

---

## DAX (Power BI / Power Pivot)

### Reference Style: Table[Column] - NOT Cell References!
```
Table[Column]           Column reference
'Table Name'[Column]    Table with spaces
RELATED(Table[Column])  Related table column
```

### Formula Pattern
```
FUNCTION(Table[Column])
FUNCTION(Table[Column], expression)
Measure := FUNCTION(...)
```

### CRITICAL: DAX vs Excel
```
// WRONG - Excel style (will NOT work in DAX)
=SUM(A1:A10)

// CORRECT - DAX style
SUM(Sales[Amount])
```

### Examples
```dax
// Simple aggregation
Total Sales = SUM(Sales[Amount])

// With filter context
Filtered Sales = CALCULATE(
    SUM(Sales[Amount]),
    Products[Category] = "Electronics"
)

// Iterator function
Weighted Avg = SUMX(
    Sales,
    Sales[Quantity] * Sales[UnitPrice]
)

// Time intelligence
YTD Sales = TOTALYTD(
    SUM(Sales[Amount]),
    Calendar[Date]
)
```

### Key Characteristics
- NO `=` prefix (it's a measure definition)
- NO cell references (A1, B2)
- Always `Table[Column]` format
- Context-aware (row context, filter context)
- CALCULATE for filter modification
- X-suffix functions for row-by-row (SUMX, AVERAGEX)

---

## Power Query (M Language)

### Reference Style: Functional Programming
```
[ColumnName]                    Current row column (in each context)
Source[ColumnName]              Specific step's column
Table.SelectRows(table, each [Column] > 0)
```

### Function Pattern
```
Category.FunctionName(param1, param2)
```

### Categories
- `Table.` - Table operations
- `List.` - List operations
- `Text.` - Text operations
- `Number.` - Number operations
- `Date.` / `DateTime.` - Date operations
- `Record.` - Record operations

### The `each` Keyword
```m
// 'each' creates a function for row-by-row processing
each [ColumnName]              // Get column value for current row
each [Price] * [Quantity]      // Calculate per row
each _ > 100                   // _ represents current item in lists
```

### Examples
```m
// Filter rows
Table.SelectRows(Source, each [Amount] > 1000)

// Add column
Table.AddColumn(Source, "Total", each [Price] * [Qty])

// Transform column
Table.TransformColumns(Source, {"Name", Text.Upper})

// Group by
Table.Group(Source, {"Category"}, {
    {"Total", each List.Sum([Amount]), type number}
})

// Combine tables
Table.Combine({Table1, Table2})
```

### Key Characteristics
- NO `=` prefix
- PascalCase function names: `Table.SelectRows`
- `each` for row operations
- `[Column]` in `each` context
- Let...in structure for multi-step
- Type annotations: `as table`, `as text`

---

## n8n (Expressions)

### Reference Style: Method on Objects
```javascript
$json.fieldName                 Access field
$json.data.hasField('key')      Method on object
$json.items.filter(...)         Method on array
$('NodeName').item.json         Reference other node
```

### Pattern: METHOD SYNTAX (not function syntax)
```javascript
// CORRECT - method on object/string/array
{{ $json.field.method() }}

// WRONG - standalone function
{{ method($json.field) }}
```

### Examples
```javascript
{{ $json.email.extractDomain() }}
{{ $json.items.filter(x => x.active) }}
{{ $json.data.hasField('email') }}
{{ $json.text.substring(0, 10) }}
{{ $json.list.every(item => item.valid) }}
```

**Full reference:** See `n8n-syntax-patterns.md`

---

## Quick Comparison Table

| Program | Reference Style | Example (Self-Explanatory) |
|---------|----------------|----------------------------|
| **Excel** | Literal values / inline arrays | `=SUM(10, 20, 30)` or `=SUM({100;200;300})` |
| **Google Sheets** | Inline arrays | `=QUERY({"A",1;"B",2}, "SELECT *")` |
| **DAX** | `Table[Column]` | `SUM(Sales[Amount])` |
| **Power Query** | `[Column]` in `each` | `Table.SelectRows(Source, each [Price] > 100)` |
| **n8n** | `$json.field.method()` | `{{ $json.email.extractDomain() }}` |

---

## Common Mistakes by Program

### Excel/Google Sheets Content
```json
// WRONG - Cell reference, reader can't understand without screenshot
"example_formula": "=SUM(A1:A10)"
"example_result": "150"

// CORRECT Option 1 - Literal values
"example_formula": "=SUM(10, 20, 30, 40, 50)"
"example_result": "150"

// CORRECT Option 2 - Inline array
"example_formula": "=AVERAGE({85, 92, 78, 95, 88})"
"example_result": "87.6"

// CORRECT Option 3 - Structured reference (self-explanatory name)
"example_formula": "=SUM(SalesTable[Amount])"
"example_result": "15000"
"example_explanation": "รวมค่าทั้งหมดในคอลัมน์ Amount ของตาราง SalesTable"

// CORRECT Option 4 - Named range (with explanation)
"example_formula": "=AVERAGE(StudentScores)"
"example_result": "82.5"
"example_explanation": "หาค่าเฉลี่ยจาก Named Range 'StudentScores' ที่มีค่า {75, 85, 90, 80}"
```

### DAX Content
```json
// WRONG - Excel cell style (DAX doesn't use cells!)
"example_formula": "=SUM(A1:A10)"

// CORRECT - DAX Table[Column] style
"example_formula": "SUM(Sales[Amount])"

// CORRECT - With CALCULATE
"example_formula": "CALCULATE(SUM(Sales[Amount]), Products[Category] = \"Electronics\")"
```

### Power Query Content
```json
// WRONG - Excel style
"example_formula": "=FILTER(A1:A10, B1:B10 > 100)"

// CORRECT - M style with each and [Column]
"example_formula": "Table.SelectRows(Source, each [Amount] > 100)"
```

### n8n Content
```json
// WRONG - Standalone function style
"example_formula": "{{ extractDomain($json.email) }}"
"example_formula": "{{ hasField($json.data, 'link') }}"

// CORRECT - Method on object style
"example_formula": "{{ $json.email.extractDomain() }}"
"example_formula": "{{ $json.data.hasField('link') }}"
```

---

## Checklist Before Creating Content

- [ ] Identified correct program
- [ ] Using correct reference style (cell vs table[column] vs $json)
- [ ] Using correct function pattern (=FUNC vs FUNC vs Category.Func vs .method())
- [ ] **Examples are SELF-EXPLANATORY without screenshots**
  - Excel/Sheets: Use literals, inline arrays, or structured refs (NOT `A1:A10`)
  - DAX: Table[Column] is already self-explanatory
  - Power Query: `[Column]` in `each` context is clear
  - n8n: `$json.field.method()` with realistic field names
- [ ] Examples match the program's actual syntax
- [ ] No mixing patterns between programs
