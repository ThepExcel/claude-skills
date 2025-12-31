# Wan 2.2 (Alibaba)

## Overview

| Aspect | Detail |
|--------|--------|
| **Provider** | Alibaba Tongyi Lab |
| **Architecture** | MoE (Mixture of Experts) + DiT |
| **Variants** | 1.3B (fast), 5B (4090), 14B (best) |
| **Resolution** | 480p to 1080p (native) |
| **Duration** | 5-10 seconds (up to 1 minute with extensions) |
| **License** | Apache 2.0 (Open Source) |
| **ComfyUI** | Native support |

## Philosophy

**"Think like a cinematographer, write like a novelist"**

Wan 2.2 excels with descriptive, scene-based prompts. Describe what happens cinematically.

## Key Capabilities

| Feature | Wan 2.2 Support |
|---------|-----------------|
| Text-to-Video | Yes |
| Image-to-Video | Yes |
| First/Last Frame Control | Yes (14B) |
| Camera Control | Yes (with training) |
| Audio | No (add separately) |

## Prompt Structure

**Optimal length:** 80-120 words

```
[SCENE]: Describe the environment and setting
[SUBJECT]: Who/what is the focus, their appearance
[ACTION]: What happens, movement, dynamics
[CAMERA]: Movement, angle, lens characteristics
[ATMOSPHERE]: Lighting, mood, color palette
[STYLE]: Cinematic reference, film stock, aesthetic
```

## Example Prompts

### Cinematic Nature

```
Slow-motion close-up of a golden eagle diving through
morning mist above a pine forest. Sunlight filters through
clouds creating god rays. The eagle's feathers ripple in
the wind as it descends. Camera tracks the bird from
above, then rotates to side view. Natural lighting,
documentary style, David Attenborough production value.
Shallow depth of field, 4K cinematic quality.
```

### Urban Scene

```
Rainy night in Tokyo's Shibuya crossing. Neon lights
reflect on wet pavement creating colorful streaks.
A lone figure with transparent umbrella walks against
the crowd. Camera follows from behind, slowly dollying
forward. Shallow depth of field isolates the subject.
Cyberpunk aesthetic, Wong Kar-wai color palette.
Cinestill 800T film look, slow motion 48fps.
```

### Character Animation

```
Young woman in flowing white dress stands on cliff edge
overlooking stormy ocean. Wind catches her hair and dress,
creating dramatic movement. She raises her arms slowly.
Camera orbits around her in slow 360-degree arc.
Golden hour backlighting creates silhouette with rim light.
Epic, emotional, cinematic. Terrence Malick visual style.
```

### Product Shot

```
Luxury perfume bottle slowly rotates on reflective black
surface. Dramatic rim lighting from behind highlights
the glass contours. Golden liquid inside catches light.
Subtle mist drifts past. Camera slowly pushes in.
High-end commercial photography style.
Clean, minimal, sophisticated aesthetic.
```

## ComfyUI Setup

### Custom Nodes

- **Comfyui-WanMoE** - Official Wan 2.2 nodes
- **ComfyUI-VideoHelperSuite** - Video I/O utilities

### Model Files

| Model | VRAM | Quality | Speed |
|-------|------|---------|-------|
| wan2.2-1.3b | ~8GB | Fast iteration | 2x faster |
| wan2.2-5b | ~16GB | Production | Standard |
| wan2.2-14b | ~24GB+ | Best quality | Slower |

### Recommended Workflow

```
1. Load Wan 2.2 model (choose variant by VRAM)
2. Connect text prompt
3. (Optional) Add image input for i2v
4. Set resolution and duration
5. Sample with appropriate steps (25-50)
6. Decode to video
```

### Key Parameters

| Parameter | Range | Notes |
|-----------|-------|-------|
| **Steps** | 25-50 | More = better quality |
| **CFG** | 7-9 | Higher = more prompt adherence |
| **Resolution** | 480p, 720p, 1080p | Match to model variant |
| **Duration** | 49-97 frames | ~2-4 seconds at 24fps |
| **Seed** | Any | Lock for consistency |

## Image-to-Video (I2V)

Wan 2.2 supports starting from an image:

```
[IMAGE]: [Image will be used as first frame]
[MOTION]: Describe what movement should happen
[CAMERA]: How camera should move
[ATMOSPHERE]: Mood and lighting changes
```

**Example I2V Prompt:**

```
The woman in the photo slowly turns her head toward camera.
Wind begins to blow her hair gently. A subtle smile forms.
Camera holds steady, medium close-up.
Soft natural lighting, warm afternoon tones.
Cinematic film grain, slight lens vignette.
```

## First/Last Frame Control (14B)

Generate video between two key frames:

```
First frame: [description of starting state]
Last frame: [description of ending state]
Transition: [how it morphs/moves between states]
```

## Motion Verbs

**Essential for good video output:**

| Category | Verbs |
|----------|-------|
| **Slow** | drifts, floats, glides, hovers, sways |
| **Fast** | rushes, darts, bursts, races, dashes |
| **Organic** | ripples, flows, pulses, breathes, blooms |
| **Mechanical** | rotates, pivots, extends, retracts |
| **Emotional** | trembles, hesitates, surges, collapses |

## Camera Movement Keywords

| Movement | Keywords |
|----------|----------|
| **Static** | "camera holds still", "locked shot" |
| **Pan** | "camera pans left/right", "horizontal sweep" |
| **Tilt** | "camera tilts up/down", "vertical sweep" |
| **Dolly** | "camera pushes in", "camera pulls back" |
| **Orbit** | "camera orbits around", "360 rotation" |
| **Crane** | "camera rises", "crane up/down" |
| **Tracking** | "camera follows", "tracking shot" |
| **Handheld** | "handheld shake", "documentary style" |

## Tips

1. **Be specific about motion** - Use dynamic verbs, not static descriptions
2. **Describe camera explicitly** - Model needs clear camera guidance
3. **Layer the scene** - Foreground, midground, background activity
4. **Include timing cues** - "slowly", "suddenly", "gradually"
5. **Reference film styles** - Director names, film stocks, genres
6. **Use I2V for consistency** - Start from AI-generated or real image
7. **Match resolution to VRAM** - Don't try 1080p on 8GB GPU

## Limitations

| Limitation | Workaround |
|------------|------------|
| No native audio | Add audio in post-processing |
| 5-10 second clips | Use video extension techniques |
| Text rendering | Burn in text in post |
| Specific faces | Use face swap tools after |
| Physics accuracy | Multiple generations, pick best |

## Prompt Checklist

```
□ Scene/environment described
□ Subject appearance detailed
□ Specific motion verbs used
□ Camera movement specified
□ Lighting/mood included
□ Style reference added
□ 80-120 words length
□ Timing cues present
```
