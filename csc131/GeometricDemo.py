"""
CSC131 - Computation Thinking
Missouri State University, Spring 2018
Lab 5: Geometric Object

File: GeometricDemo.py
Author: Jim Daehn <jdaehn@missouristate.edu>
"""
from csc131.Circle import Circle
from csc131.Triangle import Triangle


def main():
    # Testing Circle class
    c = Circle(5, "blue", False)
    print(c)
    print()

    print("Entering input values for a circle")
    r = float(input('Enter value for radius: '))

    c1 = Circle(r)

    print(c1)
    print("c1.get_area()      = {:.2f}".format(c1.get_area()))
    print("c1.get_perimeter() = {:.2f}".format(c1.get_perimeter()))
    print("c1.get_color()     = {}".format(c1.get_color()))
    print("c1.is_filled()     = {}".format(c1.is_filled()))

    # Testing Triangle class
    print("\nEntering input values for a triangle")
    s1 = float(input('Enter value for side1: '))
    s2 = float(input('Enter value for side2: '))
    s3 = float(input('Enter value for side3: '))
    color = input('Enter color of the triangle: ')
    filled = input('Is the triangle filled (1/0)? ')
    filled = (filled == "1")
    t1 = Triangle(s1, s2, s3, color, filled)

    print(t1)
    print("t1.get_area()      = {:.2f}".format(t1.get_area()))
    print("t1.get_perimeter() = {:.2f}".format(t1.get_perimeter()))
    print("t1.get_color()     = {}".format(t1.get_color()))
    print("t1.is_filled()     = {}".format(t1.is_filled()))


if __name__ == '__main__':
    main()
