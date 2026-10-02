#!/usr/bin/env python3

"""Defines the BaseGeometry class."""


class BaseGeometry:
    """Represent the base geometry."""

    def area(self):
        """Calculate the area of the geometry."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate that value is an integer greater than or equal to 0."""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
