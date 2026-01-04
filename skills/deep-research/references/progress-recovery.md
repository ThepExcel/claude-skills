# Progress & Recovery

Techniques for transparency, state management, and error recovery during long research tasks.

**Inspired by:** Gemini's thinking panel, Manus's context engineering, DeepSeek's extended thinking

## Contents
- [Progress Markers](#progress-markers)
- [Interim Save](#interim-save)
- [Error Recovery](#error-recovery)
- [Context Management](#context-management)

---

## Progress Markers

**Purpose:** Show research progress during long tasks.

**When to use:**
- Deep/Exhaustive tier (always)
- Research exceeds 5 minutes
- User requests visibility

**Format:**
```markdown
> 🔍 **Phase 3:** Retrieved 15 sources, identified 3 gaps, refining queries...
> ✅ **Phase 4:** Verified 8 C1 claims, 2 contradictions flagged for Red Team
> 🔄 **Phase 3.5:** Gap analysis complete, executing 4 follow-up queries
> ⚠️ **Backtrack:** Dead-end on [topic], pivoting to alternative angle
```

**Rules:**
- Keep updates to single line
- Include phase number
- Show concrete numbers (sources, claims, gaps)

---

## Interim Save

**Purpose:** Save progress to prevent context loss.

**When to save:**
- After Phase 4 (TRIANGULATE) completion
- After 20+ sources collected
- Before Red Team phase
- When context approaches limit

**Save Format:**

```markdown
## Interim Research State

**Timestamp:** [ISO timestamp]
**Phase completed:** [Current phase]
**Sources collected:** [N]
**C1 claims verified:** [N]

### Key Findings So Far
1. [Finding 1] — Confidence: [LEVEL]
2. [Finding 2] — Confidence: [LEVEL]

### Gaps Remaining
- [Gap 1]
- [Gap 2]

### Failed Paths (avoid repeating)
- ❌ [Query 1] → [Reason]
- ❌ [Query 2] → [Reason]

### Next Steps
1. [Action 1]
2. [Action 2]
```

**Save Location:**
- For file output: Append to research document
- For conversation: Include in context for continuation

---

## Error Recovery

**If research is interrupted:**

1. **Check interim save** for last known state
2. **Resume from last completed phase**
3. **Avoid re-searching failed paths** (check error trace)
4. **Validate existing claims** still hold (for time-sensitive topics)

**Error Trace Format:**
```markdown
### Failed Paths (avoid repeating)
- ❌ "[query]" → Paywall, no accessible content
- ❌ "[query]" → Results outdated (>6 months)
- ❌ "[query]" → Tangential, not relevant to core question
```

---

## Context Management

**From Manus's context engineering learnings:**

### Attention Anchoring

Problem: "Lost-in-the-middle" — model forgets objectives in long context.

**Solutions:**
- Keep active todo/task list updated throughout research
- Recite key objectives periodically
- Place critical info at context start AND end

### Memory Extension

**Use file system for:**
- Large interim data (>20 sources)
- Detailed source notes
- Failed path logs

**Compression strategies:**
- Compress observations while preserving key pointers (URLs, dates)
- Keep summaries in context, details in files
- Reference files by path, don't inline large content

### Failed Path Tracking

**Keep failed searches in context to avoid:**
- Repeating same unsuccessful queries
- Hitting same paywalls
- Searching outdated terms

```markdown
### Failed Paths
- ❌ "GPT-4 features 2024" → Outdated, use "GPT-5 features 2025"
- ❌ "OpenAI pricing page" → 403, use press releases instead
- ❌ "[product] API docs" → Requires auth, use r.jina.ai fallback
```

---

## Tier-Specific Recommendations

| Feature | Quick | Standard | Deep | Exhaustive |
|---------|-------|----------|------|------------|
| Progress markers | ❌ | Optional | ✅ | ✅ |
| Interim save | ❌ | ❌ | ✅ | ✅ |
| Error trace | Optional | ✅ | ✅ | ✅ |
| Full context management | ❌ | ❌ | Optional | ✅ |
