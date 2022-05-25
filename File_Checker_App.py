import os
import os.path
from pathlib import Path
from tkinter import *
import tkinter.messagebox
import pickle
from os.path import exists
import subprocess

root = tkinter.Tk()
root.title("Hey Gabe! Here's your very own File Search TOOL!")

#Crecreate GUI
frame_tasks = tkinter.Frame(root)
frame_tasks.grid(row=0, column=0)

FirstQuestion = Label(root, text="What file would you like to search for? Enter Full Name:    ")
FirstQuestion.grid(row=1, column=0)

Folder_Name = tkinter.Entry(root, width=50,)
Folder_Name.grid(row=1, column=1)

def Search_Click():
    UserInput = Folder_Name.get()
    isExist = os.path.exists (r'C:\Users\ggarc\OneDrive\Documents' + "/" + UserInput)

    if isExist is True:
        FoundIT = Label(root, text = "Found IT! The file you are looking for is here")
        FoundIT.grid(row=2)
        #def callback():
            #subprocess.Popen(r'explorer /select,"C:\Users\ggarc\OneDrive\Documents" + "/" + UserInput))
        ListDirectory = Label(root, text = os.path.abspath(r'C:\Users\ggarc\OneDrive\Documents' + "/" + UserInput), fg="RED")
        ListDirectory.grid(row=4)
        #ListDirectory.bind(("<Button-1>", lambda e: callback(r'C:\Users\ggarc\OneDrive\Documents' + "/" + UserInput)))

    else:
       Nope = Label(root, text = "No luck, the file is not in this folder")
       Nope.grid(row=2)

BlankSpace = Label(root, text="      ")
BlankSpace.grid (row=1, column=2)

SearchButton = Button(root, text=" Search ", command= Search_Click)
SearchButton.grid(row=1, column=3)


root.mainloop()
