# USPTO Provisional Patent Application — Submission Checklist

## Application: Hydro-Thermal Agitation System (HTAS)

**Title:** Systems and Methods for Automated Preparation of Granular Starch-Based Food Products via Hydro-Thermal Agitation with Closed-Loop Sensor Control

---

## ✅ Documents Prepared

| Document | File | Status |
|----------|------|--------|
| Specification | `provisional.md` → convert to PDF | ☐ Ready |
| Drawings (5 figures) | `fig1-5_*.pdf` | ✅ Generated |
| Cover Sheet | `cover_sheet.md` → complete & sign | ☐ Ready |

---

## Filing Fees (as of 2025)

| Entity Status | Fee |
|--------------|-----|
| **Micro Entity** | $60 |
| **Small Entity** | $120 |
| Large Entity | $300 |

### Micro Entity Qualification (37 CFR 1.29)
You qualify as **Micro Entity** if ALL of the following are true:
- [ ] Qualify as Small Entity (< 500 employees)
- [ ] Named on ≤ 4 previously filed patent applications (excluding provisionals & foreign)
- [ ] Gross income did not exceed 3× median household income (~$225,000 for 2024)
- [ ] Have not assigned/licensed rights to entity exceeding the income limit

### Small Entity Qualification
You qualify as **Small Entity** if:
- [ ] Individual inventor, OR
- [ ] Small business (< 500 employees), OR
- [ ] Nonprofit organization

---

## Step-by-Step Filing Instructions

### Step 1: Prepare Final Documents

```bash
# In the food_patent directory:

# 1. Convert specification to PDF (use any method):
#    - Open provisional.md in a Markdown viewer → Print to PDF
#    - Or use pandoc: pandoc provisional.md -o SPECIFICATION.pdf

# 2. Combine drawings into single PDF:
pdftk fig1_cross_section.pdf fig2_manifold.pdf fig3_agitator.pdf \
      fig4_algorithm.pdf fig5_sensor_control.pdf cat output DRAWINGS.pdf

# Or on Mac without pdftk:
# Open all PDFs in Preview → View → Thumbnails → Drag to combine → Export as PDF
```

### Step 2: Complete the Cover Sheet

Edit `cover_sheet.md` to fill in:
- [ ] Inventor name(s) and address(es)
- [ ] Correspondence address
- [ ] Entity status declaration

### Step 3: Go to USPTO Patent Center

1. **URL:** https://patentcenter.uspto.gov

2. **Create account** (if you don't have one):
   - Click "Sign In" → Create USPTO.gov account
   - Verify email

3. **Start New Submission:**
   - Click "New Submission" → "Provisional Application"

### Step 4: Upload Documents

Upload these files in order:

| Document Type | File to Upload |
|--------------|----------------|
| Specification | `SPECIFICATION.pdf` |
| Drawings | `DRAWINGS.pdf` |
| Application Data Sheet | (optional, can complete online) |

### Step 5: Complete Online Forms

The Patent Center will walk you through:
- [ ] Application type: **Provisional**
- [ ] Title of invention
- [ ] Inventor information
- [ ] Correspondence address
- [ ] Entity status (Micro/Small/Large)

### Step 6: Pay Filing Fee

- Accept the calculated fee
- Pay via credit card, deposit account, or EFT
- **Keep the confirmation receipt!**

### Step 7: Receive Filing Receipt

- USPTO will provide an **Application Number** (format: 63/XXX,XXX)
- Save this! You'll need it for the non-provisional filing

---

## Important Dates

| Event | Deadline |
|-------|----------|
| **Filing Date** | [DATE YOU FILE] |
| **12-Month Deadline** | [FILING DATE + 12 months] |
| Must file non-provisional by | ↑ or lose priority date |

---

## Post-Filing Actions

### Immediately After Filing:
- [ ] Save filing receipt PDF
- [ ] Note application number: `63/___________`
- [ ] Set calendar reminder for 11-month mark

### Within 12 Months:
- [ ] File non-provisional patent application (utility patent)
- [ ] OR file PCT application for international protection
- [ ] Claims will be formally examined in non-provisional

### Optional:
- [ ] Use "Patent Pending" on product/marketing materials
- [ ] Continue development and document improvements (for continuation applications)

---

## Files in This Directory

```
shared/food_patent/
├── SUBMISSION_CHECKLIST.md    ← You are here
├── provisional.md             ← Main specification (convert to PDF)
├── cover_sheet.md             ← Fill in inventor info
├── draft.md                   ← Original detailed draft (internal use)
├── generate_figures.py        ← Figure generation script
├── fig1_cross_section.pdf     ← FIG. 1
├── fig2_manifold.pdf          ← FIG. 2
├── fig3_agitator.pdf          ← FIG. 3
├── fig4_algorithm.pdf         ← FIG. 4
└── fig5_sensor_control.pdf    ← FIG. 5
```

---

## Quick Reference Links

- **USPTO Patent Center:** https://patentcenter.uspto.gov
- **Provisional Application Info:** https://www.uspto.gov/patents/basics/apply/provisional-application
- **Fee Schedule:** https://www.uspto.gov/learning-and-resources/fees-and-payment/uspto-fee-schedule
- **Form PTO/SB/16 (Cover Sheet):** https://www.uspto.gov/sites/default/files/documents/sb0016.pdf

---

## Need Help?

- **USPTO Contact Center:** 1-800-786-9199
- **Patent Center Help:** Click "Help" in top-right of Patent Center

Good luck with your filing! 🎉

