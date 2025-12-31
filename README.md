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

### Original Skills (by ThepExcel + Claude)

Skills developed by [ThepExcel](https://www.thepexcel.com) in collaboration with Claude.

| Skill | Description |
|-------|-------------|
| **deep-research** | Comprehensive 8-phase research with Graph-of-Thoughts, source triangulation, and claim verification |
| **creativity** | Creative thinking techniques and ideation frameworks |
| **problem-solving** | Structured problem-solving methodologies (5 Whys, Fishbone, Root Cause Analysis) |
| **triz** | TRIZ (Theory of Inventive Problem Solving) with 40 principles and contradiction matrix |
| **concept-explainer** | Master teaching methodology for explaining concepts with visualizations |
| **visualization** | Data visualization, diagrams, and Manim animations |
| **skill-creator** | Guide for creating new Claude Code skills |
| **business-management** | Business management frameworks hub (SWOT, OKR, Porter's, BCG, etc.) |
| **business-model** | Business Model Canvas, Lean Canvas, Value Proposition Canvas |
| **skill-extractor** | Extract domain expertise from experts and transform into Claude skills |
| **power-query-coach** | Coach users to transform messy data using Power Query UI |

### Third-Party Skills

Skills from external sources, included for convenience.

| Skill | Description | Source |
|-------|-------------|--------|
| **docx** | Word document creation, editing, and analysis | [Anthropic Official](https://github.com/anthropics/skills) |
| **xlsx** | Excel spreadsheet creation with formulas and formatting | [Anthropic Official](https://github.com/anthropics/skills) |
| **pptx** | PowerPoint presentation creation and editing | [Anthropic Official](https://github.com/anthropics/skills) |
| **pdf** | PDF text extraction and form filling | [Anthropic Official](https://github.com/anthropics/skills) |

## Usage

Once installed, Claude Code will automatically use these skills when relevant to your task.

You can also invoke skills directly by describing what you need:
- "Research the latest AI developments" → uses deep-research
- "Help me think creatively about this problem" → uses creativity
- "Explain how recursion works" → uses concept-explainer
- "Analyze SWOT for my business" → uses business-management
- "Create a Lean Canvas for my startup idea" → uses business-model
- "Help me create a skill from my expertise" → uses skill-extractor
- "Coach me on fixing this messy Excel data" → uses power-query-coach
- "Create a PowerPoint presentation" → uses pptx

## Structure

```
skills/
├── skill-name/
│   ├── SKILL.md           # Main skill definition
│   └── references/        # Supporting documents (optional)
│       └── methodology.md
```

## License

- **Original skills (ThepExcel):** MIT License - Feel free to use and modify.
- **Anthropic skills (docx, xlsx, pptx, pdf):** Proprietary - See LICENSE.txt in each skill folder.

## Author

Created by [ThepExcel](https://www.thepexcel.com) (Sira Ekabut)

---

*Skills marked as "ThepExcel + Claude" were developed through human-AI collaboration using Claude Code.*
