# System Prompt vs User Prompt Guide

## Core Principle

> "Anything requiring **consistency across sessions and users** belongs in system prompt. Anything **specific to this interaction** belongs in user prompt."

---

## Decision Matrix

| Question | System | User |
|----------|--------|------|
| Will this apply to ALL users? | ✅ | |
| Is this the AI's "personality"? | ✅ | |
| Is this a one-time task? | | ✅ |
| Does this contain user's input? | | ✅ |
| Is this a safety/boundary rule? | ✅ | |
| Is this dynamic context (date)? | API: ✅ | n8n: use variables |
| Is this output format spec? | ✅ | |
| Is this a specific question? | | ✅ |

---

## What Goes Where

### System Prompt Content

| Category | Examples |
|----------|----------|
| **Role/Persona** | "You are a customer support agent for Acme Corp" |
| **Persistent behavior** | Tone, formality, verbosity level |
| **Output format** | "Always respond in JSON", "Use markdown tables" |
| **Boundaries & rules** | "Never share personal data", "Always ask before deleting" |
| **Tool usage** | "Use the search tool before answering factual questions" |
| **Knowledge context** | Company-specific info, domain knowledge |

### User Prompt Content

| Category | Examples |
|----------|----------|
| **Specific task** | "Summarize this email", "Fix this bug" |
| **Dynamic content** | User's actual input, uploaded files |
| **Task-specific context** | "Here's the document to analyze" |
| **Current session info** | User details, conversation history |
| **One-time instructions** | "Make this one longer than usual" |

---

## Common Mistakes

### Mistake 1: Everything in System Prompt
```
# Bad: Task-specific in system
System: "Summarize the following document about climate change..."

# Good: Task in user prompt
System: "You are a helpful assistant that summarizes documents clearly."
User: "Summarize this document about climate change: [content]"
```

### Mistake 2: Everything in User Prompt
```
# Bad: Behavior repeated every time
User: "You are a helpful assistant. Be concise. Use markdown. Now answer: What is Python?"

# Good: Behavior in system
System: "You are a helpful assistant. Be concise. Use markdown."
User: "What is Python?"
```

### Mistake 3: Hardcoded Dynamic Data
```
# Bad: Static date in system
System: "Today is January 2, 2026..."

# Good: Dynamic variable (n8n)
System: "Today is {{ $now.format('MMMM d, yyyy') }}"

# Good: Inject at runtime (API)
system_prompt = f"Today is {datetime.now().strftime('%B %d, %Y')}"
```

---

## Platform-Specific Guidance

### Claude API
```python
response = client.messages.create(
    model="claude-sonnet-4-5-20250514",
    system="You are a helpful assistant...",  # System
    messages=[
        {"role": "user", "content": "User's request"}  # User
    ]
)
```

### OpenAI API
```python
response = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "system", "content": "You are a helpful assistant..."},
        {"role": "user", "content": "User's request"}
    ]
)
```

### Gemini API
```python
model = genai.GenerativeModel(
    model_name="gemini-2.0-flash",
    system_instruction="You are a helpful assistant..."  # System
)
response = model.generate_content("User's request")  # User
```

### n8n
- **System Message:** In AI Agent node configuration
- **User Message:** From trigger/input nodes
- **Dynamic variables:** `{{ $json.field }}`, `{{ $now }}`

---

## Production Considerations

### Token Efficiency
- System prompt: Sent once, reused (can be cached)
- User prompt: Sent each time
- **Optimization:** Put stable content in system, variable in user

### Prompt Caching (Claude)
```
System prompt → Cached (90% cost reduction)
Examples → Cached
Reference docs → Cached
User query → Not cached (variable)
```

### Security
- System prompt: Developer-controlled, harder to manipulate
- User prompt: User-controlled, may contain injection attempts
- **Rule:** Critical safety rules go in system prompt

---

## Quick Reference

```
┌─────────────────────────────────────────────────┐
│                 SYSTEM PROMPT                    │
│  • WHO the AI is (role, persona)                │
│  • HOW it should behave (tone, rules)           │
│  • WHAT format to use (output structure)        │
│  • BOUNDARIES (what not to do)                  │
└─────────────────────────────────────────────────┘
                        ↓
┌─────────────────────────────────────────────────┐
│                  USER PROMPT                     │
│  • WHAT to do now (specific task)               │
│  • WITH what (input data, context)              │
│  • FOR this case (one-time modifications)       │
└─────────────────────────────────────────────────┘
```
