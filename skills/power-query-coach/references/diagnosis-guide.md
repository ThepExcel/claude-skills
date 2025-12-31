# Diagnosis Guide

## Table of Contents

1. [Overview](#overview)
2. [Core Diagnostic Question](#core-diagnostic-question)
3. [Red Flags Checklist](#red-flags-checklist)
   - [Structure Red Flags](#structure-red-flags)
   - [Content Red Flags](#content-red-flags)
4. [Problem Categories](#problem-categories)
   - [Category 1: Wide Format](#category-1-wide-format)
   - [Category 2: Multi-Row Headers](#category-2-multi-row-headers)
   - [Category 3: Blank Cells](#category-3-blank-cells-intentionally-left-empty)
   - [Category 4: Grouped Data](#category-4-grouped-data-hidden-hierarchy)
   - [Category 5: Mixed Metrics (Stacked)](#category-5-mixed-metrics-stacked)
   - [Category 6: Date Issues](#category-6-date-issues)
   - [Category 7: Multiple Tables in One Sheet](#category-7-multiple-tables-in-one-sheet)
5. [Diagnostic Process](#diagnostic-process)
   - [Step 1: Quick Visual Scan](#step-1-quick-visual-scan-30-seconds)
   - [Step 2: Check Fundamentals](#step-2-check-fundamentals-1-min)
   - [Step 3: Identify Primary Problem](#step-3-identify-primary-problem-30-seconds)
   - [Step 4: List Secondary Issues](#step-4-list-secondary-issues-30-seconds)
   - [Step 5: Prioritize Fixes](#step-5-prioritize-fixes-30-seconds)
6. [Example Diagnostic Conversations](#example-diagnostic-conversations)
   - [Example 1: Wide Format + Blank Cells](#example-1-wide-format--blank-cells)
   - [Example 2: Grouped Data](#example-2-grouped-data)
   - [Example 3: Multi-Row Headers](#example-3-multi-row-headers)
7. [Common Diagnostic Mistakes](#common-diagnostic-mistakes)
8. [Tips for Effective Diagnosis](#tips-for-effective-diagnosis)
9. [Remember](#remember)

---

## Overview

This guide helps identify data structure problems quickly and accurately. Use it when analyzing user's data to spot red flags, categorize issues, and prioritize fixes.

## Core Diagnostic Question

**"Can this data be used directly in Pivot Table / Power BI without issues?"**

If answer is NO → identify which problems exist below.

## Red Flags Checklist

Use this checklist when first looking at data:

### Structure Red Flags
- [ ] **Wide format** - Metrics spread across columns (Jan, Feb, Mar... or Product A, Product B...)
- [ ] **Multi-row headers** - Headers span 2+ rows
- [ ] **Blank cells** - Intentionally left blank for visual grouping (similar to merged cells)
- [ ] **Grouped data** - Group headers (A, B, C) inserted between data rows
- [ ] **Subtotals/totals** - Summary rows mixed with detail rows
- [ ] **Multiple tables** - Multiple distinct tables in same sheet
- [ ] **Blank rows/columns** - Separators or formatting spacers

### Content Red Flags
- [ ] **Mixed data types** - Numbers stored as text, or vice versa
- [ ] **Inconsistent granularity** - Some rows are monthly, others are daily
- [ ] **Date format issues** - Dates as text, or ambiguous format (01/12 = Jan 12 or Dec 1?)
- [ ] **Missing values** - Not clearly marked (blank vs zero vs N/A)
- [ ] **Case inconsistency** - "Sales" vs "sales", "Product A" vs "product a"

## Problem Categories

### Category 1: Wide Format

**What it looks like**:
```
| Product | Jan | Feb | Mar | Apr |
|---------|-----|-----|-----|-----|
| A       | 100 | 150 | 200 | 120 |
| B       | 80  | 90  | 110 | 95  |
```

**Why it's wrong**:
- Metrics (Jan, Feb, Mar, Apr) are spread across columns
- Each metric should be a separate column: Product, Month, Value
- Can't filter by month easily
- Can't add new months without changing structure
- Pivot Table sees 4+ separate fields instead of 1 field with months

**Variations**:
- Metrics as columns: Sales Q1, Sales Q2, Units Q1, Units Q2
- Products as columns: Product A, Product B, Product C
- Departments/regions as columns: North, South, East, West

**Fix approach**: Unpivot

**Severity**: 🔴 High (blocks most analysis)

---

### Category 2: Multi-Row Headers

**What it looks like**:
```
| Q1    | Q1    | Q2    | Q2    |
| Sales | Units | Sales | Units |
|-------|-------|-------|-------|
| 1000  | 50    | 1200  | 60    |
```

**Why it's wrong**:
- Headers span multiple rows
- Power Query sees first row as data, not headers
- Column names unclear or missing
- Each topic (Quarter, Sales, Units) not separated properly

**Variations**:
- Category + Subcategory structure
- Time period + Metric structure
- Region + Department structure

**Fix approach**: 
- Simple cases: Transpose → Fill Down → Merge → Transpose back → Promote Headers
- Complex cases: May need Transpose → Fill Down → Merge → Unpivot → Split → Pivot
- Reliable but manual: Separate headers + Append body (requires maintaining header definitions)

**Severity**: 🟡 Medium-High (causes confusion, requires fix before analysis)

---

### Category 3: Blank Cells (Intentionally Left Empty)

**What it looks like**:
```
| Product  | Region | Sales |
|----------|--------|-------|
| Phone    | North  | 100   |
|          | South  | 150   | <- Product cell intentionally blank
|          | East   | 120   |
| Laptop   | North  | 200   |
```

**Why it's wrong**:
- Cells are intentionally left blank for visual grouping (similar to merged cells)
- Only first row of each group has the category value
- Other rows appear blank in Power Query
- Loses group information for most rows
- Inconsistent row counts

**What to tell user**:
"คอลัมน์ Product มีการ**เว้นว่างเอาไว้**ให้ข้อมูลดูง่าย (คล้ายๆ กับการ merged cell) ทำให้แถวที่ 2, 3 ไม่มีข้อมูล Product"

**Fix approach**: Fill Down

**Severity**: 🟡 Medium (easy to fix but data loss if not caught)

---

### Category 4: Grouped Data (Hidden Hierarchy)

**What it looks like**:
```
| Factory/WH | TXID   | Sales |
|------------|--------|-------|
| A          |        |       | <- Group header
| WH-001     | TX0001 | 100   |
| WH-002     | TX0002 | 150   |
| B          |        |       | <- Group header
| WH-003     | TX0003 | 200   |
```

**Why it's wrong**:
- Group headers (A, B) inserted as separate rows
- Data rows missing factory information
- Empty cells in data columns for group headers
- Hierarchy is implicit, not explicit

**Variations**:
- Department headers with employee rows
- Category headers with product rows
- Date headers with transaction rows

**Fix approach**: 
1. Fill Down (to get group into every row)
2. Filter out empty rows (remove group headers)
3. Conditional Column (to separate hierarchy levels if needed)

**Critical**: Must Fill Down **before** filtering, or hierarchy data will be lost!

**Severity**: 🔴 High (hierarchy information lost if handled wrong)

---

### Category 5: Mixed Metrics (Stacked)

**What it looks like**:
```
| Product | Payment | Attribute | Value |
|---------|---------|-----------|-------|
| Phone   | Cash    | Sales     | 1000  |
| Phone   | Cash    | Units     | 50    |
| Phone   | Card    | Sales     | 1200  |
| Phone   | Card    | Units     | 60    |
```

**Why it's wrong**:
- Multiple metrics (Sales, Units) stacked in same column
- Each metric should be separate column
- Hard to calculate (Sales / Units) in Pivot
- Requires multiple steps to filter

**Fix approach**: Pivot Column (with "Don't Aggregate" option)

**Severity**: 🟡 Medium (usable but inefficient)

---

### Category 6: Date Issues

**What it looks like**:
```
| Date       | Sales |
|------------|-------|
| 01/12/2024 | 100   | <- Is this Jan 12 or Dec 1?
| 2024-12-01 | 150   | <- Different format
| 1/12/24    | 200   | <- Short year
```

**Why it's wrong**:
- Ambiguous interpretation (US: MM/DD, UK/TH: DD/MM)
- Mixed formats in same column
- Stored as text instead of date type
- Wrong date values if locale assumed incorrectly

**Variations**:
- Multiple locales in same file
- Dates as text "January 1, 2024"
- Excel serial numbers (44927)
- Different separators: / vs - vs .

**Fix approach**: 
- Always use "Using Locale" when setting date type
- If mixed locales: may need custom logic to detect and parse correctly

**Severity**: 🔴 High (completely wrong analysis if locale is wrong)

---

### Category 7: Multiple Tables in One Sheet

**What it looks like**:
```
Sales Table (rows 1-10)

Commission Table (rows 15-20)

Totals (row 25)
```

**Why it's wrong**:
- Cannot connect to single source
- Mixing different granularities
- Unclear boundaries between tables

**Fix approach**: 
- If truly separate topics: Separate into different sheets/files
- If related: Combine with proper relationship
- Often indicates source file should be redesigned

**Severity**: 🔴 High (requires source restructuring)

---

## Diagnostic Process

### Step 1: Quick Visual Scan (30 seconds)

Look for obvious red flags:
1. Headers span multiple rows? → Multi-row headers
2. Months/products as columns? → Wide format
3. Empty rows between groups? → Grouped data
4. Merged cells? → Merged cells
5. Multiple distinct tables? → Multiple tables

### Step 2: Check Fundamentals (1 min)

Ask these questions:
1. **One header row?** If no → Multi-row headers or merged cells
2. **One column = one concept?** If no → Wide format or mixed metrics
3. **Consistent rows?** If no → Subtotals, grouped data, or multiple tables
4. **Correct data types?** If no → Date issues, text numbers

### Step 3: Identify Primary Problem (30 seconds)

What's the BIGGEST issue blocking analysis?
- Usually: Wide format OR Multi-row headers OR Grouped data
- These often need fixing before anything else

### Step 4: List Secondary Issues (30 seconds)

What else needs attention after structure is fixed?
- Data type corrections
- Date locale settings
- Removing auto-generated steps
- Case consistency

### Step 5: Prioritize Fixes (30 seconds)

**Order matters!**
1. **Structure first**: Wide format, multi-row headers, merged cells
2. **Content next**: Data types, dates, cleaning
3. **Optimization last**: Removing redundant steps, performance tuning

## Example Diagnostic Conversations

### Example 1: Wide Format + Blank Cells

**User shows**:
```
| Product  | Jan | Feb | Mar |
|----------|-----|-----|-----|
| Phone    | 100 | 150 | 200 |
|          | 80  | 90  | 110 |
| Laptop   | 200 | 220 | 250 |
```

**Diagnosis**:
> "เห็นปัญหา 2 อย่างค่ะ:
> 1. **Wide format** - เดือน (Jan, Feb, Mar) แยกเป็นคอลัมน์ ทำให้ Pivot Table เห็น 3 fields แยกกัน
> 2. **Blank cells** - คอลัมน์ Product มีการเว้นว่างเอาไว้ (คล้ายๆ กับการ merged cell) ทำให้แถวที่ 2 ไม่มีข้อมูล Product
> 
> เราจะแก้แบบนี้นะคะ:
> 1. Fill Down ก่อน (เติม Product)
> 2. Unpivot Other Columns (แปลง wide → long)"

---

### Example 2: Grouped Data

**User shows**:
```
| Factory/WH | Sales |
|------------|-------|
| A          |       |
| WH-001     | 100   |
| WH-002     | 150   |
| B          |       |
| WH-003     | 200   |
```

**Diagnosis**:
> "นี่คือ **grouped data** ค่ะ - Factory (A, B) ถูกแทรกเป็น group headers แยก
> 
> ปัญหาคือ:
> - แถว WH-001, WH-002 ไม่รู้ว่าอยู่ Factory ไหน
> - แถว A, B ไม่มีข้อมูล Sales
> 
> ⚠️ **สำคัญมาก**: ต้อง Fill Down **ก่อน** Filter เสมอ!
> ถ้า filter ก่อน → ข้อมูล Factory จะหายไปเลย"

---

### Example 3: Multi-Row Headers

**User shows**:
```
| Q1    | Q1    | Q2    | Q2    |
| Sales | Units | Sales | Units |
|-------|-------|-------|-------|
| 1000  | 50    | 1200  | 60    |
```

**Diagnosis**:
> "นี่คือ **multi-row headers** ค่ะ - หัวตาราง 2 ชั้น (Quarter + Metric)
> 
> ปัญหาคือ:
> - ไม่สามารถ filter ตาม Quarter ได้
> - Sales กับ Units ไม่ได้แยกชัดเจน
> - Structure แบบ wide
> 
> เป้าหมายคือได้ 3 คอลัมน์: Quarter, Sales, Units
> เราจะแก้หัวก่อน แล้วค่อย unpivot + pivot"

---

## Common Diagnostic Mistakes

### ❌ Mistake: Diagnosing too vaguely

**Bad**: "ข้อมูลนี้มีปัญหา structure ค่ะ ต้องแก้"

**Good**: "เห็นปัญหา 2 อย่าง: 1) Wide format - เดือนแยกเป็นคอลัมน์ 2) Merged cells ในคอลัมน์ Product"

### ❌ Mistake: Missing impact explanation

**Bad**: "ข้อมูลนี้เป็น wide format"

**Good**: "ข้อมูลนี้เป็น wide format ทำให้ Pivot Table จะเห็น 4 fields แยกกัน (Jan, Feb, Mar, Apr) แทนที่จะเป็น 1 field Month ที่ filter ได้"

### ❌ Mistake: Not prioritizing

**Bad**: [Lists 5 problems without saying which to fix first]

**Good**: "เราจะแก้หัวตารางก่อนนะคะ (ปัญหาที่ 1 และ 2) แล้วค่อยมาแก้ data type ทีหลัง (ปัญหาที่ 3)"

### ❌ Mistake: Assuming fix without asking

**Bad**: [Immediately starts explaining unpivot steps]

**Good**: "พี่ต้องการให้ข้อมูลมีหน้าตายังไงคะ? ใช้กับ Pivot Table หรือ Power BI?"

## Tips for Effective Diagnosis

1. **Always ask about source first** - "Source จริงๆ คืออะไรคะ?" This changes the approach completely
2. **Show concrete impact** - Don't just say "it's wrong", show what will happen
3. **Use visuals** - Draw before/after tables to make it clear
4. **Prioritize ruthlessly** - Fix structure before content
5. **Check for hidden issues** - Case sensitivity, locale, hardcoded steps come later but matter

## Remember

Good diagnosis:
- **Specific** (2-3 concrete problems, not "messy data")
- **Prioritized** (what to fix first)
- **Impact-focused** (explain what will happen)
- **Solution-oriented** (hint at fix approach)

The goal: User understands their problems and feels confident about the path forward! 🎯
