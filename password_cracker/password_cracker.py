import hashlib

file_path = '/usr/share/wordlists/rockyou.txt'
hashed_words_array = []
words_array = []


def read_words_from_file():
    with open(file_path, 'r', encoding='latin-1') as f:
        for line in f:
            words = line.strip().split()
            hashed_words = [hashlib.sha256(word.encode('utf-8')).hexdigest() for word in words]
            words_array.extend(words)
            hashed_words_array.extend(hashed_words)


def password_cracker(encoded_password):
    try:
        read_words_from_file()
        compare_hashes(encoded_password, hashed_words_array)
    except UnicodeDecodeError as e:
        print(f"Error: Unable to decode the file content. {e}")


def compare_hashes(encoded_password, hashed_words_array):
    for index, hashed_password in enumerate(hashed_words_array):
        if encoded_password == hashed_password:
            print(f"Match found at index {index}")
            print(f"Original word: {words_array[index]}")
            return
    print("No match found")

