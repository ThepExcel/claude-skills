---
name: skill-creator-thepexcel
description: Create new skills, modify and improve existing skills, and measure skill performance. Use when users want to create a skill from scratch, update or optimize an existing skill, run evals to test a skill, benchmark skill performance with variance analysis, optimize a skill's description for better triggering accuracy, or audit existing skill quality with a structured scoring rubric.
license: Apache 2.0 (see LICENSE.txt)
---

# Skill Creator (ThepExcel Edition)

> Based on [Anthropic's official skill-creator](https://github.com/anthropics/skills) (Apache 2.0). Enhanced with ThepExcel deployment workflow and structured audit/enhancement pipeline.

## Quick Start

| ต้องการ | Mode | ไปที่ |
|---------|------|-------|
| สร้าง skill ใหม่ | **Create** | → [Creating a Skill](#creating-a-skill) |
| ทดสอบ skill ด้วย evals | **Eval** | → [Running and Evaluating](#running-and-evaluating-test-cases) |
| ปรับปรุงตาม feedback | **Improve** | → [Improving the Skill](#improving-the-skill) |
| ตรวจคุณภาพ + enhance อย่าง structured | **Enhance** | → [Enhancement Mode](#enhancement-mode) |
| วัดผล regression / เทียบ versions | **Benchmark** | → [Benchmark & Description Opt.](#benchmark--description-optimization) |
| Deploy ไป ThepExcel infrastructure | **Deploy** | → [Deploy](#deploy-thepexcel) |

Figure out where the user is in this process and jump in. If they already have a draft, go straight to eval/iterate. If they say "just vibe with me", do that.

---

## Core Principles

**Concise is key** — Context window เป็นทรัพยากรที่แชร์กัน ทุกบรรทัดต้องจ่ายค่า token

**Explain the why** — อธิบาย *ทำไม* ไม่ใช่แค่ *อะไร* Claude ฉลาดพอ generalize จาก reasoning ดีกว่า rule แข็งทื่อ ถ้าจะเขียน ALWAYS/NEVER all caps → yellow flag: reframe เป็น reasoning แทน

**Generalize, don't overfit** — Test cases คือตัวอย่าง ไม่ใช่ spec ทั้งหมด หา pattern ที่ work broadly

**Keep the prompt lean** — อ่าน transcript จริง ถ้า skill ทำให้ waste time → ตัดออก

**Degrees of Freedom**:

| Level | เมื่อไหร่ | ตัวอย่าง |
|-------|----------|---------|
| High (text) | หลายวิธีถูกได้ | Code review guidelines |
| Medium (pseudocode) | มี pattern ที่ prefer | Report template |
| Low (scripts) | ต้องการ consistency | Database migrations |

---

## Skill Structure

```
skill-name/
├── SKILL.md (required)     ← < 500 lines ideal
│   ├── YAML frontmatter    ← name + description (+ compatibility optional)
│   └── Markdown body
├── agents/                 ← subagent instructions (grader, comparator, analyzer)
├── eval-viewer/            ← generate_review.py + viewer.html
├── assets/                 ← eval_review.html template
├── scripts/                ← deterministic code (execute without loading into context)
├── references/             ← loaded on demand (one level deep only)
└── evals/                  ← evals.json + test files
```

**Progressive Disclosure** (3 levels):
1. Metadata (name + description) — always in context (~100 words)
2. SKILL.md body — when triggered (< 500 lines)
3. Bundled resources — as needed

**Frontmatter**: `name` max 64 chars kebab-case, `description` max 1024 chars third person what + when

**"When to use" in body = useless** — Claude sees description only when deciding to trigger. Put all trigger context there.

**Description tip**: Make it slightly "pushy" to combat undertriggering — include specific contexts even if not explicitly named.

For anti-patterns: [anti-patterns.md](references/anti-patterns.md)

---

## Creating a Skill

### Step 1: Capture Intent

ถามถ้าไม่ชัด หรือ extract จาก conversation ถ้ามีอยู่แล้ว:

1. Skill ควรทำอะไร?
2. Trigger เมื่อไหร่? (user phrases/contexts)
3. Expected output format?
4. ต้องการ test cases ไหม? — Skills ที่มี objective output ควรมี (file transforms, data extraction, fixed workflows) / Subjective skills (writing style, art) ไม่จำเป็น

### Step 2: Interview & Research

ถาม edge cases, input/output formats, example files, dependencies
Check available MCPs — research via subagents ถ้าทำได้
ใช้ `/extract-expertise` สำหรับ domain ที่ซับซ้อน

### Step 3: Initialize

```bash
scripts/init_skill.py <skill-name> --path <output-directory>
```

### Step 4: Write SKILL.md

ใส่: name, description (primary trigger mechanism — all "when to use" goes here), instructions

**Writing style**: imperative form, explain *why* behind each instruction, not rigid rules. Use theory of mind.

**Design references:**
- [workflows.md](references/workflows.md) — Sequential, conditional, loops
- [output-patterns.md](references/output-patterns.md) — Templates, formatting
- [anti-patterns.md](references/anti-patterns.md) — Common mistakes

### Step 5: Write Test Cases

2-3 realistic prompts — the kind of thing a real user would actually say. Share with user for confirmation. Save to `evals/evals.json` (don't add assertions yet):

```json
{
  "skill_name": "example-skill",
  "evals": [
    {
      "id": 1,
      "prompt": "User's task prompt",
      "expected_output": "Description of expected result",
      "files": [],
      "expectations": []
    }
  ]
}
```

See [references/schemas.md](references/schemas.md) for full schema including assertions field.

---

## Running and Evaluating Test Cases

This is one continuous sequence — don't stop partway. Do NOT use any other testing skill.

Put results in `<skill-name>-workspace/` (sibling to skill directory), organized by `iteration-N/eval-name/`.

### Step 1: Spawn All Runs in the Same Turn

For each test case, launch **two subagents simultaneously** — one with-skill, one baseline. Don't launch with-skill first and come back for baselines later.

- **New skill**: baseline = no skill at all, save to `without_skill/outputs/`
- **Improving existing skill**: baseline = old version snapshot (`cp -r <skill-path> <workspace>/skill-snapshot/`), save to `old_skill/outputs/`

Write `eval_metadata.json` for each eval:
```json
{
  "eval_id": 0,
  "eval_name": "descriptive-name",
  "prompt": "The task prompt",
  "assertions": []
}
```

### Step 2: While Runs Are in Progress, Draft Assertions

Don't wait idle. Draft objectively verifiable assertions with descriptive names (they appear in the viewer). Explain them to the user. Subjective skills → qualitative only, skip assertions.

Update `eval_metadata.json` and `evals/evals.json` with assertions.

### Step 3: Capture Timing Data

When each subagent completes, save immediately — this data exists only in the task notification:

```json
{"total_tokens": 84852, "duration_ms": 23332, "total_duration_seconds": 23.3}
```

Save to `timing.json` in the run directory.

### Step 4: Grade → Aggregate → Analyze → Launch Viewer

1. **Grade** — spawn grader subagent using `agents/grader.md`, save to `grading.json`. For assertions checkable programmatically, write a script rather than eyeballing.

2. **Aggregate** — run from skill-creator directory:
   ```bash
   python -m scripts.aggregate_benchmark <workspace>/iteration-N --skill-name <name>
   ```
   Produces `benchmark.json` and `benchmark.md` with pass_rate, time, tokens (mean ± stddev + delta).

3. **Analyst pass** — read `agents/analyzer.md` (Analyzing Benchmark Results section) to surface patterns aggregate stats hide: non-discriminating assertions, high-variance evals, time/token tradeoffs.

4. **Launch viewer**:
   ```bash
   nohup python <skill-creator-path>/eval-viewer/generate_review.py \
     <workspace>/iteration-N \
     --skill-name "my-skill" \
     --benchmark <workspace>/iteration-N/benchmark.json \
     > /dev/null 2>&1 &
   VIEWER_PID=$!
   ```
   Iteration 2+: add `--previous-workspace <workspace>/iteration-<N-1>`

   Cowork/headless: use `--static <output_path>` instead. Feedback downloads as `feedback.json`.

   ⚠️ **GENERATE THE EVAL VIEWER BEFORE evaluating inputs yourself.** Get results in front of the human first.

5. **Tell the user**: "ผลอยู่ในเบราว์เซอร์แล้วค่ะ — tab Outputs ดู output แต่ละ test case, tab Benchmark ดู metrics เมื่อดูเสร็จแล้วกลับมาบอกหนูได้เลย"

### Step 5: Read Feedback

Read `feedback.json`. Empty feedback = satisfied. Focus on test cases with specific complaints.

Kill viewer: `kill $VIEWER_PID 2>/dev/null`

---

## Improving the Skill

### How to Think About Improvements

1. **Generalize** — หา pattern ที่ work broadly ไม่ใช่ fix specific test case
2. **Keep lean** — อ่าน transcript จริง ถ้า skill ทำให้ waste time → ตัดออก
3. **Explain the why** — ถ้าจะเขียน ALWAYS/NEVER → yellow flag: reframe เป็น reasoning แทน
4. **Bundle repeated work** — ถ้า 3 test cases ล้วน write `create_docx.py` เอง → bundle ใน `scripts/`

### Iteration Loop

1. Apply improvements to skill
2. Rerun all test cases into `iteration-<N+1>/` (including baselines)
3. Launch viewer with `--previous-workspace` pointing at previous iteration
4. Wait for user review → read feedback → repeat

Stop when: user satisfied / all feedback empty / not making meaningful progress.

For quick fixes (typo, small gap): direct edit → skip eval loop.

### Blind Comparison (Advanced)

For rigorous version comparison, read `agents/comparator.md` + `agents/analyzer.md` for blind A/B judgment. Optional — the human review loop is usually sufficient.

---

## Enhancement Mode

ใช้เมื่อต้องการปรับปรุง **skill เดิมที่มีอยู่แล้ว** แบบ structured — เหมาะเมื่อยังไม่รู้ว่า skill มีปัญหาตรงไหน หรืออยากยก quality ขึ้นเป็น systematic

### Route

| Condition | Path |
|-----------|------|
| Quick fix (typo, small gap) | Direct edit → done |
| Significant upgrade | Full pipeline below |

### Full Pipeline: AUDIT → RESEARCH → INTEGRATE → OPTIMIZE → VALIDATE

#### AUDIT

อ่าน target skill ทั้งหมด → score ด้วย [audit-rubric.md](references/audit-rubric.md):

```
SKILL: [name]
SCORES: Coverage [?] | Depth [?] | Structure [?] | Actionability [?] | Examples [?]
TOTAL: [?]/25 → [Draft/Working/Solid/Production]

จุดที่ควรปรับ:
1. [ปัญหา + ผลกระทบ]
```

→ ถามผู้ใช้ก่อน: "ปรับทั้งหมด หรือเลือกเฉพาะข้อ?"

#### RESEARCH

ใช้ `/deep-research` หรือ `/extract-expertise` เพื่อเติม knowledge gaps

#### INTEGRATE

Classify findings → prioritize by impact → merge ด้วย [integration-patterns.md](references/integration-patterns.md)

#### OPTIMIZE

Apply skill-creator standards: progressive disclosure, conciseness, references/

#### VALIDATE

Before/after comparison:
```
| Dimension | Before | After | เปลี่ยนอะไร |
|-----------|--------|-------|------------|
```

Log ใน [enhancement-log.md](references/enhancement-log.md) → จากนั้นรัน Eval loop เพื่อยืนยัน improvement จริง

---

## Benchmark & Description Optimization

### Benchmark

Rerun all evals 3x per configuration with `aggregate_benchmark.py`. Track pass rate, time, tokens across iterations/models. ใช้สำหรับ regression detection เมื่อ model อัปเดต หรือหลัง enhance

### Description Optimization

หลัง skill เสร็จ เสนอให้ optimize description สำหรับ triggering accuracy ที่ดีขึ้น

**Step 1**: Generate 20 trigger eval queries (mix should/should-not trigger). Be realistic — personal context, file paths, casual speech, typos. Near-miss negatives are the most valuable test cases.

Present via HTML template:
1. Read `assets/eval_review.html`, fill: `__EVAL_DATA_PLACEHOLDER__`, `__SKILL_NAME_PLACEHOLDER__`, `__SKILL_DESCRIPTION_PLACEHOLDER__`
2. Write to `/tmp/eval_review_<skill-name>.html` → open it
3. User edits, clicks "Export Eval Set" → `~/Downloads/eval_set.json`

**Step 2**: Run optimization loop (background):
```bash
python -m scripts.run_loop \
  --eval-set <path-to-trigger-eval.json> \
  --skill-path <path-to-skill> \
  --model <model-id-powering-this-session> \
  --max-iterations 5 \
  --verbose
```
Splits 60/40 train/test, iterates up to 5x, returns `best_description` selected by test score to avoid overfitting.

**Step 3**: Apply `best_description` to SKILL.md frontmatter. Show before/after + scores.

Note: requires `claude -p` CLI → Claude Code only, not Claude.ai

---

## Deploy (ThepExcel)

```
┌─ Skill ใหม่
│   ├─ Public?   → /mnt/d/agent-skills/[skill-name]/
│   └─ Private?  → /mnt/d/claude-private/skills/[skill-name]/
│
├─ Symlink
│   └─ ln -s /mnt/d/[repo]/[skill-name] ~/.claude/skills/[skill-name]
│
├─ Update registry
│   └─ /mnt/d/claude-master/CLAUDE.md → Skills Inventory
│
└─ Commit & Push
    └─ git add → commit → push (ทั้ง skill repo + claude-master)
```

Validate before deploy:
```bash
scripts/quick_validate.py <path/to/skill-folder>
scripts/package_skill.py <path/to/skill-folder>
```

---

## Platform Notes

| Platform | Subagents | Viewer | Description Opt |
|----------|-----------|--------|-----------------|
| **Claude Code** | ✅ Parallel | ✅ Browser | ✅ |
| **Claude.ai** | ❌ → run serially | ❌ → show inline | ❌ |
| **Cowork** | ✅ | `--static` flag | ✅ |

**Claude.ai**: skip baselines + benchmarking, run test cases yourself one at a time, show results + ask feedback inline.

---

## References

| File | Content |
|------|---------|
| [references/schemas.md](references/schemas.md) | JSON structures: evals.json, grading.json, benchmark.json, timing.json, etc. |
| [references/progressive-disclosure.md](references/progressive-disclosure.md) | Loading patterns (high-level, domain, conditional) |
| [references/workflows.md](references/workflows.md) | Sequential, conditional, feedback loops |
| [references/output-patterns.md](references/output-patterns.md) | Templates, formatting, terminology |
| [references/anti-patterns.md](references/anti-patterns.md) | Common mistakes to avoid |
| [references/audit-rubric.md](references/audit-rubric.md) | Quality scoring 5 dimensions × 1-5 |
| [references/integration-patterns.md](references/integration-patterns.md) | How to merge findings into skills |
| [references/enhancement-log.md](references/enhancement-log.md) | History of skill enhancements |
| [agents/grader.md](agents/grader.md) | Evaluate assertions against outputs |
| [agents/comparator.md](agents/comparator.md) | Blind A/B comparison between two outputs |
| [agents/analyzer.md](agents/analyzer.md) | Analyze benchmark patterns + why one version beat another |

---

## Related Skills

- `/extract-expertise` — Extract expert knowledge to inform skill content
- `/deep-research` — Research domain before building or enhancing skill
- `/optimize-prompt` — Optimize skill descriptions and system prompts
