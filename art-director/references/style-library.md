# Style Library — Reusable Style Profiles

Battle-tested style recipes with proven prompts, color formulas, and scene guides.

## How to Use

### When generating a set or series:

1. **Check library first** — does a matching profile exist?
2. **Load profile** — read the style file from `references/`
3. **Apply constants** — use Face Constant, Color Formula, Style DNA verbatim
4. **Pick from scene/pose lists** — don't invent, use what's proven to work
5. **Follow the prompt template** — fill in the blanks

### When to create a new profile:

- After generating 5+ images in a style with consistent results
- When a style fusion produces something worth repeating
- When user develops a "signature look" they want to reuse

---

## Style Profiles Index

| Profile | Fusion | Subject | Mood |
|---------|--------|---------|------|
| [bourdin-newton-orange](style-bourdin-newton-orange.md) | Guy Bourdin x Helmut Newton | East Asian idol, editorial | Sexy, powerful, surreal |

---

## Style Mixing System

### Why Mix Styles?

Single photographer reference = predictable. Two complementary references = unique.

**Rule:** Pick 2 photographers with **complementary** strengths:

| Photographer A | Photographer B | Fusion Result |
|---------------|----------------|---------------|
| Bourdin (color, surreal) | Newton (power, shadow) | Editorial sexy with graphic punch |
| Von Unwerth (playful) | Lindbergh (raw, B&W) | Candid intimacy, authentic |
| Testino (warm glamour) | Walker (fantasy) | Luxurious dreamscape |
| Gravure (innocent) | Newton (power) | Cute + confident tension |
| K-Beauty (clean) | Bourdin (color) | Fresh face, saturated world |

### How to Mix

```
1. PICK dominant source (60-70%) — drives lighting + composition
2. PICK accent source (30-40%) — adds flavor via color/mood/pose
3. DEFINE which elements come from which:
   - Lighting: [source A or B]
   - Color palette: [source A or B]
   - Pose language: [source A or B]
   - Composition: [source A or B]
4. TEST with 3-5 images → keep what works, drop what clashes
5. DOCUMENT as profile if results are good
```

### Anti-Patterns

| Don't | Why |
|-------|-----|
| Mix 3+ photographers | Dilutes identity, becomes generic |
| Mix similar styles (Newton + Lindbergh) | Both B&W dramatic — no contrast, no fusion |
| Mix without defining which element from which | Gets muddy, AI averages everything |
| Copy style DNA without testing | Every fusion needs 3-5 test shots first |

---

## Style Profile Template

When creating a new profile, use this structure:

```markdown
# [Style Name] — [Short Description]

> Analyzed from [N] selected favorites ([source])

## Identity

| Element | Value |
|---------|-------|
| **Style** | [Photographer(s) reference] |
| **Model** | [AI model + settings] |
| **Resolution** | [WxH] |
| **Subject** | [Brief description] |

## Face Constant
[Exact face description to reuse across all images in set]

## Color Formula
[Main color + accents + background — with hierarchy rules]

## Style DNA
[What each source contributes — table format]

## What Works
[Camera distances, angles, poses, expressions — with % from tested images]

### Anti-Boring Elements
[At least 1 per image: unusual angle, texture, frame-in-frame, motion, surreal, geometry]

## Scenes That Work
[Full body/wide scenes + close-up techniques — what and why]

## What Doesn't Work
[Avoid list with reasons]

## Prompt Template
[Fill-in-the-blank structure]

### Example Prompts
[2-3 concrete examples from tested images]
```

---

## Key Principles

### Face Constant = Set Consistency

Every image in a set uses the **exact same face description**. Without it, AI generates different faces every time.

**Must include:**
- Ethnicity + age
- Face shape (V-line, oval, round)
- Key features (eyes, nose, lips — be specific)
- Skin finish (porcelain, tan, matte, dewy)
- Makeup level (explicit negatives if natural: "no blush, no foundation")

### Color Formula = Visual Cohesion

A set needs a dominant color + 1-2 accents on neutral background.

**Ti (提) Principle:** Saturated color only at focal points. Don't spread vivid color everywhere — concentrate it on outfit/subject, keep background neutral.

### Anti-Boring = What Separates Good from Great

Every image needs at least 1 element that makes a viewer pause:

| Category | Examples |
|----------|----------|
| **Angle** | Bird's eye, dutch tilt, from below chin, upside down |
| **Texture** | Water ripple, shadow stripes, hair strands, fabric folds |
| **Frame** | Mirror reflection, corridor, pillar divide, through fingers |
| **Motion** | Hair wind, blazer flowing, mid-step, caught moment |
| **Surreal** | Bubble gum, floating, oversized prop |
| **Geometry** | Stairs pattern, symmetry, diagonal line, vanishing point |

### Simple Pose > Complex Pose

AI generates simple poses better than complex ones:
- 1-2 actions max ("lying on side, propped on elbow")
- Don't describe contorted positions
- "Concrete bench" > "scaffolding climbing"
- Let the scene/angle create interest, not the pose
