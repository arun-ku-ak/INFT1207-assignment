# Name: Arun Kumar
#Student ID: 100961975
# Date: February 16, 2025

class TemperatureSensor:
    def __init__(self):
        self.min_temp = -50
        self.max_temp = 150

    def validate_temperature(self, temperature):
        """Helper method to validate a single temperature reading"""
        if not isinstance(temperature, (int, float)):
            raise ValueError(f"Invalid input type: {temperature}. Temperature must be an integer or float.")

        if temperature < self.min_temp or temperature > self.max_temp:
            raise ValueError(
                f"Temperature out of range: {temperature}. Valid range is {self.min_temp} to {self.max_temp}.")
        return True

    def process_temperatures(self, temperatures):
        """Method to process a list of temperature readings"""
        if not temperatures:
            raise ValueError("Temperature list is empty.")

        validated_temperatures = []
        for temp in temperatures:
            if self.validate_temperature(temp):
                validated_temperatures.append(temp)
        return validated_temperatures

    def get_average_temperature(self, temperatures):
        """Method to calculate the average temperature of a list"""
        if not temperatures:
            raise ValueError("Cannot calculate average of an empty list.")
        return sum(temperatures) / len(temperatures)
