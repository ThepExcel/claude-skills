# Agent Skills

A model-agnostic collection of skills for AI coding agents. Works with Claude Code, Cursor, Windsurf, and other AI-powered tools.

**See also:** [agentskills.io](https://agentskills.io/) - The community hub for AI agent skills

**Author:** [ThepExcel](https://www.thepexcel.com) • **License:** MIT

---

## Installation Methods

### Method 1: Plugin Marketplace (Recommended)

Easiest way - works with `claude plugin install`:

```bash
claude plugin install ThepExcel/thepexcel-claude-plugins
```

This installs from the [thepexcel-claude-plugins](https://github.com/ThepExcel/thepexcel-claude-plugins) repo (auto-synced from this repo).

### Method 2: Manual Installation

**User-level (all projects):**
```bash
git clone https://github.com/ThepExcel/agent-skills.git
mkdir -p ~/.claude/skills
cp -r agent-skills/deep-research ~/.claude/skills/
rm -rf agent-skills
```

**Project-level (current project only):**
```bash
git clone https://github.com/ThepExcel/agent-skills.git
mkdir -p .claude/skills
cp -r agent-skills/deep-research .claude/skills/
rm -rf agent-skills
```

### Installation Scopes

| Scope | Location | Availability |
|-------|----------|--------------|
| **User** | `~/.claude/skills/` | All your projects |
| **Project** | `.claude/skills/` | Current project only |

---

## Available Skills

| Skill | Description |
|-------|-------------|
| `deep-research` | 8-phase research with citations and source verification |
| `triz` | TRIZ innovation methodology for technical problem-solving |
| `explain-concepts` | Educational explanations with Feynman, Socratic methods |
| `problem-solving` | Systematic problem analysis with Polya method |
| `generate-creative-ideas` | Creative ideation with SCAMPER and more |
| `design-business-model` | Business Model Canvas and Lean Canvas |
| `manage-business-strategy` | Strategic analysis frameworks |
| `power-query-coaching` | Power Query M code coaching |
| `optimize-prompt` | AI prompt optimization for various platforms |
| `prompt-ai-image-video` | Image/video generation prompts |
| `extract-expertise` | Extract domain knowledge from experts |
| `create-visualization` | Diagrams and Manim animations |
| `skill-creator-thepexcel` | Create new Claude skills |

---

## For AI Agents: Claude Code Complete Reference

This section is designed for AI agents (Claude, GPT, etc.) to understand Claude Code's architecture and use it effectively.

### Table of Contents

1. [Configuration Scope System](#1-configuration-scope-system)
2. [CLAUDE.md System](#2-claudemd-system)
3. [Skills vs Slash Commands](#3-skills-vs-slash-commands)
4. [Creating Skills](#4-creating-skills)
5. [Creating Slash Commands](#5-creating-slash-commands)
6. [MCP (Model Context Protocol)](#6-mcp-model-context-protocol)
7. [Hooks System](#7-hooks-system)
8. [Plugin Marketplace](#8-plugin-marketplace)
9. [File Organization Best Practices](#9-file-organization-best-practices)
10. [New Commands & Features](#10-new-commands--features-v21)

---

### 1. Configuration Scope System

Claude Code uses a hierarchical configuration system with four scopes:

| Scope | Location | Applies To | Version Control |
|-------|----------|------------|-----------------|
| **Managed** | System directories (see below) | All users on machine | Yes (deployed by IT) |
| **User** | `~/.claude/` | All projects globally | No (personal) |
| **Project** | `.claude/` in repo root | Current project only | Yes (shared) |
| **Local** | `.claude/settings.local.json` | Current project, personal | No (gitignored) |

**Managed Settings Locations:**
- macOS: `/Library/Application Support/ClaudeCode/`
- Linux: `/etc/claude-code/`
- Windows: `C:\Program Files\ClaudeCode\`

#### Precedence Order (highest to lowest)
1. **Managed** - Cannot be overridden (enterprise policies)
2. **Command line arguments** - Temporary session overrides
3. **Local** - Personal project overrides
4. **Project** - Team-shared settings
5. **User** - Personal defaults

#### Key Files by Scope

```
~/.claude/                          # USER SCOPE
├── settings.json                   # User preferences, permissions
├── CLAUDE.md                       # Global instructions for all projects
├── skills/                         # User-installed skills
├── commands/                       # User slash commands
├── agents/                         # User subagents
└── rules/                          # User-level rules (v2.0.64+)

.claude/                            # PROJECT SCOPE (version controlled)
├── settings.json                   # Project settings (includes hooks)
├── CLAUDE.md                       # Project-specific instructions
├── skills/                         # Project skills
├── commands/                       # Project slash commands
├── agents/                         # Project subagents
└── rules/                          # Modular rule files (v2.0.64+)

.claude/settings.local.json         # LOCAL SCOPE (gitignored)
CLAUDE.local.md                     # Personal project instructions (gitignored)
```

#### settings.json Structure

```json
{
  "permissions": {
    "allow": ["Bash(git:*)", "Bash(npm *)"],
    "deny": ["Bash(rm -rf:*)"],
    "defaultMode": "default"
  },
  "hooks": {
    "PreToolUse": [...]
  },
  "env": {
    "MY_VAR": "value"
  },
  "model": "claude-sonnet-4-20250514",
  "language": "thai",
  "attribution": {
    "commit": "Generated with AI\n\nCo-Authored-By: Claude <noreply@anthropic.com>",
    "pr": ""
  }
}
```

#### New Settings (v2.1+)

| Setting | Purpose | Example |
|---------|---------|---------|
| `language` | Response language | `"japanese"`, `"thai"` |
| `respectGitignore` | Control @ file picker | `true` (default) |
| `showTurnDuration` | Hide "Cooked for Xm Xs" | `false` |
| `attribution` | Customize commit/PR bylines | See above |
| `fileSuggestion` | Custom @ search command | `{"type": "command", "command": "..."}` |
| `autoUpdatesChannel` | Release channel | `"stable"` or `"latest"` |

---

### 2. CLAUDE.md System

CLAUDE.md files provide persistent instructions that Claude reads automatically at the start of every conversation.

#### File Locations (all are read, in order)

| Location | Purpose | When Read |
|----------|---------|-----------|
| Enterprise path (see Scope System) | Organization-wide instructions | Always |
| `~/.claude/CLAUDE.md` | Global user instructions | Always |
| `./CLAUDE.md` or `./.claude/CLAUDE.md` | Project root instructions | When in project |
| `./CLAUDE.local.md` | Personal project instructions | When in project (gitignored) |
| `./subdirectory/CLAUDE.md` | Directory-specific | When working in that directory |

#### Imports (v2.0.67+)

CLAUDE.md files can import other files using `@path/to/file` syntax:

```markdown
See @README.md for project overview and @package.json for npm commands.

# Additional Instructions
- Git workflow: @docs/git-instructions.md
- Personal prefs: @~/.claude/my-project-prefs.md
```

#### Modular Rules with `.claude/rules/` (v2.0.64+)

Organize instructions into multiple files:

```
.claude/rules/
├── code-style.md      # Code style guidelines
├── testing.md         # Testing conventions
├── security.md        # Security requirements
└── frontend/
    ├── react.md
    └── styles.md
```

**Path-specific rules** with frontmatter:

```markdown
---
paths:
  - "src/api/**/*.ts"
  - "lib/**/*.ts"
---

# API Development Rules
- All endpoints must include input validation
- Use standard error response format
```

#### Best Practices for CLAUDE.md

1. **Keep it concise** - ~150-200 instructions max for reliable following
2. **Use structured format** - Headers, tables, code blocks
3. **Include three elements:**
   - **WHAT**: Project structure, tech stack, file locations
   - **WHY**: Purpose, goals, context
   - **HOW**: Commands to run, coding conventions, verification steps

#### Extended Memory Options

Beyond the official CLAUDE.md system, there are community tools for enhanced memory:

| Tool | Description |
|------|-------------|
| **[claude-mem](https://github.com/thedotmack/claude-mem)** | Plugin that auto-captures session context and injects into future sessions |
| **[Memory Bank pattern](https://github.com/centminmod/my-claude-code-setup)** | Structured memory files adapted from Cline methodology |
| **MCP Memory servers** | Knowledge graph via MCP for cross-project preferences |
| **Simple `docs/` folder** | Store knowledge in docs/ and reference with `@docs/file.md` |

> **Tip:** Keep CLAUDE.md lean (loaded every session). Put detailed docs in separate files and use `@imports` or `@docs/` references.

#### CLAUDE.md Template

```markdown
# Project Name

## Context
Brief description of what this project does.

## Tech Stack
- Language: TypeScript
- Framework: Next.js
- Database: PostgreSQL

## Project Structure
\`\`\`
src/
├── components/    # React components
├── pages/         # Next.js pages
└── lib/           # Utility functions
\`\`\`

## Commands
- `npm run dev` - Start development server
- `npm test` - Run tests
- `npm run build` - Build for production

## Coding Conventions
- Use TypeScript strict mode
- Prefer functional components
- Write tests for new features

## Important Files
- `src/lib/api.ts` - API client
- `src/config.ts` - Configuration
```

---

### 3. Skills vs Slash Commands

#### Post v2.1.3: Just Use Skills

> **Key Change:** As of v2.1.3, skills and slash commands are **merged internally**. They work identically — both appear in `/` menu, both can be auto-triggered by Claude.

#### Recommendation: Always Create Skills

| Reason | Explanation |
|--------|-------------|
| **Same effort** | Minimal skill = just `skills/name/SKILL.md` (one folder + one file) |
| **More flexible** | Can add scripts, references, assets later without restructuring |
| **Cross-platform** | Works on Claude.ai, API, AND Claude Code |
| **Future-proof** | Skills are the direction Anthropic is investing in |

```
# Minimal skill structure
skills/my-task/
└── SKILL.md    # Same content as a command file would have
```

#### When Slash Commands Still Make Sense

Slash commands (`commands/name.md`) are only useful for:
- Legacy projects that already have them
- Quick throwaway scripts you'll delete soon

**For new work: just create skills.**

#### Comparison (for reference)

| Aspect | Skills | Slash Commands |
|--------|--------|----------------|
| **Location** | `skills/name/SKILL.md` | `commands/name.md` |
| **Supporting files** | Yes | No |
| **Cross-platform** | Claude.ai, API, Claude Code | Claude Code only |
| **Invocation** | `/name` or auto | `/name` or auto |
| **Recommendation** | **Use this** | Legacy only |

---

### 4. Creating Skills

#### Using the Official Skill-Creator

The easiest way to create skills is using the official `skill-creator` from Anthropic's plugin marketplace:

```bash
# Install from official Anthropic marketplace (auto-available)
/plugin install skill-creator@claude-plugins-official

# Then ask Claude to help create a skill
> Help me create a skill for [your use case]
```

Alternatively, you can install from the [Anthropic Skills repo](https://github.com/anthropics/skills):

```bash
/plugin marketplace add anthropics/skills
/plugin install skill-creator@anthropic-skills
```

#### Skill Directory Structure

```
skills/
└── my-skill/
    ├── SKILL.md              # Required: main instructions
    ├── SOURCES.md            # Recommended: attribution
    ├── scripts/              # Optional: executable code
    │   └── helper.py
    ├── references/           # Optional: supporting docs
    │   ├── guide.md
    │   └── examples.md
    └── assets/               # Optional: templates, images
        └── template.txt
```

#### SKILL.md Format

```markdown
---
name: skill-name
description: Describe when Claude should use this skill. Be specific about triggers.
allowed-tools:
  - Read
  - Grep
  - Glob
model: claude-sonnet-4-20250514
context: fork
agent: Explore
hooks:
  PreToolUse:
    - matcher: "Bash"
      hooks:
        - type: command
          command: "./validate.sh"
          once: true
---

# Skill Name

## When to Use
- User asks to "create something"
- User needs help with "specific task"

## Instructions

Step-by-step instructions for Claude to follow.

### Step 1: Understand the Request
Gather necessary information...

### Step 2: Execute the Task
Perform the main action...

### Step 3: Verify Results
Confirm the output is correct...

## Examples

### Example 1: Basic Usage
User: "Help me with X"
Action: Do Y, then Z

## Guidelines
- Always verify before executing
- Ask for clarification if ambiguous
```

#### SKILL.md Frontmatter Fields

| Field | Required | Description |
|-------|----------|-------------|
| `name` | Yes | Lowercase, hyphens, max 64 chars |
| `description` | Yes | Trigger description, max 1024 chars. Claude uses this to decide when to apply |
| `allowed-tools` | No | Tools Claude can use without permission. Supports YAML lists |
| `model` | No | Override model (e.g., `claude-sonnet-4-20250514`) |
| `context` | No | Set to `fork` to run in isolated sub-agent context |
| `agent` | No | Agent type for fork: `Explore`, `Plan`, `general-purpose`, or custom |
| `hooks` | No | Scoped hooks: `PreToolUse`, `PostToolUse`, `Stop` |
| `user-invocable` | No | Show in `/` menu (default: `true`). Set `false` to hide |
| `disable-model-invocation` | No | Block Skill tool from calling this (default: `false`) |

#### New Features (v2.1+)

- **Hot-reload**: Skills are reloaded automatically when modified (no restart needed)
- **YAML-style lists**: Use YAML lists for `allowed-tools` for cleaner syntax
- **Progressive disclosure**: Put detailed docs in separate files, Claude reads on-demand
- **Bundled scripts**: Scripts in skill directory can be executed without reading into context

---

### 5. Creating Slash Commands

> **Recommendation:** Create [Skills](#4-creating-skills) instead. Since v2.1.3, skills and commands work identically, but skills are more flexible and cross-platform. This section is kept for reference and legacy support.

#### Command File Location

```
.claude/commands/my-command.md      # Project scope
~/.claude/commands/my-command.md    # User scope
```

#### Command File Format

```markdown
---
description: Brief description shown in /help
argument-hint: <required-arg> [optional-arg]
allowed-tools: Bash, Read, Write
---

## Context

Current information Claude should know:
- Git status: !`git status --short`
- Current branch: !`git branch --show-current`

## Your Task

Based on the context above, perform these steps:

1. First step
2. Second step
3. Final step

Do not do anything else.
```

#### Dynamic Context with !`command`

Use `!`backticks`` to inject command output (requires `allowed-tools` with `Bash`):

```markdown
## Context
- Current directory: !`pwd`
- Files changed: !`git diff --name-only`
- Package version: !`node -p "require('./package.json').version"`
```

#### Positional Arguments

Access individual arguments with `$1`, `$2`, etc. (not just `$ARGUMENTS`):

```markdown
---
argument-hint: [pr-number] [priority] [assignee]
description: Review pull request
---

Review PR #$1 with priority $2 and assign to $3.
```

#### Frontmatter Fields

| Field | Required | Description |
|-------|----------|-------------|
| `description` | Yes | Shown in command help |
| `argument-hint` | No | Usage hint: `<required> [optional]` |
| `allowed-tools` | No | Restrict tools: `Bash(git:*), Read` |
| `model` | No | Override model for this command |
| `context` | No | Set to `fork` to run in sub-agent context |
| `agent` | No | Agent type for fork (requires `context: fork`) |
| `hooks` | No | Scoped hooks for this command's execution |
| `disable-model-invocation` | No | Block Skill tool from calling this |

---

### 6. MCP (Model Context Protocol)

MCP allows Claude Code to connect to external tools and services.

#### Configuration File Locations

| Scope | Location | Purpose |
|-------|----------|---------|
| User | `~/.claude.json` | Personal MCP servers (in main config) |
| Project | `.mcp.json` | Shared MCP servers (version controlled) |
| Managed | `/etc/claude-code/managed-mcp.json` | Enterprise MCP servers |

#### .mcp.json Format

```json
{
  "mcpServers": {
    "stdio-server": {
      "type": "stdio",
      "command": "npx",
      "args": ["-y", "@package/mcp-server"],
      "env": {
        "API_KEY": "${API_KEY}",
        "HOST": "${HOST:-localhost}"
      }
    },
    "http-server": {
      "type": "http",
      "url": "https://api.example.com/mcp"
    }
  }
}
```

#### MCP Server Types

| Type | Use Case | CLI Flag |
|------|----------|----------|
| `stdio` | Local process (default) | `--command`, `--args` |
| `http` | Remote HTTP API | `--transport http` |
| `sse` | Server-Sent Events | `--transport sse` |

#### Environment Variable Expansion
- `${VAR}` - Use environment variable
- `${VAR:-default}` - Use default if not set

#### Adding MCP Servers via CLI

```bash
# Add stdio server (default)
claude mcp add github --command "npx" --args "-y @anthropic/mcp-github"

# Add HTTP server (v2.1+)
claude mcp add linear --transport http https://mcp.linear.app/mcp

# Add SSE server (v2.1+)
claude mcp add asana --transport sse https://mcp.asana.com/sse

# Add with JSON config
claude mcp add-json db '{"command":"npx","args":["-y","@anthropic/mcp-postgres"],"env":{"DATABASE_URL":"${DATABASE_URL}"}}'

# List servers
claude mcp list

# Enable/disable servers
/mcp enable server-name
/mcp disable server-name

# Remove server
claude mcp remove github
```

#### MCP Permissions (v2.0.70+)

Wildcard permissions for MCP tools:

```json
{
  "permissions": {
    "allow": ["mcp__github__*"],
    "deny": ["mcp__filesystem__*"]
  }
}
```

#### MCP Settings

| Setting | Purpose |
|---------|---------|
| `enableAllProjectMcpServers` | Auto-approve all project MCP servers |
| `enabledMcpjsonServers` | List of approved servers: `["github", "linear"]` |
| `disabledMcpjsonServers` | List of blocked servers |
| `allowedMcpServers` | Managed allowlist (enterprise) |
| `deniedMcpServers` | Managed denylist (enterprise) |

---

### 7. Hooks System

Hooks execute code in response to Claude Code events.

#### Hook Configuration Location

> **Important:** Hooks are configured in `settings.json`, NOT in a separate `hooks.json` file.

| Scope | Location |
|-------|----------|
| User | `~/.claude/settings.json` |
| Project | `.claude/settings.json` |
| Local | `.claude/settings.local.json` |
| Plugin | `hooks/hooks.json` (for plugins only) |

#### Hook Configuration Format

In `settings.json`:

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Bash",
        "hooks": [
          {
            "type": "command",
            "command": "python3 .claude/hooks/validate.py",
            "timeout": 30
          }
        ]
      }
    ],
    "PostToolUse": [
      {
        "matcher": "Write|Edit",
        "hooks": [
          {
            "type": "command",
            "command": "$CLAUDE_PROJECT_DIR/.claude/hooks/format.sh"
          }
        ]
      }
    ],
    "SessionStart": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "echo 'Session started'"
          }
        ]
      }
    ]
  }
}
```

#### Hook Types (PascalCase!)

| Hook | Trigger | Use Case |
|------|---------|----------|
| `SessionStart` | Session begins | Setup, logging, env init |
| `SessionEnd` | Session ends | Cleanup, summary |
| `PreToolUse` | Before tool execution | Validation, blocking, modification |
| `PostToolUse` | After tool execution | Logging, formatting, cleanup |
| `PermissionRequest` | Permission prompt shown | Auto-approve, policy enforcement |
| `UserPromptSubmit` | User sends message | Preprocessing, context injection |
| `Stop` | Claude stops responding | Post-processing |
| `SubagentStop` | Subagent completes | Aggregate results |
| `PreCompact` | Before context compaction | Save important context |
| `Notification` | Notification triggered | Custom notifications |

#### Matcher Patterns

- Simple match: `"Bash"` - matches Bash tool only
- Regex: `"Write|Edit"` - matches Write or Edit
- Wildcard: `"*"` or `""` - matches all tools
- MCP tools: `"mcp__server__tool"` format

#### Hook Options (v2.1+)

| Option | Purpose |
|--------|---------|
| `type` | `"command"` (bash) or `"prompt"` (LLM-based) |
| `command` | Bash command to execute |
| `prompt` | LLM prompt (for `type: "prompt"`) |
| `timeout` | Timeout in seconds (default: 600) |
| `once` | Run only once per session: `true` |

#### Practical Example: Block .env File Access

Prevent accidental exposure of secrets by blocking direct reads of `.env` files:

```json
// In settings.json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Read|Grep",
        "hooks": [
          {
            "type": "command",
            "command": "if echo \"$TOOL_INPUT\" | grep -qE '\\.env($|[^a-zA-Z])'; then echo '{\"decision\": \"block\", \"reason\": \"Direct .env access blocked. Use environment variables instead.\"}'; else echo '{\"decision\": \"approve\"}'; fi"
          }
        ]
      }
    ]
  }
}
```

Or use a script file `.claude/hooks/block-env.sh`:

```bash
#!/bin/bash
# Block direct access to .env files
if echo "$TOOL_INPUT" | grep -qE '\.env($|[^a-zA-Z])'; then
    echo '{"decision": "block", "reason": "Direct .env access blocked for security. Use environment variables instead."}'
else
    echo '{"decision": "approve"}'
fi
```

Then reference it:

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Read|Grep",
        "hooks": [
          {
            "type": "command",
            "command": ".claude/hooks/block-env.sh"
          }
        ]
      }
    ]
  }
}
```

#### Hook Response (for PreToolUse)

Hook script can output JSON to control behavior:

```json
{"decision": "block", "reason": "Operation blocked by policy"}
```

```json
{"decision": "approve"}
```

```json
{"decision": "ask", "updatedInput": {"command": "modified command"}}
```

#### Environment Variables

| Variable | Description |
|----------|-------------|
| `$CLAUDE_PROJECT_DIR` | Project root directory |
| `${CLAUDE_PLUGIN_ROOT}` | Plugin directory (for plugin hooks) |

#### Hooks in Skills/Commands (v2.1+)

Define scoped hooks in frontmatter:

```yaml
---
name: secure-deploy
hooks:
  PreToolUse:
    - matcher: "Bash"
      hooks:
        - type: command
          command: "./validate-deploy.sh"
          once: true
---
```

---

### 8. Plugin Marketplace

#### Installing from Marketplace

```bash
# Add marketplace (supports GitHub, GitLab, local paths, URLs)
/plugin marketplace add owner/repo-name
/plugin marketplace add https://gitlab.com/company/plugins.git
/plugin marketplace add ./local-marketplace

# Install plugin (user scope by default)
/plugin install plugin-name@marketplace-name

# Install with scope (-s or --scope)
/plugin install plugin-name@marketplace-name -s project
/plugin install plugin-name@marketplace-name -s user

# Enable/disable plugins
/plugin enable plugin-name@marketplace-name
/plugin disable plugin-name@marketplace-name

# Update marketplace
/plugin marketplace update marketplace-name

# Remove plugin
/plugin uninstall plugin-name@marketplace-name
```

#### Plugin Scopes

| Scope | Who can use | Stored in |
|-------|-------------|-----------|
| User | You, all projects | `~/.claude/settings.json` |
| Project | All collaborators | `.claude/settings.json` |
| Local | You, this project | `.claude/settings.local.json` |
| Managed | All users (enterprise) | Managed settings |

#### Creating a Marketplace

Repository structure:

```
my-marketplace/
├── .claude-plugin/
│   └── marketplace.json
├── skills/
│   ├── skill-one/
│   │   └── SKILL.md
│   └── skill-two/
│       └── SKILL.md
├── plugins/                    # Mixed-component plugins
│   └── my-plugin/
│       ├── .claude-plugin/
│       │   └── plugin.json
│       ├── commands/           # NOT inside .claude-plugin/
│       ├── agents/
│       ├── skills/
│       ├── hooks/
│       │   └── hooks.json      # Plugin hooks go here
│       ├── .mcp.json           # Plugin MCP servers
│       └── .lsp.json           # Language server config (v2.0.74+)
└── README.md
```

> **Common Mistake:** Don't put `commands/`, `agents/`, `skills/`, or `hooks/` inside `.claude-plugin/`. Only `plugin.json` goes there.

#### LSP Support in Plugins (v2.0.74+)

Plugins can include Language Server Protocol configuration for code intelligence:

```json
// .lsp.json
{
  "go": {
    "command": "gopls",
    "args": ["serve"],
    "extensionToLanguage": {
      ".go": "go"
    }
  },
  "python": {
    "command": "pyright-langserver",
    "args": ["--stdio"],
    "extensionToLanguage": {
      ".py": "python"
    }
  }
}
```

Users must have the language server binary installed.

#### marketplace.json Format

```json
{
  "$schema": "https://anthropic.com/claude-code/marketplace.schema.json",
  "name": "marketplace-name",
  "version": "1.0.0",
  "description": "Description of this marketplace",
  "owner": {
    "name": "Owner Name",
    "email": "email@example.com"
  },
  "plugins": [
    {
      "name": "plugin-name",
      "description": "What this plugin does",
      "source": "./plugins/plugin-name",
      "category": "productivity",
      "tags": ["tag1", "tag2"],
      "skills": [
        "./skills/skill-one",
        "./skills/skill-two"
      ]
    }
  ]
}
```

#### plugin.json Format (for individual plugins)

```json
{
  "name": "plugin-name",
  "description": "Plugin description",
  "version": "1.0.0",
  "author": {
    "name": "Author Name"
  }
}
```

---

### 9. File Organization Best Practices

#### Recommended Project Structure

```
project/
├── .claude/                    # Claude Code config (version controlled)
│   ├── settings.json           # Project settings + hooks
│   ├── settings.local.json     # Personal settings (gitignored)
│   ├── CLAUDE.md               # Alternative location for project instructions
│   ├── commands/
│   │   └── deploy.md
│   ├── skills/
│   │   └── project-skill/
│   │       └── SKILL.md
│   ├── agents/
│   │   └── reviewer.md
│   └── rules/                  # Modular rules (v2.0.64+)
│       ├── code-style.md
│       └── testing.md
├── .mcp.json                   # MCP servers (version controlled)
├── CLAUDE.md                   # Project instructions
├── CLAUDE.local.md             # Personal project instructions (gitignored)
└── src/                        # Project source code
```

#### .gitignore Recommendations

```gitignore
# Claude Code local settings
.claude/settings.local.json
.claude.local/

# Personal skills (if using symlinks)
.claude/skills/*
!.claude/skills/project-specific/
```

#### Naming Conventions

| Component | Convention | Example |
|-----------|------------|---------|
| Skills | lowercase-with-hyphens | `deep-research` |
| Commands | lowercase-with-hyphens | `deploy-prod` |
| Agents | lowercase-with-hyphens | `code-reviewer` |
| Config files | lowercase.json | `settings.json` |

---

### 10. New Commands & Features (v2.1+)

#### New Slash Commands

| Command | Purpose |
|---------|---------|
| `/plan` | Enter plan mode directly from prompt |
| `/teleport` | Resume remote session from claude.ai |
| `/remote-env` | Configure remote session environment |
| `/tasks` | View and manage background tasks |
| `/stats` | Usage stats, streaks, model preferences |
| `/rename <name>` | Name sessions for easy resume |
| `/config` | Open settings interface (searchable) |
| `/terminal-setup` | Setup Shift+Enter for various terminals |
| `/context` | Visualize context window usage |

#### Background Tasks (v2.0.60+)

- Press `Ctrl+B` to background running tasks
- Use `/tasks` to view background tasks
- Agents run asynchronously and notify when done

#### Named Sessions (v2.0.64+)

```bash
# Name current session
/rename my-feature

# Resume by name
claude --resume my-feature

# Or from REPL
/resume my-feature
```

#### Status Line (v2.0.65+)

Configure a custom status line in `settings.json`:

```json
{
  "statusLine": {
    "type": "command",
    "command": "~/.claude/statusline.sh"
  }
}
```

Available fields: `context_window.used_percentage`, `context_window.remaining_percentage`, `current_usage`

#### Sandbox Mode

Isolate bash commands with filesystem and network restrictions:

```json
{
  "sandbox": {
    "enabled": true,
    "autoAllowBashIfSandboxed": true,
    "excludedCommands": ["docker", "git"],
    "network": {
      "allowLocalBinding": true
    }
  }
}
```

---

## Repository Structure

This repository (`agent-skills`) contains skills in a flat structure for easy cloning:

```
agent-skills/
├── deep-research/
│   ├── SKILL.md
│   ├── SOURCES.md
│   └── references/
├── triz/
├── ... (other skills)
└── README.md
```

The companion repository [`thepexcel-claude-plugins`](https://github.com/ThepExcel/thepexcel-claude-plugins) contains the same skills in nested plugin format for `claude plugin install`. It is **auto-synced** from this repo via GitHub Actions.

---

## Contributing

1. Fork this repository
2. Create a new skill folder with `SKILL.md`
3. Add `SOURCES.md` for attribution
4. Submit a pull request

See the [skill-creator-thepexcel](./skill-creator-thepexcel/) skill for guidance on creating effective skills.

---

## License

- **ThepExcel original skills:** MIT License
- **skill-creator-thepexcel:** Apache 2.0 (based on [Anthropic's skill-creator](https://github.com/anthropics/skills))

---

## Author

Created by [Sira Ekabut](https://www.thepexcel.com) (ThepExcel)

*Developed through human-AI collaboration using Claude Code.*
