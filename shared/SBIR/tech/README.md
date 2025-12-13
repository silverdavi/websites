# Technical Documentation

Technical specs, architecture, DSL design, and micro-VM documentation.

## Contents

- `dsl_spec.md` — DSL grammar, semantics, safety constraints
- `bytecode_format.md` — Bytecode specification and encoding
- `micro_vm.md` — Interpreter architecture and execution model
- `hardware_targets.md` — ESP32, Arduino, RP2040 specifications
- `demos.md` — Demo application descriptions

## Key Technical Parameters

| Spec | Target |
|------|--------|
| Interpreter Flash | ≤64 KB |
| Runtime RAM | ≤16 KB |
| Event→Action latency | ≤20 ms |
| Target boards | ESP32, Arduino, RP2040 |

