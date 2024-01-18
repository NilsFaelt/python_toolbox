"""Password cracker"""
import hashlib
import os

passwords = []
rock_you = []
file_path = '/usr/share/wordlists/rockyou.txt'


def password_cracker():
    """Function for cracking passwords"""
    with open('hashed_passwords.txt', 'r') as f:
        passwords = f.read().splitlines()
    with open(file_path, 'rb') as f:
        rock_you = f.read()
    
    print(rock_you)
    print('passssssswoooooord crack')

# def generate_hash(password):
    
#     hash = hashlib.sha256(password.encode('utf-8'))
#     print(hash.hexdigest())
#     return hash    