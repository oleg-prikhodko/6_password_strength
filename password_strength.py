import argparse
import re
import sys
from getpass import getpass


def load_strings_from_file(filepath):
    with open(filepath) as text_file:
        strings = [line.strip() for line in text_file]
        return strings


def get_password_strength(password, blacklisted_passwords, words):
    password_rating = 10

    if password in blacklisted_passwords:
        password_rating = 1
        return password_rating

    has_a_word = password in words
    recommended_password_length = 8
    is_too_short = len(password) < recommended_password_length
    has_no_digits = re.search(r"\d", password) is None
    has_no_special_characters = re.search(r"[^\w]", password) is None
    is_uppercase_or_lowercase_only = password.islower() or password.isupper()
    has_repetitive_character = re.search(r"(.)\1", password) is not None
    has_phone_number_or_date = (
        re.search(r"\d{2,3}?-?\d{2}-?\d{2,4}?", password) is not None
    )
    has_plate_number = (
        re.search(r"[a-zA-Z]{1}\d{3}[a-zA-Z]{2}", password) is not None
    )

    password_strength_criteria = [
        has_a_word,
        is_too_short,
        has_no_digits,
        has_no_special_characters,
        is_uppercase_or_lowercase_only,
        has_repetitive_character,
        has_phone_number_or_date,
        has_plate_number,
    ]
    password_rating -= sum(password_strength_criteria)
    return password_rating


if __name__ == "__main__":
    try:
        parser = argparse.ArgumentParser()
        parser.add_argument("-b", "--blacklist")
        parser.add_argument("-w", "--words")
        arguments = parser.parse_args()
        blacklist_filepath = arguments.blacklist
        words_filepath = arguments.words

        if blacklist_filepath is None:
            print("Continuing without password blacklist")
            blacklisted_passwords = []
        else:
            blacklisted_passwords = load_strings_from_file(blacklist_filepath)

        if words_filepath is None:
            print("Continuing without words list")
            words = []
        else:
            words = load_strings_from_file(words_filepath)

        password = getpass("Enter password: ")
        rating = get_password_strength(password, blacklisted_passwords, words)
        print("Password rating:", rating)
    except FileNotFoundError:
        sys.exit("Blacklist or words file not found")
