'''This assignement was done by me (shirwac), but whenever I have encoutred errors that i could not debug,
   I have used ChatGPT to help me debug and fix the errors. I have learned a lot from this process, and I am grateful for the assistance.
   I have also used ChatGPT to do docstrings for me, since I have used JSdocs from JavaScript before, and I wanted to learn how to do it in Python.
 '''
import random
import string

def get_password_length():
    """
    Prompt the user until they provide a valid password length (8-16).

    @returns {int} A valid password length between 8 and 16.
    """
    while True:
        user_input = input("Enter the desired password length (8-16): ")
        if not user_input.isdigit():
            print("Error: Please enter a valid number.")
            continue
        length = int(user_input)
        if 8 <= length <= 16:
            return length
        else:
            print("Error: Password length must be between 8 and 16 characters.")


def generate_password(length):
    """
    Generate a random secure password that meets the requirements.

    Requirements:
    - At least one lowercase letter
    - At least one uppercase letter
    - At least one digit
    - At least one special character
    - Cannot begin with a digit or special character

    @param {int} length - Desired password length (8–16).
    @returns {str} A randomly generated secure password.
    """
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    special_chars = "!@#$%^&*()-_=+"

    # Ensure at least one of each required type
    password_chars = [
        random.choice(lowercase),
        random.choice(uppercase),
        random.choice(digits),
        random.choice(special_chars),
    ]

    # Fill the remaining length with random choices from all categories
    all_chars = lowercase + uppercase + digits + special_chars
    while len(password_chars) < length:
        password_chars.append(random.choice(all_chars))

    # Shuffle to avoid predictable order
    random.shuffle(password_chars)

    # Ensure the first character is not a digit or special char
    if password_chars[0] in digits + special_chars:
        for i in range(1, len(password_chars)):
            if password_chars[i] in lowercase + uppercase:
                password_chars[0], password_chars[i] = password_chars[i], password_chars[0]
                break

    return "".join(password_chars)


def main():
    """
    Main program flow:
    1. Prompt for password length
    2. Generate a secure password
    3. Display the result

    @returns {None}
    """
    length = get_password_length()
    password = generate_password(length)
    print("Generated password:", password)


if __name__ == "__main__":
    main()
