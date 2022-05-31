from utility.config import config

from abstractions.logger import AbstractLogger
from abstractions.observable import Observable
from abstractions.observer import Observer

from Lab1.operation_system import Operation_system
from Lab1.storage import Storage
from Lab1.user import User
from Lab1.keyboard import Keyboard


class Computer(Observable):
    def __init__(self, logger: AbstractLogger, storage_size=10,
                 computer_name='DFS', first_user_login='S',
                 first_user_password='1', first_user_systme_type='linux',
                 ):  # мб добавить передачу имён операц

        self.__logger: AbstractLogger = logger  # ДОЛЖНО ОСТАТЬСЯ В КОМПЕ
        self.__observers = []  # ДОЛЖНО ОСТАТЬСЯ В КОМПЕ

        self.operation_systems = [Operation_system('linux'),
                                  Operation_system('macosx'),
                                  Operation_system('windows')]

        self.computer_name = computer_name
        self.users = [User(first_user_login, first_user_password,
                           first_user_systme_type)]

        self.storage = Storage(storage_size, self.computer_name,
                               self.operation_systems, self.users)
        self.keyboard = Keyboard()

        self.comp_power_status = True
        self.logged_user = self.users[0]

    def get_logged_user(self):
        return self.logged_user

    def get_computer_name(self):
        return self.computer_name

    def get_power_status(self):
        return self.comp_power_status

    def turn_computer_power_status(self, login=None, password=None):
        if self.get_power_status() == True:
            self.comp_power_status = False
        else:
            self.comp_power_status = True
            print('\nYou turned on computer\n')
            print('\nYou should login to the system\n')
            self.__login(login, password)

    def __login(self, user_login, user_password):
        if self.get_power_status():
            access_info = self.__check_access_rights(user_login, user_password)
            if access_info[0] is not False:
                self.logged_user = access_info[1]

    def __check_access_rights(self, login, password):
        for i in self.users:
            if i.get_login() == login:
                if i._get_password() == password:
                    return (True, i)
        return (False)

    def change_logged_user(self, user_login, user_password):
        self.__login(user_login, user_password)

    def add_user(self, user_login, user_password, user_systme_type):
        if self.get_power_status():
            #print('\n ADDING A NEW USER \nEnter info in order:\n Login \n Password \n System_type')
            self.users.append(User(user_login, user_password, user_systme_type))
            self.storage._add_new_user_directory(self.users[-1])
        else:
            print('\nComputer status - OFF\n')

    def del_user(self, user_login, user_password):
        if self.get_power_status():
            permission_data = self.__check_access_rights(user_login, user_password)
            if permission_data[0]:
                self.storage._delete_user(permission_data[1])
                self.users.remove(permission_data[1])

    def free_user_memory(self):
        return self.storage.get_free_user_storage_size()

    def enter_command(self, command):
        command = list(command[0].split(' '))
        if self.get_power_status():
            numb_of_op_system = None
            for i in range(len(self.operation_systems)):
                if self.operation_systems[i]._get_system_type() == self.logged_user.get_operation_system_type():
                    numb_of_op_system = i
                    break
            if self.operation_systems[numb_of_op_system]._get_command(command[0]):
                path = ('/home/siarhei/Programming/IIT/Univer/ППвИС/Computers_data/'
                +str(self.computer_name)+'/'+str(self.logged_user.get_operation_system_type())
                +'/User_storage/'+str(self.logged_user.get_login()))
                self.operation_systems[numb_of_op_system]._run_command(command[0], path, command[1])

    # осталось от прошлого владельца
    def subscribe(self, observer: Observer) -> None:
        self.__observers.append(observer)

    def unsubscribe(self, observer: Observer) -> None:
        self.__observers.remove(observer)

    def notify(self) -> None:
        for item in self.__observers:
            item.handle(self, self.__logger)

    def get_report_on_car(self) -> None:
        self.__logger.disable_logging()

        '''if self.engine_is_running:
            print('For current moment car engine is running')
        else:
            print('For current moment car engine is not running')

        print(f'Actual speed is  {self.__get_driving_display__.actual_speed}')
        print(f'Actual consumption {self.__get_driving_display__.actual_consumption}')
        print(f'Actual fill level is {self.__get_fuel_tank_display__.fill_level}')'''

        # хуйнюшка для репорта
        self.__logger.enable_logging()
