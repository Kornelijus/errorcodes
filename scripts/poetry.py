"""Scripts to be used with `poetry run`."""


def test() -> None:
    from pytest import main
    from sys import exit

    pytest_args = ["-v", "tests"]
    exit(main(pytest_args))


def check() -> None:
    from subprocess import run

    ruff_args = ["ruff", "check", "."]
    run(ruff_args)


def format() -> None:
    from subprocess import run

    ruff_args = ["ruff", "format", "."]
    run(ruff_args)
