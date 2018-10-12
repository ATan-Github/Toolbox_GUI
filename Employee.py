""" Creates the "Employee" Object """
try:
    import Tkinter as tk
except ImportError:
    import Tkinter as tk

import csv

e_list = 'employees.csv'

class Employee():
    
    def __init__(self, employee_name, if_selected):
        self.employee_name = employee_name
        self.if_selected = if_selected

    def create_employees(self):
        with open(e_list, 'r') as csv_file:
            csv_reader = csv.reader(csv_file)

            for person in csv_reader:
                self.employee_name.append(person)
        
        num_employees = len(self.employee_name)
        for i in range(num_employees):
            self.if_selected.append(tk.IntVar())

        self.employees = [self.employee_name, self.if_selected]

        return self.employees

    def get_num_employees(self):
        num_employees = len(self.employee_name)
        return num_employees
