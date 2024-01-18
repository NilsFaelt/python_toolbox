import hashlib

file_path = '/usr/share/wordlists/rockyou.txt'

hashed_words_array = []

try:
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            words = line.strip().split()
            hashed_words = [hashlib.sha256(word.encode('utf-8')).hexdigest() for word in words]
            hashed_words_array.extend(hashed_words)
except UnicodeDecodeError:
    print("Error: Unable to decode the file content.")

print(hashed_words_array[0])
print(hashed_words_array[10])
