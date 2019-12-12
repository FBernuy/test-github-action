from some_code.some_module import SomeClass


def test_some_class():
    """Tests SomeClass methods and usage"""
    some_instance = SomeClass()
    assert some_instance._some_att == 0, "Error on default initial value"

    some_instance.set_att(7)
    assert some_instance._some_att == 7, "Error on setter method"

    value = some_instance.get_att()
    assert value == some_instance._some_att, "Error on getter method"

    other_instance = SomeClass(13)
    assert other_instance._some_att == 13, "Error on initial value"
