# Password Strength Calculator

Ranks passwords on a scale from 1 to 10

# Quickstart

Program requires two files in a same folder to work correctly - blacklist.txt (contains blacklisted passwords - you could get (this one)[https://github.com/danielmiessler/SecLists/raw/master/Passwords/Common-Credentials/10-million-password-list-top-1000000.txt]) and words.txt (english words list, download it (here)[https://github.com/dwyl/english-words/raw/master/words.txt])

Example of script launch on Linux, Python 3.5:

```bash
$ python password_strength.py
Enter password: supercoolpassword
No digits
No special characters
Not both upper-case and lower-case letters
Repetetive character
Password rating: 6
```

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
