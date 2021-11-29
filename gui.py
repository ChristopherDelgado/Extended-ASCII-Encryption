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
    lbl = tk.Label(window, text="")
    lbl.config(text="Encrypted: " + result[0])
    lbl.pack()

    inp = inputtxt.get(1.0, "end-1c")
    lbl = tk.Label(window, text="")
    lbl.config(text="Key: " + result[1])
    lbl.pack()

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


# creating the window label
window.title('Extended ASCII Encryption')

# start the window
window.mainloop()
