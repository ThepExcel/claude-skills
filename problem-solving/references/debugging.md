# Software Debugging Flow

Systematic debugging methodology integrated with Good Teacher mode.

---

## When to Use

**Triggers:** "bug", "error", "doesn't work", "debug", "broken", "crash", "fail", code-related "stuck"

**Maps to Polya:**

| Polya Phase | Debug Step |
|-------------|-----------|
| UNDERSTAND | REPRODUCE + ISOLATE |
| PLAN | DIAGNOSE (form hypothesis) |
| EXECUTE | FIX |
| REVIEW | VERIFY + PREVENT |

---

## The Debug Cycle

```
REPRODUCE → ISOLATE → DIAGNOSE → FIX → VERIFY → PREVENT
```

### Step 1: REPRODUCE

**Goal:** Make the bug happen reliably.

**Good Teacher questions:**

| EN | TH |
|----|-----|
| "Can you reproduce this consistently?" | "ทำให้ bug เกิดซ้ำได้ทุกครั้งไหม?" |
| "What exact steps trigger this?" | "ขั้นตอนไหนที่ทำให้เกิด bug?" |
| "Does it happen every time or intermittently?" | "เกิดทุกครั้ง หรือบางครั้ง?" |
| "When did it last work correctly?" | "ครั้งสุดท้ายที่ทำงานปกติคือเมื่อไหร่?" |
| "What's the exact error message?" | "Error message เต็มๆ คืออะไร?" |

**Key insight:** If you can't reproduce it, you can't verify a fix.

**If not reproducible:**
- Gather more data: logs, conditions, environment
- Ask: "เกิดขึ้นกับทุกคน หรือเฉพาะคุณ?"
- Ask: "มี pattern ไหม? ช่วงเวลา? ขนาดข้อมูล?"

### Step 2: ISOLATE

**Goal:** Narrow down where the bug lives.

**Techniques:**

| Technique | When | How |
|-----------|------|-----|
| **Binary search** | Large codebase, unknown location | Comment out half, see if bug persists |
| **Minimal reproduction** | Complex setup | Remove components until bug disappears |
| **Git bisect** | Bug appeared at some point | Binary search through commits |
| **Input variation** | Data-dependent | Change inputs systematically |
| **Environment comparison** | Works somewhere, fails elsewhere | Diff configurations |

**Good Teacher questions:**

| EN | TH |
|----|-----|
| "Where does it work and where does it break?" | "ตรงไหนยังทำงาน ตรงไหนพัง?" |
| "What's the smallest example that shows the bug?" | "ตัวอย่างเล็กที่สุดที่เห็น bug คืออะไร?" |
| "What changed between when it worked and now?" | "อะไรเปลี่ยนไประหว่างตอนที่ใช้ได้กับตอนนี้?" |
| "If you remove X, does it still fail?" | "ถ้าเอา X ออก ยังพังอยู่ไหม?" |

### Step 3: DIAGNOSE

**Goal:** Understand the root cause.

**Scientific Method for Debugging:**

```
1. OBSERVE    → What exactly happens? (error, wrong output, crash)
2. HYPOTHESIZE → What could cause this?
3. PREDICT    → If hypothesis correct, what else should we see?
4. TEST       → Check the prediction
5. CONCLUDE   → Hypothesis correct?
   → YES → Root cause found → Step 4
   → NO  → New hypothesis → Back to step 2
```

**Good Teacher questions:**
- "จาก error message คุณคิดว่าเกิดอะไรขึ้น?"
- "สมมติฐานของคุณคืออะไร?"
- "ถ้าสมมติฐานถูก เราน่าจะเห็นอะไรอีก?"
- "จะทดสอบสมมติฐานนี้ได้ยังไง?"

**Common mistake:** Fixing symptoms without understanding cause. Always ask: "นี่แก้ที่อาการ หรือที่สาเหตุ?"

### Step 4: FIX

**Goal:** Implement the minimal correct fix.

**Good Teacher questions:**
- "วิธีแก้ที่ง่ายที่สุดที่แก้ตรงสาเหตุคืออะไร?"
- "การแก้นี้จะมี side effect ไหม?"
- "คุณแก้ที่อาการ หรือที่สาเหตุ?"

**Principle:** Fix the cause, not the symptom. The smallest change that solves the root cause is the best fix.

### Step 5: VERIFY

**Goal:** Confirm fix works and nothing else broke.

**Checklist:**
- [ ] Original bug no longer reproducible
- [ ] Related functionality still works
- [ ] Edge cases handled
- [ ] Tests pass (existing + new)

**Good Teacher question:** "จะรู้ได้ยังไงว่าแก้ได้จริง ไม่ใช่แค่บังเอิญ?"

### Step 6: PREVENT

**Goal:** Ensure this bug type doesn't recur.

**Good Teacher questions:**
- "จะ catch bug แบบนี้เร็วขึ้นได้ยังไง?"
- "ควรเพิ่ม test สำหรับกรณีนี้ไหม?"
- "มี pattern เดียวกันในที่อื่นไหม?"

---

## Common Bug Patterns

Quick diagnosis based on symptoms:

| Pattern | Symptoms | Likely Cause | First Question |
|---------|----------|-------------|----------------|
| **Works locally, fails in prod** | Environment-specific | Config, dependencies, env vars | "อะไรต่างระหว่าง local กับ prod?" |
| **Intermittent failure** | Sometimes works | Race condition, timing, external dependency | "มี pattern ไหม? ช่วงเวลา? Load?" |
| **Regression** | Used to work | Recent code/dependency change | "อะไรเปลี่ยนไปล่าสุด?" |
| **Edge case** | Works for most inputs | Boundary conditions, null/empty | "ค่าที่ fail ต่างจากค่าที่ผ่านยังไง?" |
| **Performance** | Slow, timeout, OOM | N+1 queries, memory leak, missing index | "ช้าตลอด หรือช้าเมื่อ [condition]?" |
| **Silent failure** | No error, wrong result | Logic error, wrong assumption | "ค่าที่ได้คืออะไร? คาดหวังอะไร?" |

---

## Debugging with Good Teacher Mode

### When to Guide vs. When to Answer

| Situation | Mode |
|-----------|------|
| User learning to debug | Good Teacher — guide through the cycle |
| Production is down | Direct Answer — fix now, learn later |
| User has hypothesis | Good Teacher — help them test it |
| Error is trivial (typo, syntax) | Direct Answer — don't over-teach |
| User says "just fix it" | Direct Answer — respect their time |

### Example: Good Teacher Debugging

```
User: "unit test fail แต่ไม่รู้ทำไม"

[REPRODUCE]
Teacher: "test fail ด้วย error อะไร? assertion fail หรือ exception?"

User: "assertion fail — expected 10 แต่ได้ 0"

[ISOLATE]
Teacher: "ดี! ปัญหาอยู่ที่ค่าที่ return มา
function ที่ test ทำอะไร? ลองอธิบายสั้นๆ"

User: "มันรวมราคาสินค้าใน cart"

[DIAGNOSE]
Teacher: "ถ้า expected 10 แต่ได้ 0 — สมมติฐานของคุณคืออะไร?
ทำไมมันอาจ return 0?"

User: "อ๋อ! cart มันว่างเปล่า — ผมลืม add item ก่อน assert!"

[VERIFY + PREVENT]
Teacher: "หาเจอเองแล้ว! เพิ่ม setup ให้ add item ก่อน test
บทเรียนคืออะไร? จะป้องกันยังไงในอนาคต?"
```

### Example: Direct Answer Debugging

```
User: "production down! 500 error ช่วยด่วน"

Teacher: "เข้าใจ — ส่ง error log มาเลย จะช่วยดูทันที"

[User sends log: ConnectionRefusedError port 5432]

Teacher: "Database connection refused ที่ port 5432
1. เช็คว่า PostgreSQL running อยู่: `systemctl status postgresql`
2. เช็ค connection string ใน config
3. เช็คว่า port ไม่ได้ถูก block

เริ่มจากข้อ 1 ก่อน — database ยัง running อยู่ไหม?"
```

---

## Reading Error Messages

Guide users to read error messages systematically:

```
1. TYPE:     Error type/class → บอก category ของปัญหา
2. MESSAGE:  Description → บอกอะไรผิด
3. LOCATION: File + line number → บอกที่ไหน
4. STACK:    Call trace → บอก path ที่โปรแกรมเดิน
```

**Good Teacher question:** "จาก error message 4 ส่วนนี้ คุณเห็นอะไร?"

**Common student mistakes:**
- อ่านแค่บรรทัดแรก (miss root cause ที่อยู่ล่างๆ)
- Google ทั้ง error message (miss specific context)
- Ignore stack trace (miss where it actually broke)
