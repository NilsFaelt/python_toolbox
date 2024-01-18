"""Password cracker"""
import hashlib
import os

passwords = []
rock_you = []
file_path = '/usr/share/wordlists/rockyou.txt'


def password_cracker():
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            for line in f:
                words = line.strip().split()
                rock_you.extend(words)
    except UnicodeDecodeError:
        print("Error: Unable to decode the file content.")


    print(rock_you)


    
