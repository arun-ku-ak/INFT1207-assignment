import random
import string
def generate_password():
    while True:
        try:
            total_length = int(input("Enter the total length of the password: "))
            if total_length < 8:
                print("Please enter a value of greater than or equal to 8 to create a secure password.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a valid integer.")