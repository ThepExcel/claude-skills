---
name: skill-creator-thepexcel
description: Guide for creating and enhancing skills. Use when users want to create a new skill, update/improve an existing skill, or audit skill quality. Supports both creation from scratch and enhancement of existing skills with audit rubric scoring.
license: Apache 2.0 (see LICENSE.txt)
---

# Skill Creator (ThepExcel Edition)

> Based on [Anthropic's official skill-creator](https://github.com/anthropics/skills) (Apache 2.0). Enhanced with ThepExcel deployment workflow and enhancement pipeline.

## Quick Start

| ต้องการ | ใช้ Mode | ไปที่ |
|---------|---------|------|
| สร้าง skill ใหม่ | **Create** | → [Creation Process](#creation-process) |
| ปรับปรุง skill เดิม | **Enhance** | → [Enhancement Mode](#enhancement-mode) |
| ตรวจคุณภาพ | **Audit only** | → [Audit Rubric](references/audit-rubric.md) |

---

## Core Principles

### Concise is Key

Context window เป็นทรัพยากรที่แชร์กัน — ทุกบรรทัดต้องจ่ายค่า token

**Claude ฉลาดอยู่แล้ว** → ใส่เฉพาะสิ่งที่ Claude ไม่รู้:
- "Claude ต้องการคำอธิบายนี้จริงไหม?"
- "ย่อหน้านี้คุ้มค่า token ไหม?"

### Degrees of Freedom

| Level | เมื่อไหร่ | ตัวอย่าง |
|-------|----------|---------|
| **High** (text) | หลายวิธีถูกได้ | Code review guidelines |
| **Medium** (pseudocode) | มี pattern ที่ prefer | Report template |
| **Low** (scripts) | ต้องการ consistency | Database migrations |

### Test with All Models

| Model | Check |
|-------|-------|
| **Haiku** | ให้ guidance พอไหม? |
| **Sonnet** | ชัดเจนและ efficient? |
| **Opus** | ไม่ over-explain? |

---

## Skill Structure

```
skill-name/
├── SKILL.md (required)     ← < 500 lines
│   ├── YAML frontmatter    ← name + description only
│   └── Markdown body       ← loaded when triggered
├── scripts/                ← deterministic code
├── references/             ← loaded as needed (one level deep)
└── assets/                 ← templates, not loaded into context
```

### Frontmatter Rules

| Field | Rules |
|-------|-------|
| `name` | Max 64 chars, lowercase + numbers + hyphens |
| `description` | Max 1024 chars, third person, what + when |

### Description Best Practices

```yaml
# Good: what + when + triggers
description: Extract text and tables from PDF files, fill forms, merge documents.
  Use when working with PDF files or when the user mentions PDFs or document extraction.

# Bad: first person, vague
description: I can help you with PDFs.
```

**"When to Use" in body = useless** — Claude only sees description when deciding to trigger.

### Naming Conventions

| Pattern | Examples |
|---------|----------|
| **Verb-noun** | `design-business-model`, `create-visualization` |
| **Noun-verb-ing** | `power-query-coaching`, `problem-solving` |
| **Recognized terms** | `triz`, `deep-research` |

### Bundled Resources

| Type | เมื่อไหร่ | โหลดเข้า context? |
|------|----------|-----------------|
| **scripts/** | Code ที่ใช้ซ้ำ, ต้อง deterministic | ไม่ (execute ตรง) |
| **references/** | Docs ที่อ้างอิงระหว่างทำงาน | ใช่ (on demand) |
| **assets/** | Templates, logos, boilerplate | ไม่ |

**ห้ามสร้าง:** README.md, CHANGELOG.md, INSTALLATION_GUIDE.md — skills สำหรับ AI ไม่ใช่คน

### Progressive Disclosure

| Level | When | Limit |
|-------|------|-------|
| Metadata | Always loaded | ~100 words |
| SKILL.md body | When triggered | < 500 lines |
| References | As needed | Unlimited |

**Details:** See [progressive-disclosure.md](references/progressive-disclosure.md)

---

## Creation Process

### Overview

```
1. Understand → 2. Plan → 3. Init → 4. Edit → 5. Package → 6. Deploy → 7. Iterate
```

### Step 1: Understand

**ถามผู้ใช้:**
- "Skill นี้ต้องรองรับ functionality อะไรบ้าง?"
- "ยกตัวอย่าง 2-3 scenarios ที่จะใช้"
- "ผู้ใช้จะพูดอะไรที่ควร trigger skill นี้?"

**Tip:** ใช้ `/extract-expertise` สำหรับ domain ที่ซับซ้อน

### Step 2: Plan

วิเคราะห์แต่ละ example:

| Task | Repeatable? | Resource |
|------|------------|----------|
| Same code every time | Yes → script | `scripts/rotate_pdf.py` |
| Same boilerplate | Yes → asset | `assets/template/` |
| Rediscovering info | Yes → reference | `references/schema.md` |

### Step 3: Initialize

```bash
scripts/init_skill.py <skill-name> --path <output-directory>
```

### Step 4: Edit

**Order:** resources first → test scripts → update SKILL.md last

**Design pattern references:**
- [workflows.md](references/workflows.md) — Sequential, conditional, loops
- [output-patterns.md](references/output-patterns.md) — Templates, formatting
- [anti-patterns.md](references/anti-patterns.md) — Common mistakes

### Step 5: Package & Validate

```bash
scripts/package_skill.py <path/to/skill-folder>
scripts/quick_validate.py <path/to/skill-folder>
```

### Step 6: Deploy (ThepExcel)

```
┌─ Skill ใหม่
│   ├─ Public? (ใครก็ใช้ได้)  → /mnt/d/agent-skills/[skill-name]/
│   └─ Private? (เฉพาะพี่ระ)  → /mnt/d/claude-private/skills/[skill-name]/
│
├─ Symlink ไป global
│   └─ ln -s /mnt/d/[repo]/[skill-name] ~/.claude/skills/[skill-name]
│
├─ Update registry
│   └─ เพิ่มใน /mnt/d/claude-master/CLAUDE.md → Skills Inventory
│
└─ Commit & Push
    └─ git add → commit → push (ทั้ง skill repo + claude-master)
```

### Step 7: Iterate

1. ใช้ skill กับงานจริง
2. สังเกตจุดที่ติดขัด
3. ปรับปรุง (ใช้ Enhancement Mode)

See [evaluation.md](references/evaluation.md) for Claude A/B testing pattern.

---

## Content Guidelines

### Avoid Time-Sensitive Information

```markdown
# Bad
If you're doing this before August 2025, use the old API.

# Good
## Current method
Use the v2 API endpoint.
```

### Use Consistent Terminology

เลือกคำเดียว ใช้ตลอดทั้ง skill:

| Good | Bad |
|------|-----|
| Always "API endpoint" | Mix "endpoint", "URL", "route" |
| Always "extract" | Mix "extract", "pull", "get" |

---

## Quality Checklist

### Core
- [ ] Description: what + when, third person, specific triggers
- [ ] SKILL.md body < 500 lines
- [ ] No time-sensitive info, consistent terminology
- [ ] Concrete examples (not abstract)
- [ ] References one level deep

### Code
- [ ] Scripts handle errors, no magic constants
- [ ] Required packages listed
- [ ] Forward slashes (no Windows paths)

### Testing
- [ ] Tested with real usage scenarios
- [ ] Tested with target models

---

## Enhancement Mode

ใช้เมื่อ **ปรับปรุง skill เดิม**

### Route Decision

| Condition | Path |
|-----------|------|
| Quick fix (typo, small gap) | Direct edit → skip audit |
| Significant upgrade | Full pipeline below |

### Full Enhancement Pipeline

```
1. AUDIT → 2. RESEARCH → 3. INTEGRATE → 4. OPTIMIZE → 5. VALIDATE
```

#### Step 1: AUDIT

อ่าน target skill → score ด้วย [audit rubric](references/audit-rubric.md):

| Dimension | Score 1-5 |
|-----------|-----------|
| Coverage | ครอบคลุม domain แค่ไหน? |
| Depth | Surface-level หรือ expert? |
| Structure | Progressive disclosure ดีไหม? |
| Actionability | Claude execute ได้เลยไหม? |
| Examples | มี concrete examples ไหม? |

**Present ผลแบบนี้:**

```
SKILL: [name]
SCORES: Coverage [?] | Depth [?] | Structure [?] | Actionability [?] | Examples [?]
TOTAL: [?]/25 → [Draft/Working/Solid/Production]

จุดที่ควรปรับ:
1. [ปัญหา + ผลกระทบ]
2. [ปัญหา + ผลกระทบ]
```

→ **ถามผู้ใช้ก่อน:** "ปรับทั้งหมด หรือเลือกเฉพาะข้อ?"

#### Step 2: RESEARCH

ใช้ `/deep-research` หรือ `/extract-expertise` เพื่อเติม knowledge gaps

#### Step 3: INTEGRATE

Classify findings → prioritize by impact → merge ด้วย [integration patterns](references/integration-patterns.md)

#### Step 4: OPTIMIZE

Apply skill-creator standards: progressive disclosure, conciseness, references/

#### Step 5: VALIDATE

Before/after comparison:

```
| Dimension | Before | After | เปลี่ยนอะไร |
|-----------|--------|-------|------------|
```

→ Log ใน [enhancement-log.md](references/enhancement-log.md)

### Enhancement Rules

- **Research BEFORE writing** — อย่าเดา domain knowledge
- **Preserve what works** — enhance ไม่ใช่ rewrite
- **Show evidence** — link findings to changes

### Example: boost-intel Enhancement

```
BEFORE: 17/25 (Solid) — Examples 2/5, Actionability 3/5
CHANGES:
  1. +Quick Mode (30-sec sanity check)
  2. +Facilitation Guide (how Claude walks through phases)
  3. Move CAPTURE → reference (reduce bloat)
  4. +Concrete example (WordPress vs CMS — full loop)
  5. Expand REFLECT (deeper questions + pattern recognition)
AFTER: 23/25 (Production) — all dimensions ≥ 4
```

---

## Facilitation Guide

### Create Mode

```
1. ถาม: "อยากสร้าง skill อะไรคะ? ช่วยยกตัวอย่าง 2-3 scenarios"
2. วิเคราะห์: public หรือ private? simple หรือ complex?
3. ถ้า complex → ใช้ /extract-expertise ก่อน
4. Init → Edit → Test → Package → Deploy
5. สรุป: "Skill [name] สร้างเสร็จแล้วค่ะ อยู่ที่ [path]"
```

### Enhance Mode

```
1. อ่าน SKILL.md + references ทั้งหมด
2. Audit → present ผลเป็นตาราง
3. ถาม: "ปรับทั้งหมด หรือเลือกข้อ?"
4. ทำตามที่ user เลือก
5. Before/after comparison → commit
```

### Key Behaviors

- **ถามก่อนทำ** — ไม่ rewrite โดยไม่ถาม
- **Show scores** — ผู้ใช้ต้องเห็นว่าอะไรดี อะไรไม่ดี
- **ทำทีละ step** — ไม่ dump ทุกอย่างทีเดียว

---

## References

| File | Content |
|------|---------|
| [progressive-disclosure.md](references/progressive-disclosure.md) | Loading patterns (high-level, domain, conditional) |
| [workflows.md](references/workflows.md) | Sequential, conditional, feedback loops |
| [output-patterns.md](references/output-patterns.md) | Templates, examples, terminology |
| [anti-patterns.md](references/anti-patterns.md) | Common mistakes to avoid |
| [evaluation.md](references/evaluation.md) | Claude A/B testing pattern |
| [audit-rubric.md](references/audit-rubric.md) | Quality scoring (5 dimensions, 1-5 each) |
| [integration-patterns.md](references/integration-patterns.md) | How to merge findings into skills |
| [enhancement-log.md](references/enhancement-log.md) | History of skill enhancements |

---

## Related Skills

- `/extract-expertise` — Extract expert knowledge to inform skill content
- `/deep-research` — Research domain before building or enhancing skill
- `/optimize-prompt` — Optimize skill descriptions and system prompts
