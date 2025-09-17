import random
import string

def get_password_length():
    """Prompt the user until they provide a valid password length (8–16)."""
    while True:
        user_input = input("Enter desired password length (8–16): ")
        if not user_input.isdigit():
            print("❌ Invalid input! Please enter a number.")
            continue
        length = int(user_input)
        if 8 <= length <= 16:
            return length
        else:
            print("❌ Password length must be between 8 and 16.")

def generate_password(length):
    """Generate a random secure password that meets given requirements."""
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
        # Swap with a guaranteed letter
        for i in range(1, len(password_chars)):
            if password_chars[i] in lowercase + uppercase:
                password_chars[0], password_chars[i] = password_chars[i], password_chars[0]
                break

    return "".join(password_chars)

def main():
    length = get_password_length()
    password = generate_password(length)
    print("\n✅ Generated Password:", password)

if __name__ == "__main__":
    main()
