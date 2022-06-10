from Lab1.parser import Parser
from models.computer import Computer


class StateSynchronization:
    def __init__(self, logger, path='/home/siarhei/Programming/IIT/Univer/ППвИС/Computers_data'):
        self.parser = Parser(path)
        self.saved_state = self.parser.get_data()
        self.logger = logger

    def upload_state(self):
        if 'computer' in self.saved_state[0].keys():
            temp_pc = Computer(self.logger,
                               self.saved_state[0]['computer']['storage']['storage_size'],
                               self.saved_state[0]['computer']['computer_name'],
                               self.saved_state[0]['computer']['logged_user']['login'],
                               self.saved_state[0]['computer']['logged_user']['password'],
                               self.saved_state[0]['computer']['logged_user']['operation_system_type'])
            for i in self.saved_state[0]['computer']['users']:
                if i['login'] != self.saved_state[0]['computer']['logged_user']:
                    temp_pc.add_user(i['login'], i['password'], i['operation_system_type'])

            if self.saved_state[0]['computer']['comp_power_status'] is False:
                temp_pc.turn_computer_power_status()

        else:
            temp_pc = Computer(self.logger,
                               self.saved_state[0]['storage']['storage_size'],
                               self.saved_state[0]['computer_name'],
                               self.saved_state[0]['logged_user']['login'],
                               self.saved_state[0]['logged_user']['password'],
                               self.saved_state[0]['logged_user']['operation_system_type'])

            for i in self.saved_state[0]['users']:
                if i['login'] != self.saved_state[0]['logged_user']:
                    temp_pc.add_user(i['login'], i['password'], i['operation_system_type'])

            if self.saved_state[0]['comp_power_status'] is False:
                temp_pc.turn_computer_power_status()

        return temp_pc
