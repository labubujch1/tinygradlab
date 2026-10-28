# Architecture

## Current state: P0

P0 only establishes the Python package and test workflow. It intentionally contains no automatic-differentiation implementation.

## Intended dependency direction

```text
examples / user code
        |
        v
neural-network API (P2+)
        |
        v
losses and optimizers (P3+)
        |
        v
scalar autodiff engine (P1)
```

The exact module boundaries may be adjusted when a milestone exposes a concrete need. Avoid speculative abstractions before they are required by working code.

## Design constraints

- Core math and gradient propagation are implemented in this repository.
- Runtime dependencies remain empty in P0.
- `pytest` is a development-only dependency.
- Correctness tests precede optimization.
