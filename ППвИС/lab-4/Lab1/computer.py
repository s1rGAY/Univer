from operation_system import Operation_system
from storage import Storage
from user import User
from keyboard import Keyboard

class Computer:
    def __init__(self, storage_size, computer_name, 
    first_user_login, first_user_password, first_user_systme_type): #мб добавить передачу имён операционок
        
        self.operation_systems = [Operation_system('linux'), 
                                Operation_system('macosx'), 
                                Operation_system('windows')]

        self.computer_name = computer_name
        self.users = [User(first_user_login,first_user_password,first_user_systme_type)]
        
        self.storage = Storage(storage_size, self.computer_name, self.operation_systems, self.users)     
        self.keyboard = Keyboard()

        self.comp_power_status = True
        self.logged_user = self.users[0]
    

    def get_computer_name(self):
        return self.computer_name

    def get_power_status(self):
        return self.comp_power_status

    def turn_computer_power_status(self):
        if self.get_power_status() == True:
            print('\nYou turned off computer\n')
            self.comp_power_status = False
        else:
            self.comp_power_status = True
            print('\nYou turned on computer\n')
            print('\nYou should login to the system\n')
            self.__login()


    def __login(self):
        if self.get_power_status():
            access_info = self.__check_access_rights()
            if access_info[0] != False:
                self.logged_user = access_info[1]
        else:
            print('\nComputer status - OFF\n')
                
    def __check_access_rights(self):
        for j in range(3):
            print('Enter Login :')
            login = input()
            for i in self.users:
                if i.get_login() == login:
                    for a in range(3):
                        print('Enter password :')
                        password = input()
                        if i._get_password() == password:
                            return (True, i)
                        else:
                            print('Invalid password! Attemps ramained : '+str(a))
                elif i == self.users[-1]:
                    print('Access denied!')
                    return (False, None)
            print('Invalid login! Attemps ramained :'+str(j))


    def change_logged_user(self):
        self.__login()


    def add_user(self, user_login, user_password, user_systme_type):
        if self.get_power_status():
            #print('\n ADDING A NEW USER \nEnter info in order:\n Login \n Password \n System_type')
            self.users.append(User(user_login, user_password, user_systme_type))
            self.storage._add_new_user_directory(self.users[-1])
        else:
            print('\nComputer status - OFF\n')

    def del_user(self):
        if self.get_power_status():
            print('\n DELETING A USER \nTo remove user you must know it\'s login and password.')
            permission_data = self.__check_access_rights()
            if permission_data[0] == True:
                self.storage._delete_user(permission_data[1])
                self.users.remove(permission_data[1])
        else:
            print('Computer status - OFF')

    def free_user_memory(self):
        return self.storage.get_free_user_storage_size()

    def enter_command(self):
        if self.get_power_status():    
            command = self.keyboard.typing()

            numb_of_op_system = None
            for i in range(len(self.operation_systems)):
                if self.operation_systems[i]._get_system_type() == self.logged_user.get_operation_system_type():
                    numb_of_op_system = i
                    break
            if self.operation_systems[numb_of_op_system]._get_command(command)!=False:
                path = ('/home/siarhei/Programming/IIT/Univer/ППвИС/Computers_data/'
                +str(self.computer_name)+'/'+str(self.logged_user.get_operation_system_type())
                +'/User_storage/'+str(self.logged_user.get_login()))
                self.operation_systems[numb_of_op_system]._run_command(command, path)
        else:
            print('Computer status - OFF')
