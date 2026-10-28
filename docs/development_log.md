# Development Log

## P0 — project scaffold

### Scope

- Add Python package metadata and source layout.
- Add a package import/version smoke test.
- Add a runnable demo.
- Document setup, milestones, and engineering rules.

### Decisions

- Package name: `tinygradlab`.
- Python requirement: `>=3.10`.
- Build backend: setuptools.
- Runtime dependencies: none.
- Test framework: pytest (development extra only).

### Acceptance criteria

- [ ] `python -m pip install -e ".[dev]"` succeeds in a supported Python environment.
- [ ] `python -m pytest` passes.
- [ ] `python examples/scalar_demo.py` prints the expected P0 message.
- [ ] No autodiff or neural-network logic has been implemented in P0.

### Known limitations

This scaffold does not calculate gradients or train models. Those belong to P1 and later.
