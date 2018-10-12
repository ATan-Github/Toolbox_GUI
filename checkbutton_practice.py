# """ Learning how to do things """

# try:
    # # python 3.x
    # import Tkinter as tk

# except ImportError:mand to continue
    # #python 2.x
    # import Tkinter as tk
################################################
from Tkinter import *
import tkMessageBox
import Tkinter

top = Tkinter.Tk()
CheckVar1 = IntVar()
CheckVar2 = IntVar()
C1 = Checkbutton(top, text = "Music", variable = CheckVar1, \
                 onvalue = 1, offvalue = 0, height=3, \
                 width = 20, selectcolor="red", activeforeground="blue", \
                 image = '/Untitled/Users/Amanda1/gitRepos/Toolbox_GUI/flathead.jpg')
C2 = Checkbutton(top, text = "Video", variable = CheckVar2, \
                 onvalue = 1, offvalue = 0, height=3, \
                 width = 20) 
grid_rowconfigure(0, weight=1)
grid_columnconfigure(0, weight=1)
minsize(500, 500)

C1.pack()
C2.pack()
top.mainloop()













##################################################
# from Tkinter import *
# master = Tk()
# mb = Menubutton(master, text="CheckBox", relief=RAISED )
# mb.menu = Menu(mb, tearoff = 4)
# mb["menu"] = mb.menu

# Item0 = IntVar()
# Item1= IntVar()

# mb.menu.add_checkbutton(label="Item0" , variable=Item0)
# mb.menu.add_checkbutton(label="Item1", variable=Item1)

# mb.pack()
# master.mainloop()

#################################################
# tools = ["1", "2", "3" ]

# list_length = len(tools)
# presence = []
# for i in range(list_length):
    # presence.append(1)
# print(presence)
###################################################
# apple = ["mom", "dad", "poo"]
# f = open('test.txt', 'a')
# f.write('hello hello\n')
# f.writelines( "%s " % item for item in apple)
# f.close()
#####################################################
