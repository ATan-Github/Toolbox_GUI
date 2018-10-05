""" Creates a GUI to check-in/out tools. 3rd draft """
import datetime as dt
import csv
try:
    # python 3.x
    import Tkinter as tk

except ImportError:
    #python 2.x
    import Tkinter as tk


toolist = 'tools.csv'
# selected_employee = ""
toolz = []


class MainApplication(tk.Frame):
    """ Runs the GUI """
    # pylint: disable = too-many-ancestors, too-many-instance-attributes

    def __init__(self, master):
        """ MainApplication Constructor """
        tk.Frame.__init__(self, master)

        self.master = master
        self.configure_gui()
        self.create_widgets()
        self.create_menus()
        

    def configure_gui(self):
        """ configures gui settings """
        self.master.title("RMS Toolbox")
        
        self.master.resizable(width=True, height=True)

    def create_widgets(self):
        """ initializes widgets """
        tool_names = []
        tool_presence = []

        with open(toolist, 'r') as csv_file:
            csv_reader = csv.reader(csv_file)

            for tool in csv_reader:
                tool_names.append(tool)

        num_tools = len(tool_names)
        for i in range(num_tools):
            tool_presence.append(tk.IntVar())
        
        self.make_checkbuttons(tool_names, tool_presence)
        tk.Button(self, text="checkout", command=self.checkout).grid(row=40, column=40)
        # create quit app button
        tk.Button(self, text="Quit", command=self.quit_app).grid(row=400, column=100)

    def make_checkbuttons(self, tool_names, tool_presence):
        """ Creates checkbuttons for tools """
        num_buttons = len(tool_names)

        for i in range(num_buttons):
            tk.Checkbutton(self, text=tool_names[i], variable=tool_presence[i], command=lambda i=i:
                self.select_tools(tool_names[i], tool_presence[i])).grid(row=i+1, sticky=tk.W)

    def create_menus(self):
        """ creating dropdown menus """
        menu = tk.Menu(self.master)
        mb = tk.Menubutton(self, text="Employee Name")
        self.master.config(menu=menu)
        mb.submenu = tk.Menu(mb, tearoff=0)

        menu.add_cascade(label="Employee", menu=mb.submenu)

        employee_names = ["Panda", "Bob", "Pablo", "Mayo", "Porcupine"]
        employee_selected = []
        num_employees = len(employee_names)
        for i in range(num_employees):
            employee_selected.append(tk.IntVar())
        for n in range(num_employees):
            mb.submenu.add_checkbutton(label=employee_names[n], variable=employee_selected[n],
                    command=lambda n=n: self.select_employee(employee_names[n], employee_selected[n]))

    def select_employee(self, employee_name, result):
        """ selects the employee """
        if result.get() == 1:
            self.selected_employee = employee_name
        else:
            self.selected_employee = "No Employee Selected"

    def select_tools(self, selected_tool, result):
        """ shows selected tools """
        if result.get() == 1:
            toolz.append(selected_tool)
        else:
            toolz.append(0)

    def print_log(self):
        """ prints the checkout log """
        # print(self.selected_employee)
        # print(toolz)
        

        f = open('tool_log.txt', 'a')
        f.write(dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S\n'))
        f.write(self.selected_employee + " checked out: ")
        f.writelines("%s " % item for item in toolz)
        f.write("\n\n")
        f.close()

    def checkout(self):
        """ initiates actions when checkout button is pressed """
        self.print_log()
        self.quit_app()

    def quit_app(self):
        """ closes window """
        self.master.destroy()

def main():
    """ main function """
    #pylint:disable =
    root = tk.Tk()
    app = MainApplication(root)

    root.grid_rowconfigure(0, weight=1)
    root.grid_columnconfigure(0, weight=1)
    root.minsize(500, 500)

    app.pack(fill='both')
    
    app.mainloop()


if __name__ == "__main__":
    main()
