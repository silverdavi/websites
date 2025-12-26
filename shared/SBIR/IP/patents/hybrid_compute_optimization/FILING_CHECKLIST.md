# Provisional Patent Filing Checklist
## KK-2025-PROV-002: Hybrid Compute Optimization / Distributed Neuron Nodes

---

## PRE-FILING PREPARATION

### Documents Ready

- [ ] **Specification (draft.md)** — Convert to PDF
  - Title of invention
  - Field of invention
  - Background
  - Summary
  - Brief description of drawings
  - Detailed description (15+ pages)
  - Examples
  - Conclusion

- [x] **Claim Language (CLAIMS.md)** — Convert to PDF or append to specification
  - 4 independent claims + 26 dependent claims (Track One compliant)
  - Independent claims (HIL method, search-space shaping, system, robotic system)
  - Dependent claims for key features (robotics, calibration, safety)

- [ ] **Cover Sheet (COVER_SHEET.md)** — Convert to PDF
  - Inventor name and address
  - Correspondence address
  - Title of invention
  - Entity status declaration

- [x] **Drawings (6 figures)** — Created and converted to PDF
  - FIG. 1: System architecture (hybrid substrate + optimization loop)
  - FIG. 2: Search-space shaping mechanism
  - FIG. 3: Closed-loop optimization flow
  - FIG. 4: ANN-node hardware architecture
  - FIG. 5: Robotic deployment (nodes on robot body)
  - FIG. 6: Deterministic deployment artifact structure

### Prior Art / IDS Documents

- [x] **Prior Art Report (PRIOR_ART_REPORT.md)** — Internal analysis document
  - Categorized prior art references (5 categories)
  - Patent references (17 documents)
  - Non-patent literature (13 documents)
  - Distinction analysis
  - Executive summary

- [x] **IDS References (IDS_REFERENCES.md)** — For USPTO Form PTO/SB/08
  - U.S. patent documents table
  - Foreign patent documents table
  - Non-patent literature table
  - Certification statement

### Administrative Items

- [ ] **USPTO Account** — Register at https://patentcenter.uspto.gov
- [ ] **Filing Fee** — $160 (small entity) or $80 (micro entity)
- [ ] **Payment Method** — Credit card, deposit account, or EFT

---

## ENTITY STATUS VERIFICATION

### Small Entity (37 CFR 1.27) — $160 fee

Kernel Keys LLC qualifies if ALL are true:

- [x] Fewer than 500 employees
- [x] Has not assigned/licensed rights to large entity
- [x] Not majority owned by large entity

### Micro Entity (37 CFR 1.29) — $80 fee

Would qualify if ALL are true:

- [x] Qualifies as small entity
- [ ] Named on ≤4 prior US patent applications (excluding provisionals, foreign priority)
- [ ] Gross income < 3× median household income (~$240,000 in 2024)
- [ ] Has not assigned rights to entity exceeding gross income limit

> **Recommendation:** File as **Small Entity** unless you're certain of micro entity qualification.

---

## USPTO PATENT CENTER FILING STEPS

### Step 1: Access USPTO

1. Go to https://patentcenter.uspto.gov
2. Log in or create account (requires email verification)
3. Select "New Submission"

### Step 2: Select Application Type

1. Choose "Patent" → "Provisional Application"
2. Confirm "New Application"

### Step 3: Upload Documents

| Document | File Type | Required |
|----------|-----------|----------|
| Specification (SPECIFICATION.pdf/docx) | PDF/DOCX | ✓ Yes |
| Claims (CLAIMS.pdf/docx) | PDF/DOCX | ✓ Yes |
| Drawings (DRAWINGS.pdf) | PDF | Recommended |
| Cover Sheet | PDF | Optional but recommended |
| IDS (IDS_REFERENCES.pdf + copies) | PDF | Recommended |
| Application Data Sheet | PDF | Optional for provisional |

### Step 4: Enter Application Data

| Field | Value |
|-------|-------|
| Title | Systems and Methods for Closed-Loop Optimization of Hybrid and Under-Specified Compute Architectures with Language Model-Driven Search Space Shaping |
| Inventor(s) | Haim David Silver |
| Entity Status | Small Entity |
| Correspondence | Kernel Keys LLC, 7 Bancroft Rd, Poughkeepsie, NY 12601 |

### Step 5: Pay Fee

- Small Entity: **$160**
- Payment methods: Credit card, USPTO deposit account, EFT

### Step 6: Submit and Confirm

1. Review all entries
2. Click "Submit"
3. Download/print confirmation
4. Save Application Number (format: 63/XXX,XXX)

---

## POST-FILING ACTIONS

### Immediate (Day of Filing)

- [ ] Download filing receipt
- [ ] Save Application Number
- [ ] Note filing date (= priority date)
- [ ] Set 12-month calendar reminder

### Within 1 Week

- [ ] Create docket entry in tracking system
- [ ] File confirmation in company records
- [ ] Update SBIR proposal IP section with filing info

### Within 12 Months (CRITICAL)

- [ ] Decide: File non-provisional US application, OR
- [ ] Decide: File PCT international application, OR
- [ ] Let provisional expire (lose priority)

> **Deadline:** 12 months from filing date. Missing this deadline forfeits priority rights.

---

## KEY DATES TRACKER

| Event | Date | Status |
|-------|------|--------|
| Provisional Filing | ________ | ☐ |
| SBIR Phase I Submission | ________ | ☐ |
| 6-Month Review | ________ | ☐ |
| 9-Month Decision Point | ________ | ☐ |
| **12-Month Deadline** | ________ | ☐ CRITICAL |

---

## FILING COST SUMMARY

| Item | Cost |
|------|------|
| USPTO Provisional Filing Fee (Small Entity) | $160 |
| Attorney/Agent (if used) | $0 (Pro Se) |
| **Total Filing Cost** | **$160** |

### Future Costs (Non-Provisional Path)

| Item | Small Entity Cost |
|------|-------------------|
| Non-provisional filing fee | ~$800 |
| Search fee | ~$320 |
| Examination fee | ~$400 |
| Issue fee (if allowed) | ~$500 |
| Patent attorney (typical) | $5,000–$15,000 |

---

## COMMON MISTAKES TO AVOID

1. **Missing 12-month deadline** — Calendar it immediately
2. **Wrong entity status** — Verify small entity qualification
3. **Insufficient description** — Include all embodiments you may claim later
4. **No claim-like language** — Strengthens priority support
5. **Missing drawings** — Not required but highly recommended
6. **Wrong inventor** — List all true inventors, not assignees

---

## DOCUMENT ASSEMBLY CHECKLIST

Before filing, combine into single or multiple PDFs:

### Option A: Single PDF (Recommended)

1. Cover sheet (1-2 pages)
2. Specification with drawings (15-18 pages)
3. Claim language appendix (6-8 pages)

### Option B: Separate PDFs

1. Cover sheet PDF
2. Specification PDF
3. Drawings PDF
4. Claims PDF

---

## RELATIONSHIP TO PRIOR APPLICATION

This application (KK-2025-PROV-002) extends and builds upon:
- **KK-2025-PROV-001:** Systems and Methods for Grammar-Constrained Code Generation and Execution on Resource-Limited Embedded Devices

The prior application covers GC-SLM + micro-interpreter. This application adds:
- Hybrid/under-specified compute optimization
- Search-space shaping (LLM modifies IR/grammar)
- Distributed ANN-nodes for robotics
- Hardware-in-the-loop calibration

---

## FINAL VERIFICATION

Before clicking "Submit":

- [ ] Inventor name spelled correctly
- [ ] Address complete and accurate
- [ ] Title matches specification
- [ ] All pages uploaded and readable
- [ ] Fee amount correct for entity status
- [ ] Payment information valid
- [ ] Relationship to prior application noted (if filing as continuation)

---

*Checklist Version: 1.0*
*Created: December 2025*
*Docket: KK-2025-PROV-002*

