# libraries
import tkinter as tk
from pytube import YouTube
from subprocess import call
import subprocess
import sys
from requests.packages import target
import os
from tkinter import Tk, PhotoImage, Label, Entry, Button, filedialog, messagebox
from tkinter.font import Font


# Initialize the main window
root = tk.Tk('#480075')
root.title("Main menu")
root.geometry("600x320")  # Set the size of the window
root.resizable(False, False)
root.configure(bg='#b8bde9')  # Set background color
root.iconbitmap(r"C:\Users\HP\pycharm\projects\video downloader\main menu_icon.ico")

#=======================================================================================================================
# Function to open the FaceBook downloader script
def open_py_win():
    subprocess.Popen(["python", "FaceBook downloader.py"])

# Function to open the FaceBook
tk.Label(root, text="FaceBook video downloader ----> ", font=('Helvetica', 15), bg='#b8bde9').place(x=7, y=20)
download_button = tk.Button(root, text='Download video now', command=open_py_win)
download_button.place(x=40, y=50)
download_button.config(bg='#00ff8c')


#=======================================================================================================================
# Function to open the YouTube downloader script
def open_py_win():
    subprocess.Popen(["python", "youtube downloader.py"])

# YouTube downloader
tk.Label(root, text="YouTube video downloader ----->", font=('Helvetica', 15), bg='#b8bde9').place(x=7, y=157)
download_button = tk.Button(root, text='Download video now', command=open_py_win)  # set command
download_button.place(x=40, y=187)
download_button.config(bg='#00ff8c')


#=======================================================================================================================
# Function to open the Instagram downloader script
def open_py_win():
    subprocess.Popen(["python", "Instagram downloader.py"])

# Instagram downloader
tk.Label(root, text="Instagram video downloader ---->", font=('Helvetica', 15), bg='#b8bde9').place(x=7, y=90)
download_button = tk.Button(root, text='Download video now', command=open_py_win)
download_button.place(x=40, y=119)
download_button.config(bg='#00ff8c')

#=======================================================================================================================
# Function to open the Twitter downloader script
def open_py_win():
    subprocess.Popen(["python", "twitter downloader.py"])

# Twitter downloader
tk.Label(root, text="Twitter video downloader ------->", font=('Helvetica', 15), bg='#b8bde9').place(x=7, y=220)
download_button = tk.Button(root, text='Download video now', command=open_py_win)
download_button.place(x=40, y=250)
download_button.config(bg='#00ff8c')
#=======================================================================================================================

# status bar
STATUS = Label(root, text="Created by Mohamed gamal", font=('calibre', 10, 'italic'), fg='#480075', anchor='w')
STATUS.place(x=3.0, rely=1, anchor='sw', relwidth=1)
STATUS.config(bg='light blue')

root.mainloop()
