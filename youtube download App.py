from tkinter import *
from pytube import YouTube
root=Tk()
root.geometry("600x300")
root.config(bg="skyblue")
path="C:\pspp\song"
entry=Entry(root,width=100)
entry.grid(row=0,column=0,columnspan=3)
videobutton=Button(root,text="Download video",command=lambda:videodownload())
videobutton.grid(row=1,column=0)
audiobutton=Button(root,text="Download audio",command=lambda:audiodownload())
audiobutton.grid(row=1,column=2)
def audiodownload():
    current1=entry.get()
    if (current1==""):
        none1=Label(root,text="please Enter URL & then click Download")
        none1.grid()
        root.after(10000,none1.grid_remove)
    else:
        entry.delete(0,END)
        ytaudio(str(current1))
def videodownload():
    current=entry.get()
    if (current==""):
        none=Label(root,text="please Enter URL & then click Download")
        none.grid()
        root.after(10000,none.grid_remove)
    else:
        entry.delete(0,END)
        ytvideo(str(current))
def ytvideo(a):
    video_url =a
    display1=Label(root,text="please wait, your video is downloading...")
    display1.grid()
    yt = YouTube(video_url)
    stream = yt.streams.get_highest_resolution()
    stream.download(path)
    display2=Label(root,text=(" video is Downloded & saved in ",path))
    display2.grid()
    root.after(10000,display1.grid_remove)
    root.after(10000,display2.grid_remove)
def ytaudio(b):
    video_url =b
    display3=Label(root,text="please wait, your audio is downloading...")
    display3.grid()
    yt = YouTube(video_url)
    audio = yt.streams.filter(only_audio=True).first()
    audio.download(path)
    display4=Label(root,text=(" audio is Downloded & saved in ",path))
    display4.grid()
    root.after(10000,display3.grid_remove)
    root.after(10000,display4.grid_remove)
root.mainloop()