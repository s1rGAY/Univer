import json


class Parser:
    def __init__(self, path='/home/siarhei/Programming/IIT/Univer/ППвИС/Computers_data'):
        self.data = None
        self.loc_path = path+'/data.json'
        with open(self.loc_path, 'r') as load_data:
            self.data = json.loads(load_data.read())

    def update_data(self):
        with open(self.loc_path, 'r') as load_data:
            self.data = json.loads(load_data.read())

    def get_data(self):
        return self.data
