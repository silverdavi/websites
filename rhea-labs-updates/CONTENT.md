# Rhea Labs — 2025 Recap & 2026 Direction

*For Rhea Fertility / Gen Prime*

---

## TL;DR

2025: We shipped research that got accepted for oral presentation, built the Bonna Suite foundation, and added product leadership.

2026: Consolidation. More tools hit production. RheaX goes live. Cross-module learning becomes real.

---

## Who We Are

Rhea Labs is the AI and decision-systems arm of Rhea Fertility.

We don't build incremental features. We build systems that handle the hard problems:

- High-dimensional inputs
- Weak or delayed labels  
- Irreversible clinical decisions
- Heterogeneous data across clinics

Fertility medicine has plenty of data. What it lacks is **structure**.

Our job: turn clinical signals into systems that clinicians can measure, explain, and trust.

---

## 2025 Highlights

### Research: Oral Presentation Accepted

Our paper on evaluation metrics and clinical AI accountability was accepted for **oral presentation**:

> *"Not a high-level opinion piece but a rigorous analysis... includes a formal incompatibility result demonstrating potential failures of average metrics like AUC."*
>
> *"A significant and timely contribution to building and validating clinically trusted AI."*

**Title:** *From AUC to Accountability: Metric Choices, Social Norms, and the Deployment of Therapeutic AI*

This isn't academic vanity. The paper directly shapes how we validate Rhea Labs models:

- Outcome-aligned evaluation over vanity metrics
- Explicit subgroup and tail-risk constraints
- Rejection of high-AUC-low-subgroup-performance traps

It also establishes Rhea Labs as a voice in responsible clinical AI — not just a product shop.

---

### Team: Product Leadership

**December 2025:** Chris Homburger joined as **Product Manager, Rhea Labs**.

Chris works with:
- Lawrence Wu
- Daniel Madero
- David Silver

Across:
- **Bonna Suite** — the clinical AI tools
- **RheaX** — the gamete exchange platform

This marks a shift from pure R&D to structured productization.

---

### Product: The Bonna Suite

The Bonna Suite is a coherent set of AI tools spanning the fertility journey:

| Tool | Status |
|------|--------|
| Egg Freezing Calculator | Standard Product |
| Embryo Quality Assessment | Beta Adoption |
| Oocyte Viability Assessor | Used by Clinics |
| Sperm Quality Analyzer | Algorithm Ready |
| Hormonal Protocol Recommender | Data Collected |
| Endometrial Receptivity Analyzer | Early Development |

Each module targets a specific clinical decision point.

But they share:
- Common data infrastructure
- Unified evaluation philosophy
- Cross-module learning (coming 2026)

---

## Roadmap

Progress is intentionally staggered. Different tools have different:
- Data availability
- Validation burdens
- Clinical risk profiles

This is strategy, not bottleneck.

### Stage Definitions

| Stage | Definition |
|-------|------------|
| 1 | UX/UI Ready |
| 2 | API Ready |
| 3 | Data Collected |
| 4 | Algorithm Ready |
| 5 | Used by Clinics |
| 6 | Beta Adoption (>20% Rhea cycles) |
| 7 | Standard Product (>50% Rhea cycles) |
| 8 | External Usage (>10% umbrella cycles) |

### Current State (Q4 2025)

```
                        Q4'24  Q1'25  Q2'25  Q3'25  Q4'25  Q1'26  Q2'26
Egg Freezing             ██████████████████████████████████  → Standard
Embryo Quality           ████████████████████████████  → Beta Adoption
Oocyte Viability         ██████████████████  → Clinical Use
Sperm Quality            ████████████  → Algorithm Ready
Hormonal Protocol        ██████████  → Data Collection
Endometrial Receptivity  ██████  → Early Stage
```

*Full visual roadmap attached separately.*

---

## Beyond Bonna

### RheaX

Gamete exchange and coordination platform.

Not a tool — infrastructure. Shared modeling, shared data contracts, shared governance with Bonna.

### Tilly

Patient-facing and operational capabilities. Complements Bonna's clinical intelligence with workflow integration.

---

## What We Learned

**On data:**
High-quality clinical data is expensive — in time, trust, and operational cost. No shortcuts.

**On adoption:**
Clinics adopt AI when it:
1. Fits their workflow
2. Explains itself
3. Respects clinical judgment

**On rigor:**
Rigor builds slower than hype. But it compounds harder.

These lessons are now encoded in:
- Roadmap pacing
- Evaluation methodology
- Partnership model

---

## 2026 Direction

| Focus | Action |
|-------|--------|
| Consolidation | More tools reach Standard Product |
| Cross-module | Learning across Bonna Suite becomes operational |
| External | Controlled expansion beyond Rhea-owned clinics |
| Infrastructure | RheaX and Bonna share data and signal layer |

The goal isn't speed. It's **compounding trust**.

---

## Closing

Rhea Labs exists because fertility medicine needs more than incremental improvement.

It needs systems that:
- Reason under uncertainty
- Learn from outcomes
- Earn clinical confidence

2025 was foundation.

2026 is scale — carefully, responsibly, with intent.

---

*David Silver*  
*Head of AI/ML, Rhea Labs*  
*david.silver@rhea-fertility.com*

---

## Appendix: Roadmap Generation Code

```python
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import numpy as np

quarters = [
    "Q4 '23", "Q1 '24", "Q2 '24", "Q3 '24", "Q4 '24",
    "Q1 '25", "Q2 '25", "Q3 '25", "Q4 '25",
    "Q1 '26", "Q2 '26", "Q3 '26", "Q4 '26"
]

tools = [
    "Egg Freezing Calculator",
    "Embryo Quality Assessment",
    "Oocyte Viability Assessor",
    "Sperm Quality Analyzer",
    "Hormonal Protocol Recommender",
    "Endometrial Receptivity Analyzer",
]

stage_matrix = np.array([
    [0, 0, 4, 5, 5, 5, 6, 7, 7, 8, 8, 8, 8],
    [0, 0, 2, 3, 3, 4, 4, 5, 6, 7, 7, 8, 8],
    [0, 0, 0, 1, 2, 2, 3, 4, 4, 5, 6, 7, 8],
    [0, 0, 0, 0, 1, 2, 2, 3, 4, 4, 5, 6, 7],
    [0, 0, 0, 0, 1, 1, 2, 2, 3, 4, 5, 6, 7],
    [0, 0, 0, 0, 0, 1, 1, 2, 2, 2, 3, 4, 5],
])

stage_colors = {
    1: "#e6ccff", 2: "#cc99ff", 3: "#9933ff", 4: "#6600cc",
    5: "#d9b38c", 6: "#a3755a",
    7: "#99ff99", 8: "#00cc00"
}

stages_legend = [
    "1: UX/UI Ready",
    "2: API Ready",
    "3: Data Collected",
    "4: Algorithm Ready",
    "5: Used by Clinics",
    "6: Beta Adoption (>20% Rhea cycles)",
    "7: Standard Product (>50% Rhea cycles)",
    "8: External Usage (>10% umbrella cycles)"
]

custom_cmap = mcolors.ListedColormap([stage_colors[i] for i in range(1, 9)])
custom_norm = mcolors.BoundaryNorm(range(1, 10), custom_cmap.N)

fig, ax = plt.subplots(figsize=(10, 14))

for i, tool in enumerate(tools):
    x = [i] * len(quarters)
    ax.scatter(
        x, np.arange(len(quarters)),
        c=stage_matrix[i], cmap=custom_cmap, norm=custom_norm, 
        s=400, marker='s', edgecolor='black', label=tool
    )

ax.xaxis.tick_top()
ax.set_xticks(range(len(tools)))
ax.set_xticklabels(tools, fontsize=12, weight='bold', rotation=45, ha='left')
ax.set_yticks(range(len(quarters)))
ax.set_yticklabels(quarters, fontsize=11, weight='bold')
ax.set_title("Bonna Suite Development Roadmap", fontsize=18, weight='bold', pad=20)
ax.set_ylabel("Quarter", fontsize=14)
ax.set_ylim(-0.5, len(quarters) - 0.5)
ax.invert_yaxis()

legend_handles = [
    plt.Line2D([0], [0], marker='s', color='w', markerfacecolor=stage_colors[i],
               markersize=10, label=stages_legend[i - 1]) for i in range(1, 9)
]
ax.legend(handles=legend_handles, loc='lower center', bbox_to_anchor=(0.5, -0.15),
          ncol=2, fontsize=10, title="Stages", title_fontsize=12, frameon=False)

plt.tight_layout()
plt.savefig('roadmap_2025.png', dpi=150, bbox_inches='tight')
plt.show()
```

