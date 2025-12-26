# Kernel Keys — Intellectual Property Portfolio

*Embino / Hybrid Compute Optimization*

---

## Portfolio Overview

| IP Asset | Type | Status | Core Innovation |
|----------|------|--------|-----------------|
| **GC-SLM for Embedded Systems** | Patent | Filed (Provisional) | Grammar-constrained code generation + S-LoRA + micro-interpreter |
| **Hybrid Compute Optimization** | Patent | Draft | LLM-driven closed-loop optimization for under-specified architectures |
| **Constrained Code Generation** | Paper | Submitted | Theoretical foundations of GC-SLM |
| **Distributed Neuron Optimization** | Paper | Outline | Robotics application with ANN-nodes |

---

## Directory Structure

```
IP/
├── patents/
│   ├── embino_gcslm/           # Original patent: GC-SLM + DSL + micro-interpreter
│   │   ├── SPECIFICATION.pdf
│   │   ├── CLAIMS.md
│   │   ├── DRAWINGS.pdf
│   │   └── ...
│   │
│   └── hybrid_compute_optimization/   # NEW: Under-specified compute + robotics
│       ├── draft.md            # Specification draft
│       ├── CLAIMS.md           # Claim set
│       └── ...
│
└── papers/
    ├── gcslm_constrained_generation/  # Original paper: GC-SLM theory
    │   ├── main.tex
    │   └── ...
    │
    └── distributed_neuron_optimization/  # NEW: Robotics neurons paper
        ├── outline.md
        └── ...
```

---

## IP Strategy

### Core Claims (Broad)
1. **Hybrid compute co-optimization** — LLM generates candidates for deterministic + under-specified elements
2. **Search-space shaping** — LLM modifies IR/grammar/operators based on telemetry
3. **Hardware-in-the-loop calibration** — Physical telemetry drives optimization

### Dependent Branches (Narrower, Harder to Design Around)
- **Embino DSL → bytecode → micro-interpreter** (deterministic MCU deployment)
- **Distributed ANN-nodes in robotic systems** (tactile skin, reflexes)
- **Flexible substrate integration** (nerve bus, conformal sensors)
- **Safety envelope with rollback** (bounded-latency, rate limits)

### Claim Architecture

```
Independent (Broad)                    Dependent (Deep)
────────────────────                   ────────────────
Hybrid compute co-optimization    ──┬─ Grammar-constrained generation
                                    ├─ S-LoRA fine-tuning
                                    ├─ Deterministic micro-interpreter
                                    └─ Bounded-resource deployment

Search-space shaping (LLM)       ──┬─ IR/grammar mutation
                                   ├─ Constraint-aware expansion
                                   └─ Multi-objective optimization

Hardware-in-the-loop             ──┬─ Distributed ANN-nodes
                                   ├─ Robotic skin/nerves
                                   ├─ Per-node calibration
                                   └─ Embodied evaluation metrics
```

---

## Relationship Between Patents

```
┌─────────────────────────────────────────────────────────────────────┐
│                    HYBRID COMPUTE OPTIMIZATION                       │
│  (LLM-driven closed-loop for under-specified + deterministic)       │
│                                                                      │
│  ┌──────────────────────┐       ┌───────────────────────────────┐  │
│  │  EMBINO GC-SLM       │       │  DISTRIBUTED NEURON NODES     │  │
│  │  (Deterministic DSL  │       │  (Robotic skin, reflexes,     │  │
│  │   + micro-VM)        │       │   event-based sensing)        │  │
│  └──────────────────────┘       └───────────────────────────────┘  │
│              │                              │                        │
│              └──────────────┬───────────────┘                        │
│                             │                                        │
│              DEPLOYABLE DETERMINISTIC ARTIFACTS                      │
│              (Bytecode, microcode, config bits)                      │
└─────────────────────────────────────────────────────────────────────┘
```

---

## Filing Strategy

| Phase | Action | Timeline |
|-------|--------|----------|
| 1 | File provisional for hybrid compute optimization | Q1 2025 |
| 2 | Continue embino_gcslm to non-provisional | Q2 2025 |
| 3 | PCT filing for international coverage | Q3 2025 |
| 4 | Continuation applications as market develops | Ongoing |

---

*Not legal advice. Consult patent counsel before filing.*

