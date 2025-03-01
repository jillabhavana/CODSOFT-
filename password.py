import random
import string

def generate_password(length, use_digits=True, use_special_chars=True):
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits if use_digits else ''
    special_chars = string.punctuation if use_special_chars else ''

    all_chars = lower + upper + digits + special_chars

    if not all_chars:
        return "Error: No character set selected."

    password = ''.join(random.choice(all_chars) for _ in range(length))
    return password

def main():
    try:
        length = int(input("Enter password length: "))
        use_digits = input("Include digits? (yes/no): ").strip().lower() == 'yes'
        use_special_chars = input("Include special characters? (yes/no): ").strip().lower() == 'yes'

        password = generate_password(length, use_digits, use_special_chars)
        print(f"Generated Password: {password}")

    except ValueError:
        print("Invalid input! Please enter a valid number for length.")

if __name__ == "__main__":
    main()
