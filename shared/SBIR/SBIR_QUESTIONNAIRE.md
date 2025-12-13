# SBIR Questionnaire — Kernel Keys LLC (Embino Project)

*Your answers will directly populate the proposal. TBD = still needed.*

---

## Section A: Company Information

### A1. Company Basics

| Field | Your Answer |
|-------|-------------|
| Legal company name | Kernel Keys LLC |
| DBA (if different) | None |
| State of incorporation | New York |
| Date incorporated | 11/07/2024 |
| EIN (Tax ID) | 33-1937834 |
| DUNS / UEI number | **TBD** (required for submission) |
| Number of employees | 1 (founder) + contractors |
| SBC certification? (Y/N) | Yes |
| Woman-owned? (Y/N) | No |
| Minority-owned? (Y/N) | No |
| HUBZone? (Y/N) | No |

### A2. Company Address

| Field | Your Answer |
|-------|-------------|
| Street address | 7 Bancroft Rd |
| City | Poughkeepsie |
| State | NY |
| ZIP | 12601 |
| Phone | +1-929-782-2060 |
| Website | https://kernel-keys.com |

### A3. Company Structure

**Ownership (list all owners with >5% stake):**

| Name | % Ownership | Role | US Citizen/Resident? |
|------|-------------|------|---------------------|
| Haim David (David) Silver | 100% | Founder & Principal Investigator | Yes (US citizen) |

**Is the company independently owned and operated?** (Required for SBIR eligibility)

```
[x] Yes
[ ] No
```

**Any affiliations with other companies, universities, or organizations?**

```
No formal ownership or control affiliations. Informal collaborations only.
```

---

## Section B: Principal Investigator (PI)

### B1. PI Information

| Field | Your Answer |
|-------|-------------|
| Full name | Haim David (David) Silver |
| Title/Position | Founder & Principal Investigator |
| Email | **TBD** |
| Phone | +1-929-782-2060 |
| ORCID | 0000-0002-3071-304X |
| % employed by this company | >50% (SBIR-compliant) |

> **Note:** For SBIR, PI must be >50% employed by the small business. ✅

### B2. PI Qualifications

**Education (degrees, institutions, years):**

```
- Extensive graduate-level research training in computational biology, 
  evolutionary genomics, and machine learning (non-US institution)
- Microsoft Research Excellent PhD Student Scholarship — competitive 
  research-merit scholarship for top PhD-track students in CS/ML
- Continuous post-academic research and engineering career leading AI/ML 
  work in industry (Intel, Apple, Embryonics/Rhea Labs, food-tech and 
  fertility-tech startups)
```

**Relevant work experience (last 10 years):**

| Company | Role | Years | Relevance to this project |
|---------|------|-------|--------------------------|
| Embryonics / Rhea Labs | Chief Scientist / Head of AI | 2019–2024 | Medical-grade ML systems, validated pipelines, regulatory-aware design |
| Remiza LTD (Israel) | Founder & Principal Consultant | 2014–present | Data-driven solutions for traditional industries; translating ML for non-expert users |
| Apple Inc. | Machine Learning Engineer | 2016–2019 | Depth-sensing, imaging, systems-level constraints, embedded-ish stacks |
| Intel Corporation | Computer Vision / 3D Imaging Engineer | pre-2016 | RealSense depth camera algorithms, hardware constraints, low-level optimization |
| Academic research | Researcher / Co-author | 2011–2018 | Publications in Nature, PNAS, Bioinformatics; quantitative/statistical background |

**Key publications relevant to this work (list 3-5):**

```
1. Silver DH et al. "Intel RealSense SR300 coded light depth camera." 
   IEEE TPAMI, 2020.
2. Fordham DE et al. "Embryologist agreement when assessing blastocyst 
   implantation probability..." Human Reproduction, 2022.
3. Rave G, Fordham DE, Bronstein AM, Silver DH. "Enhancing Predictive 
   Accuracy in Embryo Implantation: The Bonna Algorithm..." LNCS, 2024.
4. Levin M et al. "The mid-developmental transition and the evolution 
   of animal body plans." Nature, 2016.
5. Schiffer PH et al. "The gene regulatory program of Acrobeloides nanus..."
   PNAS, 2018.
```

**Patents relevant to this work:**

```
1. "Enhanced depth mapping using visual inertial odometry" — US 12153140, Apple, 2024
2. "Calibration of a depth sensing array using color image data" — US 11914078, Apple, 2024
3. "Auto range control for active illumination depth camera" — US 10451189B2, Intel, 2019
4. "Morphological and geometric edge filters for depth images" — US 9852495B2, Intel, 2017
5. "Range reconstruction using shape prior" — US 10775501B2, Intel, 2020
6. "Code filters for coded light depth acquisition" — US 20170178294A1, Intel, 2017
7. "Estimating Oocyte Quality" — US 20220375069A1, Embryonics, 2022
8. "Predicting embryo implantation probability" — WO 2022009186A1, Embryonics, 2022
9. "Molecular embedding systems and methods" — WO 2023170641A1, Aka Foods, 2023
10. "Mixture modeling systems and methods" — WO 2023170640A1, Aka Foods, 2023
11. "Food processing systems and methods" — WO 2023170639A1, Aka Foods, 2023
```

**Prior SBIR/STTR awards?**

```
[x] No — first-time SBIR PI and company
[ ] Yes
```

### B3. PI's Role in This Project

**What specific tasks will you personally perform?**

```
- Define the Embino DSL semantics and syntax, including safety model and type system
- Design the bytecode format and execution model for the interpreter
- Implement core compiler pipeline (front-end, type checking, bytecode generation)
- Implement or closely supervise micro-interpreter for ESP32/Arduino-class devices
- Design and run performance and memory benchmarks on selected MCU boards
- Plan and conduct structured interviews and usability tests with early adopters
- Lead technical documentation, architecture docs, and Phase I final report
```

**Estimated % of your time on this project:**

```
~65%
```

---

## Section C: Team

### C1. Key Personnel (employees or to-be-hired)

**Person 1:**

| Field | Answer |
|-------|--------|
| Name (or "To be hired") | To be hired |
| Role | Compiler / Toolchain Engineer |
| Current employer | N/A |
| Relevant expertise | C/C++, compiler construction, embedded toolchains, LLVM or custom bytecode VMs |
| % time on project | 20–30% |

**Person 2:**

| Field | Answer |
|-------|--------|
| Name (or "To be hired") | To be hired |
| Role | Firmware / Embedded Engineer |
| Current employer | N/A |
| Relevant expertise | ESP32/STM32/Arduino ecosystem, real-time scheduling, hardware abstraction |
| % time on project | ~20% |

### C2. Consultants / Subcontractors

> Consultants and subs can do max 33% of the work. Max consultant rate is $1,000/day.

**Consultant 1:**

| Field | Answer |
|-------|--------|
| Name | **TBD** |
| Affiliation | Independent embedded systems expert |
| Expertise | Real-time scheduling, safety-critical control systems |
| Specific contribution | Review and stress-test interpreter scheduling/timing model; derive WCET bounds |
| Days of effort | 10–15 days |
| Rate ($/day) | $1,000 |
| Total cost | $10,000–$15,000 |
| Will they provide a Letter of Commitment? | Yes (to be obtained) |

**Consultant 2:**

| Field | Answer |
|-------|--------|
| Name | **TBD** |
| Affiliation | Independent dev-tools / UX specialist |
| Expertise | Programming language usability, dev experience for non-expert coders |
| Specific contribution | Validate DSL is understandable by non-experts; help design tutorials/examples |
| Days of effort | 5–10 days |
| Rate ($/day) | $800 |
| Total cost | $4,000–$8,000 |
| Will they provide a Letter of Commitment? | Yes (to be obtained) |

### C3. Advisory Board / Informal Advisors

| Name | Affiliation | Area of Expertise | Relationship |
|------|-------------|-------------------|--------------|
| **TBD** | | Embedded hardware | |
| **TBD** | | STEM education | |
| **TBD** | | Robotics | |

---

## Section D: Technical

### D1. The Problem

**In 2-3 sentences, what is the core problem you're solving?**

```
Low-cost microcontroller boards (Arduino, ESP32, etc.) are everywhere, but 
programming them still requires C/C++ and fragile toolchains. Non-expert users 
and small teams face steep learning curves, subtle bugs, and long iteration 
cycles. The gap between "simple idea for a behavior" and "reliable firmware" 
is unnecessarily large.
```

**Who experiences this problem? Be specific:**

```
- Makers and hobbyist roboticists building small robots and smart-home projects
- STEM educators and students using Arduino/ESP-class boards in high-school 
  and undergraduate labs
- Small hardware startups and prototyping teams needing quick iteration on 
  behavior logic without hiring full-time embedded engineers
```

**What do they do today to solve it?**

```
- Write C/C++ in Arduino IDE or vendor-specific environments
- Use MicroPython or similar interpreters when possible
- Copy/paste code from online tutorials and forums, then hack until it compiles
```

**Why is the current approach insufficient?**

```
- C/C++ is powerful but unforgiving: memory bugs, timing issues, undefined behavior
- Python-style interpreters require far more flash/RAM and often break real-time guarantees
- No small, deterministic, domain-specific language captures typical "if-this-then-that, 
  timers, and state machines" logic in a way that is both safe and compact for lowest-end boards
```

### D2. Your Solution

**In 2-3 sentences, what is your solution?**

```
Embino is a middle-level domain-specific language (DSL) for embedded behavior, 
designed around events, conditions, timers, and finite-state logic. Human-readable 
rules compile into compact, purpose-built bytecode that runs on a micro-interpreter 
fitting into tens of kilobytes on Arduino/ESP-class devices. The result is simpler, 
safer, and more portable control logic for non-expert developers.
```

**What makes it technically novel? (Not "better" but "different in kind")**

```
- Custom bytecode and interpreter specifically tailored to MCU control flows 
  (events, timers, state machines), not a general-purpose VM
- Strong restrictions and static analysis guarantee bounded resource usage 
  and deterministic timing behavior
- Intermediate "behavior representation" can be targeted from multiple front-ends 
  (text DSL, block-based editor, LLM-generated flows), but always executes via 
  the same small VM on-device
```

**What are the key technical risks?**

| Risk | Why it might fail | How you'll address it |
|------|-------------------|----------------------|
| Bytecode/interpreter footprint too large for smallest boards | Feature creep or naive bytecode design could exceed flash/RAM limits | Tight instruction set design, early size benchmarks, modular features that can be compiled out |
| Timing/scheduling guarantees insufficient for real-world tasks | Poorly designed scheduling model could lead to jitter or missed events | Explicit documented scheduling semantics, limit per-tick instruction counts, static analysis to reject overly complex programs |
| DSL too confusing or abstract for target users | Concepts like FSMs may be unfamiliar to hobbyists | Iterative user testing with real makers/educators, concrete patterns baked into examples, possible layered syntax (simple vs advanced mode) |

### D3. Prior Work / Preliminary Results

**Have you built any prototypes, proofs-of-concept, or demos?**

```
[ ] Yes
[x] No — design explored in diagrams and informal specs but not implemented.
    Phase I is explicitly about producing the first measurable implementation.
```

**Any preliminary data or benchmarks?**

```
None yet — Phase I will produce the first measurable implementation and benchmarks.
```

**Related IP (patents filed, trade secrets, copyrights)?**

```
- No existing IP directly on Embino language or bytecode
- PI has substantial prior IP in depth cameras, medical ML, and molecular modeling 
  (demonstrates track record but does not encumber Embino)
- New IP will be filed under Kernel Keys LLC
```

### D4. Phase I Objectives

**List 3-4 specific objectives with measurable outcomes:**

| # | Objective | Success Metric |
|---|-----------|----------------|
| 1 | Define DSL and safety model | Language reference (~40-page spec) + automated test suite (>100 unit tests) validating parsing and type rules |
| 2 | Build compiler from DSL to bytecode | CLI compiler that successfully compiles ≥20 non-trivial example programs; catches type/logic errors as designed |
| 3 | Implement micro-interpreter for two boards | Interpreter running on ESP32 + Arduino-class AVR with flash footprint <20KB and RAM overhead <4KB |
| 4 | Benchmark and validate usability | Performance/memory benchmarks for all examples; structured feedback from ≥10 external users; ≥5 live demos |

### D5. Phase I Tasks (High-Level)

| Task | Months | Deliverable |
|------|--------|-------------|
| DSL design and documentation | 1–2 | Language + safety spec; initial parser implementation |
| Compiler implementation | 2–4 | End-to-end compiler (DSL → bytecode) with test suite and example programs |
| Micro-interpreter implementation and optimization | 3–6 | Firmware library for ESP32/Arduino with documented API and size benchmarks |
| Benchmarking, user tests, final report | 5–6 | Benchmark report, user feedback summaries, refined Phase II plan |

---

## Section E: Commercialization

### E1. Target Market

**Who is your primary customer?**

```
- Makers and hobbyist roboticists who buy Arduino/ESP boards
- STEM educators (high school, community college, early undergraduate labs)
- Small hardware startups and prototype teams needing quick iteration without 
  hiring full-time embedded engineers
```

**What is the market size?**

| Metric | Your Estimate | Source |
|--------|---------------|--------|
| TAM (Total Addressable Market) | Global embedded dev boards + educational robotics market | **TBD — need specific numbers** |
| SAM (Serviceable Available Market) | Users of Arduino/ESP-class boards in education, maker communities, startups | **TBD** |
| SOM (Serviceable Obtainable Market, Year 1-3) | Early adopters via open-source channels, dev-board bundles, small OEM deals | **TBD** |

**Who are the key competitors?**

| Competitor | What they offer | Your advantage |
|------------|-----------------|----------------|
| Arduino IDE / C++ | Direct C++ programming for Arduino ecosystem | Higher-level, safer language; smaller cognitive load; easier for non-experts |
| MicroPython / CircuitPython | Python interpreter on some boards | Much smaller runtime footprint, deterministic timing, better for lower-end MCUs |
| Visual / flow-based tools (Node-RED, block-based) | Visual composition of logic, heavyweight runtimes | Visual front-ends could target Embino bytecode; execution stays tiny on MCU |

### E2. Customer Conversations

> This is CRITICAL. NSF wants evidence you've talked to real customers.

**List specific companies/people you've talked to about this problem:**

| Company/Person | Their role | What you learned | Interest level (1-5) |
|----------------|------------|------------------|---------------------|
| **TBD** | e.g., robotics club teacher | Pain points around C/C++ debugging | |
| **TBD** | e.g., maker-space leader | Desire for quick iteration | |
| **TBD** | e.g., hardware startup founder | Constraints on board memory | |

> ⚠️ **Need ≥10 concrete entries** — This is the biggest gap in the application.

**Are any of them willing to be pilot customers or provide commitment letters?**

```
TBD — will identify during customer discovery phase
```

### E3. Business Model

**How will you make money?**

```
[x] Sell hardware (dev boards, modules) — with Embino interpreter preloaded
[x] License software/SDK — to OEMs and robotics kit vendors
[x] SaaS subscription (cloud toolchain) — compiler, project templates, educational content
[x] OEM licensing — for companies embedding Embino in their products
```

**Pricing strategy:**

```
- Low-cost or free core SDK and interpreter for hobbyists (drive adoption)
- Margin on hardware boards and robotics kits
- Subscription or license fees from OEMs and educational institutions
```

**Revenue projections (rough):**

| Year | Revenue | Basis for estimate |
|------|---------|-------------------|
| Year 1 | Modest (pilots, early adopters) | Focus on development; early kit sales |
| Year 2 | Revenue ramp | Broader kit and OEM adoption as channels grow |
| Year 3 | Sustainable growth | Deeper OEM integration + recurring SaaS income |

### E4. Go-to-Market

**How will you reach customers?**

```
[x] Direct sales — via kernel-keys.com
[x] Resellers / distributors — Adafruit, SparkFun, etc.
[x] Online marketplace (Adafruit, SparkFun, etc.)
[x] Open-source community + premium features
[x] OEM partnerships — robotics competitions, educational programs, makerspaces
```

**What's your Phase II commercialization plan?** (Required in proposal)

```
- Harden interpreter and tooling; add wireless, networking, more sensors/actuators
- Develop visual editor / block-based front-end targeting Embino bytecode
- Formalize OEM program and educational bundles
- Build small support team to serve early industrial and educational customers
```

### E5. IP Strategy

**What IP do you have or plan to file?**

```
[x] Patents (filed or planned) — provisional patent on DSL semantics, safety guarantees, bytecode architecture
[x] Trade secrets — compiler optimizations and heuristics
[x] Copyrights — compiler/interpreter code base and documentation
[x] Trademarks — "Embino" and possibly "Kernel Keys" sub-brands
```

**Details:**

```
- File provisional patent in Phase I covering DSL semantics, safety guarantees, 
  and bytecode architecture
- Lock down brand/trademark early as name will be exposed to community and OEMs
```

---

## Section F: Broader Impacts

### F1. Societal Benefits

**How does this benefit society beyond commercial value?**

```
- Lowers barrier to embedded systems and robotics, helping more students and 
  self-taught developers gain real hardware skills
- Makes it easier for small organizations (schools, non-profits, community labs) 
  to deploy safe, understandable control logic without deep C/C++ expertise
```

**Education / workforce development angle?**

```
- Embino can be taught in short workshops where C/C++ would be too steep, 
  enabling more learners to complete functional projects and build confidence
- Provides realistic stepping stone from block-based robotics to more serious, 
  hardware-close programming
```

**Underrepresented groups / diversity angle?**

```
- By reducing complexity and tooling friction, Embino enables programs focused 
  on underrepresented groups in STEM to integrate real embedded projects without 
  relying on scarce expert mentors
```

### F2. Safety / Security

**Does your technology have safety implications?**

```
- Embedded control logic, particularly in robotics, has safety implications 
  (motors, actuators)
- The language's deterministic and constrained behavior model can improve safety 
  compared to ad hoc C hacks
```

**Does it involve:**

```
[ ] Human subjects research
[ ] Vertebrate animals
[ ] Hazardous materials
[ ] Export control concerns — unlikely, but will check for crypto/Wi-Fi elements
[ ] Critical infrastructure — no direct applications in Phase I
```

---

## Section G: Budget Inputs

### G1. Labor Rates

| Person | Role | Annual Salary | % Time | Months | Cost |
|--------|------|---------------|--------|--------|------|
| Haim David Silver | PI | $140,000 | 65% | 12 | $91,000 |
| Compiler Engineer | Key Personnel (contractor) | $110,000 | 25% | 10 | $22,917 |
| Firmware Engineer | Key Personnel (contractor) | $95,000 | 10% | 10 | $7,917 |
| **Total Labor** | | | | | **$121,834** |

### G2. Fringe Rate

**What is your fringe benefits rate?**

```
25% (conservative; covers FICA, health, retirement contributions)
Fringe cost: 25% × $121,834 = $30,459
```

### G3. Overhead/Indirect Rate

**Do you have a negotiated indirect rate?**

```
[x] No → Using provisional rate
[ ] Yes

Provisional indirect rate: 30%
Base: Modified Total Direct Costs (Labor + Fringe) = $152,293
Indirect cost: 30% × $152,293 = $45,688
```

### G4. Equipment / Supplies

| Item | Quantity | Unit Cost | Total | Justification |
|------|----------|-----------|-------|---------------|
| MacBook M4 Max 16" (64GB, 1TB) | 1 | $4,499 | $4,499 | Primary development workstation for compiler/DSL work |
| GPU Workstation (PC) | 1 | $2,800 | $2,800 | Host machine for local LLM inference and translation experiments |
| NVIDIA RTX 5090 | 2 | $2,199 | $4,398 | Local LLM inference for translator prototype; avoids cloud dependency |
| ESP32 DevKitC boards | 10 | $12 | $120 | Primary hardware target for micro-interpreter |
| Arduino Uno R4 | 5 | $27 | $135 | Secondary hardware target (AVR-class) |
| Arduino Nano Every | 5 | $15 | $75 | Low-end hardware target testing |
| Raspberry Pi Pico (RP2040) | 5 | $6 | $30 | Third hardware platform testing |
| STM32 Nucleo boards | 3 | $25 | $75 | Industrial-grade MCU testing |
| Sensors kit (IMU, distance, temp, light) | 1 | $150 | $150 | Real-world test scenarios |
| Actuators (servos, motors, relays, LEDs) | 1 | $200 | $200 | Demo applications hardware |
| Logic analyzer / oscilloscope (budget) | 1 | $300 | $300 | Timing verification and debugging |
| Misc cables, breadboards, components | 1 | $200 | $200 | Prototyping supplies |
| **Total Equipment/Supplies** | | | **$12,982** | |

### G5. Travel

| Trip | Purpose | Cost |
|------|---------|------|
| Maker Faire / Embedded World | Customer discovery, market validation | $2,000 |
| Customer site visits (2-3 trips) | In-person user testing, partnership discussions | $1,500 |
| NSF SBIR/I-Corps events | Program requirements, networking | $500 |
| **Total Travel** | | **$4,000** |

### G6. Other Direct Costs

| Item | Cost | Justification |
|------|------|---------------|
| Consultants (see Section C2) | $20,000 | Embedded systems expert + dev-tools/UX specialist |
| Cloud computing (AWS/GCP) | $3,000 | CI/CD pipelines, build testing, documentation hosting |
| Legal/IP - Provisional patent | $3,500 | DSL semantics, bytecode architecture, safety model |
| Legal/IP - Trademark filing | $1,500 | "Embino" and "Kernel Keys" marks |
| TABA (Technical & Business Assistance) | $6,500 | Required; commercialization consulting |
| **Total Other Direct** | **$34,500** |

---

### Budget Summary

| Category | Amount |
|----------|--------|
| **Direct Costs** | |
| Labor (PI + Engineers) | $121,834 |
| Fringe Benefits (25%) | $30,459 |
| Equipment/Supplies | $12,982 |
| Travel | $4,000 |
| Other Direct Costs | $34,500 |
| **Total Direct Costs** | **$203,775** |
| | |
| **Indirect Costs** (30% of labor+fringe) | $45,688 |
| | |
| **I-Corps Training** (required) | $25,000 |
| | |
| **Subtotal** | **$274,463** |
| | |
| **Fee** (7% of subtotal) | $19,212 |
| | |
| **TOTAL REQUEST** | **$293,675** |

*Under the $305,000 cap with ~$11k buffer for adjustments.*

---

### Budget Justification Notes

**Labor:** PI leads DSL design, compiler architecture, and project management (65% time). Compiler engineer implements front-end, type checker, and bytecode generator (25%, months 3-12). Firmware engineer implements micro-interpreter and hardware integration (10%, months 4-12).

**Equipment:** MacBook for primary development; GPU workstation with dual RTX 5090s enables local LLM inference for the translator prototype without cloud API costs or latency. MCU boards cover three hardware tiers (ESP32, Arduino/AVR, RP2040) as specified in objectives.

**Consultants:** Embedded systems expert ($15k) validates scheduling model and timing guarantees. Dev-tools/UX specialist ($5k) ensures DSL is accessible to non-expert users.

**I-Corps:** Required NSF training for commercialization skills; PI will participate.

**TABA:** Third-party commercialization assistance for market analysis and go-to-market refinement.

---

## Section H: Logistics

### H1. Facilities

**Where will the work be performed?**

```
Primary: Home office / small lab space in Poughkeepsie, NY (Kernel Keys LLC)
Cloud resources: Git hosting, CI pipelines, issue tracking, documentation/wiki
```

**Do you have necessary equipment/facilities?**

```
- Existing development machines (laptops/desktops)
- Will purchase range of MCU boards and sensors as listed in budget
- No specialized wet lab, fabrication, or heavy equipment required
```

### H2. Timeline Preferences

**Preferred project duration:**

```
[ ] 6 months
[ ] 9 months
[x] 12 months (typical)
[ ] 18 months (max)
```

**Preferred start date:**

```
As soon as practicable after award (TBD based on award cycle)
```

### H3. Regulatory

**Any regulatory considerations?**

```
[x] None significant in Phase I
[ ] FCC (wireless) — possible if shipping wireless dev boards; Phase I is firmware/tooling focused
[ ] FDA
[ ] Export control
```

---

## Section I: Remaining Items Needed

### ⚠️ Critical Gaps (Must Complete Before Submission)

| Item | Status | Notes |
|------|--------|-------|
| UEI number | ❌ Missing | Register at sam.gov |
| PI official email | ❌ Missing | Company email preferred |
| Salary/fringe/indirect rates | ✅ Complete | $293,675 total budget |
| Customer conversations (≥10) | ❌ Missing | **Most critical gap** — schedule calls |
| Consultant names | ❌ Missing | Need to identify and get commitments |
| Equipment costs | ✅ Complete | $12,982 in supplies |

### Budget Status

| Item | Status |
|------|--------|
| Labor rates | ✅ PI: $140k, Compiler Eng: $110k, Firmware Eng: $95k |
| Fringe rate | ✅ 25% |
| Indirect rate | ✅ 30% provisional |
| Equipment | ✅ MacBook M4 Max, GPU workstation w/ 2× RTX 5090, MCU boards |
| Travel | ✅ $4,000 |
| Consultants | ✅ $20,000 budgeted |
| I-Corps | ✅ $25,000 |
| TABA | ✅ $6,500 |
| **Total** | ✅ **$293,675** (under $305k cap) |

### Items Ready to Draft (Once Gaps Filled)

- [x] Project Summary (1 page)
- [x] Project Description (15 pages)
- [x] Budget Justification
- [x] Data Management Plan
- [ ] Biographical Sketch (needs SciENcv formatting)
- [ ] Current & Pending (needs SciENcv formatting)

---

*Last updated: 2025-11-30*
