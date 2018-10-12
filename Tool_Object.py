""" Creates the "Tool" Object """
try:
    import Tkinter as tk
except ImportError:
    import Tkinter as tk

import csv

toolist = 'tools.csv'

class Tool():
    
    def __init__(self, tool_names, tool_presence):
        self.tool_names = tool_names
        self.tool_presence = tool_presence

    def create_toolbox(self):
        with open(toolist, 'r') as csv_file:
            csv_reader = csv.reader(csv_file)

            for tool in csv_reader:
                self.tool_names.append(tool)
        
        num_tools = len(self.tool_names)
        for i in range(num_tools):
            self.tool_presence.append(tk.IntVar())

        self.toolbox = [self.tool_names, self.tool_presence]

        return self.toolbox

    def get_tool_name(index, tool_names):
        name = tool_names[index]
        return name

    def get_tool_presence(index, tool_presence):
        presence = tool_presence[index]
        return presence

























# class Tool():
    # def __init__(self, tool_name, presence):
        # self.tool_name = tool_name
        # self.presence = presence

    # def get_tool_name(self, index):
        # return self.tool_name


    # def get_presence(self):
        # return self.tool_name

# def import_tools(toolist):
    # """ import csv tool file into an array
        # tools = {tool_name : quantity}"""
    # tools = []
    # with open(toolist, 'r') as csv_file:
        # csv_reader = csv.reader(csv_file)

        # #imports and formats into [quantity, name]
        # for tool in csv_reader:
            # tools.append(tool)
            # print( tool )
        # print tools

    # return tools


# def main():
    # """ main function """
    # tools = import_tools(toolist)

if __name__ == "__main__":
    main()
