# TinyGradLab

TinyGradLab is an educational project to build a scalar automatic-differentiation engine and a small neural-network library **from scratch**.

The implementation will be written independently. We may study public descriptions of algorithms and use other libraries as optional test oracles, but core computation and gradient propagation will not be delegated to PyTorch or copied from another implementation.

## Current status

**P0 — project scaffold.** The package can be installed in editable mode and its test suite can run. No autodiff or neural-network engine has been implemented yet.

## Planned milestones

- **P0 — Scaffold:** package metadata, tests, examples, and development notes.
- **P1 — Scalar autodiff:** scalar values, operation graph, reverse-mode gradients, numerical gradient checks.
- **P2 — Neural-network building blocks:** parameters, modules, linear layers, and MLP.
- **P3 — Training loop:** losses, optimizer, and a small learnable task.
- **P4 — Observability:** computation-graph and training visualizations.
- **P5 — Tensor engine:** multidimensional tensors and batched operations.
- **P6 — Further experiments:** small sequence models and performance experiments.

Each milestone must include runnable code, automated tests, and explicit acceptance criteria before the next milestone begins.

## Requirements

- Python 3.10 or newer
- `pip`
- Git (recommended)

## Setup

### Windows PowerShell

```powershell
py -3 --version
py -3 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
python -m pytest
python examples/scalar_demo.py
```

If PowerShell blocks activation, either allow activation for the current terminal session with your organization's permitted policy, or invoke the environment's Python directly:

```powershell
.\.venv\Scripts\python.exe -m pip install -e ".[dev]"
.\.venv\Scripts\python.exe -m pytest
.\.venv\Scripts\python.exe examples/scalar_demo.py
```

### macOS / Linux

```bash
python3 --version
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
python -m pytest
python examples/scalar_demo.py
```

## Expected P0 output

The test suite should report one passing test. The demo should print the package name, version, and a message that the scalar engine will be implemented in P1.

## Repository layout

```text
tinygradlab/
├── pyproject.toml
├── README.md
├── .gitignore
├── src/
│   └── tinygradlab/
│       └── __init__.py
├── tests/
│   └── test_smoke.py
├── examples/
│   └── scalar_demo.py
└── docs/
    ├── architecture.md
    └── development_log.md
```

## Engineering rules

1. Do not implement multiple milestones at once.
2. Every public behavior needs tests.
3. Validate gradients against hand calculations and finite differences.
4. Keep runtime dependencies at zero unless a milestone justifies adding one.
5. Do not silently use another autodiff engine for core calculations.
6. Record design decisions and known limitations in `docs/development_log.md`.

## License

MIT. See `LICENSE`.

pyproject.toml：项目元数据、安装配置和测试配置。
src/tinygradlab/__init__.py：Python 包入口。
tests/test_smoke.py：验证包可以导入
examples/scalar_demo.py：第一个可运行示例。
docs/architecture.md：项目架构边界。
docs/development_log.md：阶段记录和验收标准。