from .some_module import SomeClass


def run():
    """Create a SomeClass instance, set its value to 5 and
    increments it 4 times, the returns the object value

    :return: SomeClass attribute value
    :rtype: int
    """
    print('Creating SomeClass member')
    some_member = SomeClass()
    print('Setieng value to 5')
    some_member.set_att(5)
    print('increasing value in 4')
    for _ in range(4):
        some_member.increment_att()
    print('returning value')
    return some_member.get_att()


if __name__ == "__main__":
    run()
