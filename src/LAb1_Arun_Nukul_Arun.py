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

    while True:
        try:
            num_letters = int(input("Enter the number of letters desired in the password: "))
            num_digits = int(input("Enter the number of digits desired in the password: "))
            num_special = int(input("Enter the number of special characters desired in the password: "))

            if num_letters + num_digits + num_special > total_length:
                print(f"The sum of letters, digits, and special characters exceeds the total length ({total_length}). Please enter valid values.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter valid integers.")

    letters = random.choices(string.ascii_letters, k=num_letters)
    digits = random.choices(string.digits, k=num_digits)
    special_chars = random.choices(string.punctuation, k=num_special)

    remaining_length = total_length - (num_letters + num_digits + num_special)
    if remaining_length > 0:
        all_choices = letters + digits + special_chars
        remaining_chars = random.choices(all_choices, k=remaining_length)
        password_chars = letters + digits + special_chars + remaining_chars
    else:
        password_chars = letters + digits + special_chars

    random.shuffle(password_chars)

    password = ''.join(password_chars)

    print("\nYour desired password is:", password)
    print("\nPassword successfully generated with:")
    print(f"Letters: {num_letters}")
    print(f"Digits: {num_digits}")
    print(f"Special characters: {num_special}\n")

generate_password()