#Name: Arun Kumar, Nukul Nanchahal, Arun Kumar
#Date: February 19, 2025
#Description: This code tests area calculation functions for
#               circle, trapezium, ellipse, and rhombus with valid and invalid inputs.


import unittest

# Import the TestShapes class
from test.test_Lab3_Arun_Nukul_Arun import TestShapes

def run_tests(choice):
    suite = unittest.TestSuite()

    if choice == 'c':
        suite.addTest(TestShapes('test_circle_area_valid'))
        suite.addTest(TestShapes('test_circle_area_invalid'))
    elif choice == 't':
        suite.addTest(TestShapes('test_trapezium_area_valid'))
        suite.addTest(TestShapes('test_trapezium_area_invalid'))
    elif choice == 'e':
        suite.addTest(TestShapes('test_ellipse_area_valid'))
        suite.addTest(TestShapes('test_ellipse_area_invalid'))

    elif choice == 'r':
        suite.addTest(TestShapes('test_rhombus_area_valid'))
        suite.addTest(TestShapes('test_rhombus_area_invalid'))

    else:
        print("Invalid choice. Exiting.")
        return

    runner = unittest.TextTestRunner()
    runner.run(suite)


if __name__ == "__main__":
    print("Enter a shape to test:\n"
          "'c' for Circle\n"
          "'t' for Trapezium\n"
          "'e' for Ellipse\n"
          "'r' for Rhombus\n"
          "What would you like to choose: ")
    choice = input().strip().lower()
    run_tests(choice)
