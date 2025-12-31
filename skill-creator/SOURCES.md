# Sources & Attribution

## Official Documentation

### Anthropic Best Practices (Primary Source)
| Source | Contribution |
|--------|--------------|
| [Skill Authoring Best Practices](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices) | Core principles, progressive disclosure, evaluation patterns, anti-patterns |
| [Skills Overview](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview) | Skill structure, runtime environment, how skills work |
| [Claude Code Skills Documentation](https://code.claude.com/docs/en/skills) | Skill loading and usage in Claude Code |

### Repositories
| Source | Contribution |
|--------|--------------|
| [Anthropic Skills Repo](https://github.com/anthropics/skills) | Official skill structure and examples |
| [Agent Skills Specification](https://agentskills.io/) | Open standard for agent skills |

## Design Patterns & Standards

| Pattern | Source |
|---------|--------|
| Progressive Disclosure | UX design principles (Nielsen Norman Group) |
| Modular References | Software engineering best practices |
| YAML Frontmatter | Jekyll, Hugo static site conventions |
| Evaluation-Driven Development | TDD/BDD practices adapted for AI |

## Key Concepts from Official Docs

This skill incorporates the following from Anthropic's official best practices:

1. **Concise is Key** — Context window is a public good
2. **Degrees of Freedom** — Match specificity to task fragility
3. **Test with All Models** — Different models need different detail levels
4. **Third-Person Descriptions** — Avoid POV inconsistency
5. **Progressive Disclosure** — Three-level loading system
6. **Feedback Loops** — Validate → fix → repeat pattern
7. **Claude A/B Iteration** — Design with one Claude, test with another
8. **Evaluation-Driven Development** — Build evals before writing docs
9. **Anti-Patterns** — Windows paths, nested references, voodoo constants, etc.

## Enhanced by ThepExcel

This version includes additional improvements beyond the official documentation:

### Content Additions
- Integration with `/extract-expertise` for domain expertise extraction
- Integration with `/deep-research` for knowledge gathering
- Structured reference files organization
- Quality checklist with actionable items

### Tools & Scripts
- `init_skill.py` — Skill template generation
- `package_skill.py` — Validation and packaging
- `quick_validate.py` — Fast validation check

### Practical Insights
- Real-world skill development workflow
- Common pitfalls from production experience
- Iteration patterns that work in practice

---

*This enhanced skill-creator follows Anthropic's official patterns while adding practical insights from ThepExcel's real-world skill development experience.*

**Last Updated:** 2025-12-31
