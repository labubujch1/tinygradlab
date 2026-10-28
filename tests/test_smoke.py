"""P0 smoke tests: package metadata and importability."""

import tinygradlab


def test_package_imports_and_has_version() -> None:
    assert tinygradlab.__version__ == "0.1.0"
