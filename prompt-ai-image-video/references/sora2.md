# Sora2 (OpenAI)

## Overview

| Aspect | Detail |
|--------|--------|
| **Provider** | OpenAI |
| **Access** | API + ChatGPT (Pro/Plus) |
| **Resolution** | 480p, 720p, 1080p |
| **Duration** | 5-20 seconds |
| **Audio** | Native audio generation |
| **Pricing** | Credits-based (Pro tier uses more) |

## Tiers

| Tier | Resolution | Duration | Speed | Use For |
|------|------------|----------|-------|---------|
| **Standard** | 480p-720p | 5-10s | Fast | Iteration, drafts |
| **Pro** | 720p-1080p | 10-20s | Slower | Final output |

## Philosophy

**"Think like a screenwriter, direct like Spielberg"**

Sora2 understands narrative and world physics. Write like a screenplay.

## Key Capabilities

| Feature | Support |
|---------|---------|
| Text-to-Video | Yes |
| Image-to-Video | Yes |
| Video-to-Video (Style) | Yes |
| Audio Generation | Yes (native) |
| Text Rendering | Limited |
| Storyboard Mode | Yes |
| Remix/Blend | Yes |
| **Cameo/Character** | Yes (@handle system) |

---

## Cameo & Character System

**CRITICAL:** Sora2 ใช้ @handle อ้างอิงตัวละคร ต้องถาม user ว่ามี cameo/character ไหม!

### Cameo vs Character

| Type | คืออะไร | วิธีสร้าง | ใช้กับ |
|------|---------|----------|--------|
| **Cameo** | ตัวคนจริงที่ยืนยันตัวตน | อัดคลิป + เสียงผ่าน iOS app | คนจริง (ตัวเอง/คนที่อนุมัติ) |
| **Character** | ตัวละครสมทบ | Upload คลิป/ภาพ หรือสร้างจาก Sora | สัตว์, วัตถุ, การ์ตูน, AI-generated humans |

### @Handle Reference System

เรียกใช้ character/cameo ใน prompt โดยพิมพ์ `@handle`:

```
@aiangel.03 กำลังร้องเพลงบนเวที warehouse สไตล์ rock ดิบๆ
@siraekabut กำลังต่อยมวยกับ @sama บนเวทีมวยราชดำเนิน
```

**ข้อจำกัดสำคัญ:**
- รองรับได้สูงสุด **2 characters/cameos** ต่อคลิป
- ถ้าเกิน 2 → หน้าตาอาจปนกัน/เพี้ยน

### Permission Controls

ผู้สร้าง cameo/character กำหนดได้ว่าใครใช้ได้:

| Setting | ความหมาย |
|---------|----------|
| Only me | ใช้ได้คนเดียว |
| People I approve | ต้องขออนุมัติ |
| Mutuals | คนที่ follow กัน |
| Everyone | ใครก็ใช้ได้ |

### วิธีสร้าง Character คนสมจริง (Realistic Human)

**ปัญหา:** OpenAI บล็อกการอัปโหลดภาพ/คลิปคนจริง

**Solution:** ให้ Sora สร้างคนขึ้นมาก่อน แล้วค่อย save เป็น Character

```
Step 1: Gen คลิปคนที่ต้องการ (หน้าตา, ทรงผม, บุคลิก, เสียง)
        → ปรับ prompt / Remix จนพอใจ

Step 2: กด "..." บนคลิป → Create Character
        → เลือกช่วงเวลาที่ต้องการ

Step 3: ตั้ง @handle และ permission

Step 4: ใช้งาน → พิมพ์ @handle ใน prompt ครั้งต่อไป
```

**ทำไมได้ผล:** ระบบถือว่าเป็น "fictional human" ที่ Sora สร้างเอง ไม่ใช่คนจริง

### เทคนิคการใช้ Character/Cameo

| Do | Don't |
|----|-------|
| ใส่ @handle เสมอ | บรรยายหน้าตาซ้ำซ้อน |
| ระบุชุดใหม่ถ้าต้องการเปลี่ยน | สมมติว่าจำชุดเดิมได้ |
| กำกับ mood/pose ชัดเจน | ใส่เกิน 2 characters |
| บอกเฉพาะฉาก/มุมกล้อง/บรรยากาศ | รวมทุกอย่างในประโยคเดียว |

### Prompt Template with Character

```
@handle [action/pose] at [location].
[Camera movement], [lighting description].
[Outfit if different from default]: [describe].
[Audio]: [ambient], [music style], [dialogue if any].
[Style reference].
```

**Example:**
```
@aiangel.03 performs intense rock vocals on a dark warehouse stage.
Handheld camera circles her, smoke drifts through harsh red spotlights.
Outfit: torn black tank top, leather pants, silver chain necklace.
Audio: heavy guitar riff, raw vocals, crowd cheering in background.
Live concert documentary style, gritty and authentic.
```

---

## Requirement Intake for Sora2 Prompts

**ก่อนเขียน prompt ต้องถาม user:**

1. **Character/Cameo:** มี @handle ไหม? ใครบ้าง? บทบาทอะไร?
2. **เพลง/แนว:** ภาษาอะไร? แนวไหน? (Thai rock, instrumental, etc.)
3. **สถานที่:** เวที concert? studio? warehouse? rooftop?
4. **Mood:** เท่/ดิบ/มันส์/ดราม่า/หวาน/เศร้า?
5. **สไตล์การถ่าย:**
   - Live concert documentary (handheld, raw)
   - Cinematic performance (dolly/crane, film look)
   - Music video narrative (มี story เบาๆ)
6. **ช็อตเน้น:** close-up? full body? เครื่องดนตรี?
7. **เสื้อผ้า/โทนสี:** all-black? specific outfit?
8. **Dialogue/Lyrics:** ต้องการให้ร้อง/พูดไหม? บอก 1-2 บรรทัด

---

## Prompt Structure

**Storyboard approach works best:**

```
[SCENE DESCRIPTION]
Setting: [Location and time]
Action: [What happens beat by beat]
Camera: [Movement and framing]
Audio: [Sound design, music, dialogue]
Style: [Visual aesthetic]
```

## Example Prompts

### Cinematic Scene

```
A lone astronaut walks across the red Martian surface
toward a massive abandoned structure half-buried in sand.
The sun sets behind distant mountains, casting long shadows.
Wind kicks up dust that drifts past the camera.
Shot on IMAX 70mm, Denis Villeneuve's Dune aesthetic.
Ambient wind sounds, distant metallic creaking.
Epic orchestral score builds slowly.
```

### Character Moment

```
Close-up of a young woman's face as she reads a letter.
Her expression shifts from curiosity to joy to tears.
Natural window light illuminates half her face.
Camera slowly pushes in during emotional peak.
Soft piano music, sound of paper rustling.
Indie film aesthetic, A24 production style.
```

### Action Sequence

```
Car chase through narrow European streets at night.
Red sports car drifts around corner, sparks flying.
Police cars in pursuit, sirens wailing.
Camera mounted on lead car, then cuts to aerial view.
Rain-slicked cobblestones reflect neon signs.
High energy electronic soundtrack, tire screeches.
Fast cutting, Hollywood blockbuster style.
```

### Product Commercial

```
Sleek smartphone rotates in empty white space.
Light rays catch the titanium edges.
Camera orbits slowly, revealing all angles.
Phone lands on reflective surface with gentle impact.
Minimal ambient music, soft whoosh sounds.
Apple keynote aesthetic, clean and premium.
```

## Audio Integration

Sora2 generates synchronized audio. Include:

| Audio Element | How to Prompt |
|---------------|---------------|
| **Ambient** | "sounds of [environment]", "background noise of..." |
| **Music** | "epic orchestral score", "soft piano melody", "[genre] music" |
| **SFX** | "sound of [action]", "[object] makes [sound]" |
| **Dialogue** | "person says '[dialogue]'" (limited accuracy) |
| **Silence** | "silent", "no audio", "muted" |

**Audio Example:**

```
Forest at dawn. Birds singing, leaves rustling in gentle breeze.
A deer steps into frame, hooves crunching on fallen leaves.
Soft, contemplative ambient music.
Distant stream water sounds.
```

## Storyboard Mode

For complex scenes, break into shots:

```
SHOT 1 (3s):
Wide establishing shot of Tokyo skyline at night.
Camera slowly pushes forward. City hum, distant traffic.

SHOT 2 (4s):
Cut to street level. Neon signs reflect on wet pavement.
A figure walks toward camera. Footsteps echo.

SHOT 3 (3s):
Close-up of the figure's face illuminated by phone screen.
Cyberpunk aesthetic, Blade Runner color grading.
```

## Image-to-Video

Start from reference image:

```
[Upload image as reference]
The woman in the image slowly turns to face the camera.
Her hair moves gently in an unseen breeze.
She begins to smile, eyes lighting up.
Natural lighting, shallow depth of field.
Soft romantic music swells.
```

## Style References

Sora2 understands cultural references:

| Reference | Effect |
|-----------|--------|
| **Director names** | "Wes Anderson style" - symmetry, pastels |
| **Film titles** | "Blade Runner aesthetic" - neon noir |
| **Era** | "1970s film look" - grain, warm tones |
| **Genre** | "documentary style" - handheld, natural |
| **Platform** | "Super 8mm film" - vintage, light leaks |

## Remix/Blend Features

Combine existing clips:

```
Blend video A (nature scene) with video B (urban scene)
using a smooth morph transition.
Maintain the color palette from video A.
Add cinematic film grain throughout.
```

## Tips

1. **Scene-based writing** - Describe like a screenplay
2. **Include audio** - Take advantage of native audio
3. **Use references** - Directors, films, eras work well
4. **Physical accuracy** - Sora2 understands physics
5. **Emotional beats** - Describe the feeling, not just action
6. **Pacing cues** - "slowly", "suddenly", "gradually"
7. **Start with Standard** - Iterate fast, then Pro for finals

## Prompting Patterns

### The 3-2-1 Pattern

```
[3 VISUAL DETAILS]: Environment, subject, lighting
[2 MOTION ELEMENTS]: Camera move, subject action
[1 STYLE ANCHOR]: Director/film/era reference
```

### The Screenplay Pattern

```
FADE IN:

EXT. [LOCATION] - [TIME]

[Visual description of the scene]

[Action/movement description]

[Audio/music description]
```

### The Sensory Pattern

```
SIGHT: [What we see in detail]
SOUND: [What we hear]
MOTION: [What moves and how]
MOOD: [Emotional quality]
```

## Limitations

| Limitation | Workaround |
|------------|------------|
| **ห้ามอ้างอิงชื่อศิลปิน/ดารา/วงดนตรี** | บรรยายลักษณะ/สไตล์แทน (แต่ชื่อ Director ใช้ได้ เช่น "Denis Villeneuve aesthetic") |
| Text in video | Add text in post |
| Specific faces | Use Character/Cameo @handle |
| Precise lip sync | Limited, add voiceover in post |
| Very long videos | Stitch multiple clips (Storyboard mode) |
| Real-time generation | Plan for queue times |
| Max 2 characters per clip | Split into multiple clips if needed |
| Upload real human photos | Let Sora generate first, then Create Character |
| Duration | 10s or 15s (25s with Storyboard mode) |

## Quality Checklist

```
□ Character/Cameo @handle included (if applicable)
□ Scene visually described
□ Camera movement specified
□ Audio/sound included
□ Style reference added
□ Motion verbs used
□ Timing/pacing indicated
□ Duration selected (10s/15s)
□ Storyboard structure for complex scenes
□ Max 2 characters per clip
□ Outfit specified if different from default
```

## Prompt Template

```
[SETTING]: [Time] at [location], [weather/atmosphere]
[SUBJECT]: [Who/what], [appearance], [position]
[ACTION]: [What happens], [how they move]
[CAMERA]: [Shot type], [movement], [lens feel]
[AUDIO]: [Ambient sounds], [music], [SFX]
[STYLE]: [Director/film reference], [color/look]
[DURATION]: [5s/10s/20s], [Standard/Pro]
```
