"""
CP1404/CP5632 - Practical
Password checker "skeleton" code to help you get started
"""
import random

LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
LETTERS = LETTERS + LETTERS.lower()
DIGITS = "0123456789"
SPECIAL_CHARACTERS = "!@#$%^&*()_-=+`~,./'[]<>?{}|\\"


def main():

    min_length = int(raw_input("Minimum password length: "))
    max_length = int(raw_input("Maximum password length: "))
    are_special_chars_required = bool(raw_input("Are special characters {} required (True/False): ".format(SPECIAL_CHARACTERS)))
    num_required_uppercase_characters = int(raw_input("Number of uppercase characters required: "))
    num_required_lowercase_characters = int(raw_input("Number of lowercase characters required: "))
    num_required_numbers = int(raw_input("Number of numbers required: "))

    valid_characters = LETTERS + DIGITS
    if are_special_chars_required:
        valid_characters += SPECIAL_CHARACTERS

    password = generate_password(min_length, max_length, valid_characters)

    while not is_valid_password(password, min_length, max_length, are_special_chars_required, num_required_uppercase_characters, num_required_lowercase_characters, num_required_numbers):
        print("Invalid password was generated {}".format(password))
        password = generate_password(min_length, max_length, valid_characters)
    print("Correct generated password is: {}".format(password))


def generate_password(min_length, max_length, valid_characters):

    password = ""

    for i in range(random.randint(min_length, max_length)):
        password += random.choice(valid_characters)

    return password


def is_valid_password(password, min_length, max_length, are_special_chars_required, num_required_uppercase_characters, num_required_lowercase_characters, num_required_numbers):
    """Determine if the provided password is valid."""

    if min_length > len(password) > max_length:
        return False

    count_lower = 0
    count_upper = 0
    count_digit = 0
    count_special = 0
    for char in password:
        if char.islower():
            count_lower += 1
        elif char.isupper():
            count_upper += 1
        elif char.isdigit():
            count_digit += 1
        elif char in SPECIAL_CHARACTERS:
            count_special += 1

    if count_upper < num_required_uppercase_characters or count_lower < num_required_lowercase_characters or count_digit < num_required_numbers:
        return False

    if are_special_chars_required and count_special == 0:
        return False

    # if we get here (without returning False), then the password must be valid
    return True


main()
