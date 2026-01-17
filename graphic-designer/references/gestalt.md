# Gestalt Principles of Design

## Overview

Gestalt principles explain how humans perceive visual elements as organized patterns rather than separate parts. Developed by German psychologists in the 1920s (Wertheimer, Koffka, Kohler).

**Core insight:** The whole is greater than the sum of its parts.

---

## The Six Core Principles

### 1. Proximity

**Elements close together are perceived as a group.**

```
Close = Related          Far = Separate

●●●  ●●●  ●●●           ●  ●  ●  ●  ●  ●
(3 groups)              (6 separate items)
```

**Application:**
- Group related content with less space between
- Separate unrelated content with more space
- Navigation items close together = same category

**Key insight:** Proximity is the most powerful grouping tool — it overrides color and shape cues.

**Example:** Amazon product pages cluster title, price, ratings, and "Add to Cart" closely together.

---

### 2. Similarity

**Similar elements are perceived as related.**

Similarity can be achieved through:
- Shape
- Color
- Size
- Texture
- Orientation

```
Same Color = Related

●●●  ○○○  ●●●
(black and white groups)
```

**Application:**
- Use consistent styling for related elements
- Make CTAs a different color to stand out
- Icons in same style = same category

**Example:** All navigation links same color; CTA button different color.

---

### 3. Closure

**The brain completes incomplete shapes.**

```
     ●●●●
   ●      ●
  ●        ●
  ●        ●
   ●      ●
     ●●●●

(We see a circle, not dots)
```

**Application:**
- Logo design (WWF panda, NBC peacock, FedEx arrow)
- Minimalist icons
- Interactive elements that hint at function

**Key:** Provide enough information for brain to complete — too little = confusion.

---

### 4. Figure-Ground

**We distinguish foreground (figure) from background (ground).**

```
┌─────────────────┐
│  ████████       │  Figure = dark rectangle
│  ████████       │  Ground = light background
│                 │
└─────────────────┘
```

**Application:**
- Clear focal points
- Contrast between content and background
- Modal dialogs (darken background)
- Cards on page

**Danger:** Ambiguous figure-ground causes confusion (famous vase/faces illusion).

---

### 5. Continuity

**The eye follows smooth lines and curves.**

```
    ────────────
         \
          \
           ──────────

(Eye follows the smooth path)
```

**Application:**
- Visual flow in layouts
- Leading lines in photography
- Navigation paths
- Process diagrams

**Example:** Carousel arrows suggest horizontal flow.

---

### 6. Common Fate

**Elements moving in the same direction are perceived as related.**

```
→ → →    ← ← ←
(Two groups based on direction)
```

**Application:**
- Animations that group elements
- Hover effects on related items
- Loading indicators
- Menu flyouts

---

## Additional Principles

### Symmetry & Order

Symmetrical elements perceived as unified.

```
◀ ▶    ◀───────▶
(Balanced, unified)
```

### Common Region

Elements within same boundary perceived as group.

```
┌─────────────┐
│  ● ● ●      │  ← All three dots = one group
└─────────────┘
```

---

## Application in Design

### UI/UX Design

| Element | Gestalt Principle |
|---------|------------------|
| Card layouts | Common region, proximity |
| Navigation menus | Proximity, similarity |
| Modal dialogs | Figure-ground |
| Form grouping | Proximity, common region |
| Icon sets | Similarity |
| Loading animations | Common fate |

### Logo Design

| Brand | Principle Used |
|-------|---------------|
| WWF Panda | Closure |
| FedEx Arrow | Closure, figure-ground |
| NBC Peacock | Closure |
| Olympics Rings | Proximity, continuity |
| Unilever | Closure |

### Web Design

| Pattern | Principle |
|---------|-----------|
| Spacing between sections | Proximity |
| Button styling | Similarity |
| Modal overlays | Figure-ground |
| Scroll indicators | Continuity |
| Grouped form fields | Common region |

---

## Hierarchy of Gestalt Principles

When principles conflict, this is the typical priority:

1. **Proximity** — Strongest grouping cue
2. **Common region** — Boundaries are powerful
3. **Similarity** — Color/shape second to spacing
4. **Continuity** — Eye movement
5. **Closure** — Requires cognitive effort

**Practical rule:** If you want to group elements, put them close together. If you want to separate, add space — don't rely on color alone.

---

## Common Mistakes

| Mistake | Fix |
|---------|-----|
| Relying only on color to group | Add proximity |
| Equal spacing everywhere | Vary spacing for hierarchy |
| Ambiguous figure-ground | Increase contrast |
| Incomplete closure | Add more visual hints |
| Breaking continuity | Align elements on lines/grids |

---

## Quick Reference

| Principle | One-Line Summary | Key Application |
|-----------|------------------|-----------------|
| **Proximity** | Close = related | Spacing |
| **Similarity** | Same = related | Consistent styling |
| **Closure** | Brain completes gaps | Logo design |
| **Figure-Ground** | Foreground vs background | Focal points |
| **Continuity** | Eye follows lines | Visual flow |
| **Common Fate** | Same motion = related | Animations |

---

## Resources

- [Interaction Design Foundation - Gestalt Principles](https://www.interaction-design.org/literature/topics/gestalt-principles)
- [Figma - What Are Gestalt Principles?](https://www.figma.com/resource-library/gestalt-principles/)
- [Smashing Magazine - Visual Perception and Gestalt](https://www.smashingmagazine.com/2014/03/design-principles-visual-perception-and-the-principles-of-gestalt/)
