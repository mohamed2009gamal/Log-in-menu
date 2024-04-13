# libraries
import tkinter as tk
from pytube import *
import tkinter
from tkinter import Tk, PhotoImage, Label, Entry, Button, filedialog, messagebox
import threading
import unicodedata
from requests.packages import target
import subprocess
from subprocess import call
import sys

# application options
root = tk.Tk()
root.title("FaceBook Downloader")
root.geometry("600x320")
root.resizable(False, False)
root.config(bg="light blue")
root.iconbitmap(r"C:\Users\HP\pycharm\projects\video downloader\facebook_icon.ico")

# app Logo
logo_path = "facebook_logo.png"
try:
    logo = PhotoImage(file=logo_path)
    logo_label = Label(root, image=logo)
    logo_label.place(x=90, y=-10)
finally:
    logo_label.config(bg='light blue')


# my functions---------------------------------------------------------------------------------------

def browse():
    folder = filedialog.askdirectory(title='Save Video At')
    if folder:
        folderlink.delete(0, 'end')
        folderlink.insert(0, folder)


def download_FaceBook_video():
    link = fbLink.get()
    folder = folderlink.get()

    if not link:
        messagebox.showerror("Error", "Please enter a FaceBook URL.")
        return

    try:
        yt = YouTube(link)
    except Exception as e:
        messagebox.showerror("Error", "Invalid FaceBook URL.")
        return

    if folder:
        stream = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
        if stream:
            try:
                stream.download(folder)
                STATUS.config(text='Status: Downloading video...')
            except exceptions.VideoUnavailable:
                messagebox.showerror("Error", "Video not available for download.")
        else:
            messagebox.showerror("Error", 'Video not downloaded.')
    else:
        messagebox.showerror("Error", "Please select a folder to save the video.")

    STATUS.config(text='Status: Completed')


#Back to main menu
def open_py_window():
    subprocess.Popen(["python", "main menu.py"])

goback_button = tk.Button(root, text="Main menu ", command=open_py_window, bg='#00e5ff')
goback_button.place(x=330, y=220)

# FaceBook Link
fblabal = tk.Label(root, text="Enter FaceBook URL")
fblabal.place(x=25, y=150)
fblabal.config(bg='light blue')
fbLink = tk.Entry(root, width=60)
fbLink.place(x=140, y=150)

# Download folder
folderLabel = Label(root, text='Folder link')
folderLabel.place(x=25, y=183)
folderLabel.config(bg='light blue')
folderlink = Entry(root, width=50)
folderlink.place(x=140, y=183)

# Browse Button
browseButton = Button(root, text='Browse', command=browse)
browseButton.place(x=455, y=180)
browseButton.config(bg='#1aff00')

# Download Button
download: Button = Button(root, text='Download video', command=download_FaceBook_video)
download.place(x=180, y=220)
download.config(bg='#1aff00')

# status bar
STATUS = Label(root, text="Status: Ready", font=('calibre', 10, 'italic'), fg='black', anchor='w')
STATUS.place(x=3.5, rely=1, anchor='sw', relwidth=1)
STATUS.config(bg='light blue')

# comments
#----------------------------------------------------------------
#  change app wallpaper and be like motion wallpaper
#  --------------------------------------------------------------
#  it's done with mohamed
#  at 10 March 2024
#  mohamed was 15 years old
#----------------------------------------------------------------
root.mainloop()