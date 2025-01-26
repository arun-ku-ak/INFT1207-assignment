#Name: Arun Kumar , Nukul Nanchahal, Arun Kumar
#Date: January 24, 2025
#Description: We are generating password.
# Added a password generator script
import random
import string


def get_int_input(prompt, min_value=1):
    try:
        value = int(input(prompt))
        if value < min_value:
            print(f"Please enter a value of at least {min_value}.")
            return get_int_input(prompt, min_value)
        return value
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
        return get_int_input(prompt, min_value)


def generate_password():
    total_length = get_int_input("Enter the total length of the password (min 8): ", 8)
    num_letters = get_int_input("Enter the number of letters: ")
    num_digits = get_int_input("Enter the number of digits: ")
    num_special = get_int_input("Enter the number of special characters: ")

    if num_letters + num_digits + num_special > total_length:
        print("Total characters exceed password length. Please enter valid values.")
        return generate_password()

    password_chars = (
            random.choices(string.ascii_letters, k=num_letters) +
            random.choices(string.digits, k=num_digits) +
            random.choices(string.punctuation, k=num_special) +
            random.choices(string.ascii_letters + string.digits + string.punctuation,
                           k=total_length - (num_letters + num_digits + num_special))
    )

    random.shuffle(password_chars)
    password = ''.join(password_chars)

    print("\nYour generated password:", password)
    print("\nPassword breakdown:")
    print(f"Letters: {num_letters}, Digits: {num_digits}, Special characters: {num_special}\n")


generate_password()
