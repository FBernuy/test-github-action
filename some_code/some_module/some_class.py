class SomeClass:
    """A simple class with a simple attribute"""

    def __init__(self, value: int = 0):
        """
        :param value: intitial attribute value, defaults to 0
        :type value: int, optional
        """
        self._some_att = value

    def set_att(self, some_value: int):
        """Sets the attribute value

        :param some_value: new value to set
        :type some_value: int
        """
        self._some_att = some_value

    def get_att(self) -> int:
        """Returns the attribute value

        :return: attribute value
        :rtype: int
        """
        return self._some_att

    def increment_att(self):
        """Increases the attribute value by 1"""
        self._some_att += 1
