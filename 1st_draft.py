"""Creates a GUI to check-in/out tools"""

try:
    # python 3.x
    import Tkinter as tk
    # from tkinter import ttk

except ImportError:
    # python 2.x
    import Tkinter as tk

toolz = []

class MainApplication(tk.Frame):

    """ master app """
    # pylint: disable = too-many-ancestors, too-many-instance-attributes

    def __init__(self, master):
        tk.Frame.__init__(self, master)

        self.master = master
        self.configure_gui()
        self.create_widgets()
        self.create_menus()

    def configure_gui(self):
        """ configure gui settings """
        self.master.title("RMS Toolbox")
        # self.master.geometry("280x800")
        self.master.resizable(width=True, height=True)

    def create_widgets(self):
        """ initalizes widgets """
        tools = ["Tool 1", "Tool 2", "Tool 3", "Tool 4"]
        # print( tools )
        
        var1 = tk.IntVar()
        var2 = tk.IntVar()
        var3 = tk.IntVar()
        tk.Checkbutton(self, text=tools[0], variable=var1, command=lambda:
                self.select_tools(var1, tools[0])).grid(row=1, sticky=tk.W)
        tk.Checkbutton(self, text=tools[1], variable=var2, command=lambda:
                self.select_tools(var2, tools[1])).grid(row=2, sticky=tk.W)
        tk.Checkbutton(self, text=tools[2], variable=var3, command=lambda:
                self.select_tools(var3, tools[2])).grid(row=3, sticky=tk.W)


        tk.Button(self, text="checkout", command=self.checkout).grid(row=4, column=0)
        # create quit app button
        tk.Button(self, text='Quit', command=self.quit_app).grid(row=400, column=100)

    # def tool_log(self, tool):
        # """ prints a log of tools taken out """
        # print(tool)

    def create_menus(self):
        """ creating dropdown menus """
        menu = tk.Menu(self.master)
        # submenu = tk.Menu(menu)
        mb = tk.Menubutton(self, text="Employee Name")
        self.master.config(menu=menu)
        mb.submenu = tk.Menu(mb, tearoff=0)

        var9 = tk.IntVar()
        var10= tk.IntVar()
        menu.add_cascade(label="Employee", menu=mb.submenu)
        # submenu.add_cascade(label="poke", command=lambda: self.tool_log("rawr"))
        mb.submenu.add_checkbutton(label="Laura", variable=var9, command=lambda:
                self.select_employee(var9, "Laura"))
        mb.submenu.add_checkbutton(label="Monte", variable=var10, command=lambda:
                self.select_employee(var10, "Monte"))

    def select_employee(self, result, employee_name):
        """ Selects the employee """
        self.selected_employee = "blank"
        if result.get() == 1:
            self.selected_employee = employee_name
        else: 
            self.selected_employee = "No Employee Selected" 

    def select_tools(self, result,  selected_tool):
        """ shows selected tools """
        if result.get() == 1:
            toolz.append(selected_tool)
        else:
            toolz.append(0)
        # toolz.append(self.var1.get())
        # toolz.append(self.var2.get())

    def print_log(self):
        """ prints the checkout log """
        print(self.selected_employee)
        print(toolz)

    def checkout(self):
        self.print_log()
        self.quit_app()

    def quit_app(self):
        """ closes screen """
        self.master.destroy()

   
def main():  
    """ main function """
     # pylint: disable =
    root = tk.Tk()
    app = MainApplication(root)

    root.grid_rowconfigure(0, weight=1)
    root.grid_columnconfigure(0, weight=1)
    root.minsize(500, 500)

    app.pack(fill='both')

    app.mainloop()


if __name__ == "__main__":
    main()
    
        # tk.Button(self, text=tools[0], command=lambda: self.tool_log(tools[0])).grid(row=100, column=0)
        # tk.Button(self, text=tools[1], command=lambda: self.tool_log(tools[1])).grid(row=100, column=100)
        # tk.Button(self, text=tools[2], command=lambda: self.tool_log(tools[2])).grid(row=200, column=0)
        # tk.Button(self, text=tools[3], command=lambda: self.tool_log(tools[3])).grid(row=200, column=100)

