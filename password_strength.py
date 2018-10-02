import argparse
import re
import sys
from getpass import getpass


def load_strings_from_file(filepath):
    with open(filepath) as text_file:
        strings = [line.strip() for line in text_file]
        return strings


def get_password_strength(password, blacklisted_passwords, common_words):
    password_rating = 10

    if password in blacklisted_passwords:
        password_rating = 1
        return password_rating

    common_word_flag = password in common_words
    recommended_password_length = 8
    too_short_flag = len(password) < recommended_password_length
    no_digits_flag = re.search(r"\d", password) is None
    no_special_characters_flag = re.search(r"[^\w]", password) is None
    uppercase_or_lowercase_only_flag = password.islower() or password.isupper()
    repetitive_character_flag = re.search(r"(.)\1", password) is not None
    phone_number_or_date_flag = (
        re.search(r"\d{2,3}?-?\d{2}-?\d{2,4}?", password) is not None
    )
    plate_number_flag = (
        re.search(r"[a-zA-Z]{1}\d{3}[a-zA-Z]{2}", password) is not None
    )

    password_strength_flags = [
        common_word_flag,
        too_short_flag,
        no_digits_flag,
        no_special_characters_flag,
        uppercase_or_lowercase_only_flag,
        repetitive_character_flag,
        phone_number_or_date_flag,
        plate_number_flag,
    ]
    password_rating -= sum(password_strength_flags)
    return password_rating


def load_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-b", "--blacklist")
    parser.add_argument("-w", "--words")
    arguments = parser.parse_args()
    return arguments


if __name__ == "__main__":
    try:
        arguments = load_arguments()
        blacklist_filepath = arguments.blacklist
        common_words_filepath = arguments.words

        if blacklist_filepath is None:
            print("Continuing without password blacklist")
            blacklisted_passwords = []
        else:
            blacklisted_passwords = load_strings_from_file(blacklist_filepath)

        if common_words_filepath is None:
            print("Continuing without words list")
            common_words = []
        else:
            common_words = load_strings_from_file(common_words_filepath)

        password = getpass("Enter password: ")
        rating = get_password_strength(
            password, blacklisted_passwords, common_words
        )
        print("Password rating:", rating)
    except FileNotFoundError:
        sys.exit("Blacklist or common words file not found")
