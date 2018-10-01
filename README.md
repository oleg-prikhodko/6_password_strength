# Password Strength Calculator

Ranks passwords on a scale from 1 to 10

# Quickstart

Program accepts two optional arguments : "-b" or "--blacklist" - path to file containing blacklisted passwords \(you could get [this one](https://github.com/danielmiessler/SecLists/raw/master/Passwords/Common-Credentials/10-million-password-list-top-1000000.txt)\) and "-w" or "--words" - path to file with english words \(download it [here](https://github.com/dwyl/english-words/raw/master/words.txt)\)

Example of script launch on Linux, Python 3.5:

```bash
$ python password_strength.py -b blacklist.txt -w words.txt
Enter password: supercoolpassword
Password rating: 6
```

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
