# Transformation Patterns

## Table of Contents

1. [Overview](#overview)
2. [Pattern 1: Wide Format → Long Format (Unpivot)](#pattern-1-wide-format--long-format-unpivot)
3. [Pattern 2: Multi-Row Headers → Single Row Headers](#pattern-2-multi-row-headers--single-row-headers)
4. [Pattern 3: Blank Cells → Filled Data](#pattern-3-blank-cells--filled-data)
5. [Pattern 4: Group Headers → Individual Rows](#pattern-4-group-headers--individual-rows)
6. [Pattern 5: Pivot Column](#pattern-5-pivot-column)
7. [Pattern 6: Date Locale Fixes](#pattern-6-date-locale-fixes)
8. [Pattern 7: Remove Auto-Generated Steps](#pattern-7-remove-auto-generated-steps)
9. [Pattern 8: Combine Files](#pattern-8-combine-files-multiple-files-with-same-structure)
10. [UI Quick Reference](#ui-quick-reference)

---

## Overview

This guide provides step-by-step UI instructions for transforming common data problems in Power Query. Each pattern includes:
- When to use it
- Detailed UI steps
- Why each step matters (concept + action)
- Common variations
- Warnings and gotchas

## Pattern 1: Wide Format → Long Format (Unpivot)

### When to Use

Data has metrics spread across columns (months, products, regions) and you need them in rows instead.

**Example**: Jan, Feb, Mar as columns → Month as a single column with values in another column

### Decision: Which Unpivot Method?

Power Query has 3 unpivot options:

**1. Unpivot Columns** ❌ **NEVER USE THIS**
- Records formula strangely
- Causes issues later
- Not recommended by experts

**2. Unpivot Other Columns** ✅ **USE WHEN**: You know which columns should stay fixed
- Select columns that won't change (Product, Category, ID)
- These stay as-is, everything else gets unpivoted
- Future-proof if new columns added (they'll auto-unpivot)
- **Best for**: Known ID/dimension columns that stay stable

**3. Unpivot Only Selected Columns** ✅ **USE WHEN**: You know which columns to unpivot
- Select columns that should be unpivoted (Jan, Feb, Mar)
- ID columns stay as-is
- Future-proof if those specific columns won't change
- **Best for**: Known measure columns that are stable

**Best Practice**: Use "Unpivot Other Columns" OR "Unpivot Only Selected Columns" - choose based on what you expect to change in future data.

### Step-by-Step: Unpivot Other Columns

**Example data**:
```
| Product | Region | Jan | Feb | Mar |
|---------|--------|-----|-----|-----|
| Phone   | North  | 100 | 150 | 200 |
```

**Steps**:

1. **Select ID columns** (columns that should NOT be unpivoted)
   - Click on "Product" column header
   - Hold Ctrl and click "Region" column header
   - These will stay as separate columns

2. **Access unpivot**
   - Click **Transform** tab in ribbon
   - In "Any Column" group, click **Unpivot Columns** dropdown arrow

3. **Choose "Unpivot Other Columns"**
   - Click **Unpivot Other Columns**
   - Jan, Feb, Mar will be transformed into two columns:
     - "Attribute" (contains: Jan, Feb, Mar)
     - "Value" (contains: 100, 150, 200)

4. **Rename columns**
   - Double-click "Attribute" header → rename to "Month"
   - Double-click "Value" header → rename to "Sales"

5. **Verify result**
   ```
   | Product | Region | Month | Sales |
   |---------|--------|-------|-------|
   | Phone   | North  | Jan   | 100   |
   | Phone   | North  | Feb   | 150   |
   | Phone   | North  | Mar   | 200   |
   ```

**Why this works**:
- **Concept**: Unpivot converts columns to rows, creating long format
- **Future-proof**: If April is added, it'll automatically unpivot
- **Analysis-ready**: Can now filter by Month, calculate trends, use in Pivot Table easily

**Common variation**: If months might get added (Apr, May) → "Unpivot Other Columns" handles it automatically

---

## Pattern 2: Multi-Row Headers → Single Row Headers

### When to Use

Headers span multiple rows (e.g., Category + Subcategory, Quarter + Metric).

**Example structures**:
```
| Customer    |       | Seller    |       |       |
| ID   | Name | ID    | Name | Age  |
```

```
| Q1         | Q1    | Q2         | Q2    |
| Sales | Units | Sales | Units |
```

### Decision Framework

**First, identify your data structure:**

1. **Transaction data?** (Each row = 1 transaction, already long format)
   - **Goal**: Fix column names only, NO unpivot needed
   - **Use**: Method 1 (Separate Header + Append)

2. **Wide format data?** (Metrics spread across columns)
   - **Goal**: Fix headers AND unpivot to long format
   - **Use**: Method 1 (reliable) or Method 2 (auto but complex)

3. **Mixed hierarchy?** (Some columns 1 level, some 2 levels)
   - **Use**: Method 1 (Separate Header + Append)

### Two Methods Available

**Method 1: Separate Header + Append** ✅ **Recommended**
- Manually create correct 1-row headers, then append with body
- **Best for**: Mixed hierarchy, transaction data, reliability
- **Pros**: Simple, always works, easy to troubleshoot
- **Cons**: Must maintain header definition

**Method 2: Transpose Method** 🟡 **Advanced**
- Use Transpose + Fill Down + Transpose back to auto-generate headers
- **Best for**: Uniform hierarchy, automated solution
- **Pros**: Automated, headers update from source
- **Cons**: Complex, many steps, doesn't work with mixed hierarchy

### Complete Guide

**📖 For detailed step-by-step instructions, decision trees, and examples:**

**→ See `references/multi-row-headers.md`**

That file contains:
- Complete step-by-step for both methods
- When to use which method
- Quick decision tree
- Method comparison table
- Troubleshooting tips
- Examples for transaction vs wide format data

---

## Pattern 3: Blank Cells → Filled Data

### When to Use

Cells are intentionally left blank for visual grouping (similar to merged cells functionality), and only first row of each group has data.

**Example**:
```
| Product | Sales |
|---------|-------|
| Phone   | 100   |
|         | 150   | <- Product is blank (left empty for visual grouping)
|         | 120   |
| Laptop  | 200   |
```

**Steps**:

1. **Select the column with blank cells**
   - Click the column header (e.g., "Product")

2. **Fill Down**
   - Right-click the column → **Fill** → **Down**
   - All blank cells get filled with value from above
   - Result:
     ```
     | Product | Sales |
     |---------|-------|
     | Phone   | 100   |
     | Phone   | 150   |
     | Phone   | 120   |
     | Laptop  | 200   |
     ```

**Why this works**:
- **Concept**: Fill Down copies value from above into empty cells
- **Critical**: Do this BEFORE any filtering or removing rows
- **Use case**: Blank cells are common in Excel reports where categories are shown once for visual grouping

**What to tell user**:
"คอลัมน์นี้มีการเว้นว่างเอาไว้ให้ข้อมูลดูง่าย (คล้ายๆ กับการ merged cell) ทำให้แถวที่ 2, 3 ไม่มีข้อมูล เราจะใช้ Fill Down เพื่อเติมข้อมูลให้ทุกแถวนะคะ"

**Warning**: If you filter or remove rows before Fill Down, you lose the category information forever!

---

## Pattern 4: Grouped Data → Explicit Hierarchy

### When to Use

Group headers are inserted as separate rows between data (Factory A, Factory B, etc.).

**Example**:
```
| Factory/WH | TXID   | Sales |
|------------|--------|-------|
| A          |        |       | <- Group header
| WH-001     | TX0001 | 100   |
| WH-002     | TX0002 | 150   |
| B          |        |       | <- Group header
| WH-003     | TX0003 | 200   |
```

**Critical Rule**: **Fill Down → THEN → Filter** (never the other way!)

**Steps**:

1. **Fill Down the hierarchy column**
   - Select "Factory/WH" column
   - Right-click → **Fill** → **Down**
   - Now every row has Factory code:
     ```
     | Factory/WH | TXID   | Sales |
     |------------|--------|-------|
     | A          |        |       |
     | A          | TX0001 | 100   | <- Got "A" filled
     | A          | TX0002 | 150   |
     | B          |        |       |
     | B          | TX0003 | 200   | <- Got "B" filled
     ```

2. **Separate hierarchy levels** (if needed)
   - If Factory and Warehouse are in same column, use data-driven logic:
   
   **💡 Best Method: Data-Driven Logic**
   
   **Observe what distinguishes header rows from data rows**:
   - Factory header rows (A, B, C) → **No TXID** (null/empty)
   - Warehouse data rows (WH-001, WH-002) → **Have TXID** (TX0001, TX0002)
   
   **This is the key insight!** Use data characteristics, not naming patterns.
   
   - Click **Add Column** tab → **Conditional Column**
   - Name: "Factory"
   - If `[TXID] = null` then `[Factory/WH]` else `null`
   - This extracts Factory row values when there's no TXID
   - Fill Down the new "Factory" column
   - The original column becomes "Warehouse"
   
   **Why this is best**:
   - ✅ Works with ANY factory name (A, AA, North, Site-01, anything!)
   - ✅ Data-driven, not pattern-based
   - ✅ Future-proof for new factories
   - ✅ Clear logic: "No TXID = factory header"
   
   **Less flexible alternatives**:
   - ❌ `Text.Length([Factory/WH]) = 1` - Only works for single-character names
   - ❌ `= "A" or "B" or "C"` - Hardcoded, must update for new values

3. **⚠️ Filter out empty rows (DO NOT SKIP THIS STEP!)**
   - Click "TXID" column
   - Click filter dropdown (funnel icon)
   - Click **Remove Empty**
   - This removes group header rows (A, B, C lines)
   - **Critical**: Without this step, you have duplicate/redundant rows!

4. **Clean up**
   - Remove or rename columns as needed
   - Set correct data types (Decimal Number for amounts!)

**Result**:
```
| Factory | Warehouse | TXID   | Sales |
|---------|-----------|--------|-------|
| A       | WH-001    | TX0001 | 100   |
| A       | WH-002    | TX0002 | 150   |
| B       | WH-003    | TX0003 | 200   |
```

**Why this works**:
- **Fill Down**: Makes implicit hierarchy (visual grouping) explicit (data in every row)
- **Data-driven logic**: Checks actual data characteristics (has TXID?) not patterns (text length)
- **Filter after Fill Down**: Removes now-useless group header rows
- **Flexible**: Works with any naming convention

**⚠️ Critical Warnings**: 
1. If you filter BEFORE Fill Down, the Factory information is lost forever! Always Fill Down first.
2. If you skip the Filter step, you'll have duplicate rows (the A, B, C header rows remain)

---

## Pattern 5: Stacked Metrics → Separate Columns (Pivot)

### When to Use

Multiple metrics (Sales, Units, etc.) are stacked in rows instead of being in separate columns.

**Example**:
```
| Product | Payment | Attribute | Value |
|---------|---------|-----------|-------|
| Phone   | Cash    | Sales     | 1000  |
| Phone   | Cash    | Units     | 50    |
| Phone   | Card    | Sales     | 1200  |
| Phone   | Card    | Units     | 60    |
```

**Goal**: Separate Sales and Units into their own columns

**Steps**:

1. **Select the Attribute column**
   - Click "Attribute" column header
   - This contains the metric names (Sales, Units)

2. **Pivot Column**
   - Click **Transform** tab → **Pivot Column**
   - Dialog appears

3. **Configure pivot**
   - **Values Column**: Select "Value" (contains the numbers)
   - **Advanced Options**: Click to expand
   - **Aggregate Value Function**: Select **Don't Aggregate**
   - Click OK

4. **Result**:
   ```
   | Product | Payment | Sales | Units |
   |---------|---------|-------|-------|
   | Phone   | Cash    | 1000  | 50    |
   | Phone   | Card    | 1200  | 60    |
   ```

**Why this works**:
- **Concept**: Pivot converts unique values in one column into separate columns
- **Don't Aggregate**: Critical! We want values as-is, not summed/averaged
- **Use case**: When metrics are stacked vertically but should be horizontal

**Common variation**: After unpivoting wide data, you might need to split and pivot again to get correct structure

---

## Pattern 6: Date Locale Fixes

### When to Use

Dates are ambiguous (01/12 could be Jan 12 or Dec 1) or stored as text.

**Example**:
```
| Date       | Sales |
|------------|-------|
| 01/12/2024 | 100   | <- Jan 12 (US) or Dec 1 (UK/TH)?
```

**Steps**:

1. **Select the Date column**
   - Click "Date" column header

2. **Change Type with Locale**
   - Click **Transform** tab
   - Click data type dropdown → **Date**
   - **DO NOT** just click "Date" directly!

3. **Specify Using Locale**
   - After selecting Date type, dialog appears
   - OR: Click **Transform** → **Data Type** → **Using Locale**
   - Choose correct locale:
     - "English (United States)" for MM/DD/YYYY
     - "English (United Kingdom)" for DD/MM/YYYY  
     - "Thai" for DD/MM/YYYY (Thailand standard)

4. **Verify**
   - Check a few dates to ensure correct interpretation
   - 01/12/2024 should become expected date

**Why this works**:
- **Concept**: Locale tells Power Query how to interpret ambiguous dates
- **Critical**: Without locale, Power Query guesses (often wrong!)
- **Use case**: Any date data, especially from international sources

**⚠️ Warning**: If you have MIXED locales in same column (some US, some UK), you'll need custom M code to detect and parse correctly - this is advanced!

**Best practice**: Always use "Using Locale" when setting date types, even if it seems clear.

---

## Pattern 7: Remove Auto-Generated Steps

### When to Use

Power Query auto-generates "Changed Type" steps that hardcode column names, which break when source changes.

**Problem**:
- You rename/add columns
- Old "Changed Type" step still references old column names
- Query breaks on refresh

**Steps**:

1. **Find the step**
   - Look at **Applied Steps** panel (right side)
   - Find "Changed Type" steps (usually multiple)
   - Look at formula bar to see if it has hardcoded column names

2. **Delete problematic steps**
   - Right-click the "Changed Type" step
   - Click **Delete**
   - If dialog appears about dependencies, review carefully

3. **Re-apply types correctly**
   - Select columns that need type changes
   - Set correct data type
   - For dates: Use "Using Locale"
   - This creates new "Changed Type" step with current structure

**Why this works**:
- **Problem**: Auto-steps lock in column names at that point in time
- **Solution**: Remove old locks, create new ones after transformations
- **Best practice**: Always check Applied Steps after major transformations

**Gotcha**: Sometimes you need these steps! Don't delete if they're still correct.

---

## Pattern 8: Combine Files (Multiple Files with Same Structure)

### When to Use

Multiple files (Excel, CSV) in a folder need to be combined into one table.

### Method A: From Folder (Local)

**Steps**:

1. **Get Data from Folder**
   - **Home** tab → **Get Data** → **From Folder**
   - Browse to folder containing files
   - Click OK

2. **Combine Files**
   - In preview, click **Combine** button (bottom right)
   - Or click **Transform Data** then **Combine Files** in toolbar
   - Power Query creates:
     - "Transform Sample File" query (template for transformations)
     - Main query that applies template to all files

3. **Transform the sample**
   - Click "Transform Sample File" query
   - Make any needed transformations (unpivot, remove rows, etc.)
   - These will apply to ALL files automatically

4. **Go back to main query**
   - Click main combined query
   - All files now processed with your transformations

**Why this works**:
- **Transform Sample File**: Template that's applied to every file
- **Automatic**: New files added to folder get auto-included on refresh
- **Consistent**: Ensures same transformations on all files

---

### Method B: From SharePoint Folder (Online)

**Steps**:

1. **Get Data from SharePoint Folder**
   - **Home** tab → **Get Data** → **From SharePoint Folder**
   - Enter SharePoint site URL
   - Click OK

2. **CRITICAL: Change M Code**
   - Click **Advanced Editor**
   - Find: `SharePoint.Files`
   - Change to: `SharePoint.Contents`
   - Click Done
   - *This is required for SharePoint folders to work properly*
   - Reference: https://www.thepexcel.com/power-query-get-data-online-sources/

3. **Filter to your files**
   - Filter "Folder Path" to target folder
   - Filter "Name" or "Extension" if needed

4. **Combine Files**
   - Same as Method A from here
   - Click Combine, transform sample, etc.

**Why the code change**:
- `SharePoint.Files` has limitations with folders
- `SharePoint.Contents` works more reliably
- This is a known issue/workaround

---

### Method C: Custom Function (Multiple Sheets in One File)

**When to use**: Need to combine Sheet1, Sheet2, Sheet3 from a single Excel file

**Note**: No built-in UI for this - requires creating custom function

**High-level approach**:
1. Create function that processes one sheet
2. Get list of sheet names
3. Apply function to each sheet
4. Combine results

**Details**: This requires M code. If user needs this, suggest they search for "Power Query custom function multiple sheets" or provide basic template.

---

## UI Quick Reference

### Common Locations:

**Transform Tab**:
- Unpivot Columns (and dropdown for Other/Only Selected)
- Transpose
- Fill (Right-click column → Fill → Down/Up)
- Split Column
- Extract (First/Last Characters, Text Before/After)
- Data Type (with "Using Locale" option)

**Add Column Tab**:
- Conditional Column
- Custom Column
- Duplicate Column

**Home Tab**:
- Remove Rows / Keep Rows
- Use First Row as Headers
- Combine Files

**Transform > Any Column Group**:
- Pivot Column
- Unpivot Columns (dropdown)

**Right-Click Column**:
- Fill → Down/Up
- Remove
- Duplicate Column
- Replace Values
- Split Column
- Change Type (with Using Locale)

---

## Tips for Effective Transformations

1. **Always check Applied Steps** - Understand what each step does
2. **Remove auto "Changed Type" after major changes** - Prevents breaking on refresh
3. **Fill Down before filtering** - Or you lose hierarchy information
4. **Use "Using Locale" for all dates** - Prevents misinterpretation
5. **Choose right unpivot method** - Think about future data changes
6. **Don't Aggregate when pivoting** - Usually want values as-is
7. **Test with new data** - Add a new month/product and refresh to verify future-proofing

## Remember

Good transformations are:
- **Future-proof** (handle new columns/rows automatically)
- **Clear** (each step has obvious purpose)
- **Robust** (don't hardcode values that might change)
- **Efficient** (minimum steps to achieve goal)

The goal: Transform data reliably so users can refresh anytime! 🔄✨
