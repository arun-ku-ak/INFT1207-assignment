# Name: Arun Kumar
#Student ID: 100961975
# Date: February 16, 2025


import unittest
from src.temperature_sensor import TemperatureSensor


class TestTemperatureSensor(unittest.TestCase):
    def setUp(self):
        """Set up the TemperatureSensor instance before each test"""
        self.sensor = TemperatureSensor()

    # Boundary Value Analysis (BVA)
    def test_min_boundary(self):
        """Test case for minimum boundary temperature"""
        self.assertEqual(self.sensor.process_temperatures([-50]), [-50])

    def test_max_boundary(self):
        """Test case for maximum boundary temperature"""
        self.assertEqual(self.sensor.process_temperatures([150]), [150])

    def test_near_boundary(self):
        """Test case for near-boundary temperatures"""
        self.assertEqual(self.sensor.process_temperatures([-49, 149]), [-49, 149])

    # Robustness Testing
    def test_mixed_valid_and_invalid_inputs(self):
        """Test case for a mix of valid and invalid inputs"""
        with self.assertRaises(ValueError):
            self.sensor.process_temperatures([-60, 20, 160])

    def test_alphabetic_characters_in_input(self):
        """Test case for alphabetic characters in input"""
        with self.assertRaises(ValueError):
            self.sensor.process_temperatures([20, "abc", 30])

    def test_special_characters_in_input(self):
        """Test case for special characters in input"""
        with self.assertRaises(ValueError):
            self.sensor.process_temperatures([10, "@", -40])

    # Special Scenarios
    def test_large_input_values(self):
        """Test case for very large input values, expecting a ValueError due to range"""
        with self.assertRaises(ValueError):
            self.sensor.process_temperatures([2**31 - 1, -2**31])

    def test_all_inputs_same(self):
        """Test case for when all inputs are the same"""
        self.assertEqual(self.sensor.process_temperatures([50, 50, 50]), [50, 50, 50])

    def test_empty_list(self):
        """Test case for an empty input list"""
        with self.assertRaises(ValueError):
            self.sensor.process_temperatures([])

    # Average Calculation Test
    def test_average_temperature(self):
        """Test case for calculating the average temperature"""
        self.assertEqual(self.sensor.get_average_temperature([10, 20, 30]), 20.0)

    def test_average_empty_list(self):
        """Test case for an empty list in average calculation"""
        with self.assertRaises(ValueError):
            self.sensor.get_average_temperature([])


if __name__ == '__main__':
    unittest.main()
