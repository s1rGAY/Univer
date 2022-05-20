#Neet to rebuild for MVC

from parser import Parser
from computer import Computer

class StateSynchronization:
    def __init__(self,path):
        self.parser = Parser(path)
        self.saved_state = self.parser.get_data()

    def upload_state(self):
        
        temp_pc = Computer(self.saved_state[0]['storage']['storage_size'],
        self.saved_state[0]['computer_name'],self.saved_state[0]['logged_user']['login'],
        self.saved_state[0]['logged_user']['password'],self.saved_state[0]['logged_user']['operation_system_type'])
        
        if self.saved_state[0]['comp_power_status']==False:
            temp_pc.turn_computer_power_status()
        
        for i in self.saved_state[0]['users']:
            if i['login']!=self.saved_state[0]['logged_user']:
                temp_pc.add_user(i['login'],i['password'],i['operation_system_type'])

        return temp_pc