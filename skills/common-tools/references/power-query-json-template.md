# Power Query Function JSON Template (Simple Format)

**Use this when creating/updating Power Query (M Language) function JSON files.**

## File Location
```
functions/power-query/{slug}-function-data.json
```

## Complete JSON Structure

```json
{
  "slug": "table-selectrows",
  "program": "power-query",
  "title": "Table.SelectRows - กรองแถวตามเงื่อนไข",
  "summary": "Table.SelectRows กรองแถวจากตารางตามเงื่อนไขที่กำหนด คืนค่าเป็นตารางใหม่ที่มีเฉพาะแถวที่ตรงตามเงื่อนไข",
  "description": "Table.SelectRows เป็นฟังก์ชันหลักสำหรับกรองข้อมูลใน Power Query\n.\nที่เจ๋งคือเราสามารถใช้ each syntax เพื่อเขียนเงื่อนไขได้ง่ายๆ เช่น each [Amount] > 1000\n.\nส่วนตัวผมใช้ฟังก์ชันนี้แทบทุก query เพราะการกรองข้อมูลเป็นขั้นตอนพื้นฐานที่ขาดไม่ได้ 😎",
  "syntax": "Table.SelectRows(table as table, condition as function) as table",
  "arguments": [
    {
      "name": "table",
      "required": true,
      "type": "table",
      "description": "ตารางต้นทางที่ต้องการกรอง",
      "default": ""
    },
    {
      "name": "condition",
      "required": true,
      "type": "function",
      "description": "ฟังก์ชันเงื่อนไขที่รับแถวและคืนค่า true/false",
      "default": ""
    }
  ],
  "examples": [
    {
      "title": "กรองตามค่าตัวเลข",
      "formula": "Table.SelectRows(Source, each [Amount] > 1000)",
      "result": "ตารางที่มีเฉพาะแถวที่ Amount > 1000",
      "explanation": "ใช้ each syntax เพื่อเข้าถึงคอลัมน์ Amount และเปรียบเทียบกับ 1000"
    }
  ],
  "faq": [
    {
      "q": "each คืออะไร?",
      "a": "each เป็น shorthand สำหรับ (_) => _ คือฟังก์ชันที่รับ parameter ตัวเดียว ใช้คู่กับ [ColumnName] เพื่อเข้าถึงค่าในคอลัมน์"
    }
  ],
  "tips": [
    "ใช้ and/or เพื่อรวมหลายเงื่อนไข เช่น each [A] > 1 and [B] < 10",
    "ใช้ Text.Contains สำหรับค้นหาข้อความบางส่วน"
  ],
  "related": ["table-selectcolumns", "table-removematchingrows", "list-select"],
  "resources": [
    {"title": "Microsoft Learn: Table.SelectRows", "url": "https://learn.microsoft.com/en-us/powerquery-m/table-selectrows"}
  ]
}
```

## Field Reference

| Field | Required | Description |
|-------|----------|-------------|
| `slug` | ✅ | Function identifier (lowercase, hyphenated) |
| `program` | ✅ | Always "power-query" |
| `title` | ✅ | Function name + Thai description |
| `summary` | ✅ | 1-2 sentences explaining what the function does (60-150 chars) |
| `description` | ✅ | Main content in Sira style with paragraphs separated by `\n.\n` |
| `syntax` | ✅ | M language function signature |
| `arguments` | ✅ | Array of argument objects |
| `examples` | ✅ | Array of 4+ practical examples |
| `faq` | ✅ | Array of 2-3 Q&A pairs |
| `tips` | ✅ | Array of 2-3 practical tips |
| `related` | ✅ | Array of 3-5 related function slugs (lowercase) |
| `resources` | ✅ | Array of 2+ reference links |

## Requirements

- **Examples:** Minimum 4, show real-world use cases
- **Language:** All content in Thai (Sira conversational style)
- **No extra fields:** Only use fields listed above
