"""Creates a GUI to check-in/out tools"""

import Tkinter as tk

root = tk.Tk()
frame = tk.Frame(root)
frame.pack()

button = tk.Button(frame, text="hello", fq="red", command=quit)
button.pack(side=tk.LEFT)

slogan = tk.Button(frame, text = "hurro", command=write_slogan)
slogan.pack(side=tk.LEFT)

root.mainloop()

