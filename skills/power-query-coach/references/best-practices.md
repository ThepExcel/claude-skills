# Best Practices for Power Query

## Table of Contents

1. [Overview](#overview)
2. [Core Principles](#core-principles)
   - [1. Reproducibility: Eliminate Manual Steps](#1-reproducibility-eliminate-manual-steps)
   - [2. Portability: Query Workbook Separation](#2-portability-query-workbook-separation)
   - [3. Find the True Source](#3-find-the-true-source)
   - [4. Future-Proofing: Design for Change](#4-future-proofing-design-for-change)
   - [5. Headers Before Everything](#5-headers-before-everything)
   - [6. Document and Organize](#6-document-and-organize)
   - [7. Keep It Simple](#7-keep-it-simple)
3. [Specific Practices](#specific-practices)
   - [Working with Dates](#working-with-dates)
   - [Working with Numbers](#working-with-numbers)
   - [Working with Text](#working-with-text)
   - [Combining Data](#combining-data)
   - [Performance Optimization](#performance-optimization)
4. [Workflow Best Practices](#workflow-best-practices)
   - [Starting a New Project](#starting-a-new-project)
   - [Maintaining Existing Queries](#maintaining-existing-queries)
5. [Common Patterns](#common-patterns)
   - [Pattern: Monthly Report Refresh](#pattern-monthly-report-refresh)
   - [Pattern: Combining Multiple Sources](#pattern-combining-multiple-sources)
   - [Pattern: Lookup/Reference Tables](#pattern-lookupreference-tables)
6. [Checklist for "Good" Queries](#checklist-for-good-queries)
7. [Anti-Patterns to Avoid](#anti-patterns-to-avoid)
8. [Learning Path](#learning-path)
9. [Remember](#remember)

---

## Overview

This guide covers principles and practices that lead to robust, maintainable, and future-proof Power Query solutions. Use this for general guidance and to help users build better habits.

## Core Principles

### 1. Reproducibility: Eliminate Manual Steps

**The Golden Rule**: If you can't press "Refresh" and get updated results automatically, it's not truly automated.

**What reproducibility means**:
- No manual copying/pasting between files
- No manual formatting in Excel before loading
- No "open file → delete rows → save → load" workflows
- Everything automated in Power Query

**Why it matters**:
```
❌ Bad workflow:
1. Export from system → CSV
2. Open in Excel
3. Manually delete header rows
4. Fix column names
5. Save as .xlsx
6. Load into Power Query

✅ Good workflow:
1. Load CSV directly into Power Query
2. Remove top rows in query
3. Promote/rename headers in query
4. Set types in query
5. Refresh anytime
```

**How to achieve it**:
- **Find the true source**: CSV, database, API, not manually edited files
- **Move all prep into query**: Every manual step should become a Power Query step
- **Use From Folder**: For multiple files, don't manually combine
- **Parameter**: Use parameters for changing paths/dates instead of editing query

**Questions to ask**:
- "Where does this data really come from?"
- "What manual steps do you do before loading?"
- "If new data arrives tomorrow, can you just refresh?"

**Benefits**:
- Save time (no repetitive manual work)
- Reduce errors (automation is consistent)
- Scale easily (handle 10 or 1000 files the same way)
- Documentation (query shows exactly what's done)

---

### 2. Portability: Query Workbook Separation

**The Principle**: Create Power Query transformations in a separate workbook from your data source.

**Why separate**:
```
❌ Bad: Query and data in same file
data_march.xlsx:
  - Sheet1: Raw data
  - Queries: Transformations
  
→ Hard to copy queries to data_april.xlsx
→ Hard to move to Power BI
→ Have to redo transformations each time

✅ Good: Query workbook separate
transform_pipeline.xlsx:
  - Only queries, no data
  - Points to external source
  
→ Copy queries to any new file
→ Move to Power BI easily
→ One set of transformations, many uses
```

**How to set up**:
1. Create new blank workbook: "Data_Transformations.xlsx"
2. Get Data from external source (CSV, SharePoint, folder)
3. Build all transformations
4. Save query workbook
5. Copy queries to target workbook or Power BI as needed

**Benefits**:
- **Reusability**: Same queries for different periods/regions
- **Flexibility**: Easy to move between Excel and Power BI
- **Maintenance**: Update queries in one place
- **Sharing**: Share query file, not data

**Real-world example**:
```
Monthly Sales Report:
- data_pipeline.xlsx (queries only)
  - Connects to SharePoint/sales-data-202410
  - Transformations: unpivot, clean, aggregate
  
- October_Report.xlsx
  - Loads from data_pipeline queries
  - Creates Pivot Tables
  
- November_Report.xlsx
  - Same queries, different month
  - Just change source path parameter
```

---

### 3. Find the True Source

**The Question**: "Where does this data REALLY come from?"

**Common wrong answers**:
- "I got this Excel file from my colleague"
- "It's a report that gets sent to me"
- "I download and clean it manually"

**Right answers dig deeper**:
- "It's exported from SAP as CSV"
- "It's in our SharePoint folder"
- "It comes from Salesforce API"
- "Database pulls it nightly"

**Why this matters**:
```
Scenario: User shows Excel file with neat data
Wrong: Load from Excel → Can't refresh
Right: Find it's from SharePoint → Load from SharePoint → Can refresh

Scenario: User shows manually combined sheets
Wrong: Use their combined file → Manual work on new data
Right: Get original sheets → Combine Files → Automatic on new data
```

**Questions to ask**:
1. "Where did this file come from originally?"
2. "How do you get updated data?"
3. "Does someone send this, or is it in a shared location?"
4. "Is this manually edited, or straight from the source?"

**Red flags (not true source)**:
- "I delete these rows first"
- "I fix the headers in Excel"
- "I copy from multiple sheets"
- "Someone emails it to me"

**Goal**: Connect Power Query to the actual source system (database, API, shared folder) not to manually prepared files.

**Benefits**:
- Refresh works automatically
- No manual steps to forget
- Always current data
- Audit trail clear

---

### 4. Future-Proofing: Design for Change

**The Mindset**: Data changes. New columns appear. New categories get added. Query should handle it.

**How to future-proof**:

**Use "Unpivot Other Columns"**:
```
❌ Hardcoded: Unpivot Jan, Feb, Mar
   → Apr added next month → Breaks

✅ Future-proof: Unpivot Other Columns (keep Product, Region)
   → Apr automatically unpivoted
```

**Use Dynamic Filters**:
```
❌ Hardcoded: Keep rows where Product = "A" or "B" or "C"
   → Product D added → Excluded

✅ Dynamic: Remove Empty, or keep where Sales > 0
   → Product D automatically included
```

**Avoid Hardcoded Column Names**:
```
❌ Changed Type with specific columns
   → Column renamed → Breaks

✅ Delete old Changed Type after transformation
   → Re-apply with new structure
```

**Use Parameters**:
```
❌ Hardcoded path: C:\Reports\2024\October\data.csv
   → November comes → Have to edit query

✅ Parameter: FilePath = "C:\Reports\" & Year & "\" & Month & "\data.csv"
   → Change parameter, not query
```

**Think about**:
- "What if a new column is added?"
- "What if values change?"
- "What if structure is slightly different?"
- "Will this work next month/year?"

**Test future-proofing**:
1. Add a test column to source
2. Refresh query
3. Does it handle it correctly?

---

### 5. Headers Before Everything

**The Rule**: Fix header structure BEFORE worrying about data quality.

**Why**:
```
Wrong order:
1. Fix data types → Applied to wrong columns
2. Clean data → Cleaning wrong structure  
3. Fix headers → Everything breaks
4. Have to redo steps 1-2

Right order:
1. Fix headers → Get structure right
2. Fix data types → Apply to correct columns
3. Clean data → Clean correct data
```

**Common scenarios**:

**Wide format + multi-row headers**:
- Fix BOTH at same time
- Get to single-row, long format
- Then worry about types and cleaning

**Merged cells**:
- Fill Down immediately
- Before any filtering or calculations

**Grouped data**:
- Fill Down hierarchy
- Remove group headers
- Then work with clean structure

**Why this matters**:
- Column names change during structure fixes
- Old "Changed Type" steps break
- Transformations apply to wrong columns

**Remember**: Structure first, content second

---

### 6. Document and Organize

**Name things clearly**:
```
❌ Bad query names:
- Query1
- Table_1
- Step 5

✅ Good query names:
- Sales_Raw
- Sales_Cleaned
- Sales_Aggregated
- Product_Lookup
```

**Rename steps**:
```
❌ Bad step names:
- Changed Type
- Changed Type1
- Changed Type2

✅ Good step names:
- Set_Initial_Types
- Remove_Empty_Rows
- Unpivot_Months
- Merge_with_Product_Details
```

**Add comments**:
- Right-click step → Properties → Add description
- Especially for complex M code
- Explain WHY, not just WHAT

**Group related queries**:
- Use folders/groups in Query Editor
- "Source Queries", "Transformation", "Output"

**Benefits**:
- Future you understands what past you did
- Others can understand your work
- Easier to debug and maintain

---

### 7. Keep It Simple

**The Principle**: Simplest solution that works is usually best.

**Examples**:

**Over-complicated**:
```
❌ 15 steps with complex M code to combine sheets
✅ Combine Files from folder → 3 clicks
```

**Over-engineered**:
```
❌ Custom function with error handling for every scenario
✅ Simple unpivot + filter → Handles 90% of cases
```

**Too clever**:
```
❌ Nested Table.AddColumn with LAMBDA and List.Transform
✅ Add Conditional Column in UI → Same result, readable
```

**When to use M code**:
- UI can't do it
- Complex conditional logic needed
- Performance optimization required
- Truly dynamic behavior needed

**When to stick with UI**:
- UI can do it easily
- Steps are clear
- Future maintainer will understand

**Benefits**:
- Easier to maintain
- Easier to debug
- Easier for others to understand
- Less likely to break

**Rule of thumb**: If you're writing M code, ask "Can I do this in UI instead?" If yes, probably should.

---

## Specific Practices

### Working with Dates

**Always use "Using Locale"**:
- Transform → Data Type → Date → **Using Locale**
- Choose correct locale (US, UK, Thai, etc.)
- Never just click "Date" without specifying

**Handle mixed formats**:
- If possible, standardize at source
- If not, may need M code to detect and parse

**Store as actual dates**:
- Not text like "Jan 2024"
- Not Excel serial numbers (44927)
- Actual Date type for filtering and sorting

---

### Working with Numbers

**Always prefer Decimal Number over Whole Number**:
```
✅ Use Decimal Number by default:
- Prices, amounts, monetary values
- Rates, percentages, ratios
- Weights, measurements
- Any value that might have decimals in future

✅ Use Whole Number only when certain:
- Count of discrete items (truly no decimals possible)
- But even "quantity" might need decimals (0.5 kg sold)
```

**Why Decimal is safer**:
```
Scenario: Price column
Current data: 100, 200, 300 (all whole numbers)
Set as: Whole Number

Next month: 150.50 arrives
Result: ❌ Error or truncation → Data loss!

Better: Set as Decimal Number from start
→ Works with 100, 200, 300 now
→ Works with 150.50 later
→ Future-proof! ✅
```

**Principle**: 
> **"When in doubt, use Decimal Number"**
> Decimal handles whole numbers perfectly (100 = 100.0)
> But Whole Number cannot handle decimals

**Set correct types**:
- Whole Number vs Decimal Number
- Currency if appropriate

**Be aware of Banker's Rounding**:
- Default Power Query behavior
- Round .5 to even number
- Use Number.RoundAwayFromZero if need normal rounding

**Handle negative numbers**:
- Check if stored as text with parentheses: (100)
- May need Replace or custom parsing

---

### Working with Text

**Mind case sensitivity**:
- "Product" ≠ "product"
- Use Transform → Format → UPPERCASE or lowercase if needed

**Trim whitespace**:
- Transform → Format → Trim
- Removes leading/trailing spaces
- Prevents "Product " ≠ "Product" issues

**Handle special characters**:
- Be careful with quotes, commas in CSV
- Use proper delimiters

---

### Combining Data

**Append when** (vertical combination):
- Same structure, more records
- Sales from multiple months/regions
- Requirement: Column names must match

**Merge when** (horizontal combination):
- Related data, need to enrich
- Customers + Orders, Products + Categories
- Requirement: Common key column

**Combine Files when**:
- Multiple files, same structure
- Use Transform Sample File
- All transformations in sample, not in main query

---

### Performance Optimization

**Query Folding**:
- Keep source-side operations at top (filter, select columns)
- These push to database/source (fast)
- Local operations last (slower)

**Minimize steps**:
- Remove unnecessary steps
- Combine multiple operations if possible
- Delete redundant transformations

**Disable loading** when appropriate:
- Intermediate queries don't need to load to Excel
- Right-click query → Uncheck "Enable load"
- Reduces memory usage

**Buffer() carefully**:
- Only use when needed (multiple references to expensive operation)
- Overuse can slow things down

---

## Workflow Best Practices

### Starting a New Project

**1. Understand the need**:
- What's the final output?
- Who will use it?
- How often will it refresh?

**2. Find true source**:
- Where does data really come from?
- Can we connect directly?

**3. Create query workbook**:
- Separate from data
- Build transformations

**4. Develop iteratively**:
- Get raw data
- Fix structure
- Fix content
- Create outputs
- Test refresh

**5. Document**:
- Name queries clearly
- Rename steps
- Add comments

---

### Maintaining Existing Queries

**When data changes**:
- Don't panic!
- Check Applied Steps one by one
- Find where it breaks
- Understand why
- Fix or adapt

**When source changes**:
- Update connection
- Verify column names still match
- Test thoroughly

**When requirements change**:
- Add new transformations after existing ones
- Don't delete old steps unless sure
- Test with existing outputs first

**Regular review**:
- Periodically check queries still make sense
- Remove obsolete steps
- Optimize if slow
- Update documentation

---

## Common Patterns

### Pattern: Monthly Report Refresh

**Setup**:
1. Query workbook points to SharePoint folder
2. Transformations process latest files
3. Output loaded to reporting workbook
4. Pivot Tables/charts use query output

**Monthly process**:
1. New data arrives in SharePoint
2. Open report workbook
3. Data → Refresh All
4. Charts update automatically
5. Done!

---

### Pattern: Combining Multiple Sources

**Setup**:
1. Query for each source (Database, SharePoint, CSV)
2. Transform each to common structure
3. Append all sources
4. Final cleanup and loading

**Benefits**:
- Single source of truth
- All data cleaned consistently
- Easy to add new sources

---

### Pattern: Lookup/Reference Tables

**Setup**:
1. Main transaction query
2. Separate queries for lookups (products, customers, categories)
3. Merge main with lookups to enrich
4. Final output has all needed info

**Tips**:
- Set lookups to "Enable load = False"
- Use Left Outer join for main data
- Expand only needed columns from lookup

---

## Checklist for "Good" Queries

Before considering query complete, check:

**Structure**:
- [ ] Connects to true source (not manually edited file)
- [ ] Separate query workbook (if appropriate)
- [ ] Can refresh automatically

**Transformations**:
- [ ] Headers fixed first
- [ ] Types set correctly (with "Using Locale" for dates)
- [ ] No hardcoded filters
- [ ] Future-proofed (new columns/values will work)

**Quality**:
- [ ] Steps are clear and necessary
- [ ] Queries and steps named well
- [ ] Complex steps have comments
- [ ] Old/redundant steps removed

**Testing**:
- [ ] Tested with different data
- [ ] Refresh works
- [ ] Output is correct format
- [ ] Performance acceptable

**Documentation**:
- [ ] Source documented
- [ ] Purpose clear
- [ ] Maintained able by others

---

## Anti-Patterns to Avoid

**Don't**:
- ❌ Edit source data manually before loading
- ❌ Use "Unpivot Columns"
- ❌ Hardcode values that might change
- ❌ Skip "Using Locale" for dates
- ❌ Have queries and data in same file (for production)
- ❌ Use checkbox filters for dynamic data
- ❌ Make changes to main query in Combine Files
- ❌ Filter before Fill Down on grouped data

**Do**:
- ✅ Automate everything in Power Query
- ✅ Use "Unpivot Other/Selected Columns"
- ✅ Use dynamic conditions and parameters
- ✅ Always specify date locale
- ✅ Separate query workbook for portability
- ✅ Use Remove Empty or conditions
- ✅ Transform Sample File for Combine Files
- ✅ Fill Down before filtering

---

## Learning Path

### For Beginners:
1. Master UI basics (unpivot, pivot, merge, append)
2. Understand data types and dates
3. Learn to use Applied Steps
4. Practice finding true source

### For Intermediate:
1. Future-proof transformations
2. Query workbook separation
3. Combine Files effectively
4. Understand when to merge vs append

### For Advanced:
1. Learn M code basics (when UI isn't enough)
2. Custom functions
3. Query folding optimization
4. Parameters and dynamic queries

---

## Remember

**Good Power Query practice is about**:
- **Reproducibility**: Press refresh, get results
- **Portability**: Works in different contexts
- **Future-proofing**: Handles change gracefully
- **Simplicity**: Clear, maintainable solutions
- **Documentation**: Future you will thank you

**The goal**: Build queries that work reliably, refresh automatically, and are easy to understand and maintain! 🎯✨
