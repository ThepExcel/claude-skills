# Multi-Row Headers → Single Row Headers

## Table of Contents

1. [When to Use](#when-to-use)
2. [Important Decision Framework](#important-decision-framework)
3. [Method 1: Separate Header + Append (Recommended)](#method-1-separate-header--append-recommended)
4. [Method 2: Transpose Method (Auto but Complex)](#method-2-transpose-method-auto-but-complex)
5. [Method Comparison](#method-comparison)
6. [Quick Decision Tree](#quick-decision-tree)

---

## When to Use

Headers span multiple rows (e.g., Category + Subcategory, Quarter + Metric).

**Examples**:
```
| Customer          |          | Seller         |          |          |
| ID    | Name      | ID       | Name   | Age   |
|-------|-----------|----------|--------|-------|
| C001  | John      | S01      | Alice  | 28    |
```

```
| Q1             | Q1      | Q2             | Q2      |
| Sales | Units  | Sales   | Units   |
|-------|--------|---------|---------|
| 1000  | 50     | 1200    | 60      |
```

---

## Important Decision Framework

**First, identify your data structure:**

### 1. Transaction data (Each row = 1 transaction, already long format)

**Example**: Sales transactions with Customer→ID/Name, Seller→ID/Name/Age

**Goal**: Fix column names only, **NO unpivot needed**

**Recommended**: ✅ **Method 1 (Separate Header + Append)**

**Why**: 
- Simple and reliable
- You just need correct column names
- No need for complex unpivot/pivot operations

---

### 2. Wide format data (Metrics spread across columns)

**Example**: Q1 Sales, Q1 Units, Q2 Sales, Q2 Units

**Goal**: Fix headers **AND** unpivot to long format

**Can use**: 
- ✅ **Method 1** (reliable) - Fix headers first, then unpivot separately
- 🟡 **Method 2** (auto but complex) - Combines header fix + unpivot in one flow

**Why**: 
- Method 1: More steps but clearer, works every time
- Method 2: Fewer queries but complex, many steps, easy to make mistakes

---

### 3. Mixed hierarchy (Some columns 1 level, some 2 levels)

**Example**: Date/Product/Price (1 level) + Customer→ID/Name (2 levels)

**Recommended**: ✅ **Method 1 (Separate Header + Append)**

**Why**: 
- Method 2 (Transpose) doesn't work well with mixed structures
- Method 1 gives you full control over exact column names

---

## Method 1: Separate Header + Append (Recommended)

### When to use
- ✅ Mixed hierarchy
- ✅ Transaction data (no unpivot needed)
- ✅ When you want reliability
- ✅ When you prefer clear, simple steps

### Key principle
Manually create correct 1-row headers, then append with body

### Step-by-Step Guide

#### Step 1: Create "body" query (data only)

```
1. Get Data → From Table/Range
2. ⚠️ DO NOT tick "My table has headers"
3. Delete auto "Changed Type" step (it has wrong column names)
4. Home → Remove Rows → Remove Top Rows → 2 (or however many header rows)
5. Now you have: Column1, Column2, Column3, ... with only data rows
6. Right-click query → Rename → "body"
```

**Result**: Clean data table with generic column names (Column1, Column2, etc.)

---

#### Step 2: Create "header" query (correct headers)

**In Excel**: Create new table with 1 row of correct headers

**Example for transaction data with multi-row headers**:
```
วันที่ | สินค้า | ราคาต่อชิ้น | จำนวนชิ้น | วิธีการชำระเงิน | ลูกค้า_รหัส | ลูกค้า_ชื่อ | ผู้ขาย_รหัส | ผู้ขาย_ชื่อ | ผู้ขาย_อายุ
```

**Example for wide format data that needs unpivot**:
```
Product | Payment | Q1_Sales | Q1_Units | Q2_Sales | Q2_Units
```

**In Power Query**:
```
1. Get Data → From Table/Range (from your 1-row header table)
2. ⚠️ DO NOT tick "My table has headers"
3. Delete auto "Changed Type" step
4. Now you have: Column1, Column2, Column3, ... (same structure as body!)
5. Right-click query → Rename → "header"
```

**Critical**: Header query must have exact same number of columns as body query, with same Column1, Column2, Column3 structure

---

#### Step 3: Append queries

```
1. Select "header" query
2. Home → Append Queries → Append Queries as New
3. First table: header
   Second table: body
4. OK
5. Result: Row 1 = correct headers, Row 2+ = data
6. Right-click new query → Rename → "final"
```

---

#### Step 4: Promote headers and set types

```
1. Home → Use First Row as Headers
2. Set data types:
   - Date columns: Date (Using Locale!)
   - Amount columns: Decimal Number (future-proof!)
   - Count columns: Whole Number (if truly no decimals)
   - Others: Text
3. Done! ✅
```

---

### If you have wide format data: Continue with unpivot

**For wide format** (Q1_Sales, Q1_Units, Q2_Sales, Q2_Units):

```
1. Unpivot:
   - Select "Product" and "Payment" columns
   - Transform → Unpivot Other Columns
   - You get: Attribute (Q1_Sales, Q1_Units, ...) and Value

2. Split Column:
   - Select "Attribute" column
   - Transform → Split Column → By Delimiter "_"
   - Choose "At the left-most delimiter"
   - You get: Attribute.1 (Q1, Q2) and Attribute.2 (Sales, Units)

3. Rename:
   - Attribute.1 → "Quarter"
   - Attribute.2 → "Metric"

4. Pivot Column:
   - Select "Metric" column
   - Transform → Pivot Column
   - Values Column: "Value"
   - Advanced Options → Don't Aggregate
   - Result: Product | Payment | Quarter | Sales | Units

Done! ✅
```

---

### Why Method 1 works

**Concept**: Bypass the complex header structure by creating correct headers separately

**Benefits**:
- ✅ Always works, no matter how complex the hierarchy
- ✅ Clear - you control exactly what headers should be
- ✅ Flexible - works with mixed hierarchy, transaction data, any structure
- ✅ Easy to understand - simple append operation

**Trade-off**: 
- 🟡 Must maintain 1-row header definition yourself
- 🟡 Two queries to manage (header + body)

**Best for**: Mixed hierarchy, transaction data, when you want reliability

---

## Method 2: Transpose Method (Auto but Complex)

### When to use
- ✅ Uniform hierarchy (all columns have same parent-child structure)
- ✅ You want automated solution
- ⚠️ NOT suitable for: Mixed hierarchy, transaction data

### Key principle
Use Transpose to leverage Fill Down (since Fill Right doesn't exist), then manipulate and transpose back

### Step-by-Step Guide

#### Step 1: Separate body (same as Method 1)

```
1. Get Data → From Table/Range
2. DO NOT tick "My table has headers"
3. Delete auto "Changed Type" step
4. Remove Top Rows → N (number of header rows)
5. Rename → "body"
```

---

#### Step 2: Process headers automatically

```
1. Duplicate original query → Rename "headers_raw"
2. Keep Top Rows → 2 (or number of header rows)
3. Delete auto "Changed Type" step
4. Transpose (converts columns to rows)
   - Each original column becomes a row
   - Column1 = parent category, Column2 = subcategory
```

**After Transpose example**:
```
| Column1 | Column2 |
|---------|---------|
| Q1      | Sales   |
| Q1      | Units   |
| Q2      | Sales   |
| Q2      | Units   |
```

```
5. Fill Down on Column1 (fills parent categories)
   - Select Column1
   - Transform → Fill → Down
   - This fills null cells in parent category
```

**After Fill Down**:
```
| Column1 | Column2 |
|---------|---------|
| Q1      | Sales   |
| Q1      | Units   |
| Q2      | Sales   |
| Q2      | Units   |
```

```
6. ✅ CRITICAL: Trim whitespace BEFORE merging (Best Practice!)
   - Select Column1
   - Transform → Format → Trim
   - Select Column2  
   - Transform → Format → Trim
   - This removes leading/trailing spaces from both columns
```

**Why trim first?**
- Headers may have spaces: "Status " (trailing) or " Sales" (leading)
- **Without trim before merge**: "Status " + "-" + " Jan" → "Status - Jan" ❌ (space around dash!)
- **With trim before merge**: "Status" + "-" + "Jan" → "Status-Jan" ✅ (clean delimiter)

```
7. Merge Columns: Column1 + Column2
   - Select Column1
   - Hold Ctrl, select Column2
   - Transform → Merge Columns
   - Separator: Choose delimiter:
     - "_" (underscore) - most common
     - "-" (dash) - also common
     - " " (space) - less recommended
   - Example result: "Q1_Sales", "Q1_Units", "Q2_Sales", "Q2_Units"
```

```
8. Trim delimiter (if blank cells exist)
   - If Row 2 had blank cells (common for Title/Author columns)
   - After merge you'll get: "Title-" or "-Jan" (delimiter at edge)
   - Transform → Replace Values:
     - Find: "^-" (leading dash) - use regex if available
     - Find: "-$" (trailing dash) - use regex if available
   - Or simpler: Right-click column → Transform → use M code
   - Formula bar: Text.Trim([Merged], "-")
   - Example: "Title-" → "Title", "Q1-Sales" → "Q1-Sales" (unchanged)
```

```
9. Transpose back (converts back to columns)
   - Transform → Transpose
   - You now have single-row headers with combined names
10. Rename → "header"
```

---

#### Step 3: Append with body (same as Method 1)

```
1. Select "header" query
2. Home → Append Queries → Append Queries as New
3. First table: header, Second table: body
4. Home → Use First Row as Headers
5. Set data types correctly
```

---

#### Step 4: If wide format, continue with unpivot

For wide format (Q1_Sales, Q1_Units, Q2_Sales, Q2_Units):

```
1. Unpivot Other Columns
   - Select ID columns (Product, Payment, etc.)
   - Transform → Unpivot Other Columns
   - Result: Attribute (Q1_Sales, ...) and Value

2. Split Column by Delimiter "_" (or "-")
   - Select "Attribute"
   - Split by delimiter at left-most delimiter
   - Result: Quarter (Q1, Q2) and Metric (Sales, Units)

3. ⚠️ CHECK: Do you need Index column?
   
   **✅ You DON'T need Index if:**
   - Each group (ID columns + Quarter/Month) has each metric ONLY ONCE
   - Example: Book A + Jan has Sales=1 value, Units=1 value ✅
   - In this case: Skip to step 4 (Pivot) directly
   
   **❌ You NEED Index if:**
   - Same group has same metric MULTIPLE TIMES (transaction data)
   - Example: Phone + Q1 has Sales=2 values (100, 150)
   - AND you want Don't Aggregate (keep all rows separate)
   - In this case: Add Index column
   
   **How to check:**
   - Look at your data before pivot
   - Count: How many rows for "Book A + Jan + Sales"?
   - If 1 row → No Index needed ✅
   - If 2+ rows → Need Index (or use Aggregate) ❌
   
   **If Index is needed:**
   ```
   Add Column → Index Column → From 0
   Pattern depends on your data:
   - From 0: If every row is separate transaction (0,1,2,3,...)
   - Custom pattern: If transactions span multiple rows (1,1,2,2,...)
     (requires M code for complex patterns)
   ```

4. Pivot Column
   - Select "Metric" column
   - Transform → Pivot Column
   - Values Column: "Value"
   - Advanced Options → Don't Aggregate (if each group has 1 value per metric)
   - OR → Choose Aggregate function (Sum, Average, etc.) if needed
   - Result: Product | Payment | Quarter | Sales | Units

5. Remove Index column (if you added it in step 3)
   - Right-click Index → Remove
```

**Notes on Aggregate vs Don't Aggregate:**
- **Don't Aggregate**: Use when each group has unique values
  - Example: Book A + Jan → Sales=1 value, Units=1 value
  - No Index needed in this case ✅
- **Aggregate (Sum/Average/etc.)**: Use when you want to combine multiple values
  - Example: Phone + Q1 → Sales=2 values (100, 150) → Sum = 250
  - No Index needed - aggregation handles multiple values ✅
- **Don't Aggregate + Multiple values**: Requires Index
  - Example: Phone + Q1 → Sales=2 values but want 2 separate rows
  - Must add Index to distinguish transactions ❌

---

### Why Method 2 works

**Concept**: Transpose to use Fill Down (since Fill Right doesn't exist), manipulate, transpose back

**Benefits**:
- ✅ More automated - headers created from original data
- ✅ No need to manually define headers

**Trade-off**:
- ❌ Complex - many steps, easy to make mistakes
- ❌ Doesn't work well with mixed hierarchy
- ❌ May need workarounds for pivot aggregation
- ❌ Harder to troubleshoot if something goes wrong

**Best for**: Uniform hierarchy + wide format data, when comfortable with complex transformations

---

## Method Comparison

| Aspect | Method 1: Separate + Append | Method 2: Transpose |
|--------|------------------------------|---------------------|
| **Reliability** | ✅ Always works | 🟡 Depends on structure |
| **Complexity** | ✅ Simple, clear steps | ❌ Many steps, complex |
| **Mixed hierarchy** | ✅ Perfect for this | ❌ Doesn't work well |
| **Transaction data** | ✅ Recommended | ⚠️ Overkill, not suitable |
| **Wide format data** | ✅ Works (then unpivot) | 🟡 Can work but complex |
| **Maintenance** | 🟡 Must maintain header | ✅ Auto-updates |
| **Beginner-friendly** | ✅ Easy to understand | ❌ Can be confusing |
| **Troubleshooting** | ✅ Easy to debug | ❌ Hard to find issues |

---

## Quick Decision Tree

```
START: Do you have multi-row headers?
  ↓
  ├─→ Mixed hierarchy (some 1-level, some 2-level)?
  │   → ✅ Use Method 1 (Separate + Append)
  │
  ├─→ Transaction data (no unpivot needed)?
  │   → ✅ Use Method 1 (Separate + Append)
  │
  ├─→ Wide format (need to unpivot)?
  │   ├─→ Want reliability?
  │   │   → ✅ Use Method 1 (Separate + Append + Unpivot)
  │   │
  │   └─→ Want automation + comfortable with complexity?
  │       → 🟡 Use Method 2 (Transpose Method)
  │
  └─→ Uniform hierarchy + comfortable with many steps?
      → 🟡 Consider Method 2 (Transpose Method)
      → But Method 1 is still safer!
```

---

## General Recommendation

**Start with Method 1 (Separate + Append)**. It's:
- ✅ Reliable - works for all cases
- ✅ Clear - easy to understand what's happening
- ✅ Maintainable - easy to fix if issues arise

**Use Method 2 only if**:
- You have uniform structure (all columns same hierarchy)
- You want automation (headers update automatically)
- You're comfortable with complex multi-step transformations
- You've tested thoroughly with sample data

---

## Remember

⚠️ **Always test with new data** before trusting the query!

⚠️ **For wide format**: Fix headers FIRST, then unpivot separately - don't try to do everything at once

⚠️ **For transaction data**: Method 1 is simpler - you just need correct column names, no unpivot

⚠️ **When in doubt**: Choose Method 1 (Separate + Append) - it always works! 🎯
