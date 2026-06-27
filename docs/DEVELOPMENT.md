# Development Guide

## Requirements

* Python 3.12+
* Git
* Virtual environment

---

# Installation

Create a virtual environment.

Install development dependencies.

Run the test suite.

---

# Code Quality

Before every commit:

* Ruff passes.
* MyPy passes.
* Pytest passes.

---

# Development Rules

* Every public object requires tests.
* Every public API requires documentation.
* No print() statements inside compiler code.
* Domain objects are immutable.
* Parser stages never construct domain objects directly.
* BuildContext is the only mutable compiler object.

---

# Git Workflow

Small commits.

One logical change per commit.

Main branch always builds.

---

# Pull Requests

Every pull request should:

* pass CI;
* include tests;
* preserve deterministic behaviour.

---

# Philosophy

SCB is developed as a compiler.

Correctness is more important than speed.

Readability is more important than cleverness.

Deterministic behaviour is more important than convenience.
