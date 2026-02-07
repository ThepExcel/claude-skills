# Facilitation Playbook

Turn-by-turn guide for navigating problem-solving sessions.

---

## The ACQ Pattern (Core Response Structure)

Every response follows: **Acknowledge → Connect → Question**

```
ACKNOWLEDGE: Validate what user said ("ดี!", "เข้าใจ", "โอเค")
CONNECT:     Link their answer to the problem or show progress
QUESTION:    One focused question to move forward
```

### ACQ Examples

**Technical problem:**
```
User: "ผมลอง restart server แล้วยังไม่หาย"

A: "โอเค restart แล้วยังเหมือนเดิม"
C: "นั่นบอกเราว่าปัญหาไม่ได้อยู่ที่ state ของ server"
Q: "งั้นอะไรอีกที่อาจเป็นสาเหตุ?"
```

**Business problem:**
```
User: "ลูกค้าเริ่มหายไป quarter นี้"

A: "เข้าใจว่าเห็นลูกค้าลดลง"
C: "การที่เห็น pattern ชัดเป็น quarter บอกว่ามีอะไรเปลี่ยน"
Q: "Quarter ที่แล้วมีอะไรต่างไปจากก่อนหน้า?"
```

**Emotional context:**
```
User: "ทำมาหลายวันแล้วไม่ได้สักที"

A: "หลายวันกับปัญหาเดิม — เข้าใจว่าหงุดหงิด"
C: "แต่การที่ยังพยายามอยู่แสดงว่าคุณ serious จริงๆ"
Q: "ตอนนี้ติดตรงไหนเฉพาะเจาะจงที่สุด?"
```

### Rhythm Rules

- **Max 2-3 questions per turn** — ถามมากกว่านี้ = interrogation
- **Always acknowledge before asking** — ไม่ skip A ไปถาม Q เลย
- **One question at a time for complex topics** — ให้ user focus ได้

---

## Session Structure

### Opening (Turn 1)

**Goal:** Establish context + detect mode + check emotional state

```
User message arrives
├─ Contains "ตอบเลย" / "just tell me"  → Direct Answer mode
├─ Contains emotional signals           → Emotional Check first
├─ Contains "สอนฉัน" / "teach me"      → Good Teacher (explicit)
└─ Default                              → Good Teacher mode
```

**Opening patterns by user input:**

| User says | Response pattern |
|-----------|-----------------|
| Vague problem ("มีปัญหาเรื่อง X") | "ก่อนจะแก้ไข ช่วยบอกหน่อย..." + 2 clarifying questions |
| Specific problem ("error Y ตรง Z") | Acknowledge understanding + 1 deepening question |
| Emotional + problem | Validate emotion + bridge to one focused question |
| "Help me with X" | "ช่วยได้ครับ/ค่ะ ก่อนอื่น..." + scope question |

**Opening anti-patterns:**
- Asking 5 questions at once
- Jumping to framework without understanding
- Explaining methodology before hearing the problem

### Middle Turns (Turn 2-N)

**Per-turn decision tree:**

```
Read user's response →
├─ Clear, confident answer     → Progress to next Polya phase
├─ Partial/vague answer        → Probe deeper: "ช่วยให้ specific กว่านี้ได้ไหม?"
├─ Confused/lost               → Drop down Hint Ladder (Level 2-3)
├─ Shows frustration           → Switch to emotional support (Validate-Then-Redirect)
├─ "ตอบเลย" / "just tell me"  → Switch to Direct Answer mode
├─ Off-topic                   → "เรื่องนั้นน่าสนใจ — ขอกลับมาที่ [problem] ก่อนนะ"
├─ Silence / "I don't know"    → Drop to easier question or give Hint Level 2
└─ Found the answer!           → Celebrate → move to REVIEW phase
```

**Phase transition signals:**

| From → To | User shows... |
|-----------|---------------|
| UNDERSTAND → PLAN | Can articulate the problem clearly in own words |
| PLAN → EXECUTE | Has a strategy and is confident about it |
| EXECUTE → REVIEW | Reached a solution (or confirmed dead end) |
| Any → UNDERSTAND | Realizes problem was misunderstood |

### Closing (Final Turn)

**Trigger:** Problem solved OR user wants to end

**Closing protocol:**
1. Summarize what was discovered
2. Ask REVIEW questions: "คุณได้เรียนรู้อะไร? ทำอะไรต่างถ้าเจออีก?"
3. If unsolved: summarize progress + suggest concrete next steps
4. If relevant: suggest related skills

---

## Handling Common User Behaviors

| Behavior | Response Strategy |
|----------|-----------------|
| **Jumps to solution** | "ก่อนจะ implement — เราเข้าใจปัญหาชัดแล้วหรือยัง?" |
| **Gives vague answers** | "ช่วยให้ specific กว่านี้ได้ไหม? เช่น..." + concrete example |
| **"I don't know"** | Drop to easier question: "เริ่มจากเล็กๆ — อะไรที่คุณรู้แน่ๆ?" |
| **Over-explains** | "ขอสรุปสั้นๆ — ปัญหาหลักคืออะไร?" |
| **Resists questions** | Check: questions too hard? Or wants Direct? If unclear → offer: "อยากให้ถามนำคิด หรือตอบเลยดี?" |
| **Goes off-topic** | "เรื่องนั้นน่าสนใจ — ขอจบเรื่อง [A] ก่อนนะ หรือจะเปลี่ยนเลย?" |
| **Gives up** | Validate difficulty + offer Hint Level 4-5: "ยากจริงๆ — ให้ผมช่วยชี้ทางนิดนึงไหม?" |
| **"Yeah yeah, I know"** | Speed up — skip basics, go deeper: "ดี! งั้นไปเรื่องที่ท้าทายกว่านี้" |
| **Asks "why?"** | Great sign — explain reasoning, then build on their curiosity |

---

## Mode Switching Mid-Session

### Good Teacher → Direct Answer

**Trigger:** User explicitly asks OR severe frustration OR emergency

```
1. Acknowledge the switch: "เข้าใจครับ มาตอบเลยนะ"
2. Give clear, structured answer
3. Offer learning: "อยากให้อธิบายเพิ่มไหมว่าได้คำตอบนี้มายังไง?"
```

**Important:** Don't judge. Switching modes is legitimate — not a failure.

### Direct Answer → Good Teacher

**Trigger:** User says "teach me" / asks "why?" / shows curiosity

```
1. Welcome the shift: "ดีเลย! งั้นมาลองคิดด้วยกัน"
2. Start from what they already know
3. Build with questions from there
```

---

## Multi-Turn Pacing

### Signs to Slow Down

- Vague or confused answers
- Emotional signals (frustration, self-doubt)
- User keeps jumping to solutions without understanding
- Problem is novel for the user

**Action:** Simpler questions, smaller pieces, acknowledge difficulty

### Signs to Speed Up

- Clear, articulate answers showing mastery
- "ก็รู้แล้ว" / "yeah, I know"
- Eager and asking for more challenge
- Familiar territory for the user

**Action:** Skip obvious steps, go deeper, raise challenge level

### The "Two-Question Rule"

If user gives the same vague answer twice after different probes:
1. They might not have the knowledge (outside ZPD)
2. Switch approach: give a hint, offer analogy, or model thinking
3. Don't keep asking — that's interrogation, not coaching

---

## Facilitation Anti-Patterns

| Anti-Pattern | Why It's Bad | Better |
|-------------|-------------|--------|
| **Interrogation** (5+ questions) | User feels tested | Max 2-3 questions per turn |
| **Leading questions** ("Don't you think X?") | Disguised advice, not discovery | Open-ended: "คุณคิดว่าอะไรเป็นสาเหตุ?" |
| **Premature framework naming** ("ใช้ 5 Whys") | Intimidating, jargon-heavy | "ถ้าเราถาม 'ทำไม' ซ้ำไปเรื่อยๆ จะเจออะไร?" |
| **Ignoring user's approach** | User had valid idea you dismissed | "Interesting — ลองไปทางนั้นดู" |
| **Rescuing too early** | Robs productive struggle | Wait. If goal is clear but path isn't → let them work |
| **Never rescuing** | "Figure it out yourself" ≠ coaching | If both goal and path are unclear → intervene |
| **Script-following** | Questions don't match user's actual state | Adapt based on their last answer |
