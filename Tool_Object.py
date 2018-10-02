""" Creates the "Tool" Object """

import csv

toolist = 'tools.csv'

class Tool():
    def __init__(self, tool_name, presence):
        self.tool_name = tool_name
        self.presence = presence

    def import_tools(toolist):
        """ import csv tool file into an array
            tools = {tool_name : quantity}"""
        tools = []
        with open(toolist, 'r') as csv_file:
            csv_reader = csv.reader(csv_file)

            #imports and formats into [quantity, name]
            for tool in csv_reader:
                print( tool )

    def get_tool_name(self, index):
        return self.tool_name


    def get_presence(self):
        return self.tool_name

