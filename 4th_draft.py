""" Creates a GUI to check-in/out tools. 4th draft """
import Tool_Object as Tl
import Employee as Emp
import datetime as dt
try:
    import tkinter as tk
except ImportError:
    import Tkinter as tk
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
        
    def configure_gui(self):
        """ configures gui settings """
        self.master.title("RMS Toolbox")
        
        self.master.resizable(width=True, height=True)

    def create_widgets(self):
        """ initializes widgets """
        tool_names = []
        tool_presence = []
        # toolbox = Tl.Tool(tool_names, tool_presence)
        toolbox = Tl.Tool.create_toolbox(Tl.Tool(tool_names, tool_presence))    
        self.make_checkbuttons(toolbox)
        tk.Button(self, text="checkout", command=self.checkout).grid(row=40, column=40)
        # create quit app button
        tk.Button(self, text="Quit", command=self.quit_app).grid(row=400, column=100)
         

        #create_menus ...... previously def create_menus(self):
        menu = tk.Menu(self.master)
        mb = tk.Menubutton(self, text="Employee Name")
        self.master.config(menu=menu)
        mb.submenu = tk.Menu(mb, tearoff=0)

        menu.add_cascade(label="Employee", menu=mb.submenu)

        employee_names = []
        employee_selected = []

        self.employees = Emp.Employee.create_employees(Emp.Employee(employee_names, employee_selected))
        for n in range(len(self.employees[0])):
            mb.submenu.add_checkbutton(label=self.employees[0][n], variable=self.employees[1][n])

    def make_checkbuttons(self, toolbox):
        """ Creates checkbuttons for tools """
        num_buttons = len(toolbox[0])

        for i in range(num_buttons):
            tk.Checkbutton(self, text=toolbox[0][i], bg="#66CDAA", selectcolor="#D49F9F", indicatoron=0, variable=toolbox[1][i], command=lambda i=i:
                self.select_tools(toolbox[0][i], toolbox[1][i])).grid(row=i+1, sticky=tk.W)

    # def select_employee(self, employee_name, result):
        # """ selects the employee """
        # if result.get() == 1:
            # self.selected_employee = employee_name
        # else:
            # self.selected_employee = "No Employee Selected"

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
        f.write("%s checked out: " % self.selected_employee)
        f.writelines("%s " % item for item in toolz)
        f.write("\n\n")
        f.close()

    def checkout(self):
        """ initiates actions when checkout button is pressed """
        num_selected = 0
        index = 99
        for i in range(len(self.employees[0])):
            if self.employees[1][i].get() == 1:
                num_selected += 1
                index = i
        if num_selected > 1:
            print("No more than one employee can check out the same tool.")
        elif num_selected < 1:
            print("No employee selected.")
        else:
            self.selected_employee = self.employees[0][index]
            self.print_log()
            self.quit_app()
        
        # self.print_log()
        # self.quit_app()

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
