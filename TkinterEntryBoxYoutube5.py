import sys
from tkinter import *
import tkinter as tk

#mGui is the box. Set up mGui
mGui = Tk()
mGui.geometry("450x450+500+300")
mGui.title("My Youtube Tkinter")
theEntry = StringVar()

# store mtext as directory function, 
def mhello():
  mtext = tk.filedialog.askdirectory()
  # mSrcResult = Entry(mGui, textvariable = mtext).pack()
  # self not defined: self.txt_srcname = tk.Entry(self.master, text = mtext ).pack()

  # prints directory to a label 
  mlabel2 = Label(mGui, text = mtext ).pack()
  return

#creates a label under title 
mlabel = Label(mGui, text= "The button will copy whatever directory you pick").pack()


# creates an entry field
mEntry = Entry(mGui, textvariable= theEntry).pack()
# creates a button that calls def mhello()
mbutton = Button(mGui, text="OK", command = mhello, fg="blue",bg="gray").pack()


'''
#mGui is the box. Set up mGui
mGui = Tk()
mGui.geometry("450x450+500+300")
mGui.title("My Youtube Tkinter")
theEntry = StringVar()

def mhello():
  mtext = theEntry.get()
  mlabel2 = Label(mGui,text=mtext).pack()
  return

#creates a label under title 
mlabel = Label(mGui, text= "The button will copy and print whatever you write in the entry field below").pack()


# creates an entry field
mEntry = Entry(mGui, textvariable= theEntry).pack()
# creates a button that calls def mhello()
mbutton = Button(mGui, text="OK", command = mhello, fg="blue",bg="gray").pack()
'''




