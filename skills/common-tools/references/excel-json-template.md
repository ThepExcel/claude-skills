# Excel Function JSON Template (Simple Format)

**Use this when creating/updating Excel function JSON files.**

## File Location
```
functions/excel/{slug}-function-data.json
```

## Complete JSON Structure

```json
{
  "slug": "vlookup",
  "program": "excel",
  "title": "VLOOKUP - ค้นหาข้อมูลแนวตั้ง",
  "summary": "VLOOKUP ค้นหาค่าในคอลัมน์แรกของตาราง แล้วคืนค่าจากคอลัมน์ที่ระบุในแถวเดียวกัน เหมาะสำหรับค้นหาข้อมูลที่มี key อยู่ทางซ้าย",
  "description": "VLOOKUP เป็นฟังก์ชันค้นหาที่ใช้กันมากที่สุดใน Excel\n.\nที่ต้องระวังคือ VLOOKUP ค้นหาได้จากซ้ายไปขวาเท่านั้น ถ้าข้อมูลที่ต้องการอยู่ทางซ้ายของคอลัมน์ค้นหา ต้องใช้ XLOOKUP หรือ INDEX+MATCH แทน 😎",
  "syntax": "=VLOOKUP(lookup_value, table_array, col_index_num, [range_lookup])",
  "arguments": [
    {
      "name": "lookup_value",
      "required": true,
      "type": "Any",
      "description": "ค่าที่ต้องการค้นหาในคอลัมน์แรกของ table_array",
      "default": ""
    }
  ],
  "examples": [
    {
      "title": "ค้นหาแบบ exact match",
      "formula": "=VLOOKUP(\"P001\", ProductsTable, 2, FALSE)",
      "result": "Apple",
      "explanation": "ค้นหา \"P001\" ในคอลัมน์แรกของ ProductsTable แล้วคืนค่าจากคอลัมน์ที่ 2 (ชื่อสินค้า)"
    }
  ],
  "faq": [
    {
      "q": "VLOOKUP กับ XLOOKUP ต่างกันอย่างไร?",
      "a": "XLOOKUP ยืดหยุ่นกว่า - ค้นหาได้ทั้งซ้ายและขวา, คืนค่าหลายคอลัมน์ได้, จัดการ error ได้ในตัว"
    }
  ],
  "tips": [
    "ใส่ FALSE เป็น argument สุดท้ายเสมอเพื่อค้นหาแบบ exact match",
    "ใช้ IFERROR ครอบเพื่อจัดการ #N/A"
  ],
  "related": ["xlookup", "index", "match", "hlookup"],
  "resources": [
    {"title": "Microsoft Support: VLOOKUP", "url": "https://support.microsoft.com/en-us/office/vlookup-function-0bbc8083-26fe-4963-8ab8-93a18ad188a1"}
  ]
}
```

## Field Reference

| Field | Required | Description |
|-------|----------|-------------|
| `slug` | ✅ | Function identifier (lowercase, hyphenated) |
| `program` | ✅ | Always "excel" |
| `title` | ✅ | Function name + Thai description |
| `summary` | ✅ | 1-2 sentences explaining what the function does (60-150 chars) |
| `description` | ✅ | Main content in Sira style with paragraphs separated by `\n.\n` |
| `syntax` | ✅ | Function syntax with = prefix |
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
