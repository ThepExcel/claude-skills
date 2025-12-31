# DAX Function JSON Template (Simple Format)

**Use this when creating/updating DAX function JSON files.**

## File Location
```
functions/dax/{slug}-function-data.json
```

## Complete JSON Structure

```json
{
  "slug": "calculate",
  "program": "dax",
  "title": "CALCULATE - คำนวณด้วย Filter Context ใหม่",
  "summary": "CALCULATE ประเมินผล expression ภายใต้ filter context ที่ถูกแก้ไขตาม filter arguments ที่กำหนด เป็นฟังก์ชันที่ทรงพลังที่สุดใน DAX",
  "description": "CALCULATE เป็นหัวใจของ DAX เพราะช่วยให้เราควบคุม filter context ได้\n.\nที่เจ๋งคือเราสามารถเพิ่ม ลบ หรือแก้ไข filter ได้ตามต้องการ ทำให้คำนวณค่าในมุมมองต่างๆ ได้\n.\nส่วนตัวผมใช้ CALCULATE แทบทุก measure ที่ซับซ้อนกว่าการ SUM ธรรมดา 😎",
  "syntax": "CALCULATE(<expression>, [<filter1>], [<filter2>], ...)",
  "arguments": [
    {
      "name": "expression",
      "required": true,
      "type": "Scalar Expression",
      "description": "Expression ที่ต้องการประเมินผล (ต้องคืนค่า scalar)",
      "default": ""
    },
    {
      "name": "filter",
      "required": false,
      "type": "Boolean/Table",
      "description": "Filter arguments ที่ใช้แก้ไข filter context",
      "default": ""
    }
  ],
  "examples": [
    {
      "title": "คำนวณยอดขายสินค้าเฉพาะหมวด",
      "formula": "CALCULATE(SUM(Sales[Amount]), Products[Category] = \"Electronics\")",
      "result": "ยอดขายรวมเฉพาะหมวด Electronics",
      "explanation": "CALCULATE แก้ไข filter context ให้เหลือเฉพาะ Electronics แล้วคำนวณ SUM"
    }
  ],
  "faq": [
    {
      "q": "CALCULATE กับ CALCULATETABLE ต่างกันอย่างไร?",
      "a": "CALCULATE คืนค่า scalar (ค่าเดียว) ส่วน CALCULATETABLE คืนค่าเป็น table"
    }
  ],
  "tips": [
    "ใช้ ALL() เพื่อลบ filter ออกทั้งหมด",
    "ใช้ KEEPFILTERS() เพื่อเพิ่ม filter แทนการแทนที่"
  ],
  "related": ["calculatetable", "all", "filter", "sumx"],
  "resources": [
    {"title": "Microsoft Learn: CALCULATE", "url": "https://learn.microsoft.com/en-us/dax/calculate-function-dax"}
  ]
}
```

## Field Reference

| Field | Required | Description |
|-------|----------|-------------|
| `slug` | ✅ | Function identifier (lowercase, hyphenated) |
| `program` | ✅ | Always "dax" |
| `title` | ✅ | Function name + Thai description |
| `summary` | ✅ | 1-2 sentences explaining what the function does (60-150 chars) |
| `description` | ✅ | Main content in Sira style with paragraphs separated by `\n.\n` |
| `syntax` | ✅ | DAX function syntax |
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
