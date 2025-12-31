# Decision Making Frameworks

## Decision Matrix (Weighted Scoring)

**Use when:** Choosing between multiple options with multiple criteria

### Steps

1. **List options** - What are you choosing between? (rows)
2. **Define criteria** - What matters in this decision? (columns)
3. **Weight criteria** - How important is each? (1-5 or 1-10)
4. **Score options** - Rate each option on each criterion (1-5)
5. **Calculate** - Multiply scores by weights, sum totals
6. **Decide** - Highest score wins (but use judgment)

### Template

| Option | Criteria 1 (w=3) | Criteria 2 (w=5) | Criteria 3 (w=2) | Total |
|--------|------------------|------------------|------------------|-------|
| Option A | 4 × 3 = 12 | 3 × 5 = 15 | 5 × 2 = 10 | **37** |
| Option B | 5 × 3 = 15 | 4 × 5 = 20 | 3 × 2 = 6 | **41** |
| Option C | 3 × 3 = 9 | 5 × 5 = 25 | 4 × 2 = 8 | **42** |

**Winner:** Option C (highest weighted score)

### Example: Choosing a Software Tool

| Tool | Cost (w=4) | Features (w=5) | Ease of Use (w=3) | Support (w=2) | Total |
|------|------------|----------------|-------------------|---------------|-------|
| Tool A | 5×4=20 | 3×5=15 | 4×3=12 | 3×2=6 | **53** |
| Tool B | 3×4=12 | 5×5=25 | 3×3=9 | 4×2=8 | **54** |
| Tool C | 4×4=16 | 4×5=20 | 5×3=15 | 5×2=10 | **61** |

### Common Criteria by Decision Type

| Decision Type | Typical Criteria |
|---------------|------------------|
| **Hiring** | Skills, Experience, Culture fit, Salary expectations, Growth potential |
| **Software** | Cost, Features, Integration, Support, Scalability |
| **Vendor** | Price, Quality, Reliability, Location, Terms |
| **Project** | ROI, Risk, Resources, Timeline, Strategic fit |
| **Location** | Cost, Talent pool, Market access, Infrastructure, Quality of life |

---

## Pugh Matrix

**Use when:** Comparing alternatives against a baseline/reference option

### How It Differs from Decision Matrix

- Uses a **reference/baseline** option (current state or leading option)
- Scores are **relative**: Better (+1), Same (0), Worse (-1)
- Simpler scoring, focuses on comparative advantage

### Steps

1. **Select baseline** - Current solution or best initial option
2. **List criteria** - What matters (unweighted or weighted)
3. **Compare each option** - Better (+), Same (S), Worse (-)
4. **Sum scores** - Count +1, 0, -1
5. **Evaluate** - Highest net score, but review trade-offs

### Template

| Criteria | Baseline | Option A | Option B | Option C |
|----------|----------|----------|----------|----------|
| Cost | REF | + | - | S |
| Quality | REF | S | + | + |
| Speed | REF | + | + | - |
| Support | REF | - | S | + |
| **Sum of +** | - | 2 | 2 | 2 |
| **Sum of -** | - | 1 | 1 | 1 |
| **Net Score** | 0 | +1 | +1 | +1 |

---

## Pros and Cons List

**Use when:** Quick decisions, simple comparisons, brainstorming

### Enhanced Format

Instead of simple list, add **weight** and **impact**:

| Pros | Weight | Impact |
|------|--------|--------|
| Lower cost | High | Saves $50K/year |
| Faster implementation | Medium | 2 weeks vs 2 months |
| Better support | Low | 24/7 availability |

| Cons | Weight | Impact |
|------|--------|--------|
| Learning curve | High | 1 month productivity dip |
| Less features | Medium | Missing 2 key features |
| Vendor lock-in | Low | 2-year contract |

---

## Decision Tree

**Use when:** Sequential decisions with probabilistic outcomes

### Structure

```
Decision Point (□)
├─ Option A
│  ├─ Outcome 1 (70%) → Value
│  └─ Outcome 2 (30%) → Value
└─ Option B
   ├─ Outcome 1 (50%) → Value
   └─ Outcome 2 (50%) → Value
```

### Expected Value Calculation

```
EV(Option A) = (0.70 × Value1) + (0.30 × Value2)
EV(Option B) = (0.50 × Value1) + (0.50 × Value2)

Choose option with highest EV
```

---

## Best Practices

1. **Involve stakeholders** - Different perspectives improve criteria selection
2. **Be explicit about weights** - Forces discussion about priorities
3. **Document reasoning** - Record why you assigned each score
4. **Sensitivity check** - Would changing weights change the decision?
5. **Trust your gut** - If the "winner" feels wrong, investigate why
