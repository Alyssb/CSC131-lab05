"""
CSC131 - Computation Thinking
Missouri State University, Spring 2018
Lab 5: Geometric Object

File: Circle.py
Author: Alyssa Slayton <ajs41@missouristate.edu>
"""
from csc131 import GeometricObject
from math import pi

# TODO: Replace this TODO with the Circle definition prescribed in the README.
class Circle(GeometricObject):

    def __init__(self, radius: float = 1.0, color: str = "white", filled: bool = True):
        super().__init__(color,filled)
        self._radius = radius

    def get_area(radius: float) -> float:
        return pi*(radius**2)

    def get_perimeter(radius: float) -> float:
        return pi*2*radius
