"""
CSC131 - Computation Thinking
Missouri State University, Spring 2018
Lab 5: Geometric Object

File: Triangle.py
Author: Alyssa Slayton <ajs41@missouristate.edu>
"""
from csc131.GeometricObject import GeometricObject
from math import sqrt

# TODO: Replace this TODO with the Triangle definition prescribed in the README.
class Triangle(GeometricObject):

    def __init__(self, side1: float = 1.0, side2: float = 1.0, side3: float = 1.0, color: str = "white", filled: bool=True):
        super().__init__(color,filled)
        self._side1 = side1
        self._side2 = side2
        self._side3 = side3

    def get_area(self) -> float:
        s = (self._side1 + self._side2 + self._side3) / 2
        return sqrt(s * (s - self._side1) * (s - self._side2) * (s - self._side3))