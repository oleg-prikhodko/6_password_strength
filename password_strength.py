import os.path as path
import re
import sys


def get_password_strength(password):
    blacklist_filepath = path.join(
        path.dirname(path.abspath(__file__)), "blacklist.txt"
    )
    with open(blacklist_filepath) as blacklist_file:
        blacklisted_passwords = [line.strip() for line in blacklist_file]

    words_filepath = path.join(
        path.dirname(path.abspath(__file__)), "words.txt"
    )
    with open(words_filepath) as words_file:
        words = [line.strip() for line in words_file]

    password_rating = 10

    if password in blacklisted_passwords:
        password_rating = 1
        return password_rating

    password_strength_criteria = [
        password in words,  # contains a word, abbreviation or name
        len(password) < 8,  # too short
        re.search(r"\d", password) is None,  # no digits
        re.search(r"[^\w]", password) is None,  # no special characters
        password.islower() or password.isupper(),  # uppercase/lowercase only
        re.search(r"(.)\1", password) is not None,  # character repetition
        re.search(r"\d{2,3}?-?\d{2}-?\d{2,4}?", password)
        is not None,  # phone number or date
        re.search(r"[a-zA-Z]{1}\d{3}[a-zA-Z]{2}", password)
        is not None,  # plate number
    ]
    password_rating -= sum(password_strength_criteria)
    return password_rating


if __name__ == "__main__":
    try:
        password = input("Enter password: ")
        rating = get_password_strength(password)
        print("Password rating:", rating)
    except FileNotFoundError:
        sys.exit("Blacklist or words file not found")
