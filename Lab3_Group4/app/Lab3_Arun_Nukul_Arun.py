#Name: Arun Kumar, Nukul Nanchahal, Arun Kumar
#Date: February 19, 2025
#Description: This code tests area calculation functions for
#               circle, trapezium, ellipse, and rhombus with valid and invalid inputs.


import math

# Function to calculate the area of a circle
def circle_area(radius):
    if radius <= 0:
        raise ValueError("Radius must be a positive number")
    return math.pi * radius ** 2

# Function to calculate the area of a trapezium
def trapezium_area(a, b, h):
    if a <= 0 or b <= 0 or h <= 0:
        raise ValueError("All inputs must be positive numbers")
    return ((a + b) * h) / 2

# Function to calculate the area of an ellipse
def ellipse_area(a, b):
    if a <= 0 or b <= 0:
        raise ValueError("Both semi-major and semi-minor axes must be positive numbers")
    return math.pi * a * b

# Function to calculate the area of a rhombus
def rhombus_area(d1, d2):
    if d1 <= 0 or d2 <= 0:
        raise ValueError("Both diagonals must be positive numbers")
    return (d1 * d2) / 2
