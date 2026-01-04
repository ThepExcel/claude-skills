# Qwen Image / Qwen Image Edit (Alibaba)

## Overview

| Aspect | Detail |
|--------|--------|
| **Provider** | Alibaba Qwen |
| **Parameters** | 20B (MMDiT) |
| **License** | Apache 2.0 (Open Source) |
| **Strengths** | Text rendering, Chinese/English, precise editing |
| **ComfyUI** | Native support + GGUF versions |

## Models

| Model | Purpose | Released |
|-------|---------|----------|
| **Qwen-Image** | Text-to-image generation | 2025 |
| **Qwen-Image-Edit** | Image editing | Aug 2025 |
| **Qwen-Image-Edit-2511** | Enhanced editing, better consistency | Dec 2025 |
| **Qwen-Image-Layered** | Layer-based generation | Dec 2025 |

## Prompt Philosophy

**"Paint a picture with words in structured way"**

1-3 sentences work best. Order matters: main subject first.

## Prompt Structure

```
[Subject description] + [Setting/environment] + [Style] + [Technical details]
```

### Key Parameters

| Parameter | With Lightning LoRA | Without Lightning | Notes |
|-----------|---------------------|-------------------|-------|
| **CFG/Guidance** | **1.0** (fixed) | 2.5-4.0 | Lightning requires CFG=1 |
| **Steps** | 4 or 8 | 20-40 | Match LoRA version |
| **Seed** | Any integer | Any integer | Same seed + prompt = same output |

**⚠️ CRITICAL:** เมื่อใช้ Lightning LoRA ต้องตั้ง CFG=1.0 เท่านั้น ถ้าใช้ค่าอื่นจะได้ผลลัพธ์ไม่ดี

## Generation Prompts

### Portrait
```
Professional portrait of a young Asian woman, 25 years old,
wearing a white blouse, natural makeup, gentle smile.
Soft studio lighting, neutral gray background.
Shot on 85mm lens, shallow depth of field.
Clean, commercial photography style.
```

### Text in Image
```
Minimalist poster with the text "HELLO WORLD" in bold sans-serif font.
Text is centered, white color on dark blue background.
Modern typography, clean design, no other elements.
```

### Complex Scene
```
Cozy coffee shop interior, morning light streaming through large windows.
A person reading a book at a wooden table, steaming cup of coffee nearby.
Warm color palette, natural lighting, lifestyle photography style.
Shallow depth of field focusing on the person.
```

## Edit Prompts (Qwen-Image-Edit)

### Editing Types

| Type | Description | Example |
|------|-------------|---------|
| **Appearance** | Local changes, preserve rest | Remove object, change color |
| **Semantic** | Overall changes allowed | Style transfer, rotation |
| **Text** | Modify text in image | Change words, add text |

### Edit Prompt Format

```
[What to change]: [How to change it]
[What to keep]: [Elements to preserve]
```

### Examples

**Remove Object:**
```
Remove the car in the background.
Keep the person and all foreground elements unchanged.
Extend the natural background seamlessly.
```

**Change Style:**
```
Transform this photo into a watercolor painting style.
Keep the composition and subject positioning.
Soft brushstrokes, muted colors, artistic effect.
```

**Text Edit:**
```
Change the sign text from "OPEN" to "CLOSED".
Keep the same font style, size, and color.
Preserve the rest of the image exactly.
```

**Add Element:**
```
Add a small bird perched on the tree branch in the upper right.
Natural lighting matching the scene.
Keep everything else unchanged.
```

## ComfyUI Setup

### Model Files

| File | Location | Size |
|------|----------|------|
| `qwen_image_fp8.safetensors` | `models/unet/` | ~20GB |
| `qwen_2.5_vl_7b_fp8_scaled.safetensors` | `models/text_encoders/` | ~7GB |
| `qwen_image_vae.safetensors` | `models/vae/` | ~100MB |
| `Qwen-Image-Lightning-4steps-V1.0.safetensors` | `models/loras/` | Optional |

### GGUF Versions (Lower VRAM)

| Variant | VRAM | Quality |
|---------|------|---------|
| Q8_0 | ~24GB | Best |
| Q5_K_M | ~16GB | Good |
| Q4_K_M | ~12GB | Acceptable |

### Custom Nodes

- **Comfyui-QwenEditUtils** - Editing utilities with mask support

## LoRA Configuration (ComfyUI)

**⚠️ IMPORTANT: LoRA ไม่มี Trigger Words**

Qwen Image Edit LoRAs ไม่ต้องใช้ trigger words พิเศษ เขียน prompt เป็นภาษาธรรมชาติได้เลย
ระบบจะ activate LoRA อัตโนมัติตามที่เปิดใช้งาน

### Available LoRAs

| LoRA | Purpose | When to Enable |
|------|---------|----------------|
| **Multiple-angles** | เปลี่ยนมุมกล้อง | Prompt เกี่ยวกับ camera angle (low/high angle, side view, etc.) |
| **consistence_edit** | รักษา consistency | ต้องการให้ผลลัพธ์คงเดิมมากที่สุด |
| **bfs_head_swap** | สลับหัว/หน้า | ใช้ 2 รูป - เอาหน้าจากรูป 1 ไปใส่รูป 2 |
| **clothes_tryon** | เปลี่ยนเสื้อผ้า | ใช้ 2 รูป - เอาเสื้อผ้าจากรูป 1 ไปใส่คนในรูป 2 |
| **Lightning-4steps** | เร่งความเร็ว (4 steps) | **Default ON** - ใช้เสมอเพื่อความเร็ว |
| **Lightning-8steps** | เร่งความเร็ว (8 steps) | ถ้า 4 steps ไม่ work ค่อยลอง 8 |

### Default Settings

- **เปิด:** Lightning-4steps เท่านั้น
- **ปิด:** LoRA อื่นๆ ทั้งหมด (เปิดตาม task)

### LoRA Selection by Task

| Task | LoRAs to Enable | Steps |
|------|-----------------|-------|
| **Basic edit** (แสง, สี, พื้นหลัง) | (none, ใช้ default) | 4 |
| **Camera angle change** | Multiple-angles | 4 |
| **Head/face swap** | bfs_head_swap | 4 |
| **Clothes change** | clothes_tryon | 4 |
| **High consistency** | consistence_edit | 4 |
| **Quality mode** | ปิด Lightning ทั้งคู่ | 20 |

### Speed vs Quality

| Mode | Lightning LoRA | Steps | Time | Use Case |
|------|----------------|-------|------|----------|
| **Fast** | 4-steps ON | 4 | ~10s | Iteration, testing |
| **Medium** | 8-steps ON | 8 | ~20s | ถ้า 4 steps ไม่ดีพอ |
| **Quality** | ทั้งคู่ OFF | 20 | ~50s | Final output |

### Multi-Image Editing

Qwen Image Edit รองรับ **1-3 รูป** สำหรับ reference:

| Images | Use Case | Example Prompt |
|--------|----------|----------------|
| **1 รูป** | Edit รูปเดียว | "Turn to side profile view" |
| **2 รูป** | Combine/swap elements | "Use face from image 1, pose from image 2" |
| **3 รูป** | Complex composition | "Combine elements from all three images" |

### Reference-Based Editing Best Practices

**⚠️ CRITICAL: อย่าบรรยายใบหน้าเมื่อใช้ reference image**

เมื่อใช้รูป reference สำหรับใบหน้า/ตัวคน:
- ❌ **ห้าม:** "A woman with curly hair, round face, wearing glasses..."
- ✅ **ถูกต้อง:** "Use the face from image 1" หรือ "Keep the person's appearance"

**เหตุผล:** Dual-path encoding ของ Qwen จะดึง visual features จากรูปโดยตรง การบรรยายซ้ำอาจทำให้เกิด conflict

**Pattern ที่แนะนำ:**
```
[Action/Change] + [Reference to which image] + [What to preserve]
```

**ตัวอย่าง:**
| Task | Prompt |
|------|--------|
| Face swap | "Replace face with the person from image 1. Keep pose and clothing." |
| Style transfer | "Apply the art style from image 2. Keep the subject unchanged." |
| Outfit change | "Dress in the outfit from image 2. Keep face and pose." |
| Pose transfer | "Adopt the pose from image 2. Keep the person's identity." |

### Prompt Tips for LoRA Tasks

**Camera Angle (Multiple-angles):**
```
Turn the camera to a low-angle view, looking up at the subject.
Keep appearance and clothing unchanged.
```

**Head Swap (bfs_head_swap):**

มี recommended prefix `h34d_sw4p:` ที่อาจช่วยให้ผลลัพธ์ดีขึ้น:

```
h34d_sw4p: replace the head of Picture 1 by the head from Picture 2,
strictly preserving the identity, facial features (eyes, nose, mouth),
and skin texture of Picture 2.
```

หรือแบบ simple (focus face only):
```
face swap face from Image 1 to Image 2. swap only the face and not the hair.
```

**Tips:**
- Image 1 = face source, Image 2 = body/pose
- High-quality input ไม่มี compression artifacts จะได้ผลดีกว่า

**Clothes Change (clothes_tryon):**
```
Dress the person in image 1 with the outfit from image 2.
Keep the original pose and background.
```

## Tips

1. **Prompt length:** 1-3 sentences optimal, paragraph OK
2. **Text in quotes:** For on-image text, use quotes and specify font
3. **Seed for iteration:** Lock seed to iterate on details
4. **CFG with Lightning:** ต้องใช้ CFG=1.0 เท่านั้น (fixed)
5. **CFG without Lightning:** 2.5-4.0 แนะนำ
6. **Lightning LoRA:** 4-step default, เปิด LoRA อื่นตาม task
7. **Start simple:** ลอง default ก่อน ค่อยเปิด LoRA เพิ่ม
8. **Quality for final:** ปิด Lightning + 20-40 steps สำหรับ final output
9. **Reference images:** อย่าบรรยายใบหน้าซ้ำ ให้ระบบดึงจากรูป

---

## Related Models

### Z-Image-Turbo (ไม่ใช่ Qwen)

| Aspect | Detail |
|--------|--------|
| **Type** | Text-to-Image (ไม่ใช่ Editing) |
| **Parameters** | 6B |
| **Speed** | ~1.5 seconds (8 steps) |
| **Use Case** | Fast iteration, concept exploration |

**สำคัญ:** Z-Image-Turbo เป็น text-to-image ไม่รองรับ image editing
ถ้าต้องการ edit รูป ใช้ Qwen-Image-Edit แทน

| Need | Use Model |
|------|-----------|
| Generate new image (fast) | Z-Image-Turbo |
| Edit existing image | Qwen-Image-Edit |
| High quality generation | Qwen-Image |
