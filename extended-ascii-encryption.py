# should build a gui that will allow the user to encrypt or decrypt messages
# should hold the code to build a simple gui using tkinter and this gui should hold two text fields one for the message
# and one for the key, and two buttons one for encrypting and one for decrypting

import tkinter as tk
import os


def decryption_box():

    # decryption algorithm
    def decrypt(cipher_message, key):
        # unencrypted message
        result = ''
        # key split into proper pieces
        key = key.split(' ')
        # loop over each character in the cipher, we use the minimum length between keys and cipher
        # due to a bug caused by fact that Extended ASCII includes non printable characters
        for i in range(min(len(cipher_message), len(key))):
            # cipher_message length approx. =  key length so getting both characters at i is safe
            encrypted_char_ascii = ord(cipher_message[i])
            key_char_ascii = int(key[i])
            # decrypting the char by offsetting the encrypted char by the key char
            unencrypted_char = (encrypted_char_ascii - key_char_ascii) % 256
            result += chr(unencrypted_char)
        return result

    # decrypt button callback
    def gui_decrypt():
        # get our input field
        cipher = cipherField.get('1.0', 'end-1c')
        key = keyField.get('1.0', 'end-1c')

        # exit if either of our inputs are empty
        if not cipher or not key:
            tk.Label(window, text='ENTER ALL FIELDS', fg="#FF0000").grid(row=i, column=0, pady=5)
            return

        # decrypt the message
        result = decrypt(cipher, key)

        # show result on screen
        decryptField.configure(state='normal')
        decryptField.delete('1.0', 'end')
        decryptField.insert('1.0', result)
        decryptField.configure(state='disabled')

    # creating the window
    window = tk.Tk()

    # creating the window label
    window.title('Decryption Box')

    # window size
    window.geometry('450x250')

    # telling all grid columns to center their widgets
    window.grid_columnconfigure(0, weight=1)

    # labels
    cipherLabel = tk.Label(window, text='Cipher', height=1, width=6)
    keyLabel = tk.Label(window, text='Key', height=1, width=6)
    decryptLabel = tk.Label(window, text='Decrypted', height=1, width=7)

    # encrypted message text field
    cipherField = tk.Text(window, height=1, width=50)
    keyField = tk.Text(window, height=1, width=50, )
    decryptField = tk.Text(window, height=1, width=50, state='disabled')  # disabled prevents user from typing here

    # submit button
    submitButton = tk.Button(window, text="Decrypt", height=1, width=6, command=gui_decrypt)

    # tuples of label text widgets
    textWidgets = (cipherLabel, cipherField, keyLabel, keyField, decryptLabel, decryptField, submitButton)

    # adding the list of text widgets to the window
    i = 0
    for widget in textWidgets:
        widget.grid(row=i, column=0, pady=5)
        # center this widget on the screen
        widget.grid_columnconfigure(1, weight=1)
        i += 1

    # start the window
    window.mainloop()

def encryptionBox():

    # encryption algorithm
    def encrypt(message):
        encrypted = ""
        key = ""
        # loop over every character in the text
        for char in message:
            # generate a current key for this character
            ck = ord(os.urandom(1)) + ord(os.urandom(1)) % 256
            key += str(ck) + ' '
            encrypted += chr(ord(char) + ck % 256)
        # return a tuple containing our encrypted message and the generated key
        return encrypted, key

    # update textbox with encryption and generated key
    def printInput():
        inp = inputtxt.get(1.0, "end-1c")
        result = encrypt(inp)
        keyTxt.configure(state='normal')
        keyTxt.delete('1.0', 'end')
        keyTxt.insert('1.0', result[1])
        keyTxt.configure(state='disabled')

        encryptTxt.configure(state='normal')
        encryptTxt.delete('1.0', 'end')
        encryptTxt.insert('1.0', result[0])
        encryptTxt.configure(state='disabled')

    # copy text to clipboard
    def copyToClipboard(text):
        window.clipboard_clear()
        window.clipboard_append(text)
        window.update()

    # creating the window
    window = tk.Tk()

    # window size
    window.geometry('450x250')

    # TextBox Creation
    inputtxt = tk.Text(window,
                       height=1,
                       width=50)
    inputtxt.pack()

    # Button Creation
    printButton = tk.Button(window,
                            text="Encrypt Text",
                            command=printInput)
    printButton.pack(pady=5)

    encryptTxtTile = tk.Label(window, text="")
    encryptTxtTile.config(text="Encrypted: ")
    encryptTxtTile.pack(pady=5)

    # text box creation
    encryptTxt = tk.Text(window,
                         height=1,
                         width=50,
                         state='disabled')
    encryptTxt.pack(pady=5)

    tk.Button(window, text="Copy", pady=5, command=lambda: copyToClipboard(encryptTxt.get(1.0, "end-1c"))).pack()

    encryptTxtTile = tk.Label(window, text="")
    encryptTxtTile.config(text="Key: ")
    encryptTxtTile.pack(pady=5)

    keyTxt = tk.Text(window,
                     height=1,
                     width=50,
                     state='disabled',
                     )
    keyTxt.pack()
    tk.Button(window, text="Copy", pady=5, command=lambda: copyToClipboard(keyTxt.get(1.0, "end-1c"))).pack()
    # creating the window label
    window.title('Encryption Box')
    window.mainloop()


window = tk.Tk()

# creating the window label
window.title('Decryption Box')

# window size
window.geometry('250x125')

# telling all grid columns to center their widgets
window.grid_columnconfigure(0, weight=1)

# submit button
encryptButton = tk.Button(window, text="Encrypt", height=1, width=6, command=encryptionBox)
decryptButton = tk.Button(window, text="Decrypt", height=1, width=6, command=decryption_box)

# tuples of label text widgets
textWidgets = (encryptButton, decryptButton)

# adding the list of text widgets to the window
i = 0
for widget in textWidgets:
    widget.grid(row=i, column=0, pady=5)
    # center this widget on the screen
    widget.grid_columnconfigure(1, weight=1)
    i += 1

# start the window
window.mainloop()