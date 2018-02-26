"""
CSC131 - Computation Thinking
Missouri State University, Spring 2018
Lab 5: Geometric Object

File: GeometricObject.py
"""


class GeometricObject(object):
    """
    An abstraction of a Geometric object.
    """

    def __init__(self, color: str = "white", filled: bool = True):
        """
        Initializer method with optional color and filled initial values.
        :param color: Optional parameter to specify the color of this Geometric object
        :param filled: Optional parameter to specify the fill state of this Geometric object.
        """
        self._color = color
        self._filled = filled

    def get_color(self) -> str:
        """
        Color accessor method of this Geometric object.
        :return: The color of this Geometric object is returned.
        """
        return self._color

    def set_color(self, color) -> None:
        """
        Color mutator method of this Geometric object.
        :param color: a color to give this Geometric object
        :return: None
        """
        self._color = color

    def is_filled(self) -> bool:
        """
        Filled state accessor method of this Geometric object.
        :return: True is returned if this Geometric object is filled; False otherwise.
        """
        return self._filled

    def set_filled(self, filled) -> None:
        """
        Filled state mutator method of this Geometric object.
        :param filled: The filled state to assign to this Geometric object.
        :return: None
        """
        self._filled = filled

    def __str__(self) -> str:
        """
        Generate a string representation of this Geometric object.
        :return: A string representation of this Geometric object is returned.
        """
        return "color: " + self._color + " and filled: " + str(self._filled)
