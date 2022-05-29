from model.computer import Computer

class ModelComponent():
    def __init__(self):
        self.computer = None

    def add_computer(self,storage_size,name,user,password,system_type):
        self.computer = Computer(storage_size,name,user,password,system_type)

    def comp_action(self):
        pass