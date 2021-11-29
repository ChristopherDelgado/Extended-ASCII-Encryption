# should build a gui that will allow the user to encrypt or decrypt messages
# should hold the code to build a simple gui using tkinter and this gui should hold two text fields one for the message
# and one for the key, and two buttons one for encrypting and one for decrypting

import Tkinter as tk
import encryption

# creating the window
window = tk.Tk()

# window size
window.geometry('600x400')

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

# TextBox Creation
inputtxt = tk.Text(window,
                   height=5,
                   width=20)
inputtxt.pack()

# Button Creation
printButton = tk.Button(window,
                        text="Encrypt Text",
                        command=printInput)
printButton.pack(pady = 20)

encryptTxtTile = tk.Label(window, text="")
encryptTxtTile.config(text="Encrypted: ")
encryptTxtTile.pack(pady = 10)

#text box creation
encryptTxt = tk.Text(window,
                     height=5,
                     width=20,
                     state='disabled')
encryptTxt.pack(pady = 20)

encryptTxtTile = tk.Label(window, text="")
encryptTxtTile.config(text="Key: ")
encryptTxtTile.pack(pady = 20)

keyTxt = tk.Text(window,
                     height=5,
                     width=20,
                     state='disabled',
                    )
keyTxt.pack()

# creating the window label
window.title('Extended ASCII Encryption')

# start the window
window.mainloop()
