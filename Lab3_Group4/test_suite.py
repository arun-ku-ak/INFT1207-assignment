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
    elif choice == 'e':
        suite.addTest(TestShapes('test_ellipse_area_valid'))
    elif choice == 'r':
        suite.addTest(TestShapes('test_rhombus_area_valid'))
    else:
        print("Invalid choice. Exiting.")
        return

    runner = unittest.TextTestRunner()
    runner.run(suite)


if __name__ == "__main__":
    print("Enter a shape to test ('c' for Circle, 't' for Trapezium, 'e' for Ellipse, 'r' for Rhombus):")
    choice = input().strip().lower()
    run_tests(choice)