# should build a gui that will allow the user to encrypt or decrypt messages
# should hold the code to build a simple gui using tkinter and this gui should hold two text fields one for the message
# and one for the key, and two buttons one for encrypting and one for decrypting

import tkinter as tk
import decrypt


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
    result = decrypt.decrypt(cipher, key)

    # show result on screen
    decryptField.delete('1.0', 'end')
    decryptField.insert('1.0', result)


# creating the window
window = tk.Tk()

# creating the window label
window.title('Extended ASCII Encryption')

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
    widget.grid_columnconfigure(1, weight=3)
    i += 1

# start the window
window.mainloop()
