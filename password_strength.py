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
        print("Blacklisted password")
        password_rating = 1
        return password_rating

    if password in words:
        print("Contains word, abbreviation or name")

    if len(password) < 8:
        password_rating -= 1
        print("Too short")

    if re.search(r"\d", password) is None:
        password_rating -= 1
        print("No digits")

    if re.search(r"[^\w]", password) is None:
        password_rating -= 1
        print("No special characters")

    if password.islower() or password.isupper():
        password_rating -= 1
        print("Not both upper-case and lower-case letters")

    if re.search(r"(.)\1", password):
        password_rating -= 1
        print("Repetetive character")

    if re.search(r"\d{2,3}?-?\d{2}-?\d{2,4}?", password):
        password_rating -= 1
        print("Looks like a date or a phone number")

    if re.search(r"[a-zA-Z]{1}\d{3}[a-zA-Z]{2}", password):
        password_rating -= 1
        print("Looks like a plate number")

    return password_rating


if __name__ == "__main__":
    try:
        password = input("Enter password: ")
        rating = get_password_strength(password)
        print("Password rating:", rating)
    except FileNotFoundError:
        sys.exit("Blacklist or words file not found")
