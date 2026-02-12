# Prompt Walkthroughs — ตัวอย่างจริง

## Example 1: Portrait — "ถ่ายรูปสวยๆ"

```
User: "อยากได้รูป portrait สวยๆ ของผู้หญิง"

STEP 1 INTENT: → ถาม user: "สวยแบบไหนคะ?" → user ตอบ: "ดูลึกลับหน่อย"
STEP 2 NARRATIVE: ผู้หญิงคนหนึ่งนั่งคนเดียวในคาเฟ่ตอนค่ำ กำลังคิดอะไรบางอย่าง
STEP 3 SEE: เห็นแสงจากเทียนบนโต๊ะส่องใบหน้าด้านเดียว อีกด้านจมในเงา
STEP 4 PLAN: Rembrandt lighting, warm/cool contrast, 85mm, shallow DOF

PROMPT:
"Cinematic portrait on Kodak Portra 800 film. A woman in her late 20s
sits alone at a dimly lit café table. Single candle illuminates one side
of her face in warm amber, the other half falls into cool blue shadow.
She gazes slightly past camera with a faint, unreadable expression.
85mm lens, f/1.8, shallow depth of field. Warm bokeh from distant
string lights. Smoke from a just-extinguished match drifts between
her and the lens. Rembrandt lighting, intimate mood."

WHY IT WORKS:
- "ลึกลับ" แปลเป็น → half-shadow + unreadable expression + smoke
- แสงมี motivation (เทียน) ไม่ใช่ "nice lighting"
- มี foreground (smoke) สร้าง depth
- มี story (คาเฟ่ตอนค่ำ คนเดียว) ไม่ใช่แค่ "portrait"
```

## Example 2: Product — "รูปขายของ"

```
User: "ถ่ายรูปขายนาฬิกา ให้ดูหรู"

STEP 1 INTENT: ต้องให้คนรู้สึก "อยากได้" → aspiration + premium feel
STEP 4 PLAN: Low key, hard light สร้าง highlight บน metal, dark bg

PROMPT:
"Commercial product photo. Minimalist luxury watch with silver case
on polished black marble surface. Single hard light from upper left
creates a sharp highlight along the watch bezel and a long shadow.
Dark charcoal background. Subtle reflection on marble surface.
50mm macro lens, f/8, deep focus. No text, no props, negative space
on right for copy placement. High-end editorial style."

WHY IT WORKS:
- "หรู" แปลเป็น → dark bg + marble + single hard light (not soft/friendly)
- Negative space สำหรับวาง text ภายหลัง (คิดล่วงหน้าให้ user)
- Hard light on metal = premium feel (soft light จะดูธรรมดา)
```

## REVIEW Example

```
□ INTENT MATCH  → ✅ "ร้อนแรง intimate" — prompt มี tension + skin + closeness
□ LIGHT SOURCE  → ✅ แสงจากเตาผิงด้านซ้าย ตัดกับแสงจันทร์จากหน้าต่าง
□ BORING CHECK  → ✅ ไม่ใช่ — มี "เสื้อผ้าที่ถอดแล้ววางบนเก้าอี้" เป็น story element
□ STOCK CHECK   → ✅ ไม่ stock — ไม่มีกุหลาบ/เทียน/แชมเปญ ใช้ "ห้องนั่งเล่นหลังเลิกงาน"
□ SPECIFICITY   → ✅ ไม่มีคำกว้าง
□ TENSION       → ✅ "ยิ้มแต่ตาเหนื่อย" — contrast สวย/เหนื่อย
□ LESS IS MORE  → ✅ props แค่ 1 (แก้วไวน์ครึ่งเดียว)
```

## Critique Walkthrough

```
User ส่งรูป: portrait ผู้หญิงนั่งริมหน้าต่าง แสงเรียบๆ หน้าตรง พื้นหลังผนังขาว

GOAL: "จะเอาไปลง Instagram portfolio ค่ะ"

ANALYZE:
## สิ่งที่ดีแล้ว ✓
- แสงธรรมชาติจากหน้าต่างให้ skin tone ดี
- Subject อยู่ในตำแหน่ง rule of thirds

## สิ่งที่ควรปรับ
1. [HIGH] แสง flat เกินไป → แสงหน้าต่างควรมาจากด้านเดียว
   ไม่ใช่ตรงหน้า จะได้ shadow ที่ define ใบหน้า
   → แก้: "window light from camera left, Rembrandt shadow on right cheek"

2. [HIGH] พื้นหลังว่างเปล่า → ไม่มี story ไม่มี depth
   → แก้: เพิ่ม "sheer curtain as foreground element, slightly out of focus"
   หรือ "warm afternoon light casting window shadow patterns on wall"

3. [MEDIUM] Pose หน้าตรง → ดู passport photo
   → แก้: "3/4 angle, chin slightly down, gazing through window"

PRESCRIBE PROMPT:
"Cinematic portrait, Portra 400 tones. Woman seated by tall window,
3/4 view, chin slightly lowered, gazing through glass with soft
contemplation. Window light from camera left creates Rembrandt
shadow. Sheer white curtain diffuses into soft foreground bokeh.
Warm afternoon light casts gentle window frame shadows on the wall
behind her. 85mm, f/2, shallow DOF. Intimate, reflective mood."
```
