#!/usr/bin/env python3

"""Defines the BaseGeometry class."""


class BaseGeometry:
    """Represent the base geometry."""

    def area(self):
        """Calculate the area of the geometry."""
        raise Exception("area() is not implemented")
