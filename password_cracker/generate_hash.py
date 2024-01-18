"""Genarate hashed password"""
import hashlib


def generate_hash(password):
    hash = hashlib.sha256(password.encode('utf-8'))
    print(hash)
    return hash