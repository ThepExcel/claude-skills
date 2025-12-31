# n8n Function JSON Template (Simple Format)

**Use this when creating/updating n8n function JSON files.**

## File Location
```
functions/n8n/{slug}-function-data.json
```

## Complete JSON Structure

```json
{
  "slug": "json-parse",
  "program": "n8n",
  "title": "$json - เข้าถึงข้อมูล JSON จาก Input",
  "summary": "$json ใช้เข้าถึงข้อมูลจาก input item ปัจจุบัน เป็นตัวแปรพื้นฐานที่สุดใน n8n expressions",
  "description": "$json เป็นจุดเริ่มต้นในการเข้าถึงข้อมูลใน n8n\n.\nที่เจ๋งคือเราใช้ dot notation เพื่อเข้าถึง property ลึกๆ ได้ง่าย เช่น $json.user.email\n.\nส่วนตัวผมใช้ $json ในแทบทุก expression เพราะข้อมูลจาก node ก่อนหน้ามักจะอยู่ในรูป JSON 😎",
  "syntax": "$json.propertyName",
  "arguments": [
    {
      "name": "propertyName",
      "required": true,
      "type": "string",
      "description": "ชื่อ property ที่ต้องการเข้าถึง",
      "default": ""
    }
  ],
  "examples": [
    {
      "title": "เข้าถึง property ธรรมดา",
      "formula": "$json.email",
      "result": "user@example.com",
      "explanation": "เข้าถึง property email จาก input item ปัจจุบัน"
    }
  ],
  "faq": [
    {
      "q": "$json กับ $input.item.json ต่างกันอย่างไร?",
      "a": "$json เป็น shorthand ของ $input.item.json ใช้แทนกันได้ แต่ $json สั้นกว่า"
    }
  ],
  "tips": [
    "ใช้ $json?.property เพื่อป้องกัน error เมื่อ property อาจไม่มี",
    "ใช้ $json['property-name'] เมื่อชื่อ property มี hyphen หรือ space"
  ],
  "related": ["input-item", "jmespath", "json-stringify"],
  "resources": [
    {"title": "n8n Docs: Expressions", "url": "https://docs.n8n.io/code/expressions/"}
  ]
}
```

## Field Reference

| Field | Required | Description |
|-------|----------|-------------|
| `slug` | ✅ | Function identifier (lowercase, hyphenated) |
| `program` | ✅ | Always "n8n" |
| `title` | ✅ | Function/variable name + Thai description |
| `summary` | ✅ | 1-2 sentences explaining what it does (60-150 chars) |
| `description` | ✅ | Main content in Sira style with paragraphs separated by `\n.\n` |
| `syntax` | ✅ | Usage syntax |
| `arguments` | ✅ | Array of argument/parameter objects |
| `examples` | ✅ | Array of 4+ practical examples |
| `faq` | ✅ | Array of 2-3 Q&A pairs |
| `tips` | ✅ | Array of 2-3 practical tips |
| `related` | ✅ | Array of 3-5 related function slugs (lowercase) |
| `resources` | ✅ | Array of 2+ reference links |

## Requirements

- **Examples:** Minimum 4, show real-world use cases
- **Language:** All content in Thai (Sira conversational style)
- **No extra fields:** Only use fields listed above
