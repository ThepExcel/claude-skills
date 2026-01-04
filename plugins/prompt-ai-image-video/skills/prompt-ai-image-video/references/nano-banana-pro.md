# Nano Banana Pro (Google)

## Overview

| Aspect | Detail |
|--------|--------|
| **Provider** | Google (via fal.ai) |
| **Base** | Gemini 3 Pro |
| **Pricing** | $0.13-0.24/image |
| **Resolution** | Up to 4K native |
| **Strengths** | Text rendering, semantic understanding, multi-image reference |

## Philosophy

**"Think like a Creative Director, not a keyword spammer"**

Nano Banana Pro is a "thinking" model - it understands intent, physics, and composition. Don't use tag soup.

## ICS Framework

```
Image type + Content + Style
```

| Component | Description | Example |
|-----------|-------------|---------|
| **Image** | Asset type | poster, infographic, diagram, portrait |
| **Content** | Subject matter | source data, characters, scene |
| **Style** | Visual approach | survival guide, McKinsey, comic |

## Prompt Template

```
Create a [ASSET TYPE: poster/infographic/storyboard/product ad/character sheet]
for [AUDIENCE/PLATFORM].

[Detailed content description]

Use clean grid alignment, consistent margins, readable typography.
Keep text crisp and readable.
No watermarks, no random logos, no distorted hands/faces.
Keep composition clean with whitespace and safe margins.
```

## Key Capabilities

### Text Rendering
- Best-in-class text in images
- 10+ languages supported
- Calligraphy, fonts, typography
- Prompt: "clear legible text reading '[TEXT]'"

### Multi-Image Reference
- Up to 14 reference images
- Character consistency
- Style transfer
- Prompt: "based on the reference images provided..."

### Image Editing
- In-painting (add/remove objects)
- Restoration (fix old photos)
- Colorization (B&W to color)
- Style swapping

## ComfyUI Integration

**Node:** ComfyUI Partner Nodes (native) or `ComfyUI-NanoBanano`

**Access:** Templates → Nano Banana Pro

**Note:** Requires API key (fal.ai)

## Example Prompts

### Infographic
```
Create a professional infographic explaining the water cycle
for high school science students.
Use clean flat design, blue color palette, clear icons.
Include labels for evaporation, condensation, precipitation.
Readable typography, modern educational style.
```

### Character Sheet
```
Character design sheet for a cyberpunk hacker, female, 20s.
Include front view, side view, and back view.
Neon accent colors, tech-wear clothing, augmented reality glasses.
Clean white background, consistent proportions across views.
Style: anime-influenced concept art.
```

### Product Photo
```
Professional product photo of a minimalist watch
on a marble surface with soft studio lighting.
Clean composition, shallow depth of field.
Luxury brand aesthetic, neutral color palette.
No text, no watermarks, commercial quality.
```

## Common Mistakes

| Don't | Do |
|-------|-----|
| "4k, realistic, beautiful, high quality" | Describe what makes it quality |
| Keyword spam | Structured sentences |
| Vague: "nice lighting" | Specific: "soft Rembrandt lighting" |
| Skip context | Include purpose and audience |

## Editing Prompts

For image editing mode:

```
[ACTION]: Remove the background clutter
[KEEP]: Subject and lighting unchanged
[RESULT]: Clean minimal background
```

```
Change the time of day to golden hour.
Warm the color temperature.
Add soft lens flare from the sun.
Keep the subject and composition unchanged.
```
