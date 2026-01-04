# Z-Image Turbo (Tongyi-MAI)

## Overview

| Aspect | Detail |
|--------|--------|
| **Provider** | Tongyi-MAI (Alibaba) |
| **Parameters** | 6B |
| **Pricing** | $0.005/megapixel (cheapest) |
| **Speed** | Sub-second generation |
| **License** | Open Source |

## Philosophy

**"Think like a film director, not a creative writer"**

Camera angles, lighting, composition - use technical terminology.

## Key Constraints

| Feature | Support |
|---------|---------|
| **Negative Prompts** | ❌ NOT supported |
| **Steps** | 4-8 (distilled model) |
| **Bilingual** | English + Chinese |
| **Text Rendering** | Supported |

**Important:** All constraints must go in positive prompt. No negative prompts!

## Prompt Structure

```
[Subject] + [Style modifiers] + [Quality boosters] + [Compositional directives]
```

### Six Categories

1. **Subject terms** - Main focus
2. **Style modifiers** - Artistic style
3. **Quality boosters** - Technical quality
4. **Repeating terms** - Emphasis (sparingly)
5. **Magic terms** - Model-specific triggers
6. **Compositional directives** - Framing, angle

## Prompt Template

```
[Subject description in detail].
[Setting and environment].
[Lighting: specific type and direction].
[Camera: angle, lens, depth of field].
[Style: artistic reference or genre].
[Quality: sharp focus, high detail, clean].
```

## Example Prompts

### Portrait
```
Young Chinese woman in red Hanfu, intricate embroidery.
Impeccable makeup, red floral forehead pattern.
Elaborate high bun, golden phoenix headdress, red flowers, beads.
Soft studio lighting, shallow depth of field.
Professional portrait photography, sharp focus, high detail.
```

### Cinematic
```
Wong Kar-wai film style, lonely man smoking cigarette
in narrow Hong Kong hallway, 1990s.
Greenish fluorescent lighting, heavy shadows, moody atmosphere.
35mm film grain, anamorphic lens flare.
Cinematic composition, melancholic mood.
```

### Product
```
Luxury perfume bottle on reflective black surface.
Dramatic rim lighting from behind, soft fill from front.
Clean minimal composition, negative space on left.
Commercial product photography, sharp focus, no reflections.
High-end brand aesthetic, sophisticated.
```

## Replacing Negative Prompts

Since negatives don't work, include positive alternatives:

| Instead of Negative | Use Positive |
|--------------------|--------------|
| "no blur" | "sharp focus, crisp details" |
| "no distortion" | "accurate proportions, correct anatomy" |
| "no noise" | "clean, noise-free, smooth" |
| "no watermark" | "clean image, no text overlays" |
| "no bad hands" | "well-formed hands, correct fingers" |

## Director Mindset

Think in terms of:
- **Angles:** "low angle looking up", "eye level", "bird's eye"
- **Lighting:** "Rembrandt lighting", "rim light", "soft diffused"
- **Lens:** "85mm portrait lens", "wide angle 24mm", "telephoto compression"
- **Composition:** "rule of thirds", "centered symmetry", "leading lines"

## ComfyUI Setup

**Native support** in ComfyUI

### Key Settings

| Setting | Recommended |
|---------|-------------|
| Steps | 4-8 |
| CFG | Not applicable (distilled) |
| Resolution | Square HD, Portrait, Landscape presets |

### Image Sizes

- `square_hd` - 1024x1024
- `square` - 512x512
- `portrait_4_3` - 768x1024
- `portrait_16_9` - 576x1024
- `landscape_4_3` - 1024x768
- `landscape_16_9` - 1024x576

## Tips

1. **Keep focused:** 3-5 key visual concepts max
2. **Be specific:** No vague words like "beautiful" or "nice"
3. **Technical terms:** Use photography/cinematography vocabulary
4. **Anatomy note:** Hands/fingers significantly improved
5. **Speed:** Great for iteration and prototyping
