# should build a gui that will allow the user to encrypt or decrypt messages
# should hold the code to build a simple gui using tkinter and this gui should hold two text fields one for the message
# and one for the key, and two buttons one for encrypting and one for decrypting

import tkinter as tk
import encryption

# creating the window
window = tk.Tk()

# window size
window.geometry('450x250')

#textBox
def printInput():

    inp = inputtxt.get(1.0, "end-1c")
    result = encryption.ascii_caesar_shift(inp)
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

# TextBox Creation
inputtxt = tk.Text(window,
                   height=1,
                   width=50)
inputtxt.pack()

# Button Creation
printButton = tk.Button(window,
                        text="Encrypt Text",
                        command=printInput)
printButton.pack(pady = 5)

encryptTxtTile = tk.Label(window, text="")
encryptTxtTile.config(text="Encrypted: ")
encryptTxtTile.pack(pady = 5)

#text box creation
encryptTxt = tk.Text(window,
                     height=1,
                     width=50,
                     state='disabled')
encryptTxt.pack(pady = 5)

tk.Button(window, text="Copy", pady=5, command=lambda: copyToClipboard(encryptTxt.get(1.0, "end-1c"))).pack()

encryptTxtTile = tk.Label(window, text="")
encryptTxtTile.config(text="Key: ")
encryptTxtTile.pack(pady = 5)



keyTxt = tk.Text(window,
                     height=1,
                     width=50,
                     state='disabled',
                    )
keyTxt.pack()
tk.Button(window, text="Copy", pady=5, command=lambda: copyToClipboard(keyTxt.get(1.0, "end-1c"))).pack()
# creating the window label
window.title('Extended ASCII Encryption')

# start the window
window.mainloop()
