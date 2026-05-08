from some_code.some_script import run


def test_run_returns_expected_value() -> None:
    assert run() == 199, "Unexpected return value"


def test_run_returns_int() -> None:
    assert isinstance(run(), int)


def test_run_is_idempotent() -> None:
    assert run() == run()
