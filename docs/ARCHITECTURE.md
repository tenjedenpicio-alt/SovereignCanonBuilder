# SCB Architecture

## Purpose

This document describes the internal architecture of Sovereign Canon Builder.

The specification defines *what* SCB must do.

This document explains *how* the implementation is organized.

---

# High-Level Architecture

```
Source File

↓

Compiler

↓

Pipeline

↓

Immutable Domain

↓

Repository

↓

Exporters
```

---

# Major Components

## compiler/

Owns the compilation process.

Contains:

* Pipeline
* Pipeline stages
* BuildContext

---

## domain/

Contains immutable semantic objects.

Nothing in this package performs parsing.

Objects are created only by factories.

---

## factories/

Responsible for constructing domain objects.

All validation of construction invariants occurs here.

---

## validation/

Contains semantic validation rules.

Validation never modifies domain objects.

---

## statistics/

Collects build metrics.

---

## exporters/

Converts compiled data into external formats.

---

## common/

General utilities shared across the project.

---

# Information Flow

Compilation always proceeds forward.

```
SourceDocument

↓

RawEntry

↓

LoreEntity

↓

LoreDatabase
```

Earlier stages are never modified by later stages.

---

# Design Principles

* Immutable domain model
* Deterministic compilation
* Explicit diagnostics
* Source traceability
* Read-only repository
* Factory-based construction
* No hidden global state
* Small composable compiler stages
