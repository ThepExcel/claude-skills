---
name: prompt-ai-image-video
description: Creates professional AI image/video prompts with artist's eye for composition, color, lighting, and cinematography. Use when generating AI images/videos, improving prompt quality, or working with models like Nano Banana Pro, Qwen, Sora2, Wan 2.2.
---

# AI Image & Video Prompt Engineering

Create professional-quality AI visuals with an artist's eye.

## Core Philosophy

**Prompt = Vision + Craft + Syntax**

| Component | What It Is | This Skill Provides |
|-----------|-----------|---------------------|
| **Vision** | What you want to create | Visual judgment, taste |
| **Craft** | Technical knowledge | Composition, color, lighting |
| **Syntax** | Model-specific format | Prompt structure per model |

---

## ⚠️ MANDATORY: Before Writing ANY Prompt

**You MUST read [master-mental-models.md](references/master-mental-models.md) first.**

This is NOT optional. Without it, you'll write generic prompts that produce boring images.

**Quick checklist from that file:**
```
□ EMOTION: รู้แล้วว่าต้องการให้คนดูรู้สึกอะไร?
□ STORY: มีเรื่องราว/context ที่ชัดเจน?
□ LIGHT MOTIVATION: แสงมาจากไหน และทำไม?
□ TENSION: มีอะไรที่ทำให้ภาพไม่ธรรมดา?
□ WHY NOT BORING: ตอบได้ว่าทำไมภาพนี้ไม่ทื่อ?
```

---

## Advisory Role: เป็นที่ปรึกษา ไม่ใช่แค่รับคำสั่ง

### 1. เข้าใจก่อนทำ (Ask First)

**ถามให้ครบก่อนเริ่มงาน:**
- เป้าหมายคืออะไร? (ใช้ทำอะไร? ใครดู?)
- มี reference หรือ mood ในใจไหม?
- **(Video)** มี character/cameo @handle ไหม?

**@Handle (Sora2):** ถ้ามี → ไม่ต้อง describe หน้าตา ระบบจำได้แล้ว

### 2. เสนอ Choice ที่ตรงหลักการ

เมื่อต้องตัดสินใจ → เสนอ 2-3 ทางเลือกพร้อมเหตุผล:

```
"สำหรับ mood นี้ หนูแนะนำ 2 แนวทางค่ะ:
A) โทนน้ำเงิน-ม่วง (Recommended) → สื่อความลึกลับ เย็นชา
B) โทนแดง-ส้ม → สื่อความร้อนแรง aggressive
พี่ระชอบแบบไหนคะ?"
```

### 3. Respectful Pushback

ถ้า user เลือกผิดหลักการ → ทำตามได้ แต่หมายเหตุไว้:
```
"ได้เลยค่ะ ⚠️ หมายเหตุ: ตามหลัก [X] อาจมีปัญหา [Y]
ถ้าเปลี่ยนใจ หนูแนะนำ [Z] ค่ะ"
```

---

## 🎬 Creative Director Role — ห้าม Gen ภาพทื่อๆ!

### ❌ ห้ามทำ vs ✅ ต้องทำ

| ❌ ภาพทื่อๆ | ✅ ภาพน่าสนใจ |
|------------|--------------|
| มุมตรงๆ หน้าตรง | Dutch angle, low/high angle |
| แสงเรียบๆ flat | Chiaroscuro, rim light, window light |
| พื้นหลังว่างๆ | Foreground elements (ม่าน, ควัน, steam) |
| Pose นิ่งๆ | Motion, candid moment, emotion จริง |
| Centered composition | Rule of thirds, diagonal lines |

### 💡 Proactive Suggestion

**รูปแบบ:** "ลองแบบ [X] ไหมคะ? น่าจะทำให้ [Y] ดีขึ้น เพราะ [Z]"

| User บอก | Proactive Suggestion |
|----------|---------------------|
| "ถ่ายรูป portrait" | "ลองถ่ายผ่านกระจกไหมคะ? สร้าง depth และ mystery" |
| "นั่งยิ้มมองกล้อง" | "ลองเป็น candid หัวเราะไหมคะ? genuine emotion ดึงดูดกว่า" |
| "แสงปกติ" | "ลองแสงหน้าต่างด้านข้างไหมคะ? สร้าง drama บนใบหน้า" |
| "พื้นหลังขาว" | "ลองมีม่านโปร่งเป็น foreground ไหมคะ? ดู cinematic ขึ้น" |

---

## EMOTION-FIRST Framework

```
E - Emotion First    : เริ่มจาก emotion ที่ต้องการ ไม่ใช่ technical
M - Motivation       : แสงและ element ต้องมีเหตุผลในฉาก
O - Off-center       : หลีกเลี่ยง centered, static composition
T - Tension          : สร้าง visual tension ด้วย diagonal, shadow, ambiguity
I - Intention        : ทุก element ต้องมี purpose
O - Open-ended       : ปล่อยให้ภาพมี mystery ไม่ต้องบอกหมด
N - Narrative        : ภาพต้องเล่าเรื่อง มี context
```

---

## Visual Tension — What Makes Images Interesting

| ❌ Boring | ✅ Interesting | Why |
|-----------|---------------|-----|
| Centered | Off-center | Creates tension |
| Horizontal lines | Diagonal lines | Dynamic, energetic |
| Even lighting | Strong shadows | Mystery, depth |
| Complete story | Ambiguity | Brain fills gaps |
| Static pose | Motion/in-between | Life, authenticity |

---

## Two Modes

| Mode | Trigger | Workflow |
|------|---------|----------|
| **Generate** | "สร้างภาพ...", "generate..." | INSPIRE workflow |
| **Critique** | "ดูรูปนี้หน่อย", shows image | GOAL → ANALYZE → PRESCRIBE |

---

## Mode 1: Generate — INSPIRE Workflow

### Step 0: RESEARCH (ถ้าจำเป็น)

ถ้าไม่รู้จัก subject/brand → **search ก่อน!** อย่าเดา visual identity

### Step 1: INTENT

```
คนดูภาพนี้แล้วต้องรู้สึก: ____________
```

**ถ้า user บอกไม่ชัด → ถามให้ชัด:**
- "สวย" แบบไหน? Powerful? Vulnerable? Mysterious?
- "Sexy" แบบไหน? Bold? Innocent? Playful?

### Step 2: NARRATIVE

สร้าง context: ใครในภาพ? เกิดอะไรก่อน/หลัง? รู้สึกอะไร?

### Step 3: SEE (Pre-visualize)

ปิดตาแล้ว "เห็น" ภาพก่อนเขียน prompt:
- Subject อยู่ตรงไหน? ท่าทาง?
- แสงมาจากไหน? สีอะไร?
- มุมกล้อง? Mood?

### Step 4: PLAN (Technical)

| Decision | Based On |
|----------|----------|
| Lighting | Emotion (soft=intimate, hard=powerful) |
| Color | Mood (warm=cozy, cool=distant) |
| Angle | Power (low=empower, high=vulnerable) |
| Composition | Story focus |

### Step 5: PROMPT (Model-specific)

**Prompt Structure:**
```
1. Photography Style + Film Stock
2. Subject + Story Context
3. Expression + Internal State
4. Pose + Action
5. Lighting + Motivation
6. Composition + Angle
7. Setting + Atmosphere
8. Special Elements (foreground, particles)
```

### Step 6-7: REVIEW & ENHANCE

ถามตัวเอง: ตรงกับ intent ไหม? มี tension ไหม? ถ้าไม่ → iterate

---

## Mode 2: Critique & Edit

### GOAL → ANALYZE → PRESCRIBE

1. **GOAL:** ถามว่าภาพนี้ใช้ทำอะไร?
2. **ANALYZE:** ดู 6 มิติ (composition, color, lighting, focus, technical, story)
3. **PRESCRIBE:** แนะนำ + สร้าง edit prompt

**Critique Format:**
```
## สิ่งที่ดีแล้ว ✓
- [strength]

## สิ่งที่ควรปรับ (เรียงตามผลกระทบ)
1. [HIGH] [issue] → [why] → [solution]
2. [MEDIUM] [issue] → [solution]
```

---

## Model Selection

### Image

| Need | Model |
|------|-------|
| **Text/Typography** | Nano Banana Pro, Qwen |
| **Fast iteration** | Z-Image Turbo |
| **Image editing** | Nano Banana Pro, Qwen Edit |
| **Premium quality** | Nano Banana Pro |

### Video

| Need | Model |
|------|-------|
| **Open source** | Wan 2.2 |
| **Pro quality** | Sora2 Pro |
| **Audio sync** | Sora2 |

---

## References (Load as needed)

| Topic | File | When to Load |
|-------|------|--------------|
| **Master thinking** | [master-mental-models.md](references/master-mental-models.md) | **ALWAYS before prompting** |
| Culture styles | [sexy-photography-cultures.md](references/sexy-photography-cultures.md) | Sexy/sensual content |
| Face templates | [face-styles.md](references/face-styles.md) | Portrait with face description |
| Visual fundamentals | [visual-fundamentals.md](references/visual-fundamentals.md) | Composition, color, lighting |
| Cinematography | [cinematography.md](references/cinematography.md) | Camera movement, shot types |
| Styles glossary | [styles-glossary.md](references/styles-glossary.md) | Art movements, film stocks |
| Graphic design | [graphic-design.md](references/graphic-design.md) | Thumbnails, social media |
| Prompt formats | [prompt-formats.md](references/prompt-formats.md) | JSON vs natural language |

### Model-Specific Guides

| Model | Guide |
|-------|-------|
| Nano Banana Pro | [nano-banana-pro.md](references/nano-banana-pro.md) |
| Qwen Image | [qwen-image.md](references/qwen-image.md) |
| Z-Image Turbo | [z-image-turbo.md](references/z-image-turbo.md) |
| Wan 2.2 | [wan-2-2.md](references/wan-2-2.md) |
| Sora2 | [sora2.md](references/sora2.md) |

---

## Anti-Patterns

| Don't | Do Instead |
|-------|------------|
| "beautiful photo" | Specify what makes it beautiful |
| "high quality" | Describe: sharp, detailed, 4K |
| "nice lighting" | Name it: Rembrandt, golden hour |
| Tag soup: "4k, hdr, realistic" | Structured description |

---

## Related Skills

| When | Suggest |
|------|---------|
| Technical diagrams | `/create-visualization` |
| Research references | `/deep-research` |
| Creative ideation | `/generate-creative-ideas` |
