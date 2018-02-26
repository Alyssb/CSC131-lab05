from csc131.Triangle import Triangle
from math import sqrt
import unittest


class MyTestCase(unittest.TestCase):
    
    def test_init_default_triangle(self):
        triangle = Triangle()
        actual_properties = {"color": triangle._color, "filled": triangle._filled, "side1": triangle._side1,
                             "side2": triangle._side2, "side3": triangle._side3}
        expected_properties = {"color": "white", "filled": True, "side1": 1.0, "side2": 1.0, "side3": 1.0}
        self.assertDictEqual(actual_properties, expected_properties)

    def test_init_parameterized_triangle(self):
        test_side1 = 2
        test_side2 = 4
        test_side3 = 6
        test_color = "black"
        test_filled = False
        triangle = Triangle(side1=test_side1, side2=test_side2, side3=test_side3, color=test_color, filled=test_filled)
        actual_properties = {"color": triangle._color, "filled": triangle._filled, "side1": triangle._side1,
                             "side2": triangle._side2, "side3": triangle._side3}
        expected_properties = {"color": test_color, "filled": test_filled, "side1": test_side1, "side2": test_side2,
                               "side3": test_side3}
        self.assertDictEqual(actual_properties, expected_properties)

    def test_get_area_default_triangle(self):
        test_side1, test_side2, test_side3 = 1.0, 1.0, 1.0
        triangle = Triangle()
        actual = triangle.get_area()
        s = (test_side1 + test_side2 + test_side3) / 2
        expected = sqrt(s * (s - test_side1) * (s - test_side2) * (s - test_side3))
        self.assertEqual(expected, actual)

    def test_get_perimeter_default_triangle(self):
        triangle = Triangle()
        actual = triangle.get_perimeter()
        expected = 3
        self.assertEqual(expected, actual)

    def test_get_area_parameterized_triangle(self):
        test_side1 = 2
        test_side2 = 4
        test_side3 = 6
        test_color = "black"
        test_filled = False
        triangle = Triangle(side1=test_side1, side2=test_side2, side3=test_side3, color=test_color, filled=test_filled)
        actual = triangle.get_area()
        s = (test_side1 + test_side2 + test_side3) / 2
        expected = sqrt(s * (s - test_side1) * (s - test_side2) * (s - test_side3))
        self.assertEqual(expected, actual)

    def test_get_perimeter_parameterized_triangle(self):
        test_side1 = 2
        test_side2 = 4
        test_side3 = 6
        test_color = "black"
        test_filled = False
        triangle = Triangle(side1=test_side1, side2=test_side2, side3=test_side3, color=test_color, filled=test_filled)
        actual = triangle.get_perimeter()
        expected = test_side1 + test_side2 + test_side3
        self.assertEqual(expected, actual)

    def test_str_default_triangle(self):
        triangle = Triangle()
        actual = str(triangle)
        expected = "Triangle: side1 = {} side2 = {} side3 = {} color: white and filled: True".format(1.0, 1.0, 1.0)
        self.assertEqual(expected, actual)

    def test_str_parameterized_triangle(self):
        test_side1 = 2
        test_side2 = 4
        test_side3 = 6
        test_color = "black"
        test_filled = False
        triangle = Triangle(side1=test_side1, side2=test_side2, side3=test_side3, color=test_color, filled=test_filled)
        actual = str(triangle)
        expected = "Triangle: side1 = {} side2 = {} side3 = {} color: {} and filled: {}".format(test_side1, test_side2,
                                                                                                test_side3, test_color,
                                                                                                test_filled)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
