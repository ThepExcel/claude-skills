# Financial Analysis Frameworks

## Return on Investment (ROI)

**Use when:** Evaluating investment profitability, comparing options, marketing effectiveness

### Formula

```
ROI = (Net Profit / Investment Cost) × 100%

or

ROI = ((Final Value - Initial Investment) / Initial Investment) × 100%
```

### Example

```
Investment: ฿100,000 in marketing campaign
Revenue generated: ฿250,000
Costs (excluding marketing): ฿100,000
Net Profit: ฿250,000 - ฿100,000 - ฿100,000 = ฿50,000

ROI = (฿50,000 / ฿100,000) × 100% = 50%
```

### Strengths & Limitations

| Strengths | Limitations |
|-----------|-------------|
| Simple to calculate | Ignores time value of money |
| Easy to understand | Doesn't account for risk |
| Universal applicability | Can be manipulated by timeframe |

---

## Net Present Value (NPV)

**Use when:** Long-term investment decisions, comparing projects with different timelines

### Formula

```
NPV = Σ (Cash Flow_t / (1 + r)^t) - Initial Investment

Where:
- t = time period
- r = discount rate (cost of capital)
```

### Decision Rule

| NPV | Decision |
|-----|----------|
| > 0 | Accept (creates value) |
| = 0 | Indifferent |
| < 0 | Reject (destroys value) |

### Example

```
Initial Investment: ฿1,000,000
Discount Rate: 10%
Cash Flows:
- Year 1: ฿300,000
- Year 2: ฿400,000
- Year 3: ฿500,000

NPV = 300,000/(1.1)¹ + 400,000/(1.1)² + 500,000/(1.1)³ - 1,000,000
NPV = 272,727 + 330,579 + 375,657 - 1,000,000
NPV = -฿21,037

Decision: Reject (negative NPV)
```

### Strengths & Limitations

| Strengths | Limitations |
|-----------|-------------|
| Considers time value of money | Requires accurate cash flow estimates |
| Accounts for all cash flows | Discount rate selection is subjective |
| Direct measure of value creation | Complex to calculate |

---

## Internal Rate of Return (IRR)

**Use when:** Comparing projects of different sizes, evaluating investment attractiveness

### Definition

IRR is the discount rate that makes NPV = 0

### Decision Rule

| If IRR | Decision |
|--------|----------|
| > Cost of Capital | Accept |
| = Cost of Capital | Indifferent |
| < Cost of Capital | Reject |

### Example

```
If NPV = 0 when discount rate = 15%
And your cost of capital = 10%

IRR (15%) > Cost of Capital (10%)
Decision: Accept
```

### IRR vs NPV

| Situation | Use IRR | Use NPV |
|-----------|---------|---------|
| Single project, go/no-go | ✓ | ✓ |
| Comparing different-sized projects | ✗ | ✓ |
| Non-conventional cash flows | ✗ | ✓ |
| Ranking mutually exclusive projects | ✗ | ✓ |

---

## Break-Even Analysis

**Use when:** Pricing decisions, cost planning, viability assessment

### Formula

```
Break-Even Point (Units) = Fixed Costs / (Price per Unit - Variable Cost per Unit)

Break-Even Point (Revenue) = Fixed Costs / Contribution Margin Ratio

Contribution Margin = Price - Variable Cost
Contribution Margin Ratio = Contribution Margin / Price
```

### Example

```
Fixed Costs: ฿500,000/month
Price per Course: ฿3,000
Variable Cost per Course: ฿500 (payment processing, support)

Contribution Margin = ฿3,000 - ฿500 = ฿2,500

Break-Even = ฿500,000 / ฿2,500 = 200 courses/month
```

### Break-Even Chart

```
Revenue/
Cost (฿) │                    /
         │               /  Break-Even
         │          /  ★ Point
         │     / Revenue
         │  /
         │─────────────── Total Cost
         │    Fixed Cost
         └────────────────────── Units
```

---

## Payback Period

**Use when:** Quick assessment of investment recovery, liquidity concerns

### Formula

```
Simple Payback = Initial Investment / Annual Cash Flow

For uneven cash flows: Count years until cumulative cash flow = investment
```

### Example

```
Investment: ฿1,000,000
Annual Cash Flow: ฿300,000

Payback Period = ฿1,000,000 / ฿300,000 = 3.33 years
```

### Discounted Payback

Same as simple payback, but using discounted cash flows (accounts for time value).

---

## Financial Metrics Summary

### When to Use Each

| Metric | Best For | Limitations |
|--------|----------|-------------|
| **ROI** | Quick comparisons, marketing | Ignores time value |
| **NPV** | Long-term projects, value creation | Needs discount rate |
| **IRR** | Comparing returns across projects | Multiple IRR issues |
| **Payback** | Liquidity concerns, risk assessment | Ignores cash flows after payback |
| **Break-Even** | Pricing, viability | Assumes linear relationships |

### Quick Decision Guide

```
Question: Should we invest in this project?

Step 1: Calculate Break-Even → Is it achievable?
Step 2: Calculate Payback → Is recovery time acceptable?
Step 3: Calculate NPV → Does it create value?
Step 4: Calculate IRR → Does it exceed our hurdle rate?

All positive → Strong investment candidate
```

---

## Cost-Benefit Analysis Template

```markdown
## Cost-Benefit Analysis: [Project Name]

### Costs
| Category | Amount | Timing | Certainty |
|----------|--------|--------|-----------|
| Initial investment | ฿X | Upfront | High |
| Operating costs | ฿Y/year | Ongoing | Medium |
| Opportunity cost | ฿Z | - | Low |
| **Total Costs** | ฿XX | | |

### Benefits
| Category | Amount | Timing | Certainty |
|----------|--------|--------|-----------|
| Revenue increase | ฿A/year | Year 2+ | Medium |
| Cost savings | ฿B/year | Year 1+ | High |
| Intangible benefits | ฿C (estimated) | Ongoing | Low |
| **Total Benefits** | ฿YY | | |

### Summary
| Metric | Value |
|--------|-------|
| Net Benefit (Benefits - Costs) | ฿XX |
| Benefit-Cost Ratio | X.X |
| Payback Period | X years |
| NPV | ฿XX |
| IRR | XX% |

### Recommendation
[Accept/Reject with reasoning]
```
