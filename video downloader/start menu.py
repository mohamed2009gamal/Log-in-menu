# libraries
import tkinter as tk
from tkinter import Tk, PhotoImage, Label, Entry, Button, filedialog, messagebox
import sys
import time
from subprocess import call
import subprocess
import os

# Initialize the main window
root = tk.Tk()
root.title("Start menu")
root.geometry("500x500")
root.resizable(False, False)
root.configure(bg='#4b99ff')
root.iconbitmap(r"C:\Users\HP\pycharm\projects\video downloader\Start menu.ico")

logo_path = 'Start menu_logo.png'
logo_label = None

try:
    current_dir = os.path.dirname(os.path.realpath(__file__))
    logo_path = os.path.join(current_dir, logo_path)
    logo = PhotoImage(file=logo_path)
    logo_label = Label(root, image=logo)
    logo_label.place(x=10, y=150)
finally:
    if logo_label is not None:
        logo_label.config(bg='#4b99ff')

# Functions

def open_py_window():
    subprocess.Popen(["python", "main menu.py"])

# Function to control age
def agecontrol():
    try:
        age = int(age_entry.get())
        if age < 12:
            messagebox.showerror("Error", "You are too young to use this program.")
            root.destroy()
        elif age > 80:
            messagebox.showerror("Error", "You are too old to use this program.")
            root.destroy()
        else:
            messagebox.showinfo("Age control", "True, fild your username to continue")
    except ValueError:
        messagebox.showerror("Error", "Please enter your age.")
        age_entry.focus()

def label(fild=None):
    try:
        age.label = int(age_entry.get())
        username.label = str(username.entry.get())
    except ValueError:
        messagebox.showerror("Error", "Sorry, labels can't be empty!.")
        age_entry.focus()
    if lables is not fild:
        messagebox.showerror("Error", "Sorry, labels can't be empty!.")
        age_entry.focus()

# Age control button
control_button = tk.Button(root, text=" Control", command=agecontrol, bg='#995aec')
control_button.place(x=360, y=37)

# Age ask label
age_label = tk.Label(root, text="How old are you?", font=('Helvetica', 15), bg='#4b99ff')
age_label.place(x=50, y=5)

# Age note label
age_label = tk.Label(root, text="note : at least 12", font=('Helvetica', 15), bg='#4b99ff')
age_label.place(x=310, y=5)

# Age entry label
age_entry = tk.Entry(root, width=10, bg='#ffa500')
age_entry.place(x=87, y=37)
age_entry.focus()

# Username
username_label = tk.Label(root, text="Username", font=('Helvetica', 15), bg='#4b99ff')
username_label.place(x=10, y=75)

# Username entry label
username_entry = tk.Entry(root, width=60, bg='#ffa500')
username_entry.place(x=120, y=80)
username_entry.focus()

# Username check button
def check_username():
    username_str = username_entry.get()
    if not username_str:
        messagebox.showerror("Error", "Username can't be empty!.")
    else:
        messagebox.showinfo('Welcome', f'Hello, {username_str}!')

# Check username button
check_username_button = tk.Button(root, text="Check Username", command=check_username, bg='light green')
check_username_button.place(x=65, y=115)

# start button
start_button = tk.Button(root, text="Start and go main menu", command=open_py_window, bg='light green')
start_button.place(x=300, y=115)

root.mainloop()