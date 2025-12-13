# Embino — Project Overview

*A middle-level programming stack for microcontrollers*

---

## One-Liner

A toolchain that converts human-readable control rules into compact bytecode and runs them on ESP/Arduino-class boards via a tiny interpreter, making embedded prototyping faster and safer for non-experts.

---

## The Problem

Microcontrollers power sensors, appliances, robots, locks, lights, motors, drones, meters—billions of embedded nodes. Programming them still looks like 1985:

- Hand-written C/C++
- Low-level memory management
- Device-specific registers
- Manual GPIO configuration
- Timing quirks and interrupts
- Painful debugging
- Zero abstraction for intent

Python/MicroPython adds overhead and unpredictability. LLMs cannot run on MCUs and introduce nondeterminism.

**Gap:** No middle-level abstraction between natural language and C code that is safe, deterministic, compact, and runnable on $1 microcontrollers.

---

## The Solution

Embino provides a three-component stack:

### 1. Embino DSL

A tight, rule-oriented language expressing:
- Events and conditions
- Thresholds and timers
- Actions and state

Expressive enough for real behavior. Constrained enough to compile into deterministic bytecode fitting in kilobytes.

**Example:**
```
When motion is detected after 22:00
  and brightness < 30%
then turn on lamp for 120 seconds.
```

### 2. Translator

A controlled offline model (not running on device) that:
- Transforms short human instructions into Embino DSL
- Rejects ambiguous instructions
- Ensures unambiguous, verifiable logic

### 3. Micro-VM

A tiny runtime in C/C++ for:
- ESP32
- Arduino/AVR
- RP2040 (Pico)

Guarantees:
- Deterministic execution
- Bounded RAM usage (<16 KB)
- Small Flash footprint (<64 KB)
- Predictable timing (<20 ms latency)

**Pipeline:** Human instruction → DSL → verified bytecode → deterministic execution on cheap hardware.

---

## Technical Specifications

| Parameter | Target |
|-----------|--------|
| Interpreter Flash | ≤64 KB |
| Runtime RAM | ≤16 KB |
| Event→Action latency | ≤20 ms |
| Translation accuracy | ≥80% correct first try |

### Target Hardware

- ESP32 (primary)
- Arduino Uno/Nano (ATmega328P)
- RP2040 (Raspberry Pi Pico)

### Demo Applications

1. **Smart light controller** — motion + light sensor
2. **Environmental monitor** — thresholds, alarms, logging
3. **Robot behavior** — obstacle avoidance + timeouts

---

## Abstraction Ladder

| Layer | Example | Abstraction | Pros | Cons |
|-------|---------|-------------|------|------|
| Machine code | `1011 0001...` | None | Maximum control | Impossible to reason about |
| Assembly | `MOV R0, #1` | Very low | Deterministic | Verbose, hardware-bound |
| C/C++ | `for (int i=0; i<n; i++)` | Low/medium | Fast, portable | Undefined behavior, subtle bugs |
| Python | `return sum(a)` | High | Rapid development | Heavy runtime, unsuitable for MCUs |
| **Embino DSL** | `When motion... then turn on lamp` | Very high (structured) | Safe, deterministic, compact | Domain-specific |
| General LLM | "Write Arduino code to..." | Very high (free-form) | Flexible | Too large, nondeterministic |

Embino sits between Python and LLMs: structured like programming, expressive like English, safe like a finite-state machine.

---

## Hardware Roadmap

### Stage 1 — Add-On Module (12-24 months)

Small external board attaching via UART/I²C/SPI:
- Houses Embino runtime
- Bridges old workflows with new system
- Zero hardware changes to existing boards

**Revenue:** Dev boards, makers, robotics startups, schools

### Stage 2 — System-on-PCB (24-36 months)

Embino integrated on the same board as MCU:
- Integrated interpreter
- Standard pinout (Arduino/Pico style)
- Ready for industrial prototyping

**Revenue:** Volume dev-board sales, robotics kits, automation integrators

### Stage 3 — On-Board Chip (36+ months)

Custom MCU with Embino baked in:
- ROM-resident interpreter
- Bootloader integrated with toolchain
- Custom SoB variants for OEMs

**Revenue:** Licensing to appliance manufacturers, industrial OEMs

---

## Market

### Microcontroller Market

- **Annual shipments:** 30-40 billion units
- **Applications:** Consumer electronics, automotive, industrial, IoT, appliances, robotics, medical devices

### Developer Board Market

- **Volume:** Tens of millions/year
- **Players:** Arduino, ESP32, Pico, Adafruit, SparkFun
- **Use:** Education, prototyping, consumer robotics

### Target Segments

| Timeline | Market |
|----------|--------|
| Short-term | Dev boards, makers, education |
| Mid-term | Robotics startups, automation integrators, small OEMs |
| Long-term | Appliance manufacturers, industrial controls, automotive subsystems |

Even 0.1% of MCU deployments = 30-40 million units/year addressable.

---

## SBIR Phase I Plan

**Goal:** Prove technical feasibility and commercial interest ($300k, 12 months)

### Objectives

1. **DSL + Safety Model** — Define language, grammar, static semantics, safety constraints
2. **LLM Translator** — Build pipeline with ambiguity detection and validation
3. **Micro-VM** — Implement interpreter on ESP32/Arduino with demos
4. **User Validation** — Study with 8-10 participants + partner letters

### Timeline

| Period | Focus |
|--------|-------|
| Months 1-3 | DSL design, reference interpreter, test harness |
| Months 4-6 | Translator prototype, ESP32 port, partner outreach |
| Months 7-9 | Micro-VM optimization, demos, initial user tests |
| Months 10-12 | Formal user study, refinement, Phase II prep |

### Deliverables

- DSL spec document
- Reference interpreter (Python)
- LLM-assisted translator prototype
- Micro-VM firmware (ESP32, Arduino)
- 3 demo applications with measured metrics
- User study report
- 2+ letters of support

### Success Criteria

- DSL expresses 3 real scenarios
- ≥80% translation accuracy (remainder flagged, not wrong)
- All demos within resource limits
- Users complete tasks faster with fewer errors
- At least one company commits to pilot/evaluate

---

## Innovation

### Technical

- New abstraction level (not a feature or library)
- Formal safety model with bounded resources
- Deterministic execution guarantees
- LLM-assisted translation with validation (rejects ambiguity)

### Commercial

- First middle-level stack specifically for MCU behavior
- Clear hardware roadmap (add-on → integrated → custom chip)
- Massive underserved market

---

## Risks and Mitigations

| Risk | Mitigation |
|------|------------|
| DSL cannot capture enough behavior | Iterative design with real scenarios; formal expressiveness analysis |
| Translation too unreliable | Strict validation; reject ambiguous inputs; user clarification loop |
| Runtime exceeds resource limits | Conservative targets; optimization phase; hardware tier selection |
| Market adoption slow | Early partner engagement; maker community focus; open-source components |

---

## Team Structure

| Role | Focus |
|------|-------|
| PI / Founder | DSL design, architecture, embedded integration |
| Embedded engineer | Firmware, micro-VM, GPIO drivers |
| PL/compiler consultant | DSL spec, code review |
| TABA consultant | Commercialization |

---

## Website Content (for embino.com)

### Hero Section

**Tagline:** Tiny intelligence for tiny devices

**Subhead:** A middle-level programming stack that brings structured, safe, deterministic logic to ESP32, Arduino, and any $1 microcontroller.

### Key Messages

1. **Not LLMs on MCUs** — LLMs are too big and nondeterministic. Embino compiles to compact, deterministic bytecode.

2. **Not another Python** — No runtime overhead, no garbage collection, no surprises. Predictable timing guaranteed.

3. **Not a library** — A new abstraction layer. Express intent, not implementation.

### Demo Showcase

- Motion-controlled lighting
- Sensor threshold alarms
- Simple robot behaviors

### Specs (datasheet style)

- Flash: <64 KB
- RAM: <16 KB
- Latency: <20 ms
- Targets: ESP32, Arduino, RP2040

---

## Links

- **Project site:** embino.com
- **Company:** kernel-keys.com
- **Personal:** dhsilver.me

---

*Last updated: 2025-11-30*

