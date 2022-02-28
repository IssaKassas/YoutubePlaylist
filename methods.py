# three methods getvideos threading download 

from tkinter import DISABLED, END, Button, Entry, Listbox , NORMAL
from tkinter.messagebox import showinfo
from pyyoutube import Api
from pytube import Playlist, YouTube
from threading import Thread
from style import apikey

def getVideos(list : Listbox , playlist: Entry , download: Button):
    global itemById
    
    list.delete(0 , END)
    
    api = Api(
        api_key = apikey
    )
    
    if "youtube" in playlist.get():
        link = playlist.get()
    
    else:
        print("this link was not youtube url")
        
    playlist_url = Playlist(link)
    
    itemById = api.get_playlist_items(
        playlist_id = playlist_url.playlist_id,
        count = None,
        return_json = True
    )
    
    for index , videoid in enumerate(itemById['items']):
        list.insert(
            END , f"{str(index + 1)}.{videoid['contentDetails']['videoId']}"
        )
        
    download.config(state = NORMAL)

def threading(list : Listbox , download : Button , btn : Button):
    # call download method to download videos function
    thread = Thread(
        target = downloadStart(list , download , btn)
    )
    thread.start()
    
    # try:
    #     thread.start()
    # except ThreadError:
    #     print("error")

def downloadStart(list : Listbox , download : Button , btn : Button):
    download.config(state = DISABLED)
    btn.config(state = DISABLED)
    
    # iterate all selected videos
    
    for i in list.curselection():
        videoid = itemById['items'][i]["contentDetails"]['videoId']
        
        link = f"https://www.youtube.com/watch?v={videoid}"
        
        youtubeObject = YouTube(link)
        
        filters = youtubeObject.streams.filter(
            progressive = True,
            file_extension = "mp4"
        )
        
        filters.get_highest_resolution().download()
    showinfo(
        "Success Downloading" ,
        "Video Successfully downloaded"
    )
    download.config(state = NORMAL)
    btn.config(state = NORMAL)
