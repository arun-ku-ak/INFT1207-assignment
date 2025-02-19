#Name: Arun Kumar, Nukul Nanchahal, Arun Kumar
#Date: February 19, 2025
#Description: This code tests area calculation functions for
#               circle, trapezium, ellipse, and rhombus with valid and invalid inputs.


import unittest
from Lab3_Group4.app.Lab3_Arun_Nukul_Arun import circle_area, trapezium_area, ellipse_area, rhombus_area

class TestShapes(unittest.TestCase):

    def setUp(self):
        print("Setup: Preparing tests...")

    def tearDown(self):
        print("Teardown: Cleaning up after tests...")

    # Test for valid circle area
    def test_circle_area_valid(self):
        self.assertAlmostEqual(circle_area(3), 28.274333882308138, places=5)

    # Test for invalid circle area (negative radius)
    def test_circle_area_invalid(self):
        with self.assertRaises(ValueError):
            circle_area(-1)

    # Test for valid trapezium area
    def test_trapezium_area_valid(self):
        self.assertAlmostEqual(trapezium_area(5, 10, 4), 30.0, places=5)

    # Test for invalid trapezium area (negative side length)
    def test_trapezium_area_invalid(self):
        with self.assertRaises(ValueError):
            trapezium_area(-5, 10, 4)

    # Test for valid ellipse area
    def test_ellipse_area_valid(self):
        self.assertAlmostEqual(ellipse_area(4, 3), 37.69911184307752, places=5)

    # Test for invalid ellipse area (zero or negative axis)
    def test_ellipse_area_invalid(self):
        with self.assertRaises(ValueError):
            ellipse_area(4, -3)
        with self.assertRaises(ValueError):
            ellipse_area(0, 3)

    # Test for valid rhombus area
    def test_rhombus_area_valid(self):
        self.assertAlmostEqual(rhombus_area(5, 6), 15.0, places=5)

    # Test for invalid rhombus area (zero or negative diagonal length)
    def test_rhombus_area_invalid(self):
        with self.assertRaises(ValueError):
            rhombus_area(-5, 6)
        with self.assertRaises(ValueError):
            rhombus_area(5, 0)

if __name__ == "__main__":
    unittest.main()

