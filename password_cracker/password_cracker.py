import hashlib

# /usr/share/wordlists/rockyou.txt
file_path = '/usr/share/wordlists/rockyou.txt'
hashed_words_array = []
words_array = []


def password_cracker(encoded_password):
    try:
        with open(file_path, 'r', encoding='latin-1', errors='replace') as f:
            for line in f:
                words = line.strip().split()
                hashed_words = [hashlib.sha256(word.encode('utf-8')).hexdigest() for word in words]
                words_array.extend(words)
                hashed_words_array.extend(hashed_words)
        compare_hashes(encoded_password, hashed_words_array)
    except UnicodeDecodeError:
        print("Error: Unable to decode the file content.")

def compare_hashes(encoded_password, hashed_words_array):
    for index, hashed_password in enumerate(hashed_words_array):
        if encoded_password == hashed_password:
            print(f"Match found at index {index}")
            print(f"Original word: {words_array[index]}")
            return
    print("No match found")

# Example usage
