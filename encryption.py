import os


def ascii_caesar_shift(message):
    encrypted = ""
    key = ""
    for char in message:
        new_value = ((ord(os.urandom(1)) + ord(os.urandom(1))) % 256)
        print(new_value)
        key += str(new_value) + ' '
        encrypted += chr((ord(char) + new_value) % 256)  # 256 for ASCII characters
    return (encrypted, key)
