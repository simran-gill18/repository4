import os
from tkinter.filedialog import askdirectory

import pygame
from mutagen.id3 import ID3
from tkinter import *
 
root = Tk()
root.minsize(300,300)
 

 
listofsongs = []
songname = []

#v = StringVar() (no need mutagen)              # writes playing song's name after this, updatelabel(), songlabelpack.
#songlabel = Label(root,textvariable=v,width=35)
 
index = 0         # rule



def nextsong(event):          # button start next song after this and bind
    global index
    index += 1
    pygame.mixer.music.load(listofsongs[index])
    pygame.mixer.music.play()
    #updatelabel()

def prevsong(event):
    global index
    index -= 1
    pygame.mixer.music.load(listofsongs[index])
    pygame.mixer.music.play()
    #updatelabel()
 
def stopsong(event):
    pygame.mixer.music.stop()
    #v.set("")

#def updatelabel():           #no start without mutagen. says list index out of range.
    #global index
    #global songname
    #v.set(listofsongs[index])
    #return songname


def directorychooser():      # song starts when this written
 
    directory = askdirectory()
    os.chdir(directory)
 
    for files in os.listdir(directory):
        if files.endswith(".mp3"):
            
            listofsongs.append(files)

    pygame.mixer.init()
    pygame.mixer.music.load(listofsongs[0])
    pygame.mixer.music.play()


directorychooser() 

    
label = Label(root,text='Music Player')     # words
label.pack()
 
listbox = Listbox(root)                # painting
listbox.pack()

listofsongs.reverse()         # changes names from a to z.

for items in listofsongs:           # song names are written in box. they are written from z to a.
    listbox.insert(0,items)

listofsongs.reverse()



nextbutton = Button(root,text = 'Next Song')      # buttons appear. can be pressed. no stop song or start next.
nextbutton.pack()
 
previousbutton = Button(root,text = 'Previous Song')
previousbutton.pack()
 
stopbutton = Button(root,text='Stop Music')
stopbutton.pack()


nextbutton.bind("<Button-1>",nextsong)          # 1 and leftclick are same
previousbutton.bind("<Button-1>",prevsong)
stopbutton.bind("<Button-1>",stopsong)

#songlabel.pack()

 
 
root.mainloop()
