# NSF SBIR Phase I Submission Guide — Embino

*Strategic guide for maximizing approval probability*

---

## Overview: What Makes NSF SBIR Different

NSF SBIR is **highly competitive** (~15-20% approval rate). Unlike other agencies:

1. **Project Pitch is MANDATORY** — You cannot submit without an invitation
2. **Commercialization weighs heavily** — Not just technical merit
3. **I-Corps training expected** — $25k budget line
4. **No general letters of support** — Only commitment letters from subcontractors/consultants
5. **Three review criteria** — Technical Merit, Broader Impacts, Commercialization Potential

---

## The Two-Step Process

### Step 1: Project Pitch (Get Invited First)

The Project Pitch is a **brief online form** submitted through NSF's portal. It's reviewed in 2-3 weeks.

**What reviewers look for:**
- Clear problem/solution with technical risk
- Evidence of commercial potential
- Team capability signal
- Alignment with NSF priorities (deep tech, not incremental)

**Pitch Strategy:**
- Lead with the problem (programming MCUs is stuck in 1985)
- Name the gap explicitly (no safe middle layer between NL and C)
- State what's new (DSL + Micro-VM + validated translator)
- Show you've thought about market (billions of MCUs, underserved makers)

### Step 2: Full Proposal (After Invitation)

Invitation is valid for **two** submission windows. Next deadlines:
- **March 05, 2025**
- **July 02, 2025**
- **November 05, 2025**

---

## The Three Review Criteria (Know What Scores)

### 1. Intellectual Merit (Technical Innovation)

**What they want:**
- Is this actually new? (Not a library, not incremental)
- Is there real technical risk? (Not routine engineering)
- Is the R&D plan sound?
- Can this team execute?

**Embino strengths:**
- Novel abstraction layer (DSL with formal safety model)
- Clear technical risks identified (DSL expressiveness, translation reliability, resource limits)
- Well-defined objectives with measurable outcomes

**What to strengthen:**
- Cite related work / prior art to show gap
- Preliminary data (even a toy DSL grammar + working interpreter)
- Named experts (PL/compilers consultant, embedded systems advisor)

### 2. Broader Impacts (Societal Benefit)

**What they want:**
- Who benefits beyond your company?
- Education, workforce, economic competitiveness?
- Underrepresented groups? STEM pipeline?

**Embino angles:**
- Democratizes embedded programming (non-experts can prototype)
- Educational value (teaching control logic without C complexity)
- Economic: US competitiveness in IoT/robotics manufacturing
- Safety: Deterministic behavior in safety-critical applications

### 3. Commercialization Potential (Market Viability)

**What they want:**
- Real market evidence (not just TAM/SAM numbers)
- Specific customers you've talked to
- Clear business model
- Competitive advantage / defensibility (IP, network effects, switching costs)

**Embino needs:**
- Letters of commitment (not support!) from potential customers/pilots
- Specific conversations with dev-board vendors, robotics startups, automation integrators
- Revenue model clarity (SDK licensing? Board sales? SaaS toolchain?)

---

## Common Rejection Reasons (Avoid These)

1. **"Incremental, not innovative"** — Show what's truly new
2. **"Insufficient technical risk"** — If it's obviously feasible, it's not SBIR material
3. **"Weak commercialization plan"** — Vague market size without customer evidence
4. **"Team lacks capability"** — No named experts or track record
5. **"Scope too broad"** — Phase I is proof-of-concept, not product launch
6. **"Budget doesn't align with work"** — Every dollar must tie to a task
7. **"Poor writing quality"** — Reviewers skim; clarity matters

---

## NSF-Specific Requirements Checklist

### Required Documents

| Document | Status | Notes |
|----------|--------|-------|
| Project Pitch (online) | ❌ Not submitted | Submit anytime; requires invitation |
| Cover Sheet (Research.gov) | — | Generated at submission |
| Project Summary (1 page) | ❌ To write | Overview, Intellectual Merit, Broader Impacts |
| Project Description (15 pages) | ❌ To write | The core proposal |
| Budget + Justification | ❌ To prepare | ≤$305k, must include I-Corps ($25k) + TABA ($6.5k) |
| Biographical Sketches (SciENcv) | ❌ Needed | For PI + all senior personnel |
| Current & Pending (SciENcv) | ❌ Needed | For PI + all senior personnel |
| Collaborators & Affiliations (COA) | ❌ Needed | Excel template from NSF |
| Data Management Plan | ❌ To write | 1-2 pages |
| Letters of Commitment | ❌ To collect | From consultants, subawardees only |
| Project Pitch Invitation Email | — | Upload after receiving |

### What You CANNOT Include

- ❌ General letters of support
- ❌ URLs in Project Description
- ❌ Appendices (unless specifically allowed)
- ❌ Pre-award costs

---

## Recommended Timeline

| When | Action |
|------|--------|
| Week 1-2 | Fill out questionnaire (next file); draft Project Pitch |
| Week 3 | Submit Project Pitch; line up consultants |
| Week 4-5 | (Wait for invitation) Begin SciENcv biosketches |
| Week 6+ | Full proposal writing; budget preparation |
| 2 weeks before deadline | Internal review; finalize letters |
| 1 week before | Research.gov submission + compliance check |

---

## Budget Strategy ($305k)

Based on `basic_project.md`, a strong budget structure:

| Category | Amount | Justification |
|----------|--------|---------------|
| Direct Labor (PI + 1 engineer) | ~$130k | 1.0 FTE PI + 0.5-0.75 FTE embedded engineer |
| Fringe Benefits | ~$32k | ~25% of labor |
| Overhead/Indirect | ~$49k | ~30% of (labor + fringe) |
| Consultants | ~$25k | PL/compiler expert + embedded advisor |
| Equipment & Supplies | ~$10k | Dev boards, sensors, actuators |
| Travel | ~$5k | Customer visits, NSF events |
| TABA | $6.5k | Commercialization assistance (required) |
| I-Corps | $25k | Required budget line |
| Fee (7%) | ~$20k | Allowed profit margin |
| **Total** | ~$303k | Under $305k cap |

---

## Embino's Competitive Advantages

Highlight these throughout:

1. **Novel abstraction** — Not a framework, not a library, a new layer
2. **Formal safety guarantees** — Bounded resources, deterministic timing
3. **LLM bridge with validation** — Best of both worlds (expressiveness + safety)
4. **Hardware-agnostic** — Works on ESP32, Arduino, RP2040
5. **Clear roadmap** — Add-on → Integrated → Custom chip

---

## Next Steps

1. **Fill out the questionnaire** → `SBIR_QUESTIONNAIRE.md`
2. **Draft your Project Pitch** → Use template in `drafts/`
3. **Reach out to potential consultants** → PL/compiler expert, embedded advisor
4. **Identify 2-3 pilot customers** → For commitment letters
5. **Create SciENcv accounts** → For biosketches

---

*Last updated: 2025-11-30*

