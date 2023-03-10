from pytube import Playlist, YouTube
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox as mb


root = Tk()
root.title("Youtube Downloader")
root.geometry("250x200")

root.grid_rowconfigure(index=0, weight=1)
root.grid_columnconfigure(index=0, weight=1)
root.grid_columnconfigure(index=1, weight=1)
 
text_editor = Text()
text_editor.grid(column=0, columnspan=2, row=0)

choices = ['144p', '240p', '360p', '720p', '1080p','1440p','2160p']
variable = StringVar(root)
variable.set('720p')

quality_option = OptionMenu(root, variable, *choices)

 
# открываем файл в текстовое поле
def open_directory():
    text = text_editor.get("1.0", END)
    if text != '\n':
        DIRECTORY = filedialog.askdirectory()
        if DIRECTORY:
            text = text_editor.get("1.0", END)
            case = text.split('/')[-1].split('?')[0]
            try:
                quality = variable.get()
                if case == 'playlist':
                    p = Playlist(text)
                    for video in p.videos:
                        video.streams.filter(res=quality).first().download(DIRECTORY)
                else:
                    yt = YouTube(text)
                    yt.streams.filter(res=quality).first().download(DIRECTORY)
            except Exception as e:
                mb.showerror(
                    "Ошибка", 
                    e)
    else:
        mb.showerror(
            "Ошибка", 
            "Введите ссылку на видео или плейлист в YouTube")


open_button = ttk.Button(text="Скачать", command=open_directory)
open_button.grid(column=0, row=1, sticky=NSEW, padx=10)
quality_option.grid(column=1, row=1)

 
root.mainloop()

