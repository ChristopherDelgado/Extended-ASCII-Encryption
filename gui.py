# should build a gui that will allow the user to encrypt or decrypt messages
# should hold the code to build a simple gui using tkinter and this gui should hold two text fields one for the message
# and one for the key, and two buttons one for encrypting and one for decrypting

import tkinter as tk

# creating the window
window = tk.Tk()

# creating the window label
window.title('Extended ASCII Encryption')

# window size
window.geometry('600x400')

# telling all grid columns to center their widgets
window.grid_columnconfigure(0, weight=1)

# encrypted message text field
cipherField = tk.Text(window, height=1, width=50)
keyField = tk.Text(window, height=1, width=50, state='disabled')
decryptField = tk.Text(window, height=1, width=50, state='disabled')
submitButton = tk.Button(window, text="Decrypt", height=2, width=4)

# tuple of text widgets
widgets = (cipherField, keyField, decryptField, submitButton)

# adding the list of text widgets to the window
i = 0
for widget in widgets:
    widget.grid(row=i, column=0)
    # center this widget on the screen
    widget.grid_columnconfigure(1, weight=1)
    i += 1

# adding the button to the window
# decryption handling

# start the window
window.mainloop()
