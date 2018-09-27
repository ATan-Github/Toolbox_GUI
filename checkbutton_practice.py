""" Learning how to use checkbuttons """

from Tkinter import *
master = Tk()
mb = Menubutton(master, text="CheckBox", relief=RAISED )
mb.menu = Menu(mb, tearoff = 4)
mb["menu"] = mb.menu

Item0 = IntVar()
Item1= IntVar()

mb.menu.add_checkbutton(label="Item0" , variable=Item0)
mb.menu.add_checkbutton(label="Item1", variable=Item1)

mb.pack()
master.mainloop()
