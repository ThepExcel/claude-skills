# Claude Skills Collection

A collection of reusable skills for Claude Code and Claude.ai.

**Learn more:** [Claude Skills คืออะไร? วิธีสร้างและใช้งาน](https://www.thepexcel.com/claude-skills/)

---

## Installation

### For Claude Code (CLI)

```bash
# Clone this repo
git clone https://github.com/ThepExcel/claude-skills.git
cd claude-skills

# Create symlinks to make skills globally available
mkdir -p ~/.claude/skills
for skill in */; do
    [[ -d "$skill" && ! "$skill" == .* ]] && ln -s "$(pwd)/$skill" ~/.claude/skills/$(basename "$skill")
done
```

After installation, Claude Code will automatically use these skills when relevant.

### For Claude.ai (Web)

1. Download the skill folder you want (e.g., `deep-research/`)
2. **ZIP the entire folder** (not just the files inside!)
   ```bash
   # Correct way - ZIP the folder
   zip -r deep-research.zip deep-research/
   ```
3. Go to **Settings > Capabilities** in Claude.ai
4. Scroll down to **Skills** section and click **Upload skill**

> **Important:** ZIP must contain the folder structure. If you ZIP only the files, Claude won't find SKILL.md!
>
> **Requirements:** Pro, Max, Team, or Enterprise plan.

---

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
| **ai-image-video-prompt** | Professional AI image/video prompt engineering with visual artist's eye |
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

---

## Usage Examples

Once installed, just describe what you need:

- "Research the latest AI developments" → uses **deep-research**
- "Help me think creatively about this problem" → uses **creativity**
- "Explain how recursion works" → uses **concept-explainer**
- "Analyze SWOT for my business" → uses **business-management**
- "Create a Lean Canvas for my startup idea" → uses **business-model**
- "Help me create a skill from my expertise" → uses **skill-extractor**
- "Coach me on fixing this messy Excel data" → uses **power-query-coach**
- "Create an image prompt for product photography" → uses **ai-image-video-prompt**
- "Create a PowerPoint presentation" → uses **pptx**

---

## Skill Structure

```
claude-skills/
├── README.md
├── skill-name/
│   ├── SKILL.md           # Main skill definition (required)
│   ├── SOURCES.md         # Attribution & sources
│   └── references/        # Supporting documents (optional)
│       └── methodology.md
└── another-skill/
    └── ...
```

---

## License

- **Original skills (ThepExcel):** MIT License - Feel free to use and modify.
- **Anthropic skills (docx, xlsx, pptx, pdf):** See LICENSE.txt in each skill folder.

---

## Author

Created by [Sira Ekabut](https://www.thepexcel.com) (ThepExcel)

*Skills marked as "ThepExcel + Claude" were developed through human-AI collaboration using Claude Code.*
