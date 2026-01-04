# Platform-Specific Optimization Guide

## Claude API

### Structure
- **Format:** XML tags (Claude is fine-tuned to parse XML)
- **Tag names:** Semantic (`<instructions>`, `<context>`, not `<section1>`)

### Best Practices
```xml
<context>
Role and project description
</context>

<instructions>
1. Step one
2. Step two
</instructions>

<examples>
<example type="good">...</example>
<example type="bad">...</example>
</examples>
```

### Key Points
- Use `tools` API parameter for tools (not prompt injection) — +2% accuracy
- Claude 4.x takes instructions literally — be explicit
- Add context/motivation: "Your response will be read aloud by TTS, so never use ellipses"
- Avoid "think" word with Opus 4.5 when extended thinking disabled — use "consider", "evaluate"

### Anti-Over-Engineering (Opus Required)
```
Avoid over-engineering. Only make changes that are directly requested.
Keep solutions simple and focused. Don't add features beyond what was asked.
Don't create helpers or abstractions for one-time operations.
```

---

## OpenAI API (GPT-4/5)

### Structure
- **Format:** Message roles (`system`, `user`, `assistant`)
- **System message:** Role, behavior, constraints

### Best Practices
```python
messages = [
    {"role": "system", "content": "You are a helpful assistant..."},
    {"role": "user", "content": "User's request..."}
]
```

### Key Points
- Pin model version for production: `gpt-4.1-2025-04-14`
- Use `tools` parameter for function calling (not prompt injection)
- GPT-5.2: More concise by default, stronger instruction adherence
- For conciseness: "Your response should be composed of smoothly flowing prose paragraphs"

### Verbosity Control
```
When writing reports, write in clear, flowing prose using complete paragraphs.
Avoid excessive bullet points. Instead, incorporate items naturally into sentences.
```

---

## Gemini API

### Structure
- **Format:** XML tags OR Markdown (pick one, don't mix)
- **System instructions:** Separate field in API

### Best Practices
```python
model = genai.GenerativeModel(
    model_name="gemini-2.0-flash",
    system_instruction="You are a helpful assistant..."
)
```

### Key Points
- **Critical instructions at END** for long context
- Temperature = 1.0 is optimal (don't change)
- Default is concise — request detail explicitly if needed
- Add knowledge cutoff: "Your knowledge cutoff date is January 2025"

### Grounding Clause
```
You are a strictly grounded assistant limited to the information provided.
In your answers, rely only on the facts that are directly mentioned in the context.
```

---

## CLAUDE.md (Claude Code)

### Structure
- **Format:** XML tags + Markdown hybrid
- **Loaded:** Every session automatically

### Best Practices
```markdown
<context>
Project description and your role
</context>

<principles>
Core rules that apply to all tasks
</principles>

<instructions>
## Common Workflows
...
</instructions>
```

### Key Points
- **Keep inline** — no progressive disclosure (loaded every session anyway)
- **150-200 instructions** recommended max
- Include: context, principles, workflows, troubleshooting
- Exclude: API docs, rarely-used details, things Claude already knows

### What to Include
| Include | Exclude |
|---------|---------|
| Project context & role | External API documentation |
| Core principles & rules | Rarely-used details |
| Common workflows | Tutorial explanations |
| Troubleshooting | Things Claude knows |

---

## ChatGPT Custom Instructions

### Structure
- **Format:** Markdown (plain text)
- **Limit:** 1500 characters per field

### Best Practices
```markdown
## About Me
- I work on [X]
- I prefer [style]

## How to Respond
- Be concise
- Use code blocks for code
- Always explain tradeoffs
```

### Key Points
- **Two fields:** "About you" + "How to respond"
- Use Memory for personal preferences, Custom Instructions for format
- Layer: User level → Project level → Custom GPT → Chat
- Keep concise due to character limit

---

## n8n & Workflow Tools

### Structure
- **Format:** Plain text with dynamic variables
- **System prompt:** In AI Agent node configuration

### Best Practices
```
You are a [specific role] that helps users with [specific tasks].
Your goal is to [main objective].
You have access to the following tools: [list tools].
Current date: {{ $now.format('yyyy-MM-dd') }}
```

### Key Points
- **Make prompts dynamic:** Use `{{ $now }}` for dates
- **Rename tools clearly:** "AddEntry" not "Tool1"
- **Add memory node:** For multi-turn conversations
- **Define explicit boundaries:** Permission checks, rate limits

### Tool Naming
```
# Bad
Tool1, Tool2, Helper

# Good
AddCalendarEntry, SearchDatabase, SendEmail
```

---

## Platform Comparison Matrix

| Aspect | Claude API | OpenAI API | Gemini API | CLAUDE.md | ChatGPT | n8n |
|--------|------------|------------|------------|-----------|---------|-----|
| Format | XML | Roles | XML/MD | XML+MD | MD | Plain |
| Tools | API field | API field | API field | N/A | Actions | Nodes |
| Limit | 200K tokens | 128K | 2M | ~200 instructions | 1500 chars | Varies |
| Model clause | Anti-over-eng | Verbosity | Grounding | Anti-over-eng | Concise | Boundaries |
