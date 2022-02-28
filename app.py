# gui application using tkinter
from tkinter import Button, Entry, Label, Listbox, Scrollbar, StringVar, Tk
from tkinter.constants import RIGHT , BOTH, YES , DISABLED
from methods import getVideos, threading
from style import bg , font1 , font2 , bg2, fg

app = Tk()
app.geometry("500x500")
app.title("Downloader Application")
app.config(bg = bg)

lbl1 = Label(
    app,
    text = "Youtube Playlist Downloader",
    bg = bg,
    font = font1
)

lbl2 = Label(
    app,
    text = "Enter Playlist URL:",
    bg = bg,
    font = font2
)

url = StringVar()
playlistUrl = Entry(
    app,
    width = 60,
    textvariable = url
)

btn = Button(
    app,
    text = "Get Videos",
    bg = bg2,
    fg = fg,
    command = lambda: getVideos(videos , playlistUrl , download)
)

# Scrollbar and ListBox
scroll = Scrollbar(
    app
)

videos = Listbox(
    app,
    selectmode = "multiple"
)

download = Button(
    app,
    text = "Download Start",
    state = DISABLED,
    bg = bg2,
    fg = fg,
    command = lambda : threading(videos , download , btn)
)

lbl1.pack(pady = 12)
lbl2.pack(pady = 6)
playlistUrl.pack(pady = 6)
btn.pack(pady = 10)
scroll.pack(side = RIGHT, fill = BOTH)
videos.pack(expand = YES , fill = BOTH)


videos.config(
    yscrollcommand = scroll.set
)

scroll.config(
    command= videos.yview
)
download.pack(pady = 10)
app.mainloop()