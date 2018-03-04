from csc131.Circle import Circle
from math import atan
import unittest


class CircleUnitTest(unittest.TestCase):
    PI = 4 * atan(1)

    def test_init_default_circle(self):
        circle = Circle()
        actual_properties = {"color": circle._color, "filled": circle._filled, "radius": circle._radius}
        expected_properties = {"color": "white", "filled": True, "radius": 1.0}
        self.assertDictEqual(actual_properties, expected_properties)

    def test_init_parameterized_circle(self):
        radius = 5.0
        color = "black"
        filled = False
        circle = Circle(radius, color, filled)
        actual_properties = {"color": circle._color, "filled": circle._filled, "radius": circle._radius}
        expected_properties = {"color": color, "filled": filled, "radius": radius}
        self.assertDictEqual(actual_properties, expected_properties)

    def test_get_area_default_circle(self):
        circle = Circle()
        radius = 1.0
        actual = circle.get_area()
        expected = CircleUnitTest.PI * radius * radius
        self.assertEqual(expected, actual)

    def test_get_perimeter_default_circle(self):
        circle = Circle()
        radius = 1.0
        actual = circle.get_perimeter()
        expected  = 2 * CircleUnitTest.PI * radius
        self.assertEqual(expected, actual)

    def test_get_area_parameterized_circle(self):
        radius = 1.0
        circle = Circle(radius)
        actual = circle.get_area()
        expected = CircleUnitTest.PI * radius * radius
        self.assertEqual(expected, actual)

    def test_get_perimeter_parameterized_circle(self):
        radius = 2.0
        circle = Circle(radius)
        actual = circle.get_perimeter()
        expected  = 2 * CircleUnitTest.PI * radius
        self.assertEqual(expected, actual)

    def test_str_default_circle(self):
        circle = Circle()
        actual = str(circle)
        expected = "Circle: radius = {} color: white and filled: True".format(1.0)
        self.assertEqual(expected, actual)

    def test_str_parameterized_circle(self):
        test_radius = 2
        test_color = "red"
        test_filled = False
        circle = Circle(radius=test_radius, color=test_color, filled=test_filled)
        actual = str(circle)
        expected = "Circle: radius = {} color: {} and filled: {}".format(test_radius, test_color, test_filled)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()

