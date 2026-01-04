# Claude Skills Collection

A collection of reusable skills for Claude Code and Claude.ai.

**Learn more:** [Claude Skills คืออะไร? วิธีสร้างและใช้งาน](https://www.thepexcel.com/claude-skills/)

---

## Installation

### For Claude Code (CLI)

#### Method 1: Plugin Marketplace (Recommended)

The easiest way to install skills. Add this marketplace once, then install any skill you want:

```bash
# Step 1: Add the marketplace
/plugin marketplace add ThepExcel/claude-skills

# Step 2: Install the skills you want
/plugin install research-skills@thepexcel-skills -s project
/plugin install problem-solving-skills@thepexcel-skills -s project
/plugin install document-skills@thepexcel-skills -s project
```

**Available skill bundles:**

| Bundle | Skills Included |
|--------|-----------------|
| `research-skills` | deep-research, explain-concepts |
| `problem-solving-skills` | problem-solving, triz, generate-creative-ideas |
| `business-skills` | design-business-model, manage-business-strategy |
| `ai-prompt-skills` | optimize-prompt, prompt-ai-image-video, skill-creator, extract-expertise |
| `visualization-skills` | create-visualization, power-query-coaching |
| `document-skills` | xlsx, docx, pptx, pdf |

**Installation scopes:**

| Scope | Flag | Where | Use case |
|-------|------|-------|----------|
| `project` | `-s project` | Current project only | Recommended for most cases |
| `user` | `-s user` (default) | All projects | Personal productivity skills |

> **Note:** Plugin files are cached in `~/.claude/plugins/cache/`, not copied into your project. They work seamlessly but won't appear in your project folder.

**Other useful commands:**
```bash
/plugin list thepexcel-skills              # List all available skills
/plugin marketplace update thepexcel-skills # Update to latest version
/plugin uninstall research-skills@thepexcel-skills
```

#### Method 2: Manual Clone + Symlink

For full control, offline access, or if you want files in your project:

```bash
# Clone this repo
git clone https://github.com/ThepExcel/claude-skills.git
cd claude-skills

# Create symlinks to make skills globally available
mkdir -p ~/.claude/skills
for skill in skills/*/; do
    skill_name=$(basename "$skill")
    ln -sf "$(pwd)/$skill" ~/.claude/skills/$skill_name
done
```

After installation, Claude Code will automatically use these skills when relevant.

### For Claude.ai (Web)

**Step 1: Download the skill folder**

Choose one of these methods:

| Method | How |
|--------|-----|
| **Download entire repo** | Click green **Code** button → **Download ZIP** → Extract → Find the skill folder in `skills/` |
| **Use download tool** | Go to [download-directory.github.io](https://download-directory.github.io/) → Paste folder URL (e.g., `https://github.com/ThepExcel/claude-skills/tree/main/skills/deep-research`) |
| **Git clone** | `git clone https://github.com/ThepExcel/claude-skills.git` → Copy the folder from `skills/` |

**Step 2: ZIP the folder**

```bash
# ZIP the skill folder (must contain SKILL.md)
cd skills
zip -r deep-research.zip deep-research/
```

**Step 3: Upload to Claude.ai**

1. Go to **Settings > Capabilities**
2. Scroll down to **Skills** section
3. Click **Upload skill** and select your ZIP file

> **Important:** ZIP must contain the folder with SKILL.md inside!
>
> **Requirements:** Pro, Max, Team, or Enterprise plan.

---

## Available Skills

### Original Skills (by ThepExcel + Claude)

Skills developed by [ThepExcel](https://www.thepexcel.com) in collaboration with Claude.

| Skill | Description |
|-------|-------------|
| [**create-visualization**](skills/create-visualization/) | Data visualization, diagrams, and Manim animations |
| [**deep-research**](skills/deep-research/) | Comprehensive 8-phase research with Graph-of-Thoughts, source triangulation, and claim verification |
| [**design-business-model**](skills/design-business-model/) | Business Model Canvas, Lean Canvas, Value Proposition Canvas |
| [**explain-concepts**](skills/explain-concepts/) | Master teaching methodology for explaining concepts with visualizations |
| [**extract-expertise**](skills/extract-expertise/) | Extract domain expertise from experts and transform into Claude skills |
| [**generate-creative-ideas**](skills/generate-creative-ideas/) | Creative thinking techniques and ideation frameworks |
| [**manage-business-strategy**](skills/manage-business-strategy/) | Business management frameworks hub (SWOT, OKR, Porter's, BCG, etc.) |
| [**power-query-coaching**](skills/power-query-coaching/) | Coach users to transform messy data using Power Query UI |
| [**optimize-prompt**](skills/optimize-prompt/) | Prompt optimization consultant for Claude API, OpenAI, Gemini, CLAUDE.md, ChatGPT, n8n |
| [**problem-solving**](skills/problem-solving/) | Structured problem-solving methodologies (5 Whys, Fishbone, Root Cause Analysis) |
| [**prompt-ai-image-video**](skills/prompt-ai-image-video/) | Professional AI image/video prompt engineering with visual artist's eye |
| [**skill-creator**](skills/skill-creator/) | Guide for creating new Claude Code skills |
| [**triz**](skills/triz/) | TRIZ (Theory of Inventive Problem Solving) with 40 principles and contradiction matrix |

### Anthropic Official Skills (Pre-optimized)

Skills from Anthropic's official repository. These follow Anthropic's best practices and are already optimized for token efficiency.

| Skill | Description | Source |
|-------|-------------|--------|
| [**docx**](skills/docx/) | Word document creation, editing, and analysis | [Anthropic Official](https://github.com/anthropics/skills) |
| [**pdf**](skills/pdf/) | PDF text extraction and form filling | [Anthropic Official](https://github.com/anthropics/skills) |
| [**pptx**](skills/pptx/) | PowerPoint presentation creation and editing | [Anthropic Official](https://github.com/anthropics/skills) |
| [**xlsx**](skills/xlsx/) | Excel spreadsheet creation with formulas and formatting | [Anthropic Official](https://github.com/anthropics/skills) + ThepExcel |

> **Note:** xlsx enhanced by ThepExcel with Power Query routing to `/power-query-coaching`.

---

## Usage Examples

Once installed, invoke skills directly with `/skill-name` for guaranteed activation:

| Command | What It Does |
|---------|--------------|
| `/create-visualization` | Data visualization, diagrams, Manim animations |
| `/deep-research` | Comprehensive 8-phase research with source verification |
| `/design-business-model` | Business Model Canvas, Lean Canvas |
| `/docx` `/pdf` `/pptx` `/xlsx` | Office document operations |
| `/explain-concepts` | Master teaching methodology with visualizations |
| `/extract-expertise` | Transform domain expertise into Claude skills |
| `/generate-creative-ideas` | Creative thinking and ideation techniques |
| `/manage-business-strategy` | SWOT, OKR, Porter's Five Forces, BCG Matrix |
| `/optimize-prompt` | Improve system prompts for any AI platform |
| `/power-query-coaching` | Step-by-step Power Query UI guidance |
| `/problem-solving` | 5 Whys, Fishbone, Root Cause Analysis |
| `/prompt-ai-image-video` | Professional AI image/video prompts |
| `/skill-creator` | Guide for creating new skills |
| `/triz` | 40 TRIZ principles and contradiction matrix |

---

## Repository Structure

```
claude-skills/
├── .claude-plugin/
│   └── marketplace.json   # Marketplace configuration
├── skills/
│   ├── deep-research/
│   │   ├── SKILL.md       # Skill instructions (required)
│   │   ├── references/    # Reference docs (optional)
│   │   └── assets/        # Templates, images (optional)
│   ├── xlsx/
│   └── ...
└── README.md
```

### 3-Level Progressive Loading

Skills use smart loading - Claude only loads what's needed:

| Level | When Loaded | Token Cost | Content |
|-------|-------------|------------|---------|
| **1. Metadata** | Session start | ~100 tokens | `name` + `description` from YAML |
| **2. Instructions** | Skill triggered | <5,000 tokens | SKILL.md body |
| **3. Resources** | When needed | Unlimited | Files in `references/`, `scripts/` |

This means you can have dozens of skills installed without performance impact!

---

## License

- **Original skills (ThepExcel):** MIT License - Feel free to use and modify.
- **Anthropic skills (docx, xlsx, pptx, pdf):** See LICENSE.txt in each skill folder.

---

## Author

Created by [Sira Ekabut](https://www.thepexcel.com) (ThepExcel)

*Skills marked as "ThepExcel + Claude" were developed through human-AI collaboration using Claude Code.*
