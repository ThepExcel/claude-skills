# Teaching Methodology Reference

Complete reference for explanation modes and master teaching techniques.

## Table of Contents

1. [7 Explanation Modes](#explanation-modes)
   - [ELI5](#mode-1-eli5)
   - [Feynman](#mode-2-feynman)
   - [Socratic](#mode-3-socratic)
   - [Visual](#mode-4-visual)
   - [Analogy Hunter](#mode-5-analogy-hunter)
   - [Progressive](#mode-6-progressive)
   - [Collaborative Exploration](#mode-7-collaborative-exploration)
2. [7 Master Principles](#master-principles)
3. [Cross-Industry Insights](#cross-industry-insights)
4. [Anti-Patterns](#anti-patterns)

---

## Explanation Modes

### Mode Selection Quick Reference

| Mode | Best For | Speed |
|------|----------|-------|
| ELI5 | Quick understanding | Fast |
| Feynman | Mastery verification | Medium |
| Socratic | Critical thinking | Slow |
| Visual | Spatial/structural | Medium |
| Analogy | Abstract concepts | Fast |
| Progressive | Complex multi-part | Slow |
| Collaborative | No definitive answer | Varies |

---

### Mode 1: ELI5

**Goal:** Maximum simplification.

**Template:**
```
[Concept] is like [everyday thing].
When [situation], it [does what].
That's why [real-world result].
```

**Example - Recursion:**
> Recursion is like looking at yourself in two mirrors facing each other.
> You see yourself, inside yourself, inside yourself... going on forever.
> In programming, a function calls itself until we tell it to stop.

---

### Mode 2: Feynman

**Goal:** Deep mastery through teaching.

**Process:**
1. Ask learner to explain the concept to you
2. Listen for gaps and hesitations
3. Ask clarifying questions at weak points
4. Have them revise and re-explain

**Prompts:**
- "Pretend I know nothing. Explain it to me."
- "I'm confused about [X]. Can you clarify?"
- "What would happen if [edge case]?"

---

### Mode 3: Socratic

**Goal:** Guide learner to discover answer themselves.

**Question progression:**
```
What do you think [X] means?
     ↓
Why do you think that?
     ↓
What if [counter-example]?
     ↓
How might we reconcile that?
     ↓
So what does that tell us?
```

**Rules:**
- One question at a time
- Wait for response
- Never give answer directly
- Praise the process

---

### Mode 4: Visual

**Goal:** Spatial understanding through diagrams.

**Choose the right tool:**

| Complexity | Tool | Speed |
|------------|------|-------|
| Simple (hierarchy, flow) | ASCII | Instant |
| Standard concept | WebSearch for existing diagram | Fast |
| Custom/unique | AI image generation | Slower |

**ASCII patterns (use when sufficient):**
```
Hierarchy:          Flow:
    Root            Input → Process → Output
    ├── Child A               ↓
    └── Child B          Side Effect

Comparison:         State:
┌─────────┬─────────┐    [A] ──→ [B]
│  Left   │  Right  │     ↑      │
└─────────┴─────────┘     └──────┘
```

**Using real images:**
```bash
# Option 1: Find existing diagram (FREE)
WebSearch "concept X diagram"

# Option 2: Generate custom visual (PAID - ask user first!)
# Always ask: "ต้องการให้สร้างภาพไหมครับ? (มีค่าใช้จ่าย)"
python3 tools/generate_image.py "educational diagram showing [concept]" -o explanation.png
```

**When to use images over ASCII:**
- Physical processes (physics, biology, engineering)
- 3D spatial relationships
- Complex multi-step workflows
- When learner says "ยังนึกภาพไม่ออก"

**Always explain what the visual shows.**

---

### Mode 5: Analogy Hunter

**Goal:** Unlock understanding through multiple analogies.

**Template per analogy:**
```
[Concept] is like [Analogy from Domain X].
- [Part A] maps to [Part A']
- [Part B] maps to [Part B']
Limitation: Breaks down when [edge case].
```

**Example - API:**
1. **Restaurant:** API = waiter between you and kitchen
2. **Library:** API = librarian who fetches books
3. **Plug/Socket:** API = standard interface

---

### Mode 6: Progressive

**Goal:** Master complex topics layer by layer.

**Layers:**
```
Layer 0: Prerequisites - What must they know first?
Layer 1: Big Picture - Core concept in 2-3 sentences
Layer 2: Mechanics - How it works
Layer 3: Nuances - Edge cases, exceptions
Layer 4: Mastery - Advanced applications
```

**Check understanding at each layer before proceeding.**

---

### Mode 7: Collaborative Exploration

**Goal:** Learn together when no definitive answer exists.

**When to use:**
- Philosophy, ethics, contested theories
- Emerging technology (no established best practices)
- Personal decisions (career, life choices)
- Topics where AI is uncertain

**Process:**
```
1. Acknowledge → "นี่เป็นเรื่องที่ยังไม่มีคำตอบตายตัว"
2. Present    → Show 2-3 perspectives fairly
3. Invite     → "คุณคิดว่ายังไงครับ?"
4. Explore    → Use Socratic to guide discovery
5. Synthesize → Help form their own view
```

**Key mindset shifts:**
- Teacher → Co-learner
- Giving answers → Asking questions
- Certainty → Intellectual humility

**Example prompts:**
- "มาลองคิดด้วยกันนะครับ..."
- "มีหลายมุมมองในเรื่องนี้..."
- "ผมเองก็ไม่แน่ใจ 100% ลองดูข้อมูลด้วยกัน..."
- "ถ้าเราดูจากมุม X... แต่ถ้ามองจากมุม Y..."

**Pairs well with:** `/deep-research` when AI needs to learn first.

---

### Mode Combinations

| Combination | Use Case |
|-------------|----------|
| Visual + Progressive | Complex systems |
| ELI5 → Socratic | Start simple, deepen |
| Analogy → Feynman | Introduce, then verify |
| Research → Collaborative | AI uncertain, then explore together |
| Collaborative → Socratic | Open question, guide to insight |

---

## Master Principles

### 1. SIMPLIFY (Feynman)
> "If you can't explain it to a 6-year-old, you don't understand it."

- Strip jargon completely
- Find the ONE essential thing
- Test: Would a child understand?

### 2. BRIDGE (Buddha's Upaya)
Connect unknown to known via metaphors.

**Famous examples:**
- The Burning House - urgency
- The Raft - teachings as tools
- The Blind Men & Elephant - partial perspectives

### 3. CHUNK (Miller/Sweller)
- Working memory: 5±2 items max
- Optimal chunk: 3-4 items
- Use progressive disclosure

### 4. SCAFFOLD (Vygotsky ZPD)
```
[Too Easy] ← [ZPD: Can do with help] → [Too Hard]
                    ↓
              Target Zone
```

### 5. QUESTION (Socrates)
- Clarifying: "What do you mean by...?"
- Probing: "Why do you think that?"
- Challenge: "What's the counter-argument?"

2x retention when learner reaches conclusion themselves.

### 6. MULTI-MODE (Dual Coding)
Visual + Verbal = 2x retention.
- Diagrams alongside explanations
- Concrete examples (don't just define)
- Stories and narratives

### 7. RETRIEVE (Testing Effect)
Testing produces 50% more learning than re-studying.
- "Can you explain it back?"
- "What would happen if...?"

---

## Cross-Industry Insights

| Domain | Principle | Application |
|--------|-----------|-------------|
| Comedy | Timing & pauses | Let insights land |
| Jazz | Responsive adaptation | Read learner, adapt real-time |
| Martial Arts | Belt progression | Clear milestones |
| Meditation | Gentle redirection | Guide without judgment |
| Game Design | Difficulty curves | Flow = between boredom & frustration |
| Improv | "Yes, And" | Build on learner's understanding |

---

## Anti-Patterns

| Bad | Better |
|-----|--------|
| Info dump | Chunk into 3-5 pieces |
| Abstract definitions only | Concrete examples first |
| Ignoring prior knowledge | Assess and bridge |
| One explanation fits all | Adapt to learner |
| Moving on without checking | Verify understanding |
| Jargon-heavy | Plain language |
| Passive presentation | Active questioning |
| **Pretending to know** | **Research first or explore together** |
| **Forcing single answer** | **Present multiple perspectives** |
