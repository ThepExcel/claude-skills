# Slide Background Design (Lessons Learned)

เมื่อใช้ AI gen backgrounds สำหรับ presentation slides:

## Workflow ที่ Work

```
1. REFERENCE FIRST — ขอดู reference ที่ user ชอบก่อน
2. ANALYZE PATTERNS — สรุป style patterns จาก references
3. GEN COMPLETE BG — Gen ทั้ง slide background (ไม่แยกชิ้น)
4. NO TEXT — บอก "NO TEXT" ให้ชัด, user วาง text เอง
5. ITERATE — ปรับตาม feedback (size, position, simplicity)
```

## What Works

| Technique | Why |
|-----------|-----|
| Gen ทั้ง background (ไม่แยก elements) | ได้ภาพ cohesive สวยกว่า |
| ใช้ `--edit` กับ logo/brand asset เป็น ref | AI เห็น shape จริง ไม่ต้องเดา |
| บอก "NO TEXT" ชัดเจน | Text จาก AI มักผิด/ไม่สวย |
| White background แทน transparent | Nano Banana Pro ทำ alpha จริงไม่ได้ |
| เริ่ม simple แล้วค่อยเพิ่ม | Logo เล็กมุมเดียว ดีกว่าเยอะทุกมุม |
| ระบุ aspect ratio (16:9) | ได้ proportion ที่ถูกต้อง |

## What Doesn't Work

| Technique | Problem |
|-----------|---------|
| "TRANSPARENT BACKGROUND" | ได้ checkerboard ปลอม ไม่ใช่ alpha จริง |
| อธิบาย logo shape เอง | AI ตีความผิด ใช้ --edit กับ ref แทน |
| Gen แยกชิ้นแล้วประกอบ | Elements ไม่ match กัน, เสียเวลา |
| Decoration เยอะ (ทุกมุม) | รกเกินไป ไม่ professional |
| Gen พร้อม text | Text มักผิด font/spelling |

## Prompt Template: Slide Background

```
Professional presentation [SLIDE_TYPE] slide background,
16:9 aspect ratio. NO TEXT. [STYLE] STYLE.

BACKGROUND: [describe bg - color, grid, gradient]

DECORATIVE ELEMENTS: [describe accents - position, size, style]
- Use "small" / "subtle" / "minimal" for accents
- Specify exact corner (top-left, bottom-right only, etc.)

LAYOUT: [describe empty areas for content]
- "Leave [area] empty for [content type]"

COLORS: [list specific hex codes]

STYLE: [overall mood - modern, tech, minimal, etc.]
```

## Brand Logo as 3D Element

เมื่อต้องการแปลง logo เป็น 3D wireframe:

```bash
# Step 1: แปลง logo เป็น wireframe ก่อน
python tools/generate_image.py "Transform this logo into a 3D golden wireframe version. Use exact shape from reference. Golden wireframe mesh with glowing nodes. White background." --edit path/to/logo.png -o wireframe-logo.png

# Step 2: ใช้ wireframe logo ใน slide background
python tools/generate_image.py "Professional slide background... [describe layout with wireframe logo from reference]" --edit wireframe-logo.png -o slide-bg.png -a 16:9
```

## Transparent PNG Workaround

Nano Banana Pro **ไม่รองรับ** transparent PNG โดยตรง

**ทางเลือก:**
1. **White bg (แนะนำ)** — ถ้า slide เป็น white อยู่แล้ว ใช้ได้เลย
2. **Background removal** — Gen บน white แล้วใช้ `fal-ai/bria/background/remove` ลบ bg ทีหลัง
