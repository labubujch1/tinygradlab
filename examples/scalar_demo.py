"""P0 smoke demo; scalar arithmetic and autodiff arrive in P1."""

from tinygradlab import __version__


def main() -> None:
    print(f"TinyGradLab v{__version__}")
    print("P0 scaffold is ready.")
    print("P1 will implement the scalar Value type and reverse-mode autodiff.")


if __name__ == "__main__":
    main()
