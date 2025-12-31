# Power Query Coach

An interactive coaching skill that helps transform messy data into clean, analysis-ready formats using Power Query UI. Perfect for office workers who know basic Power Query but struggle with problematic data structures.

## What This Skill Does

**Power Query Coach helps you**:
- 🔍 Diagnose data structure problems (wide format, multi-row headers, blank cells, grouped data)
- 🎯 Visualize the ideal "goal state" for your data
- 📋 Get step-by-step UI guidance for transformations (70-80% solvable without M code)
- ⚠️ Avoid common pitfalls and mistakes
- 🔮 Prevent future issues with best practices

## Who It's For

**Target users**:
- Office workers who know basic Power Query
- Data analysts preparing data for Pivot Tables or Power BI
- Anyone struggling with "ugly data" that can't be analyzed
- Teams wanting to standardize data transformation approaches

**Prerequisites**: Basic familiarity with Power Query (how to open it, what a query is)

## Quick Start

### Example Interaction

**You**: "I have sales data with months as columns (Jan, Feb, Mar) and I can't filter by month in my Pivot Table."

**Power Query Coach**:
> "สวัสดีค่ะ! ฟ้าจะช่วยพี่แปลงข้อมูลให้เป๊ะนะคะ 😊
> 
> ก่อนอื่น - ข้อมูลนี้จะเอาไปใช้กับอะไรคะ? แล้ว source จริงๆ มาจากไหน?
>
> [After you answer...]
>
> เห็นแล้วค่ะ! นี่คือปัญหา **wide format** - เดือนแยกเป็นหลายคอลัมน์ ทำให้ Pivot Table เห็น 3 fields แยกกัน (Jan, Feb, Mar) แทนที่จะเป็น 1 field ที่ filter เดือนได้
>
> เป้าหมายคือได้ข้อมูลแบบนี้:
> | Product | Month | Sales |
>
> มาแก้กันทีละขั้นตอนนะคะ..."

## Key Improvements (v2)

This skill has been refined based on real-world usage feedback:

**✅ Better Terminology**
- "Blank cells" instead of "merged cells" (more accurate)
- Clear distinction between visual grouping and actual merges

**✅ Data-Driven Logic**
- Use `if [TXID] = null` instead of `Text.Length = 1`
- Check data characteristics, not naming patterns
- More flexible and future-proof

**✅ M Code Reference**
- Proper syntax for special characters: `[#"Factory/Warehouse"]`
- Explains when to use `[#"..."]` format

**✅ Data Type Best Practices**
- Decimal Number as default for amounts (future-proof)
- Clear guidance on when to use Whole Number

**✅ Respect User Data**
- Always ask before removing columns
- Confirm transformations that affect data

**✅ Complete Workflows**
- Emphasize: Fill Down → Create Column → Fill Down → Filter
- Never skip the Filter step after grouped data

**✅ Multi-Row Headers Methods**
- Method 1: Separate Header + Append (reliable, recommended)
- Method 2: Transpose Method (auto but complex)
- Clear decision framework for which to use

## File Structure

```
power-query-coach/
├── SKILL.md                           # Main coaching workflow
├── README.md                          # This file
└── references/
    ├── diagnosis-guide.md             # How to diagnose problems
    ├── transformation-patterns.md     # UI step-by-step solutions
    ├── common-pitfalls.md            # Mistakes and recovery
    ├── best-practices.md             # Principles and tips
    └── examples.md                   # Real before/after cases
```

## Key Concepts

### The Core Principle

**Good data = Single-row headers + Separate topics + Long format**

Not just about having one header row - it's about:
- ✅ Each column represents ONE concept
- ✅ Long format (not wide)
- ✅ Consistent granularity
- ✅ Correct data types

### The Most Important Rules

1. **⚠️ Fill Down BEFORE Filter** - When dealing with grouped data, always Fill Down first or you lose hierarchy forever
2. **⚠️ Always Filter After Fill Down** - Don't skip this step or you'll have duplicate rows
3. **⚠️ Use Data-Driven Logic** - Check data characteristics (`[TXID] = null`) not patterns (`Text.Length = 1`)
4. **⚠️ Always use "Using Locale" for dates** - Never set date type without specifying locale
5. **⚠️ Never use "Unpivot Columns"** - Use "Unpivot Other Columns" or "Unpivot Only Selected Columns" instead
6. **⚠️ Case sensitivity everywhere** - Power Query treats "Sales" ≠ "sales"
7. **⚠️ M Code special characters** - Use `[#"Column/Name"]` for columns with `/`, `-`, space, etc.
8. **⚠️ Decimal Number default** - Use Decimal for amounts (future-proof for decimals)
9. **⚠️ Ask before removing columns** - Respect user's data
10. **⚠️ Find the true source** - Connect to original data source, not manually edited files

## Installation

### Option 1: Claude.ai Projects (Recommended)

1. Create or open a Claude Project
2. Go to Project Knowledge
3. Upload this entire folder as Custom Knowledge
4. The skill will be available in all chats within the project

### Option 2: Direct Use

Simply reference the files in your conversations:
- Read SKILL.md for the coaching approach
- Use references/ files for specific guidance

## How to Use

**Start a conversation describing your data problem**:
- "I have employee sales data with months as separate columns"
- "My data has group headers (A, B, C) inserted between rows"
- "Headers span 2 rows and I don't know how to fix it"
- Upload a screenshot of your problematic data

**The coach will**:
1. Ask clarifying questions
2. Diagnose specific problems
3. Show ideal structure
4. Guide step-by-step through Power Query UI
5. Warn about pitfalls
6. Suggest best practices

## What Problems Can Be Solved

### ✅ Fully Supported (UI-based)

1. **Wide Format** → Unpivot to long format
2. **Multi-Row Headers** → Single-row headers (2 methods)
3. **Blank Cells** → Fill Down
4. **Grouped Data** → Explicit hierarchy
5. **Stacked Metrics** → Separate columns
6. **Date Locale Issues** → Proper interpretation
7. **Combine Multiple Files** → Single table

### 🟡 May Need M Code

- Complex multi-row headers
- Mixed date locales in same column
- Custom transformations beyond UI

## Examples Included

1. **Wide Format** (Employee Sales) - Months as columns → Long format
2. **Stacked Metrics** (Product + Payment) - Metrics in rows → Separate columns
3. **Grouped Data** (Factory/Warehouse) - Group headers → Explicit hierarchy (with data-driven logic!)
4. **Multi-Row Headers** (Q1-Q3 + Sales/Units) - 2 rows → Proper structure

See `references/examples.md` for detailed walkthroughs.

## Credits

Created using the **Skill Extractor** methodology.

**Expert knowledge**: ThepExcel (เทพเอ็กเซล) - Excel, Power BI, AI, and automation consulting

**Version**: 2.0 (Updated with real-world feedback)

---

**Ready to transform your data?** Start using the Power Query Coach skill! 🚀✨
