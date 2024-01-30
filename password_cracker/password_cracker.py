import hashlib

file_path = '/usr/share/wordlists/rockyou.txt'
words_array = []


def generate_hashed_words(file_path):
    """Generator function to yield hashed words"""
    try:
        with open(file_path, 'r', encoding='latin-1', errors='replace') as f:
            for line in f:
                words = line.strip().split()
                hashed_words = (hashlib.sha256(word.encode('utf-8')).hexdigest() for word in words)
                words_array.extend(words)
                yield from hashed_words
    except Exception as e:
        print(f"Error: {e}")

def password_cracker(encoded_password):
    """Function for cracking passwords"""
    hashed_words_generator = generate_hashed_words(file_path)
    
    for index, hashed_password in enumerate(hashed_words_generator):
        if encoded_password == hashed_password:
            print(f"Match found at index {index}")
            print(f"Original word: {words_array[index]}")
            return
    print("No match found")

if __name__ == "__main__":
    encoded_password = input("Enter the encoded password to crack: ")
    password_cracker(encoded_password)
