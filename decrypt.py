def decrypt(cipher_message, key):
    # unencrypted message
    result = ''
    # key split into proper pieces
    key = key.split(' ')
    # loop over each character in the cipher and key and decrypt
    for i in range(len(cipher_message)):
        # cipher_message length = key length so getting both characters at i is safe
        encrypted_char_ascii = ord(cipher_message[i])
        key_char_ascii = int(key[i])
        # decrypting the char by offsetting the encrypted char by the key char
        unencrypted_char = (encrypted_char_ascii - key_char_ascii) % 256
        result += chr(unencrypted_char)
        print(result)
    return result

