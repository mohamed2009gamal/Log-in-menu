# libraries
import os
import tkinter as tk
import random
import string
from tkinter import PhotoImage, Label, Button, messagebox, filedialog


# application options
root = tk.Tk()
root.title("Encrypt what you want")
root.geometry("700x400")
root.resizable(False, False)
root.configure(bg='#71b2bd')
root.iconbitmap(r"C:\Users\HP\pycharm\projects\crypt_1\crypt_icon.ico")

logo_path = 'crypt_logo.png'
logo_label = None

try:
    current_dir = os.path.dirname(os.path.realpath(__file__))
    logo_path = os.path.join(current_dir, logo_path)
    logo = PhotoImage(file=logo_path)
    logo_label = Label(root, image=logo)
    logo_label.place(x=295, y=220)
finally:
    if logo_label is not None:
        logo_label.config(bg='#71b2bd')


#=======================================================================================================================
# title
title_label = tk.Label(root, text="Encrypt your text message", font=('Helvetica', 17), bg='#71b2bd')
title_label.place(x=240, y=10)

#=======================================================================================================================
# Output encrypted text message
output_encrypted = tk.Label(root, text="Output encrypted message--->", font=('Helvetica', 13), bg='#71b2bd')
output_encrypted.place(x=10, y=130)

# Output encrypted label
output_encrypted = tk.Entry(root, width=85, bg='#ff6100')
output_encrypted.pack()
output_encrypted.place(x=70, y=160)
output_encrypted.focus()

#=======================================================================================================================
# Functions
def caesar_cipher(plain_text, shift):
    alphabet = 'a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z'
    encrypted_text = ''

    for letter in plain_text.lower():
        if letter.isalpha():
            index = (alphabet.index(letter) + shift) % 26
            encrypted_text += alphabet[index]
        else:
            encrypted_text += letter

    return encrypted_text


chars = " " + string.whitespace + string.punctuation + string.digits + string.ascii_letters
chars = list(chars)
key = chars.copy()
random.shuffle(key)


def encrypt():
    plain_text = encrypt_entry.get()
    encrypted_text = caesar_cipher(plain_text, 8)
    output_encrypted.insert(tk.END, encrypted_text)


# Encryption Button
encryption_Button = tk.Button(root, text='crypt your message', command=encrypt, bg='#936dbd')
encryption_Button.place(x=535, y=81)

def label(fild=None, encrypt_entry_label=None, encrypt_label=None):
    try:
        encrypt_label.label = int(encrypt_label.get())
        encrypt_entry.label = str(encrypt_entry.entry.get())
    except ValueError:
        messagebox.showerror("Error", "Sorry, this label can't be empty!.")
        encrypt_entry.focus()
    if encrypt_entry_label is not fild:
        messagebox.showerror("Error", "Sorry, labels can't be empty!.")
        encrypt_entry.focus()


encrypt_text_label = tk.Label(root, text="Enter message to encrypt--->", font=('Helvetica', 13), bg='#71b2bd')
encrypt_text_label.place(x=10, y=50)

# Encrypt entry label
encrypt_entry = tk.Entry(root, width=75, bg='#ffa500')
encrypt_entry.place(x=70, y=85)
encrypt_entry.focus()

#=======================================================================================================================
# status bar
STATUS = Label(root, text="Created by Mohamed gamal", font=('calibre', 10, 'italic'), fg='#480075', anchor='w')
STATUS.place(x=3.0, rely=1, anchor='sw', relwidth=1)
STATUS.config(bg='light blue')

#=======================================================================================================================
# Function to browse
def browse():
    filedialog.askdirectory(title='Save Video At')

# Browse Button
browseButton = Button(root, text='Browse', command=browse)
browseButton.place(x=600, y=155)
browseButton.config(bg='#1aff00')

# Comments:>
#=======================================================================================================================
# libraries used
#import os
#import tkinter as tk
#import random
#import string
#from tkinter import PhotoImage, Label, Button, messagebox, filedialog

# app options
# app geometry 700x400
# app bg color #71b2bd
# title
# title color #71b2bd
# title place x=240, y=10

# encrypt entry (message)
# encryption entry text color #71b2bd
# encryption entry text place x=10, y=50
# Encrypt entry  (label)
# encrypt entry  color #ffa500
# encrypt entry  place x=70, y=85

# output encrypted (message)
# output encrypted text color #71b2bd
# output encrypted text place x=10, y=130
# out put encrypted (label)
# output encrypted label color #ff6100
# output encrypted label place x=70, y=160

# encryption button
# encryption button color #936dbd
# encryption button place x=535, y=81

# status bar (bar)
# text on the bar color #480075
# bar x=3.0, rely=1, anchor='sw', relwidth=1
# bar color light blue

# browse (button)
# browse button color #1aff00
# browse button place x=600, y=155

# run app
root.mainloop()
