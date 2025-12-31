# Claude Code Skills

A collection of reusable skills for [Claude Code](https://claude.ai/claude-code).

## Installation

```bash
# Clone this repo
git clone https://github.com/ThepExcel/claude-skills.git

# Create symlinks to make skills globally available
mkdir -p ~/.claude/skills
for skill in claude-skills/skills/*/; do
    ln -s "$(pwd)/$skill" ~/.claude/skills/$(basename "$skill")
done
```

## Available Skills

| Skill | Description |
|-------|-------------|
| **deep-research** | Comprehensive 8-phase research with source triangulation and claim verification |
| **creativity** | Creative thinking techniques and ideation frameworks |
| **problem-solving** | Structured problem-solving methodologies |
| **triz** | TRIZ (Theory of Inventive Problem Solving) methodology |
| **concept-explainer** | Master teaching methodology for explaining concepts |
| **visualization** | Data visualization and diagram creation |
| **skill-creator** | Guide for creating new Claude Code skills |
| **common-tools** | Common utility tools and helpers |

## Usage

Once installed, Claude Code will automatically use these skills when relevant to your task.

You can also invoke skills directly by describing what you need:
- "Research the latest AI developments" → uses deep-research
- "Help me think creatively about this problem" → uses creativity
- "Explain how recursion works" → uses concept-explainer

## Structure

```
skills/
├── skill-name/
│   ├── SKILL.md           # Main skill definition
│   └── references/        # Supporting documents (optional)
│       └── methodology.md
```

## License

MIT License - Feel free to use and modify.

## Author

Created by [ThepExcel](https://www.thepexcel.com)
