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

| Parameter | Range | Notes |
|-----------|-------|-------|
| **CFG/Guidance** | 4-5 optimal | Lower = creative, Higher = strict |
| **Seed** | Any integer | Same seed + prompt = same output |
| **Steps** | 20-50 | More = detail, slower |

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

## Tips

1. **Prompt length:** 1-3 sentences optimal, paragraph OK
2. **Text in quotes:** For on-image text, use quotes and specify font
3. **Seed for iteration:** Lock seed to iterate on details
4. **CFG 4-5:** Sweet spot for quality vs creativity
5. **Lightning LoRA:** 4-step generation for speed
