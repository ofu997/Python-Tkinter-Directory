import sys
from tkinter import *
import tkinter as tk
import os
import datetime
import shutil

#mGui is the box. Set up mGui
mGui = Tk()
w = 450
h = 500
ws = mGui.winfo_screenwidth()
hs = mGui.winfo_screenheight()
x=(ws/2) - (w/2)
y = (hs/2) - (h/2)
mGui.geometry("%dx%d+%d+%d" % (w,h,x,y))
w, h = mGui.winfo_screenwidth(), mGui.winfo_screenheight()
#mGui.geometry("%dx%d+0+0" % (w,h))
#mGui.geometry("450x450+500+300")
mGui.title("My Youtube Tkinter")
theEntry = StringVar()
mGui.configure(background="#ffffcc")
#TkinterEntryBoxYoutube5.center_window(self,500,300)

src=""
dst=""

# store mtext as directory function, 
def mhello():
  srcraw = tk.filedialog.askdirectory()
  global src
  src = srcraw.replace('\\','//')+"//"
  
  # won't add to entry field
  '''
  mSrcResult = Entry(mGui, textvariable = "").pack()
  mSrcResult.delete(0,END)
  mSrcResult.insert(0,mtext)
  '''
  # self not defined: self.txt_srcname = tk.Entry(self.master, text = mtext ).pack()

  # prints directory to a label
  mEntry = Entry(mGui)
  mEntry.configure(width=60)
  mEntry.pack()
  mEntry.delete(0,END)
  mEntry.insert(0,"Source folder:   "+srcraw)
  # mlabel2 = Label(mGui, text = mtext ).pack(expand=TRUE)
  # mlabel3 = Label(mGui, text = type(mtext)).pack()
  return src

def BrowseDest():
  dstraw = tk.filedialog.askdirectory()
  global dst
  dst = dstraw.replace('\\','//')+"//"
  dstEntry = Entry(mGui)
  dstEntry.configure(width=60)
  dstEntry.pack()
  dstEntry.delete(0,END)
  dstEntry.insert(0,"Destination folder:   "+dstraw)
  TransferButton = Button(mGui, text="Transfer", command = Transfer(src,dst), fg="blue",bg="#ccf2ff").pack(expand=TRUE)
  return dst

def Transfer(src,dst):

  x=-1
  listoffiles=[]
  
  #CopiedFile = Entry(mGui)
  #CopiedFile.pack(expand=True)


  #OldFile = Entry(mGui)
  #OldFile.pack(expand=True)
  #OldFile.delete(0, END)

  if (src!="" and dst!=""):
    
    myfiles = os.listdir(src)
    now = datetime.datetime.now()

    #OlderFiles = Label(mGui, text= "These documents are more than 24 hours old:").pack(side=LEFT)
    #CopiedFiles = Label(mGui, text= "These documents have been copied:").pack(side=RIGHT)
    listOld=Listbox(mGui)
    listOld.pack(fill=BOTH, expand=1)
    listOld.insert(END, "Files older than 24 hours:")


    listCopies=Listbox(mGui)
    listCopies.pack(fill=BOTH, expand=1)
    listCopies.insert(END, "Files copied to " + dst + " :")
    
    

    for file in myfiles:
      x=myfiles.index(file)
      y=str(x+1)

      osFunction = os.path.getmtime(src+file)
      ageInSeconds = datetime.datetime.fromtimestamp(osFunction)
      difference = now - ageInSeconds
      differenceSec = difference.total_seconds()

      if differenceSec > (24*60*60):

        listOld.insert(END, file)
        '''
        y=Entry(mGui)
        y.configure(width=15)
        y.pack(side=LEFT)
        y.insert(0, file)
        '''
    
        #x=x+1
        #listoffiles[x]=file+"textfield"
        # print( file + " is older than 24 hours.\n" )
        
        #fileEntryBox=Entry(mGui)
        #listoffiles[x].pack(expand=True)
        #listoffiles[x].insert(0, file + " is older than 24 hours\n")
      else:
        shutil.copy( src+file , dst )
        listCopies.insert(END, file)
        '''
        y=Entry(mGui)
        y.configure(width=15)
        y.pack(side=RIGHT)
        y.insert(0, file)
        '''
        #CopiedFile.insert(0, file + " has been copied to " + dst + " ~!*\n")

  
  
  # prints directory to a label
  #mlabelDst = Label(mGui, text = dst ).pack(expand=TRUE)
  # return

#creates a label under title 
mlabel = Label(mGui, text= "This tool will copy files modified or created within 24 hours").pack()


# creates an entry field
# not needed: mEntry = Entry(mGui, textvariable= theEntry).pack()
# creates a button that calls def mhello()
mbutton = Button(mGui, text="Pick source folder", command = mhello, fg="#007399",bg="#ccf2ff").pack(expand=TRUE)
# creates a button that finds dst folder
mDstButton = Button(mGui, text="Pick destination folder", command = BrowseDest, fg="#ccf2ff",bg="#007399").pack(expand=TRUE)





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




