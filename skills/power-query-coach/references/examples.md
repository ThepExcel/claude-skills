# Power Query Examples - Before & After

## Table of Contents

1. [Overview](#overview)
2. [Example 1: Wide Format (Employee Sales)](#example-1-wide-format-employee-sales)
3. [Example 2: Stacked Metrics (Product + Payment Method)](#example-2-stacked-metrics-product--payment-method)
4. [Example 3: Grouped Data (Factory/Warehouse Hierarchy)](#example-3-grouped-data-factorywarehouse-hierarchy)
5. [Example 4: Multi-Row Headers](#example-4-multi-row-headers)
6. [Example 5: Date Locale Issues](#example-5-date-locale-issues)
7. [Pattern Summary](#pattern-summary)
8. [Remember](#remember)

---

## Overview

This file contains real-world examples of data transformation problems and their solutions. Each example shows:
- Before: Original problematic data
- Problems identified
- After: Proper structure
- Step-by-step solution
- Key lessons

Use these as reference when coaching users with similar problems.

---

## Example 1: Wide Format (Employee Sales)

### Before
```
| Product  | Jan | Feb | Mar | Apr |
|----------|-----|-----|-----|-----|
| Phone    | 100 | 150 | 200 | 120 |
|          | 80  | 90  | 110 | 95  |
| Laptop   | 200 | 220 | 250 | 230 |
|          | 180 | 190 | 210 | 200 |
```

### Problems Identified

1. **Wide format** 🔴
   - Months (Jan, Feb, Mar, Apr) are spread across columns
   - Should be: One "Month" column, one "Sales" column
   - Impact: Pivot Table will see 4 separate fields, can't filter by month easily

2. **Blank cells** 🟡
   - Product column has cells intentionally left blank for visual grouping
   - Only first row of each group has product name
   - Impact: Rows 2, 4 have blank product → data loss

### After (Proper Structure)
```
| Product | Month | Sales |
|---------|-------|-------|
| Phone   | Jan   | 100   |
| Phone   | Jan   | 80    |
| Phone   | Feb   | 150   |
| Phone   | Feb   | 90    |
| Phone   | Mar   | 200   |
| Phone   | Mar   | 110   |
| Phone   | Apr   | 120   |
| Phone   | Apr   | 95    |
| Laptop  | Jan   | 200   |
| Laptop  | Jan   | 180   |
... (and so on)
```

### Step-by-Step Solution

**Step 1: Fill Down (Fix merged cells)**
```
Action: Right-click "Product" column → Fill → Down
Result: All blank product cells now filled with value from above
```

**Step 2: Unpivot Other Columns (Convert wide → long)**
```
Action: 
1. Select "Product" column (the ID column to keep)
2. Transform tab → Unpivot Other Columns
Result: Jan, Feb, Mar, Apr converted to:
   - "Attribute" column (contains month names)
   - "Value" column (contains sales numbers)
```

**Step 3: Rename columns**
```
Action: 
- Double-click "Attribute" → rename to "Month"
- Double-click "Value" → rename to "Sales"
```

**Step 4: Set data types**
```
Action:
- Product: Text (already correct)
- Month: Text (already correct)
- Sales: Whole Number
```

### Why This Works

**Concept**: 
- Merged cells → Fill Down makes data explicit
- Wide format → Unpivot creates long format
- One column per concept (Product, Month, Sales)

**Future-proof**:
- If May is added → Automatically unpivoted (we used "Unpivot Other Columns")
- If new product added → Works automatically

**Analysis-ready**:
- Can filter by any month
- Can calculate by product
- Pivot Table has clear 3 fields
- Can create time series charts

### Key Lessons

1. **Always Fill Down before Unpivot** - Order matters!
2. **Use "Unpivot Other Columns"** - Future-proof for new months
3. **Wide → Long is the goal** - Not just single-row headers

---

## Example 2: Stacked Metrics (Product + Payment Method)

### Before
```
| Product | Payment | Attribute | Value |
|---------|---------|-----------|-------|
| Phone   | Cash    | Sales     | 1000  |
| Phone   | Cash    | Units     | 50    |
| Phone   | Card    | Sales     | 1200  |
| Phone   | Card    | Units     | 60    |
| Laptop  | Cash    | Sales     | 2000  |
| Laptop  | Cash    | Units     | 40    |
```

### Problems Identified

1. **Stacked metrics** 🟡
   - Sales and Units are in same column (Attribute)
   - Values are in single "Value" column
   - Should be: Separate Sales and Units columns
   - Impact: Hard to calculate (Sales / Units), inefficient in Pivot

### After (Proper Structure)
```
| Product | Payment | Sales | Units |
|---------|---------|-------|-------|
| Phone   | Cash    | 1000  | 50    |
| Phone   | Card    | 1200  | 60    |
| Laptop  | Cash    | 2000  | 40    |
```

### Step-by-Step Solution

**Step 1: Pivot Column (Separate metrics)**
```
Action:
1. Select "Attribute" column
2. Transform tab → Pivot Column
3. In dialog:
   - Values Column: "Value"
   - Advanced Options: Choose "Don't Aggregate"
4. Click OK
Result: "Attribute" values (Sales, Units) become column headers
```

**Step 2: Verify and set types**
```
Action:
- Product: Text
- Payment: Text
- Sales: Whole Number
- Units: Whole Number
```

### Why This Works

**Concept**:
- Pivot converts row values to column headers
- "Don't Aggregate" keeps values as-is
- Each metric (Sales, Units) gets own column

**Analysis-ready**:
- Can calculate Sales / Units easily
- Pivot Table has clear 4 fields
- Can sum/average each metric independently

### Key Lessons

1. **Pivot for stacked metrics** - When multiple measures in one column
2. **Don't Aggregate** - Critical! We want values as-is, not summed
3. **Separate topics** - Sales ≠ Units, deserve separate columns

---

## Example 3: Grouped Data (Factory/Warehouse Hierarchy)

### Before
```
| Factory/WH | TXID   | Buyer   | Product | Price | Qty |
|------------|--------|---------|---------|-------|-----|
| A          |        |         |         |       |     |
| WH-001     | TX0001 | sales ก | อาหาร   | 90    | 6   |
| WH-004     | TX0002 | sales ก | หนังสือ | 190   | 1   |
| WH-002     | TX0003 | sales ข | dvd หนัง | 399  | 3   |
| WH-003     | TX0004 | sales ก | อาหาร   | 90    | 4   |
| B          |        |         |         |       |     |
| WH-006     | TX0005 | sales ง | ของเล่น | 250   | 1   |
| WH-007     | TX0006 | sales ข | อาหาร   | 40    | 3   |
| WH-006     | TX0007 | sales ข | หนังสือ | 250   | 3   |
| C          |        |         |         |       |     |
| WH-008     | TX0008 | sales ง | ของเล่น | 250   | 2   |
| WH-010     | TX0009 | sales ง | ของเล่น | 250   | 1   |
| WH-009     | TX0010 | sales ข | ของเล่น | 190   | 1   |
```

### Problems Identified

1. **Grouped data (hidden hierarchy)** 🔴
   - Group headers (A, B, C) inserted as separate rows
   - Data rows (WH-001, WH-004, etc.) don't have factory information
   - Empty cells in all data columns for group header rows
   - Impact: Can't analyze by factory, hierarchy is implicit

2. **Mixed hierarchy levels** 🟡
   - Factory and Warehouse in same column
   - Need to separate for proper analysis

### After (Proper Structure)
```
| Factory | Warehouse | TXID   | Buyer   | Product | Price | Qty |
|---------|-----------|--------|---------|---------|-------|-----|
| A       | WH-001    | TX0001 | sales ก | อาหาร   | 90    | 6   |
| A       | WH-004    | TX0002 | sales ก | หนังสือ | 190   | 1   |
| A       | WH-002    | TX0003 | sales ข | dvd หนัง | 399  | 3   |
| A       | WH-003    | TX0004 | sales ก | อาหาร   | 90    | 4   |
| B       | WH-006    | TX0005 | sales ง | ของเล่น | 250   | 1   |
| B       | WH-007    | TX0006 | sales ข | อาหาร   | 40    | 3   |
| B       | WH-006    | TX0007 | sales ข | หนังสือ | 250   | 3   |
| C       | WH-008    | TX0008 | sales ง | ของเล่น | 250   | 2   |
| C       | WH-010    | TX0009 | sales ง | ของเล่น | 250   | 1   |
| C       | WH-009    | TX0010 | sales ข | ของเล่น | 190   | 1   |
```

### Step-by-Step Solution

**⚠️ CRITICAL ORDER: Fill Down → Create Factory Column → Fill Down Factory → Filter**

**Step 1: Fill Down (Make hierarchy explicit)**
```
Action: Right-click "Factory/WH" column → Fill → Down
Result: A fills down to WH-001, WH-004, WH-002, WH-003
        B fills down to WH-006, WH-007, WH-006
        C fills down to WH-008, WH-010, WH-009
        
Now every row has factory/warehouse information!
```

**Step 2: Separate hierarchy levels (Factory vs Warehouse)**

**💡 Best Method: Data-Driven Logic**

**Observation**:
- Factory header rows (A, B, C) → **No TXID** (null/empty)
- Warehouse data rows (WH-001, WH-004, etc.) → **Have TXID** (TX0001, TX0002, ...)

**This is the key!** Use data characteristics, not naming patterns.

```
Action:
1. Add Column tab → Conditional Column
2. Name: "Factory"
3. Condition: If [TXID] = null then [#"Factory/WH"] else null
   Note: Use [#"Factory/WH"] because column name has "/" special character!
4. This creates new "Factory" column with A, B, C where TXID is null, null elsewhere
```

**Why this is best**:
- ✅ Works with ANY factory name (A, AA, North, Site-01, anything!)
- ✅ Data-driven: checks if row has transaction data
- ✅ Future-proof: new factories automatically handled
- ✅ Clear logic: "No TXID = factory header"

**Less flexible alternatives**:
- `Text.Length([#"Factory/WH"]) = 1` - Only single characters
- `[#"Factory/WH"] = "A" or ... = "B" or ... = "C"` - Hardcoded

**Step 3: Fill Down the Factory column**
```
Action: Right-click "Factory" column → Fill → Down
Result: Now every row has factory information in the Factory column
```

**Step 4: ⚠️ Filter out header rows (DO NOT SKIP!)**
```
Action: 
1. Click "TXID" column
2. Click filter dropdown
3. Click "Remove Empty"
Result: Rows with only A, B, C (no TXID) are removed
        Only transaction rows remain

Critical: Without this step, you have duplicate/redundant header rows!
```

**Step 5: Rename and set types**
```
Action:
- Rename "Factory/WH" column to "Warehouse"
- Reorder columns: Factory, Warehouse, TXID, Buyer, Product, Price, Qty
- Set types:
  - Factory: Text
  - Warehouse: Text
  - TXID: Text
  - Buyer: Text
  - Product: Text
  - Price: Decimal Number (future-proof!)
  - Qty: Whole Number
```

### Why This Works

**Concept**:
- Fill Down converts implicit hierarchy (visual grouping) to explicit data
- Data-driven logic identifies which rows are headers vs data
- Filter removes now-useless header rows
- Result: clean hierarchy in every row

**Key principle**: Look at data characteristics (has TXID?) not naming patterns (text length)

**Future-proof**:
- New factories with any name → Works automatically
- New warehouses → Works automatically

**Analysis-ready**:
- Can analyze by Factory, Warehouse, or both
- Proper hierarchy for drill-down
- Every row has complete information
- Proper hierarchy for drill-down
- Every row has complete information

### Key Lessons

1. **⚠️ Fill Down BEFORE Filter** - Critical order! Filter first = lose hierarchy forever
2. **⚠️ Don't Forget to Filter** - After Fill Down, must remove header rows or you have duplicates
3. **Use Data-Driven Logic** - Check `if [TXID] = null` (data characteristics) not text length (patterns)
4. **M Code Special Characters** - Use `[#"Factory/WH"]` for column names with `/` or special characters
5. **Decimal for Amounts** - Use Decimal Number for Price (future-proof)

---

## Example 4: Multi-Row Headers

### Before
```
| Q1    | Q1    | Q2    | Q2    | Q3    | Q3    |
| Sales | Units | Sales | Units | Sales | Units |
|-------|-------|-------|-------|-------|-------|
| 1000  | 50    | 1200  | 60    | 1100  | 55    |
| 900   | 45    | 1150  | 58    | 1000  | 50    |
```

### Problems Identified

1. **Multi-row headers** 🟡
   - Headers span 2 rows (Quarter + Metric)
   - Power Query sees first row as data
   - Should be: Quarter, Sales, Units as separate columns

2. **Wide format** 🔴
   - Quarters spread across columns
   - Should be: One Quarter column

### After (Proper Structure)
```
| Quarter | Sales | Units |
|---------|-------|-------|
| Q1      | 1000  | 50    |
| Q1      | 900   | 45    |
| Q2      | 1200  | 60    |
| Q2      | 1150  | 58    |
| Q3      | 1100  | 55    |
| Q3      | 1000  | 50    |
```

### Step-by-Step Solution

#### Method 1: Transpose Method (For Simple Cases)

**Step 1: Keep only header rows**
```
Action: Home tab → Keep Rows → Keep Top Rows → Enter 2
Result: Only the 2 header rows remain
```

**Step 2: Transpose**
```
Action: Transform tab → Transpose
Result:
| Column1 | Column2 |
|---------|---------|
| Q1      | Sales   |
| Q1      | Units   |
| Q2      | Sales   |
| Q2      | Units   |
| Q3      | Sales   |
| Q3      | Units   |
```

**Step 3: Fill Down**
```
Action: Select Column1 → Right-click → Fill → Down
Result: All Q1 entries filled down, Q2 filled down, Q3 filled down
```

**Step 4: Merge columns**
```
Action: 
1. Select Column1, hold Ctrl, select Column2
2. Right-click → Merge Columns
3. Separator: Space
Result: "Q1 Sales", "Q1 Units", "Q2 Sales", "Q2 Units", "Q3 Sales", "Q3 Units"
```

**Step 5: Transpose back**
```
Action: Transform tab → Transpose
Result: Merged headers now in first row
```

**Step 6: Promote headers**
```
Action: Home tab → Use First Row as Headers
```

**Step 7: Delete old "Changed Type"**
```
Action: 
1. Find old "Changed Type" step in Applied Steps
2. Right-click → Delete
Reason: It has old column names, will break on refresh
```

**Step 8: Connect back to full data and unpivot**

Now you have: `Q1 Sales | Q1 Units | Q2 Sales | Q2 Units | Q3 Sales | Q3 Units`

But we need: `Quarter | Sales | Units`

**Step 9: Unpivot Other Columns** (assuming there's an ID column, if not, add index first)
```
Action: Select ID columns → Transform → Unpivot Other Columns
Result: Attribute (Q1 Sales, Q1 Units, ...) and Value columns
```

**Step 10: Split by delimiter**
```
Action: 
1. Select Attribute column
2. Transform → Split Column → By Delimiter → Space
Result: Two columns: Quarter (Q1, Q2, Q3) and Metric (Sales, Units)
```

**Step 11: Pivot the Metric**
```
Action:
1. Select Metric column
2. Transform → Pivot Column
3. Values Column: Value
4. Don't Aggregate
Result: Sales and Units as separate columns!
```

**Step 12: Final cleanup**
```
Action: Reorder columns, verify types
```

#### Method 2: Separate Header + Append (Reliable but Manual)

**When to use**: Transpose method is too complex or unreliable

**Approach**:
1. Manually define correct headers in separate query
2. Remove header rows from main data
3. Append correct headers to data

**Trade-off**: More manual, but always works

### Why This Works

**Concept**:
- Transpose converts columns↔rows, allowing manipulation of header structure
- Fill Down ensures every row has category information
- Merge combines multiple header rows
- Unpivot + Split + Pivot converts to proper long format

**Critical**:
- Must delete old "Changed Type" that has old column structure
- The goal isn't just single-row headers - it's **proper long format**

### Key Lessons

1. **Multi-row headers are complex** - Multiple steps needed
2. **Goal is structure, not just single row** - Must be Quarter | Sales | Units
3. **Delete old Changed Type** - Or query breaks on refresh
4. **Test with real data** - Transpose method can be tricky

---

## Example 5: Date Locale Issues

### Before
```
| Date       | Sales |
|------------|-------|
| 01/12/2024 | 100   |
| 02/01/2025 | 150   |
| 15/03/2024 | 200   |
```

### Problems Identified

1. **Ambiguous dates** 🔴
   - 01/12/2024 could be Jan 12 or Dec 1
   - US format (MM/DD/YYYY) vs UK/TH format (DD/MM/YYYY)
   - Stored as text, not Date type

### After (Proper Structure - Assuming Thai/UK Format)
```
| Date       | Sales |
|------------|-------|
| 2024-12-01 | 100   | <- December 1, 2024
| 2025-01-02 | 150   | <- January 2, 2025
| 2024-03-15 | 200   | <- March 15, 2024
```

### Step-by-Step Solution

**Step 1: Change type with locale**
```
Action:
1. Select Date column
2. Transform tab → Data Type dropdown → Date → Using Locale
3. Dialog appears: Choose "English (United Kingdom)" or "Thai"
4. Click OK
```

**Step 2: Verify**
```
Action: Spot check dates to ensure correct interpretation
Example: 01/12/2024 should become December 1 (not January 12)
```

### Why This Works

**Concept**:
- Locale tells Power Query HOW to interpret ambiguous dates
- Without locale, Power Query guesses (often wrong!)
- "Using Locale" explicitly specifies interpretation

**Critical**:
- **ALWAYS** use "Using Locale" when setting date types
- Never just click "Date" without specifying

### Key Lessons

1. **Always specify locale** - Even if it seems obvious
2. **Verify interpretation** - Check a few dates manually
3. **Standardize at source if possible** - Use ISO format (YYYY-MM-DD) to avoid ambiguity

---

## Pattern Summary

| Problem Type       | Key Transform       | Critical Warning                  |
|--------------------|---------------------|-----------------------------------|
| Wide Format        | Unpivot Other/Selected | Use Other/Selected, not "Unpivot Columns" |
| Merged Cells       | Fill Down           | Fill Down before other operations |
| Grouped Data       | Fill Down → Filter  | **ALWAYS** Fill Down before Filter! |
| Stacked Metrics    | Pivot Column        | Use "Don't Aggregate"             |
| Multi-row Headers  | Transpose + Fill + Merge | Delete old "Changed Type"         |
| Date Ambiguity     | Using Locale        | **ALWAYS** specify locale         |

---

## Remember

**Every example follows the same principles**:
1. **Structure first** - Fix headers and format before content
2. **One column = one concept** - Separate topics clearly
3. **Long format** - Not wide (unpivot when needed)
4. **Explicit data** - Every row complete (Fill Down)
5. **Future-proof** - Use "Other Columns", dynamic filters
6. **Verify types** - Especially dates with locale

The goal: Transform messy data into clean, analysis-ready format! 🎯✨
