import pytest

from some_code.some_module import SomeClass


@pytest.fixture
def default_instance() -> SomeClass:
    return SomeClass()


@pytest.fixture
def valued_instance() -> SomeClass:
    return SomeClass(10)
