---
name: ai-image-video-prompt
description: |
  Professional AI image/video prompt engineering with visual artist's eye. Creates prompts that produce stunning, professional-quality visuals by understanding composition, color theory, lighting, cinematography, and model-specific techniques. Use when: (1) User wants to generate AI images/videos, (2) "create image of...", "generate video...", (3) Needs help with prompts for Nano Banana Pro, Qwen Image, Z-Image Turbo, Wan 2.2, Sora2, or similar models, (4) Wants to improve visual quality of AI outputs.
---

# AI Image & Video Prompt Engineering

Create professional-quality AI visuals with an artist's eye.

## Core Philosophy

**Prompt = Vision + Craft + Syntax**

| Component | What It Is | This Skill Provides |
|-----------|-----------|---------------------|
| **Vision** | What you want to create | Visual judgment, taste |
| **Craft** | Technical knowledge | Composition, color, lighting, cinematography |
| **Syntax** | Model-specific format | Prompt structure per model |

---

## Two Modes

| Mode | Trigger | Workflow |
|------|---------|----------|
| **Generate** | "สร้างภาพ...", "generate image of..." | VISUALIZE → COMPOSE → PROMPT |
| **Critique & Edit** | "ดูรูปนี้หน่อย", "ปรับปรุงรูปนี้", shows image | GOAL → ANALYZE → DIAGNOSE → PRESCRIBE |

---

## Mode 1: Generate

### Workflow: RESEARCH → VISUALIZE → COMPOSE → PROMPT

### Step 0: RESEARCH (Know your subject first)

**ถ้าไม่รู้จัก subject/brand/concept → ต้อง search ก่อน!**

Before creating any prompt, ask yourself:
- Do I know this brand's visual identity? (logo, colors, style)
- Do I understand this concept/product? (what it looks like, key features)
- Are there existing visual references I should match?

**Examples that require research:**
| Request | What to Search |
|---------|----------------|
| "สร้างภาพ Claude Skills" | Claude brand colors (#da7756), Skills icon (🧩), SKILL.md visual |
| "ภาพสำหรับ ThepExcel" | ThepExcel logo, brand colors, existing style |
| "Midjourney style image" | Midjourney's typical aesthetic, common outputs |
| "Apple product shot" | Apple's photography style, lighting, backgrounds |

**How to research:**
1. Use `WebSearch` to find brand guidelines, visual identity
2. Look for official logos, color codes, design systems
3. Find example images that represent the brand/concept
4. Ask user if they have specific references

**IMPORTANT:** Don't guess visual identity. Wrong colors or misrepresented brands look unprofessional.

---

### Step 1: ASK PROMPT FORMAT

**ถาม user ว่าต้องการ prompt แบบไหน:**

```
"พี่ระต้องการ prompt แบบไหนคะ?
1. Natural Language - บรรยายเป็นประโยค เหมาะกับงาน creative, exploration
2. JSON Structured - แยกเป็น field ชัดเจน เหมาะกับงาน production, batch, ต้องการความแม่นยำ"
```

| Format | Best For | Pros | Cons |
|--------|----------|------|------|
| **Natural Language** | Creative exploration, emotional scenes, one-off images | Flexible, nuanced, evocative | Less consistent, harder to reproduce |
| **JSON Structured** | Production work, batch generation, precise control | Repeatable, consistent, machine-friendly | Less creative freedom, rigid |

**JSON Prompt Example:**
```json
{
  "subject": "Professional woman, 30s, confident smile",
  "setting": "Modern office with large windows",
  "lighting": "Soft natural light from left, subtle rim light",
  "composition": "Rule of thirds, subject on right",
  "camera": "85mm f/1.8, shallow depth of field",
  "style": "Corporate editorial, warm tones",
  "mood": "Professional yet approachable"
}
```

**Natural Language Equivalent:**
```
Professional woman in her 30s with a confident smile, standing in a modern
office with large windows. Soft natural light streams from the left with
subtle rim lighting. Composed using rule of thirds with subject on the right.
Shot with 85mm f/1.8 for shallow depth of field. Corporate editorial style
with warm tones. Professional yet approachable mood.
```

**Default:** If user doesn't specify, use Natural Language for creative work, JSON for production/batch.

---

### Step 2: VISUALIZE (What's the final image?)

Before writing any prompt, answer:

```
1. SUBJECT: Who/what is the main focus?
2. MOOD: What emotion should it evoke?
3. STYLE: Photorealistic? Artistic? Cinematic?
4. PURPOSE: Where will this be used?
```

### Step 3: COMPOSE (Apply visual fundamentals)

| Element | Quick Decision | Reference |
|---------|----------------|-----------|
| **Composition** | Rule of thirds? Symmetry? Leading lines? | [visual-fundamentals.md](references/visual-fundamentals.md) |
| **Color** | Warm/cool? Complementary? Monochrome? | [visual-fundamentals.md](references/visual-fundamentals.md) |
| **Lighting** | Golden hour? Studio? Dramatic? | [visual-fundamentals.md](references/visual-fundamentals.md) |
| **Lens** | Wide (context)? Tele (compression)? | [visual-fundamentals.md](references/visual-fundamentals.md) |
| **Angle** | Eye level? Low (power)? High (vulnerable)? | [visual-fundamentals.md](references/visual-fundamentals.md) |

**For thumbnails/social media:** See [graphic-design.md](references/graphic-design.md)

### Step 4: PROMPT (Model-specific syntax)

| Model | Best For | Guide |
|-------|----------|-------|
| **Nano Banana Pro** | Text, infographics, editing | [nano-banana-pro.md](references/models/nano-banana-pro.md) |
| **Qwen Image** | Text rendering, Chinese | [qwen-image.md](references/models/qwen-image.md) |
| **Z-Image Turbo** | Fast, budget | [z-image-turbo.md](references/models/z-image-turbo.md) |
| **Wan 2.2** | Video, motion | [wan-2-2.md](references/models/wan-2-2.md) |
| **Sora2** | Pro video, audio | [sora2.md](references/models/sora2.md) |

---

## Mode 2: Critique & Edit

### Workflow: GOAL → ANALYZE → DIAGNOSE → PRESCRIBE

When user shows an image and wants to improve it:

### Step 1: GOAL (ถามเป้าหมายก่อน)

**ต้องถามก่อนวิจารณ์:**

```
"ภาพนี้จะใช้ทำอะไรคะ?"
"อยากให้ออกมาเป็นแบบไหน?"
"มีอะไรที่รู้สึกว่ายังไม่ใช่ไหม?"
```

| Goal Type | Focus Areas |
|-----------|-------------|
| **Commercial/Product** | Clean, professional, brand consistency |
| **Social Media** | Eye-catching, scroll-stopping, mood |
| **Thumbnail** | Readable text, high contrast, face expression, CTR |
| **Portfolio/Art** | Technical excellence, artistic vision |
| **Editorial** | Story, emotion, narrative |
| **Personal** | Subject flattering, memorable moment |

### Step 2: ANALYZE (วิเคราะห์ 6 มิติ)

| Dimension | Questions to Ask |
|-----------|------------------|
| **Composition** | Subject placement? Balance? Leading lines? Clutter? |
| **Color** | Harmony? Temperature? Matches mood? Distracting? |
| **Lighting** | Direction? Quality? Flattering? Mood-appropriate? |
| **Focus/DOF** | Sharp where needed? Distracting background? |
| **Technical** | Exposure? Noise? Sharpness? Resolution? |
| **Story/Mood** | Does it convey intended emotion? Authentic? |
| **Typography** | (For thumbnails) Readable? Hierarchy? Contrast? Position? |

### Step 3: DIAGNOSE (ระบุปัญหา + จัดลำดับ)

**Format:**

```
## สิ่งที่ดีแล้ว ✓
- [strength 1]
- [strength 2]

## สิ่งที่ควรปรับ (เรียงตามผลกระทบ)
1. [HIGH IMPACT] [issue] → [why it matters for goal]
2. [MEDIUM] [issue] → [why]
3. [LOW] [issue] → [optional improvement]
```

### Step 4: PRESCRIBE (แนะนำ + สร้าง Edit Prompt)

**Two paths:**

| Path | When | Output |
|------|------|--------|
| **Reshoot** | Fundamental issues (lighting, angle) | Shot recommendations |
| **Edit** | Fixable post-processing | Edit prompt for AI model |

**Edit Prompt Template:**

```
[ACTION]: [specific change]
[TARGET]: [what to affect]
[PRESERVE]: [what to keep unchanged]
[STYLE]: [desired look after edit]
```

**Example Edit Prompts:**

| Issue | Edit Prompt |
|-------|-------------|
| Distracting background | "Blur the background to create bokeh effect, keep subject sharp" |
| Wrong color temp | "Warm up the image, add golden hour color grading" |
| Flat lighting | "Add dramatic side lighting, increase contrast in shadows" |
| Cluttered | "Remove the [object] in background, extend clean background" |
| Wrong mood | "Make the atmosphere more moody and cinematic, add blue tones" |

### Critique Voice

**เป็นกลาง + สร้างสรรค์:**
- ชมก่อน → บอกจุดแข็ง
- วิจารณ์เพื่อพัฒนา → ไม่ใช่เพื่อ criticize
- ให้ทางออก → ไม่ใช่แค่บอกปัญหา
- เคารพเป้าหมายของ user → ไม่ยัดเยียด taste ของตัวเอง

---

## Model Selection Guide

### Image Generation

| Need | Model | Why |
|------|-------|-----|
| **Text/Typography** | Nano Banana Pro, Qwen Image | Best text rendering |
| **Fast iteration** | Z-Image Turbo | $0.005/MP, sub-second |
| **Image editing** | Qwen Image Edit, Nano Banana Pro | In-painting, style transfer |
| **Budget production** | Z-Image Turbo | Cheapest per image |
| **Premium quality** | Nano Banana Pro | Best semantic understanding |

### Video Generation

| Need | Model | Why |
|------|-------|-----|
| **Open source/Local** | Wan 2.2 | Free, ComfyUI native |
| **Quick clips** | Wan 2.2 5B | Runs on 4090 |
| **Pro quality** | Sora2 Pro | Best fidelity |
| **Audio sync** | Sora2 | Native audio generation |
| **Fast iteration** | Sora2 (standard) | Quick turnaround |

---

## Prompt Templates

### Image: Professional Portrait

```
[SUBJECT]: Professional headshot of [description], [age], [ethnicity]
[LIGHTING]: Rembrandt lighting with soft fill, subtle rim light
[COMPOSITION]: Centered, shallow depth of field, clean background
[STYLE]: Editorial photography, Kodak Portra 400
[TECHNICAL]: 85mm f/1.8, studio lighting, 4K resolution
```

### Image: Cinematic Landscape

```
[SCENE]: [Location description] at [time of day]
[COMPOSITION]: Rule of thirds, leading lines toward [focal point]
[ATMOSPHERE]: [Weather], [mood] atmosphere
[COLOR]: [Color palette], [film stock look]
[TECHNICAL]: Wide angle 24mm, deep focus, anamorphic 2.35:1
```

### Video: Cinematic Scene (Wan 2.2 / Sora2)

```
[OPENING]: Camera [movement] revealing [scene description]
[SUBJECT]: [Character/object] [action with motion verbs]
[ENVIRONMENT]: [Setting] with [atmospheric details]
[CAMERA]: [Shot type], [movement], [speed]
[ATMOSPHERE]: [Lighting], [color palette], [mood]
[STYLE]: Cinematic film scene, [film stock], [director reference]
```

---

## References

| Topic | File |
|-------|------|
| Composition, Color, Lighting, Lens | [visual-fundamentals.md](references/visual-fundamentals.md) |
| Camera Movement, Shot Types | [cinematography.md](references/cinematography.md) |
| Art Movements, Film Stocks | [styles-glossary.md](references/styles-glossary.md) |
| Thumbnails, Social Media | [graphic-design.md](references/graphic-design.md) |
| JSON vs Natural Language Prompts | [prompt-formats.md](references/prompt-formats.md) |

---

## Anti-Patterns

| Don't | Do Instead |
|-------|------------|
| "beautiful photo" | Specify what makes it beautiful |
| "high quality" | Describe the quality (sharp, detailed, 4K) |
| "nice lighting" | Name the lighting (Rembrandt, golden hour) |
| Tag soup: "4k, hdr, realistic" | Structured description |
| Vague colors: "colorful" | Specific: "teal and orange palette" |

---

## Iteration Strategy

1. **Start simple** → Core subject + style
2. **Add specifics** → Lighting, composition, color
3. **Test variations** → Different angles, moods, styles
4. **Use seed** → Lock good results, iterate details
5. **Combine strengths** → Image → Video pipeline

---

## Related Skills

| When | Suggest |
|------|---------|
| Technical diagrams (physics, math, flowcharts) | `/visualization` - Matplotlib/Manim for STEM |
| Research visual references | `/deep-research` - find inspiration |
| Creative ideation | `/creativity` - brainstorm concepts |

**Note:** Use `/visualization` for technical diagrams (FBD, plots, flowcharts). Use this skill for AI-generated realistic/artistic images and videos.
