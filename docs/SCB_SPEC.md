# Sovereign Canon Builder Specification (SCB_SPEC)

**Version:** 1.0 (Draft)

**Status:** Design Frozen

---

# 1. Purpose

The Sovereign Canon Builder (SCB) is a deterministic compiler for Sovereign Canon corpora.

Its purpose is to transform structured human-authored lore into a validated, indexed, reproducible semantic database suitable for retrieval, analysis, export, and future tooling.

SCB is a compiler.

It is **not** an editor, generator, search engine, or AI system.

---

# 2. Design Philosophy

SCB is founded upon the following principles.

## 2.1 Determinism

Given:

* identical input,
* identical compiler version,
* identical configuration,

SCB shall always produce identical output.

No stage of compilation may rely upon randomness, timestamps, machine state, or undefined ordering.

---

## 2.2 Immutability

All semantic objects produced during compilation are immutable.

Once created, objects shall never change.

Mutable state exists only inside the BuildContext.

---

## 2.3 Source Traceability

Every object produced by the compiler shall retain a traceable relationship to its original source.

Every diagnostic shall identify the precise location that caused it.

---

## 2.4 Forward Compilation

Compilation proceeds strictly forward.

Information flows only toward later stages.

Later stages shall never modify earlier stages.

---

## 2.5 Explicit Diagnostics

Compiler problems shall be represented by structured diagnostics.

Silent failures are prohibited.

Unexpected exceptions represent compiler defects.

---

## 2.6 Reproducibility

A successful compilation must be reproducible across machines and operating systems.

---

# 3. Compiler Responsibilities

SCB shall:

* load source documents;
* normalize source text;
* identify lore entries;
* parse headers;
* parse sections;
* construct immutable semantic objects;
* validate structural correctness;
* build searchable indexes;
* collect compilation statistics;
* export structured representations.

SCB shall never modify the original source corpus.

---

# 4. Compiler Pipeline

Compilation consists of the following stages.

Source File

↓

LoaderStage

↓

SourceDocument

↓

SplitterStage

↓

RawEntry

↓

HeaderStage

↓

LoreEntity

↓

SectionStage

↓

Section Objects

↓

IndexerStage

↓

LoreDatabase

↓

Validator

↓

Statistics

↓

Exporters

The pipeline is strictly sequential.

No stage may execute before its predecessor has completed successfully.

---

# 5. Domain Model

The following domain objects constitute the immutable semantic model.

* SourceSpan
* SourceDocument
* RawEntry
* Section
* LoreEntity
* LoreDatabase
* Diagnostic
* Severity
* BuildInfo
* BuildMetrics

These objects form the stable internal API of SCB.

---

# 6. Construction

Domain objects shall not be created directly by parser stages.

Creation is delegated to factories.

Factories are responsible for enforcing object invariants.

---

# 7. Repository

LoreDatabase represents the completed corpus.

It behaves as a read-only repository.

Consumers may:

* retrieve entities by identifier;
* retrieve entities by name;
* retrieve entities by type;
* iterate over entities;
* determine repository size.

Consumers shall never modify repository contents.

---

# 8. Build Context

BuildContext represents mutable compiler state.

It contains:

* configuration;
* diagnostics;
* build metadata;
* compilation metrics;
* current pipeline products.

No mutable compiler state shall exist outside BuildContext.

---

# 9. Diagnostics

Every diagnostic contains:

* unique code;
* severity;
* message;
* source location;
* optional notes;
* optional suggested resolution.

Diagnostic codes are stable across compiler versions.

---

# 10. Grammar

The Sovereign Canon grammar is defined independently of parser implementation.

Parser stages consume grammar definitions rather than hard-coded strings.

Grammar changes shall require modification only within the grammar definition.

---

# 11. Build Metadata

Each successful compilation produces build metadata including:

* compiler version;
* source fingerprint;
* build timestamp;
* platform information;
* compilation statistics.

---

# 12. Statistics

Compilation statistics shall include, at minimum:

* documents;
* entries;
* entities;
* sections;
* diagnostics;
* warnings;
* errors;
* compilation duration.

---

# 13. Public API

SCB exposes a stable public API.

Backward compatibility shall be preserved throughout all 1.x releases whenever practical.

---

# 14. Testing

Every public module shall possess automated tests.

Compiler correctness takes precedence over implementation speed.

---

# 15. Versioning

SCB follows Semantic Versioning.

Major versions may introduce breaking changes.

Minor versions add functionality while preserving compatibility.

Patch versions correct defects without altering public behaviour.

---

# 16. Non-Goals

SCB intentionally does not perform:

* automatic lore generation;
* source modification;
* AI reasoning;
* semantic guessing;
* automatic correction of invalid lore.

Such functionality belongs to external tooling.

---

# 17. Design Freeze

The architecture defined within this specification is considered frozen.

Future implementation shall conform to this specification.

Architectural changes require explicit revision of the specification before implementation.

---

# 18. Guiding Principle

SCB shall remain a deterministic compiler whose behaviour is entirely defined by its specification.

The specification is authoritative.

The implementation exists to satisfy the specification.


# 19. Sovereign Canon Principles

Authoritative Source Principle — The compiler never invents knowledge. Only the source corpus defines canon.

Losslessness Principle — Compilation must never discard information unless explicitly instructed.

Neutrality Principle — SCB records and validates lore without interpreting, judging, or reconciling contradictions beyond defined validation rules.

Transparency Principle — Every output produced by SCB must be traceable back to its originating source.
