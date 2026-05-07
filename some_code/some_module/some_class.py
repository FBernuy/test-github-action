class SomeClass:
    """A simple class with a simple attribute."""

    def __init__(self, value: int = 0) -> None:
        self._att: int = value

    @property
    def att(self) -> int:
        return self._att

    @att.setter
    def att(self, value: int) -> None:
        self._att = value

    def increment_att(self) -> None:
        """Increases the attribute value by 1."""
        self._att += 1
