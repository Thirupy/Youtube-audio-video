import os
import threading
from tkinter import *
from tkinter import messagebox
from pytube import YouTube

def audiodownload():
    url = entry.get()
    if not url:
        messagebox.showerror("Error", "Please enter a valid YouTube URL.")
        return

    entry.delete(0, END)
    download_thread = threading.Thread(target=ytaudio, args=(url,))
    download_thread.start()

def videodownload():
    url = entry.get()
    if not url:
        messagebox.showerror("Error", "Please enter a valid YouTube URL.")
        return

    entry.delete(0, END)
    download_thread = threading.Thread(target=ytvideo, args=(url,))
    download_thread.start()

def ytvideo(url):
    try:
        yt = YouTube(url)
        stream = yt.streams.get_highest_resolution()
        file_path = os.path.join(download_path.get(), yt.title + ".mp4")
        display1.config(text="Downloading video...")
        stream.download(download_path.get())
        display1.config(text=f"Video downloaded and saved in:\n{file_path}")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def ytaudio(url):
    try:
        yt = YouTube(url)
        audio = yt.streams.filter(only_audio=True).first()
        file_path = os.path.join(download_path.get(), yt.title + ".mp3")
        display1.config(text="Downloading audio...")
        audio.download(download_path.get())
        display1.config(text=f"Audio downloaded and saved in:\n{file_path}")
    except Exception as e:
        messagebox.showerror("Error", str(e))

root = Tk()
root.geometry("600x300")
root.config(bg="skyblue")
root.title("YouTube Downloader")

Label(root, text="Enter YouTube URL:").grid(row=0, column=0, padx=10, pady=10)

entry = Entry(root, width=70)
entry.grid(row=0, column=1, columnspan=2)

Label(root, text="Download Location:").grid(row=1, column=0, padx=10, pady=5)

download_path = StringVar()
download_path.set("Downloads")h
entry_path = Entry(root, textvariable=download_path, width=60)
entry_path.grid(row=1, column=1, columnspan=2)

videobutton = Button(root, text="Download Video", command=videodownload)
videobutton.grid(row=2, column=0, padx=10, pady=10)

audiobutton = Button(root, text="Download Audio", command=audiodownload)
audiobutton.grid(row=2, column=2, padx=10, pady=10)

display1 = Label(root, text="", fg="green")
display1.grid(row=3, column=0, columnspan=3, pady=20)

root.mainloop()
