import tkinter as tk 
import tkinter.scrolledtext as st
from tkinter import filedialog
import main as yd

root = tk.Tk()
root.title("Youtube Video Downloader")


tk.Label(root, text = 'Youtube Downloder', font=("Times New Roman", 12),
        background='green', foreground="white").grid(column=1, row= 0)
tk.Label(root, text = 'Playlist link girin: ', font=("Times New Roman", 12)).grid(column=0, row= 1)

entry1 = tk.Entry(root)
entry1.grid(column=1, row=1)

text_area = st.ScrolledText(root, width=50, height=8, font=("Times New Roman", 12)).grid(column=1, pady=10, padx=10)

def get_playlist_mp3():
    playlist = entry1.get()
    folder_path = filedialog.askdirectory()
    yd.get_playlist_mp3(playlist, folder_path)


button3 = tk.Button(root, text="Mp3 playlist downloader ", command = get_playlist_mp3)
button3.grid(sticky= "nsew")

root.mainloop()