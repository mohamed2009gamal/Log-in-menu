# libraries
import tkinter as tk
import statistics
from tkinter import Tk, PhotoImage, Label, Entry, Button, filedialog, messagebox
from pytube import *
import threading
import unicodedata
from requests.packages import target
import subprocess
from subprocess import call

# application title
root = Tk()
root.title("youtube Downloader")
root.geometry("600x320")
root.resizable(False, False)

# app options---------------------------------------------------------------------------------------
root.config(bg="light blue")
root.iconbitmap(r"C:\Users\HP\pycharm\projects\video downloader\youtube_icon.ico")

# app Logo
logo_path = "youtube_logo.png"
try:
    logo = PhotoImage(file=logo_path)
    logo_label = Label(root, image=logo)
    logo_label.place(x=150, y=30)
finally:
    logo_label.config(bg='light blue')


# my functions---------------------------------------------------------------------------------------

#Back to main menu
def open_py_window():
    subprocess.Popen(["python", "main menu.py"])


goback_button = tk.Button(root, text="Main menu ", command=open_py_window, bg='#00e5ff')
goback_button.place(x=330, y=220)


def browse():
    folder = filedialog.askdirectory(title='Save Video At')
    if folder:
        folderlink.delete(0, 'end')
        folderlink.insert(0, folder)


def finish():
    messagebox.showinfo("Success", "Video downloaded successfully.")
    ytLink.focus()
    folderlink.focus()
    ytLink.focus_set()
    folderlink.focus_set()


def download_youtube_video():
    link = ytLink.get()
    folder = folderlink.get()
    yt = YouTube(link, on_complete_callback=finish)
    stream = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
    if stream:
        stream.download(folder)
        STATUS.config(text='Status: Downloading video...')
    else:
        messagebox.showerror("Error", 'Video not downloaded.')
    if folderLabel and youtube_link(not_filed):
        messagebox.showerror("Error", "please filed label")
        expect()
        ytLink.focus()
        folderlink.focus()
        ytLink.focus_set()
        folderlink.focus_set()
    STATUS.config(text='Status: Completed')

# YouTube Link
ytlabal = Label(root, text="Enter YouTube URL")
ytlabal.place(x=25, y=150)
ytlabal.config(bg='light blue')

ytLink = Entry(root, width=60)
ytLink.place(x=140, y=150)

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
download: Button = Button(root, text='Download video', command=download_youtube_video)
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
