#!/usr/bin/python3
"""BaseGeometry class module"""


class BaseGeometry:
    """Geomerty utility class"""

    def area(self):
        """Represent area
        Raises:
            Exception: [area() is not implemented]
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates value
        Arguments:
            name {str} -- name of an instance
            value {int} -- type of instance
        Raises:
            TypeError: [must be an integer]
            ValueError: [must be greater than 0]
        """
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))

        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))
