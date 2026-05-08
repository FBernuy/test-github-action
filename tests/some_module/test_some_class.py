from some_code.some_module import SomeClass


def test_default_initial_value(default_instance: SomeClass) -> None:
    assert default_instance.att == 0


def test_custom_initial_value() -> None:
    instance = SomeClass(13)
    assert instance.att == 13


def test_property_setter(default_instance: SomeClass) -> None:
    default_instance.att = 7
    assert default_instance.att == 7


def test_property_setter_overwrites(default_instance: SomeClass) -> None:
    default_instance.att = 7
    default_instance.att = 99
    assert default_instance.att == 99


def test_increment(default_instance: SomeClass) -> None:
    default_instance.att = 5
    default_instance.increment_att()
    assert default_instance.att == 6


def test_multiple_increments(default_instance: SomeClass) -> None:
    for _ in range(4):
        default_instance.increment_att()
    assert default_instance.att == 4


def test_negative_initial_value() -> None:
    instance = SomeClass(-5)
    assert instance.att == -5


def test_increment_from_negative() -> None:
    instance = SomeClass(-1)
    instance.increment_att()
    assert instance.att == 0


def test_instances_are_independent() -> None:
    a = SomeClass(1)
    b = SomeClass(100)
    a.increment_att()
    assert a.att == 2
    assert b.att == 100


def test_fixture_valued_instance(valued_instance: SomeClass) -> None:
    assert valued_instance.att == 10


def test_set_then_increment(valued_instance: SomeClass) -> None:
    valued_instance.att = 0
    valued_instance.increment_att()
    assert valued_instance.att == 1
