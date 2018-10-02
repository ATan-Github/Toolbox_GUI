# """ Learning how to use checkbuttons """

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
apple = ["mom", "dad", "poo"]
f = open('test.txt', 'a')
f.write('hello hello\n')
f.writelines( "%s " % item for item in apple)
f.close()
