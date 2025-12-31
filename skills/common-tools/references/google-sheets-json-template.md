# Google Sheets Function JSON Template (Simple Format)

**Use this when creating/updating Google Sheets function JSON files.**

## File Location
```
functions/google-sheets/{slug}-function-data.json
```

## Complete JSON Structure

```json
{
  "slug": "query",
  "program": "google-sheets",
  "title": "QUERY - ค้นหาข้อมูลด้วย SQL-like syntax",
  "summary": "QUERY ใช้ภาษาคล้าย SQL เพื่อค้นหา กรอง จัดเรียง และจัดกลุ่มข้อมูลในตาราง เป็นฟังก์ชันที่ทรงพลังที่สุดใน Google Sheets",
  "description": "QUERY เป็นฟังก์ชันที่ทำให้ Google Sheets โดดเด่นกว่า Excel\n.\nที่เจ๋งคือเราใช้ภาษา SQL-like ที่คุ้นเคยในการจัดการข้อมูล ไม่ต้องเขียนสูตรซ้อนกันหลายชั้น\n.\nส่วนตัวผมใช้ QUERY แทน FILTER+SORT เพราะอ่านง่ายกว่าและยืดหยุ่นกว่ามาก 😎",
  "syntax": "=QUERY(data, query, [headers])",
  "arguments": [
    {
      "name": "data",
      "required": true,
      "type": "Range/Array",
      "description": "ช่วงข้อมูลที่ต้องการ query",
      "default": ""
    },
    {
      "name": "query",
      "required": true,
      "type": "Text",
      "description": "Query string ในรูปแบบ Google Visualization API Query Language",
      "default": ""
    },
    {
      "name": "headers",
      "required": false,
      "type": "Number",
      "description": "จำนวนแถว header ในข้อมูล",
      "default": "-1 (auto-detect)"
    }
  ],
  "examples": [
    {
      "title": "เลือกเฉพาะบางคอลัมน์",
      "formula": "=QUERY(A1:D100, \"SELECT A, C, D\")",
      "result": "ตารางที่มีเฉพาะคอลัมน์ A, C, D",
      "explanation": "ใช้ SELECT เพื่อเลือกเฉพาะคอลัมน์ที่ต้องการ เหมือน SQL"
    }
  ],
  "faq": [
    {
      "q": "QUERY ต่างจาก FILTER อย่างไร?",
      "a": "QUERY ยืดหยุ่นกว่ามาก - เลือกคอลัมน์, จัดเรียง, จัดกลุ่ม, คำนวณ aggregate ได้ในสูตรเดียว ส่วน FILTER ทำได้แค่กรองแถว"
    }
  ],
  "tips": [
    "ใช้ Col1, Col2 แทน A, B เมื่อ data เป็น array ไม่ใช่ range",
    "ใช้ FORMAT เพื่อจัดรูปแบบผลลัพธ์"
  ],
  "related": ["filter", "sort", "importrange"],
  "resources": [
    {"title": "Google Docs: QUERY", "url": "https://support.google.com/docs/answer/3093343"}
  ]
}
```

## Field Reference

| Field | Required | Description |
|-------|----------|-------------|
| `slug` | ✅ | Function identifier (lowercase, hyphenated) |
| `program` | ✅ | Always "google-sheets" |
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
