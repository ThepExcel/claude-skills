# TRIZ Case Studies & Examples

Real-world applications of TRIZ methodology.

---

## Technology Cases

### Samsung Galaxy: Battery vs Weight

**Contradiction:** Better battery (Parameter 19: Energy) worsens Weight (Parameter 1)

**Principles Applied:**
- #3 Local Quality: Variable thickness battery
- #28 Mechanics Substitution: Wireless charging
- #40 Composite Materials: New battery chemistry

**Result:** 30% more capacity without weight increase

---

### SpaceX: Reusable Rockets

**IFR:** "Rocket itself returns and lands"

**Contradiction:** Reusability (Parameter 34: Ease of repair) worsens Weight (Parameter 1)

**Principles Applied:**
- #13 The Other Way Round: Land the rocket (vs. discard)
- #15 Dynamics: Retractable landing legs
- #25 Self-Service: Autonomous landing

**Result:** 10x cost reduction

---

### Tesla: Range vs Charging Time

**Contradiction:** Longer range (Parameter 15: Duration) requires larger battery which worsens Charging time (Parameter 25: Loss of time)

**Principles Applied:**
- #1 Segmentation: Supercharger network (charge in segments)
- #10 Preliminary Action: Pre-condition battery before arrival
- #35 Parameter Changes: Different charging curves for different states

**Result:** 15-min charging for 200+ miles

---

## Software Cases

### Netflix: Personalization vs Simplicity

**Contradiction:** More personalization (Parameter 33: Ease of operation for power users) increases complexity (Parameter 36: Device complexity)

**Principles Applied:**
- #1 Segmentation: Micro-genres instead of broad categories
- #25 Self-Service: Algorithm learns automatically without user effort
- #35 Parameter Changes: Dynamic UI adapts to user behavior

**Result:** Hyper-personalized experience with simple interface

---

### Microservices: Flexibility vs Complexity

**Contradiction:** Independent deployment (Parameter 35: Adaptability) worsens System complexity (Parameter 36)

**Principles Applied:**
- #1 Segmentation: Break monolith into services
- #24 Intermediary: API Gateway, Service Mesh
- #25 Self-Service: Auto-discovery, self-healing

**Result:** Netflix, Amazon scale with thousands of services

---

### Git: Collaboration vs Conflicts

**Contradiction:** Multiple contributors (Parameter 39: Productivity) causes merge conflicts (Parameter 27: Reliability)

**Principles Applied:**
- #1 Segmentation: Branch-based development
- #10 Preliminary Action: Pull before push
- #17 Another Dimension: Distributed (not centralized)

**Result:** Millions collaborate on same codebase

---

## Classic TRIZ Cases

### Airplane De-icing

**Problem:** Ice forms on wings during flight

**IFR:** "Wing itself prevents ice formation"

**FOS Search:**
| Industry | Solution | Mechanism |
|----------|----------|-----------|
| Medicine | Blood vessels | Warm fluid circulation |
| Nature | Lotus leaf | Hydrophobic surface |
| Food | Non-stick pan | Surface coating |

**Solution:** Heated wing edges + hydrophobic coating

---

### Submarine Periscope

**Physical Contradiction:** Periscope must be LONG (to see above water) AND SHORT (to not be detected)

**Separation in Time:** Extend when needed, retract otherwise

**Separation in Space:** Multiple short sections that extend

**Solution:** Telescoping periscope

---

### Coffee Cup Lid

**Physical Contradiction:** Opening must be LARGE (to drink) AND SMALL (to prevent spilling)

**Separation in Condition:** Large when tilted (drinking), small when upright (carrying)

**Solution:** Shaped opening that controls flow based on tilt angle

---

## Thai Language Examples

| English Term | Thai | Example |
|--------------|------|---------|
| Ideal Final Result | ผลลัพธ์ในอุดมคติ | "ท่อน้ำป้องกันการรั่วได้เอง" |
| Technical Contradiction | ข้อขัดแย้งทางเทคนิค | ความเร็ว vs น้ำหนัก |
| Physical Contradiction | ข้อขัดแย้งทางกายภาพ | ต้องร้อนและเย็นพร้อมกัน |
| Inventive Principle | หลักการประดิษฐ์คิดค้น | การแบ่งส่วน, การกลับด้าน |
| Separation Principle | หลักการแยก | แยกในเวลา/พื้นที่/สภาวะ |

---

## Quick Reference: Principle Application Patterns

### Most Versatile Principles by Domain

| Domain | Top Principles | Why |
|--------|---------------|-----|
| **Software** | 1, 2, 10, 13, 24, 25 | Modular, async, caching patterns |
| **Hardware** | 1, 3, 15, 28, 35, 40 | Materials, dynamics, energy |
| **Process** | 10, 19, 20, 21, 25 | Timing, flow, automation |
| **UX** | 1, 3, 13, 15, 33 | Personalization, simplicity |

### Common Contradiction Pairs → Principles

| Improve | Worsens | Try Principles |
|---------|---------|---------------|
| Speed | Reliability | 10, 21, 35 |
| Strength | Weight | 1, 28, 40 |
| Features | Simplicity | 1, 2, 15 |
| Security | Performance | 10, 24, 28 |
| Flexibility | Stability | 1, 15, 35 |
