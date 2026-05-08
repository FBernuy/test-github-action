from .some_module import SomeClass


def run() -> int:
    """Create a SomeClass instance, set its value to 5, increment it 4 times,
    then return the final value (expected: 9).
    """
    print("Creating SomeClass instance")
    some_member = SomeClass()
    print("Setting value to 5")
    some_member.att = 5
    print("Incrementing value 4 times")
    for _ in range(4):
        some_member.increment_att()
    print("Returning value")
    return some_member.att


if __name__ == "__main__":
    run()
