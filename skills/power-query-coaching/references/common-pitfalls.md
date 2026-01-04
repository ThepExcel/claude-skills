# Common Pitfalls and Recovery Strategies

## Table of Contents

1. [Overview](#overview)
2. [Critical Gotchas (Must Know!)](#critical-gotchas-must-know)
   - [1. M Code Column References with Special Characters](#1-m-code-column-references-with-special-characters)
   - [2. Case Sensitivity](#2-case-sensitivity)
   - [3. Lazy Filter (Hardcoded Values)](#3-lazy-filter-hardcoded-values)
   - [4. Wrong Order: Filter Before Fill Down](#4-wrong-order-filter-before-fill-down)
   - [5. Banker's Rounding](#5-bankers-rounding-not-normal-rounding)
   - [6. Date Locale Misinterpretation](#6-date-locale-misinterpretation)
   - [7. Auto "Changed Type" With Hardcoded Columns](#7-auto-changed-type-with-hardcoded-columns)
   - [8. Sort Then Remove Duplicates](#8-sort-then-remove-duplicates-loses-original-sort)
   - [9. Using Whole Number When Should Use Decimal](#9-using-whole-number-when-should-use-decimal)
   - [10. Unpivot Columns (The Forbidden One)](#10-unpivot-columns-the-forbidden-one)
   - [11. Merge vs Append Confusion](#11-merge-vs-append-confusion)
   - [12. Transform Sample File Not Used Correctly](#12-transform-sample-file-not-used-correctly)
3. [Mistakes by Experience Level](#mistakes-by-experience-level)
   - [Beginner Mistakes](#beginner-mistakes)
   - [Intermediate Mistakes](#intermediate-mistakes)
   - [Advanced Mistakes](#advanced-mistakes)
4. [Recovery Strategies](#recovery-strategies)
   - [General Recovery Approach](#general-recovery-approach)
   - [Specific Recoveries](#specific-recoveries)
5. [Proactive Warning Phrases](#proactive-warning-phrases)
6. [Diagnostic Questions for Troubleshooting](#diagnostic-questions-for-troubleshooting)
7. [Prevention > Recovery](#prevention--recovery)
8. [Remember](#remember)

---

## Overview

This guide covers common mistakes users make with Power Query, why they happen, and how to recover. Use this when user encounters issues or to warn them proactively.

## Critical Gotchas (Must Know!)

### 1. M Code Column References with Special Characters

**Problem**: Column names with special characters need special syntax in M code

**Where it matters**:
- Column names with `/` : `Factory/Warehouse`
- Column names with `-` : `Product-Code`
- Column names with spaces: `My Column`
- Column names starting with numbers: `2024 Sales`
- Any special characters or reserved words

**Correct syntax**:
```
❌ Wrong: [Factory/Warehouse]
✅ Right: [#"Factory/Warehouse"]

❌ Wrong: [Product-Code]
✅ Right: [#"Product-Code"]

❌ Wrong: [My Column]
✅ Right: [#"My Column"]
```

**Rule**: 
- Simple names (letters, numbers, underscore): `[ColumnName]`
- Special characters or spaces: `[#"Column Name"]`

**Why it matters**:
- If you write M code or conditional columns with wrong syntax → Error
- Example in Factory/Warehouse case: `if [TXID] = null then [#"Factory/Warehouse"] else null`

**Prevention**:
- When referencing columns in formulas, check if name has special characters
- Use `[#"..."]` syntax for any non-simple names
- Power Query UI usually generates correct syntax, but manual formulas need attention

---

### 2. Case Sensitivity

**Problem**: Power Query is case-sensitive EVERYWHERE

**Where it matters**:
- Column names: "Sales" ≠ "sales"
- Filter values: "Product A" ≠ "product a"  
- M code: `Table.SelectRows` ≠ `table.selectrows`
- Combine files: Files with different casing create separate columns

**Example disaster**:
```
File1.xlsx has column: "Product"
File2.xlsx has column: "product"
→ Combine Files creates TWO columns: "Product" and "product"
→ Data split across both, analysis broken
```

**Prevention**:
- Standardize column names at source
- Use Transform > Format > UPPERCASE or lowercase
- Always check combined data for duplicate columns with different cases

**Recovery**:
- Rename columns to match
- Or merge columns if data already split

**Why it happens**: Power Query treats text literally, unlike Excel which is case-insensitive

---

### 2. Lazy Filter (Hardcoded Values)

**Problem**: Using UI checkbox filter hardcodes specific values into query

**Where it happens**:
- Click filter dropdown
- Check/uncheck specific items
- This creates: `Table.SelectRows(#"Previous Step", each [Column] = "Value1" or [Column] = "Value2")`

**Why it's bad**:
```
January data: Filter shows "Product A", "Product B", "Product C"
→ You uncheck "Product C"
→ Query hardcodes: Keep only "Product A" and "Product B"
→ February data: New "Product D" arrives
→ Query still only keeps A and B
→ Product D is silently excluded!
```

**Better alternatives**:

**Alternative 1: Remove Empty**
- If you want to remove blanks:
- Click filter dropdown → **Remove Empty**
- This creates dynamic filter, not hardcoded values

**Alternative 2: Keep/Remove Rows with condition**
- **Home** tab → **Remove Rows** → **Remove Blank Rows**
- Or use conditional logic: "keep rows where [Sales] > 0"

**Alternative 3: Custom condition in filter**
- Instead of checking boxes, use "Text Filters" or "Number Filters"
- "Contains", "Greater than", etc. are dynamic

**Recovery**:
- Go to Applied Steps
- Find the filter step
- Look at formula bar: if it says `= "Value1" or = "Value2"` → it's hardcoded
- Delete the step and redo with Remove Empty or condition

**Why it happens**: UI checkbox filter is convenient but creates static filter

---

### 3. Wrong Order: Filter Before Fill Down

**Problem**: Filtering before Fill Down loses hierarchy information permanently

**Scenario**:
```
| Factory | Sales |
|---------|-------|
| A       |       | <- Group header
| WH-001  | 100   |
| WH-002  | 150   |
| B       |       | <- Group header
```

**Wrong order**:
1. Filter out empty Sales → Removes A and B rows
2. Try to Fill Down → Nothing to fill! Factory info is gone

**Correct order**:
1. Fill Down Factory column → A fills down to WH-001 and WH-002
2. Filter out empty Sales → Removes group headers but data rows have Factory

**Recovery**:
- If you already filtered: **Undo is your only hope**
- Delete the filter step in Applied Steps
- Redo: Fill Down first, then filter

**Rule**: **Always Fill Down before filtering grouped data**

**Why it happens**: Users see empty rows and want to remove them immediately, not realizing they contain critical information

---

### 4. Banker's Rounding (Not Normal Rounding!)

**Problem**: Power Query uses banker's rounding, not mathematical rounding

**What it is**:
- Normal rounding: 0.5 → 1, 1.5 → 2, 2.5 → 3
- Banker's rounding: 0.5 → 0 (even), 1.5 → 2 (even), 2.5 → 2 (even)
- Rule: Round .5 to nearest EVEN number

**Example**:
```
Number.Round(0.5) = 0  (not 1!)
Number.Round(1.5) = 2  (correct)
Number.Round(2.5) = 2  (not 3!)
Number.Round(3.5) = 4  (correct)
```

**Why it matters**:
- Financial calculations may be off
- Sum of rounded values ≠ expected
- Different from Excel's ROUND()

**Solution**:
- If you need mathematical rounding: Use M code `Number.RoundAwayFromZero()`
- If banker's rounding is OK: No action needed
- Be aware: Default is banker's

**Why it happens**: Banker's rounding reduces statistical bias in large datasets

---

### 5. Date Locale Misinterpretation

**Problem**: Dates interpreted with wrong locale (US vs UK/TH)

**Disaster scenario**:
```
Data has: 01/12/2024
Intended: December 1, 2024 (UK/TH format: DD/MM/YYYY)
Power Query assumes: January 12, 2024 (US format: MM/DD/YYYY)
→ All dates wrong!
→ December becomes January, etc.
```

**How it happens**:
- Click column type dropdown → Date (WITHOUT "Using Locale")
- Power Query guesses locale based on system settings
- Often guesses wrong

**Prevention**:
- **ALWAYS** use "Using Locale" when setting date type
- Click Transform tab → Data Type → **Using Locale**
- Explicitly choose: English (United States), English (United Kingdom), Thai, etc.

**Detection**:
- Spot check a few dates after conversion
- If December 1 became January 12 → wrong locale
- Some dates may error if impossible (e.g., 13/05 in MM/DD)

**Recovery**:
- Delete the "Changed Type" step
- Redo with correct locale:
  - Transform → Data Type → Date → **Using Locale** → [Correct Locale]

**Why it happens**: Date formats are ambiguous, and defaults often wrong

---

### 6. Auto "Changed Type" With Hardcoded Columns

**Problem**: Power Query auto-generates "Changed Type" step when loading data, hardcoding column names

**Scenario**:
```
1. Load data with columns: Product, Jan, Feb, Mar
2. Auto "Changed Type" step created: Sets types for these 4 columns
3. You unpivot Jan, Feb, Mar → Now have Product, Month, Value
4. Auto "Changed Type" still references Jan, Feb, Mar
5. Refresh → Error! Jan, Feb, Mar don't exist anymore
```

**Detection**:
- Look at Applied Steps panel
- Find "Changed Type" step (usually first step)
- Look at formula bar: `= Table.TransformColumnTypes(#"Promoted Headers",{{"Jan", type number}, {"Feb", type number}...})`
- If it references columns you transformed → it's a problem

**Prevention**:
- After major transformations (unpivot, pivot, merge): Delete old "Changed Type"
- Re-apply data types to new structure
- New "Changed Type" step created with current columns

**Recovery**:
- Delete the problematic "Changed Type" step
- Select all columns
- Set correct types again
- For dates: Use "Using Locale"

**Why it happens**: Power Query tries to be helpful by auto-detecting types, but locks in column names

---

### 7. Sort Then Remove Duplicates (Loses Original Sort!)

**Problem**: Using "Remove Duplicates" after "Sort Rows" removes the sort

**What happens**:
```
1. Sort by Date (oldest to newest)
2. Remove Duplicates by Product (to keep first occurrence)
3. Result: Duplicates removed, but order is NOT by date anymore!
```

**Why**:
- "Remove Duplicates" doesn't preserve previous sort
- It uses its own internal ordering

**Solution**:
- If you need first/last by sort order:
  - Sort first
  - **Group By** with "All Rows" option
  - Take first row from each group
  - This preserves sort order

**Alternative**:
- Add an index column while sorted
- Remove duplicates
- Sort by index
- Remove index

**Why it happens**: Remove Duplicates is not sort-aware

---

### 9. Using Whole Number When Should Use Decimal

**Problem**: Setting numeric columns as Whole Number when they might have decimals in the future

**Scenario**:
```
Current data: Price = 100, 200, 300 (no decimals)
→ Auto-detect or user sets as Whole Number

Next month: Price = 150.50 (has decimals)
→ Query errors or truncates decimals → Data loss!
```

**Why it's bad**:
- Whole Number truncates/rejects decimal values
- Future data with decimals will error or lose precision
- Common in: Prices, amounts, rates, percentages, weights

**Best Practice**:
```
✅ Use Decimal Number by default for:
- Prices (99.99, 149.50)
- Amounts (1,234.56)
- Rates and percentages (98.5%)
- Weights/measurements (1.5 kg)
- Any monetary values

✅ Use Whole Number only when certain:
- Count of items (truly can't have decimals)
- IDs/codes (but Text is usually better)
```

**Principle**: 
> **"When in doubt, use Decimal Number"**
> - It's future-proof (supports decimals later)
> - It handles whole numbers fine (100 = 100.0)
> - Safer than risking data loss

**Prevention**:
- Default to Decimal Number for all numeric values
- Only use Whole Number when absolutely certain no decimals possible
- Even "quantity" might have decimals (0.5 kg sold)

**Recovery**:
- Change column type to Decimal Number
- Refresh query
- Check if any data was lost in previous runs

---

### 10. Unpivot Columns (The Forbidden One)

**Problem**: "Unpivot Columns" option creates weird formula that causes issues

**What's wrong**:
- Records formula differently than Other/Selected
- Can cause unexpected behavior later
- Power Query experts avoid it

**What to use instead**:
- "Unpivot Other Columns" - Select columns to keep fixed, unpivot the rest
- "Unpivot Only Selected Columns" - Select columns to unpivot specifically

**Why this matters**:
- Future-proofing
- Reliability
- Best practices from experts

**Rule**: ❌ Never use "Unpivot Columns" - Use Other or Selected instead

---

### 11. Merge vs Append Confusion

**Problem**: Using Merge when should Append, or vice versa

**Append (Union)**:
- Combines tables VERTICALLY (rows on top of rows)
- Use when: Same structure, different data (Jan + Feb sales, North + South regions)
- Requirement: Column names must match
- Example: 100 rows + 200 rows = 300 rows, same columns

**Merge (Join)**:
- Combines tables HORIZONTALLY (columns side by side)
- Use when: Related data, need to match rows (Customers + Orders)
- Requirement: Common key column
- Example: 100 rows + metadata = 100 rows, more columns

**Common mistakes**:
- Trying to append tables with different column names → Extra columns created
- Trying to merge tables that should be appended → One-to-many issues

**Solution**:
- Ask: "Same topic, more records?" → Append
- Ask: "Related topics, need to enrich?" → Merge

---

### 12. Transform Sample File Not Used Correctly

**Problem**: Making changes to main combined query instead of Transform Sample File

**Scenario**:
```
Combine Files from folder
→ Creates "Transform Sample File" and main query
→ User edits main query directly
→ Changes aren't applied to all files consistently
```

**Correct approach**:
1. Find "Transform Sample File" query
2. Make ALL transformations there (unpivot, remove rows, etc.)
3. Main query automatically applies to all files

**Why**:
- Transform Sample File = template
- Changes there apply to every file
- Changes in main query only affect combined result

**Detection**:
- If some files seem transformed differently
- Check if Transform Sample File was edited

---

## Mistakes by Experience Level

### Beginner Mistakes

**1. Trying to edit in Excel instead of Power Query**
- Problem: Make manual changes in Excel, then can't reproduce
- Solution: Put ALL data prep in Power Query for reproducibility

**2. Not knowing where source is**
- Problem: Can't refresh because don't know original file location
- Solution: Always document and use "true source" (not manually edited files)

**3. Clicking "Load" too early**
- Problem: Load messy data without transforming
- Solution: Always "Transform Data" first, inspect and clean, then Load

**4. Promoting headers at wrong time**
- Problem: Headers get treated as data or vice versa
- Solution: Check data carefully, promote headers after removing top rows if needed

**5. Not checking data types**
- Problem: Numbers stored as text, dates as text
- Solution: Always verify data types, use "Using Locale" for dates

---

### Intermediate Mistakes

**1. Hardcoded filters (Lazy Filter)**
- Covered above - use dynamic conditions instead

**2. Not future-proofing**
- Problem: Query works now but breaks when columns/values change
- Solution: Use "Other Columns", conditions, not hardcoded lists

**3. Combining files with mismatched columns**
- Problem: Case differences, spelling differences create duplicate columns
- Solution: Standardize at source or transform in sample file

**4. Ignoring Applied Steps**
- Problem: Don't understand what each step does
- Solution: Review steps, rename unclear ones, delete unnecessary ones

**5. Over-complicating transformations**
- Problem: Too many steps, convoluted logic
- Solution: Simplify, combine steps, use better UI options

---

### Advanced Mistakes

**1. Not optimizing query folding**
- Problem: Slow queries because transformations done locally instead of at database
- Solution: Understand query folding, keep folding steps at top

**2. Creating too many queries**
- Problem: Many single-use queries instead of reusable functions
- Solution: Create custom functions for repeated transformations

**3. Mixing M code and UI haphazardly**
- Problem: Hard to maintain, unclear logic
- Solution: Be consistent - mostly UI with M when needed, or structured M code

**4. Not handling errors**
- Problem: One bad row breaks entire query
- Solution: Use try...otherwise, remove errors, or handle specifically

---

## Recovery Strategies

### General Recovery Approach

**1. Check Applied Steps**
- Find where issue occurred
- Read formula bar to understand what step does

**2. Use "Go Back"**
- Click earlier step in Applied Steps
- See data at that point
- Identify exactly where it broke

**3. Delete problematic step**
- Right-click step → Delete
- Or edit formula bar directly

**4. Redo correctly**
- Reapply transformation the right way
- Verify results

**5. Test with new data**
- Add test record
- Refresh query
- Ensure it still works

---

### Specific Recoveries

**Problem: Wrong data types**
→ Delete "Changed Type" step → Re-apply correct types with "Using Locale" for dates

**Problem: Lost data after filter**
→ Delete filter step → Fill Down first → Re-apply filter

**Problem: Hardcoded values**
→ Delete filter step → Use "Remove Empty" or condition instead

**Problem: Columns not combining**
→ Check column names (case sensitivity!) → Rename to match → Combine again

**Problem: Dates wrong**
→ Delete date conversion → Use "Using Locale" with correct locale

**Problem: Query breaks on refresh**
→ Check for hardcoded column names in "Changed Type" → Delete → Re-apply

**Problem: Too slow**
→ Check if query folding works → Keep source-side operations at top → Limit local transformations

---

## Proactive Warning Phrases

Use these when guiding users:

**For Fill Down + Filter**:
> "⚠️ สำคัญมาก: ต้อง Fill Down ก่อน แล้วค่อย Filter นะคะ ถ้าทำกลับกัน Factory information จะหายไปเลย!"

**For Unpivot choice**:
> "⚠️ อย่าเลือก 'Unpivot Columns' นะคะ ใช้ 'Unpivot Other Columns' หรือ 'Unpivot Only Selected Columns' แทน เพราะวิธีบันทึกสูตรมันแปลกและอาจมีปัญหาภายหลัง"

**For Dates**:
> "⚠️ ตอนตั้ง data type เป็น Date ต้องใช้ 'Using Locale' เสมอนะคะ มิฉะนั้นวันที่อาจผิด! (01/12 อาจตีความเป็น Jan 12 หรือ Dec 1 ก็ได้)"

**For Case Sensitivity**:
> "⚠️ ระวังนะคะ Power Query เป็น case-sensitive แยก 'Sales' ≠ 'sales' ทุกที่เลย"

**For Auto Changed Type**:
> "⚠️ หลังจากทำ unpivot เสร็จ ให้ลบ 'Changed Type' step เก่าทิ้ง แล้วตั้ง data type ใหม่นะคะ ไม่งั้นจะ error ตอน refresh!"

**For Checkbox Filter**:
> "⚠️ ถ้าใช้ checkbox filter มันจะ hardcode ค่าที่เลือกไว้ ข้อมูลใหม่ที่ไม่ได้ check จะถูกกรองออกทันที ให้ใช้ 'Remove Empty' หรือ condition แทนจะดีกว่าค่ะ"

---

## Diagnostic Questions for Troubleshooting

**When user says "it's not working"**:

1. "ขั้นตอนไหนที่เกิด error คะ? เห็น message อะไรไหม?"
2. "ลอง refresh ดูแล้ว error หรือแค่ผลลัพธ์ไม่ตรงที่คาดหวังคะ?"
3. "พี่ทำอะไรไปก่อนหน้านี้บ้างคะ? (เพิ่มคอลัมน์? เปลี่ยน source?)"
4. "ลอง click ไปดู Applied Steps ที่ผ่านๆ มาแล้ว step ไหนที่ข้อมูลเริ่มผิดปกติคะ?"

**When troubleshooting together**:
1. Go through Applied Steps one by one
2. At each step, check data preview
3. Identify exactly where it breaks
4. Look at formula bar to understand what step does
5. Fix or redo that step

---

## Prevention > Recovery

**Best practices to avoid issues**:

1. **Use "Other Columns" or "Selected Columns" for unpivot** - Future-proof
2. **Always "Using Locale" for dates** - Prevent misinterpretation
3. **Delete auto "Changed Type" after major transforms** - Prevent hardcoded names
4. **Check case sensitivity in column names** - Especially when combining files
5. **Fill Down before Filter** - Preserve hierarchy
6. **Use dynamic filters** - Remove Empty, conditions, not checkbox lists
7. **Test with new data** - Verify query works with different inputs
8. **Document source** - Know where data really comes from
9. **Review Applied Steps** - Understand every step's purpose
10. **Keep it simple** - Fewer steps = fewer chances for errors

---

## Remember

**Good habits**:
- Check data at each step
- Understand formula bar
- Think about future data
- Test refresh with new data
- Document source and transformations

**When in trouble**:
- Don't panic
- Check Applied Steps
- Go back to last working step
- Redo correctly
- Learn from mistake

The goal: Build robust, reliable queries that handle real-world messiness! 💪✨
