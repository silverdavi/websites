# Market Documentation

*Evidence and analysis for commercialization section*

---

## Market Size

### Total Addressable Market (TAM)

| Metric | Value | Source |
|--------|-------|--------|
| MCU annual shipments | 30-40 billion units | IC Insights, Yole |
| MCU market value | ~$28B (2024) | Mordor Intelligence |
| Embedded software tools market | ~$12B | MarketsandMarkets |

### Serviceable Available Market (SAM)

| Segment | Value | Notes |
|---------|-------|-------|
| Arduino ecosystem | ~30M boards/year | Arduino + clones |
| ESP32 market | ~100M+ units | Espressif shipments |
| Educational robotics | ~$3B | Growing 15%/year |
| Maker/hobbyist tools | ~$1B | Dev boards, kits |

### Serviceable Obtainable Market (SOM)

| Year | Target | Basis |
|------|--------|-------|
| Year 1 | $50k-100k | Early adopters, dev licensing |
| Year 2 | $250k-500k | SDK licenses, education |
| Year 3 | $1M+ | OEM pilots, volume |

---

## Customer Segments

### Segment 1: Makers / Hobbyists

**Profile:**
- Arduino, ESP32 users
- Building home automation, robots, gadgets
- Frustrated with C/C++ complexity
- Active on Reddit, Discord, YouTube

**Pain Points:**
- Steep learning curve
- Debugging is painful
- Timing issues crash projects
- Want to describe behavior, not write code

**Channels:**
- Adafruit, SparkFun
- Arduino forums
- r/arduino, r/esp32
- Hackster.io

### Segment 2: Educational Institutions

**Profile:**
- K-12 STEM programs
- University embedded systems courses
- Robotics clubs

**Pain Points:**
- C/C++ is a barrier to teaching concepts
- Students get stuck on syntax, not logic
- Want to focus on behavior and design

**Channels:**
- Educational resellers
- Conference presentations
- Free/open-source tier

### Segment 3: Robotics Startups

**Profile:**
- Building prototypes on ESP32/STM32
- Small teams (2-10 engineers)
- Moving fast, need reliability

**Pain Points:**
- Embedded bugs delay launches
- Hard to hire embedded engineers
- Want predictable behavior

**Channels:**
- YC/accelerator networks
- Robotics conferences
- Direct outreach

### Segment 4: OEMs / Industrial

**Profile:**
- Appliance manufacturers
- Industrial automation
- High-volume products

**Pain Points:**
- Firmware bugs are expensive
- Long certification cycles
- Need deterministic behavior

**Channels:**
- Trade shows
- OEM partnerships
- System integrators

---

## Competitors

| Competitor | What They Offer | Embino Advantage |
|------------|-----------------|------------------|
| Arduino IDE | C/C++ programming | Too low-level, no behavior abstraction |
| MicroPython | Python on MCU | Runtime overhead, unpredictable GC |
| PlatformIO | Better toolchain for C | Still C, no abstraction |
| Node-RED | Visual flow programming | Server-side, not for MCUs |
| BlocklyDuino | Block-based coding | Still compiles to C, limited expressiveness |
| ChatGPT/Copilot | Code generation | Nondeterministic, can't verify output |

**Key Differentiation:**
- New abstraction layer (not just better tools)
- Formal safety guarantees (bounded resources)
- Deterministic execution (predictable timing)
- LLM bridge with validation (best of both worlds)

---

## Customer Conversations

> **Critical:** Document all conversations here for proposal evidence.

| Date | Company/Person | Their Role | Key Insights | Interest (1-5) | Follow-up? |
|------|----------------|------------|--------------|----------------|------------|
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |

### Questions to Ask in Customer Calls

1. What's your current workflow for programming microcontrollers?
2. What's the most frustrating part?
3. How much time do you spend on debugging vs. building features?
4. Have you tried alternatives (MicroPython, visual tools)?
5. If you could describe behavior in plain English and have it "just work," what would that be worth?
6. Would you try a new tool if it was open-source and worked with your existing boards?
7. Would you pay for a commercial version with support?

### Target Companies to Contact

**Dev Board Vendors:**
- Adafruit
- SparkFun
- Seeed Studio
- Arduino (direct)

**Robotics Startups:**
- [Research YC robotics companies]
- [Search AngelList/Crunchbase]

**Educational:**
- Local universities (CS/EE departments)
- FIRST Robotics suppliers
- Code.org partners

**Automation Integrators:**
- Regional industrial automation firms
- Smart home installers

---

## Letters of Support

> **Note:** NSF does NOT accept general letters of support. Only letters of commitment from consultants/subawardees.

However, for your own records and Phase II prep:

### Potential Support Contacts

| Company | Contact | Status | Notes |
|---------|---------|--------|-------|
| | | ☐ Not contacted | |
| | | ☐ Contacted | |
| | | ☐ Interested | |
| | | ☐ Willing to pilot | |

### Letter Template (for your records, NOT for NSF submission)

```
To Whom It May Concern,

[Company] is interested in [Embino project] because [specific pain point].

We would be interested in [evaluating/piloting] the system if it demonstrates 
[specific capability].

[Optional: We would consider licensing/purchasing if ...]

Sincerely,
[Name, Title, Company]
```

---

## Revenue Model

### Phase 1: Open Core (Years 1-2)

| Offering | Price | Target |
|----------|-------|--------|
| Open-source DSL + reference interpreter | Free | Community building |
| CLI toolchain | Free | Developer adoption |
| Pro SDK (IDE integration, debugging) | $99-199/year | Professional devs |
| Team license | $499-999/year | Startups |

### Phase 2: Hardware Integration (Years 2-3)

| Offering | Price | Target |
|----------|-------|--------|
| Add-on module (retrofit board) | $29-49 | Makers |
| Integrated dev board | $49-79 | Education, prototyping |
| Volume licensing | Negotiated | Distributors |

### Phase 3: OEM Licensing (Years 3+)

| Offering | Price | Target |
|----------|-------|--------|
| Runtime licensing (per unit) | $0.10-0.50 | High-volume OEMs |
| Custom chip integration | Negotiated | Strategic partners |
| Support/consulting | $150-250/hr | Enterprise |

---

*Last updated: 2025-11-30*
