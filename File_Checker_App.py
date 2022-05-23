import os
import os.path
from os.path import exists
from pathlib import Path
from tkinter import *
import tkinter.messagebox
import pickle

root = tkinter.Tk()
root.title("Hey Gabe! Here's your very own File Search TOOL!")

#Crecreate GUI
frame_tasks = tkinter.Frame(root)
frame_tasks.grid(row=0, column=0)

FirstQuestion = Label(root, text="What folder would you like to search in? Enter Path:")
FirstQuestion.grid(row=1, column=0)

FirstQuestion_response = tkinter.Entry(root, width=75)
FirstQuestion_response.grid(row=1, column=1)


root.mainloop()



