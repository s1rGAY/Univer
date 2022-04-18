#from webbrowser import MacOSX
import json
from multiprocessing.reduction import sendfds
import os
import shutil
import jsons

path = '/home/siarhei/Programming/IIT/Univer/ППвИС/Computers_data'

#прописать для всего гттеры и сеттеры(по всему коду

class Parser:
    def __init__(self, path=path+'/data.json'):
        self.data = None
        with open(path,'r') as load_data:
            self.data = json.loads(load_data.read())

    def update_data(self, path=path+'/data.json'):
        with open(path,'r') as load_data:
            self.data = json.loads(load_data.read())

    def upload_data_to_program(self):
        tem_data = []
        for i in self.data:
            tem_data.append(Computer(i['storage']['storage_size']))

    def get_data(self):
        return self.data

class Saver:
    def __init__(self, *objects):
        
        with open(path+'/data.json','w') as write_file:
            write_file.write(jsons.dumps(objects, strip_nulls = True,
            strip_privates = True, strip_properties = True))

class User:
    def __init__(self, login, password, operation_system_type):
        self.login = login
        self.password = password
        self.operation_system_type = operation_system_type
    
    def get_user_info(self):
        return self.login, self.password, self.operation_system_type

    def change_user_info(self):
        print('Please, enter password :')
        password = input()
        if password is self.password:
            print('What would you change?')
            param = input()
            if param == 'login':
                print('Please, enter new Login : ')
                self.login = str(input())
            elif param == 'password':
                print('Please, enter new Password : ')
                self.password = str(input())
            else:
                print('No such param')
        else:
            print('Access denied!')

class Computer:
    def __init__(self, storage_size):
        self.operation_systems = [Operation_system('linux'), 
                                Operation_system('macosx'), 
                                Operation_system('windows')]

        print('Enter info in order: \n Computer Name \n Login \n Password \n System_type')
        self.computer_name = input()
        self.users = [User(input(),input(),input())]
        
        self.storage = Storage(storage_size, self.computer_name, self.operation_systems, self.users)
        self.keyboard = Keyboard()

        self.comp_power_status = True
        self.logged_user = self.users[0]
    
    def __is_on(self):
        return self.comp_power_status

    #Done
    def turn_computer_status(self):
        if self.__is_on() == True:
            print('You turned off computer')
            self.comp_power_status = False
        else:
            self.comp_power_status = True
            print('You turned on computer')
            print('You should login to the system')
            self.__login()

    def __login(self):
        if self.__is_on():
            access_info = self.__check_access_rights()
            if access_info[0] != False:
                self.logged_user = access_info[1]
        else:
            print('Computer status - OFF')
    
    #Done (Op System)             
    def __check_access_rights(self):
        for j in range(3):
            print('Enter Login :')
            login = input()
            for i in self.users:
                if i.login == login:
                    for a in range(3):
                        print('Enter password :')
                        password = input()
                        if i.password == password:
                            return (True, i)
                        else:
                            print('Invalid password! Attemps ramained : '+str(a))
                elif i == self.users[-1]:
                    print('Access denied!')
                    return (False, None)
                print('Invalid login! Attemps ramained :'+str(j))

    #Done 
    def change_logged_user(self):
        self.__login()  

    #Done (Op System)
    def add_user(self):
        if self.__is_on():
            print('\n ADDING A NEW USER \nEnter info in order:\n Login \n Password \n System_type')
            self.users.append(User(input(),input(),input()))
            self.storage.add_new_user_direcrory(self.users[-1])
        else:
            print('Computer status - OFF')

    #Done (Op System)
    def del_user(self):
        if self.__is_on():
            print('\n DELETING A USER \nTo remove user you must know it\'s login and password.')
            permission_data = self.__check_access_rights()
            if permission_data[0] == True:
                self.storage.delete_user(permission_data[1])
                self.users.remove(permission_data[1])
        else:
            print('Computer status - OFF')

    #Done
    def enter_command(self):
        if self.__is_on():    
            command = self.keyboard.typing()

            numb_of_op_system = None
            for i in range(len(self.operation_systems)):
                if self.operation_systems[i].type == self.logged_user.operation_system:
                    numb_of_op_system = i
                    break
            if self.operation_systems[numb_of_op_system].commands.get_command(command)!=False:  #переделать тк возвращало описание команды захардкодил на !=False
                path = ('/home/siarhei/Programming/IIT/Univer/ППвИС/Computers_data/'
                +str(self.computer_name)+'/'+str(self.logged_user.operation_system)
                +'/User_storage/'+str(self.logged_user.login))
                self.operation_systems[numb_of_op_system].run_command(command, path)
        else:
            print('Computer status - OFF')

class Keyboard:
    def typing(self):
        return input()


#добавить ограничения по размеру(сейчас может в - уходить)
#пофиксить сохранение состояний(компа) + json file
class Storage:
    def __init__(self, size, computer_name, operation_systems, users):
        self.path_to_comp = (path + '/' + computer_name)
        self.storage_size = size
        self.user_storage_size = int(size*0.7)
        self.system_storage_size = int(size*0.3)

        os.chdir(path=path)
        os.mkdir(self.path_to_comp)
        
        for i in operation_systems:
            os.chdir(self.path_to_comp) #заходим в папку компа

            os.mkdir(i.type)
            os.chdir(self.path_to_comp+'/'+str(i.type))# в папку операционки

            os.mkdir('System_storage')
            os.chdir((self.path_to_comp+'/'+str(i.type)+'/System_storage'))# /операционка/System_storage

            writing_commands_to_storage = open('Commands_and_descriptions.txt', 'w')
            writing_commands_to_storage.write(str(i.commands.get_commands())) # записываем команды
            
            os.chdir(self.path_to_comp+'/'+str(i.type))
            os.mkdir('User_storage') # операционка + User_strorage

            if i.type == users[0].operation_system_type:
                os.chdir((self.path_to_comp+'/'+str(i.type)+'/System_storage'))
                os.mkdir(users[0].login) # операционка/System_storage + Login
                os.chdir((self.path_to_comp+'/'+str(i.type)+'/System_storage/'+users[0].login))#
                writing_user_info_to_storage = open('User_info.txt','w')
                writing_user_info_to_storage.write(str(users[0].get_user_info()))

                os.chdir(self.path_to_comp+'/'+str(i.type)+'/User_storage')
                os.mkdir(users[0].login)

    #Done
    def get_storage_info(self):
        return {self.storage_size:' storage size.',
                self.system_storage_size : ' free system memory.',
                self.user_storage_size :' free user memory'}
    
    #Done
    def __clear_user_s_storage(self, user):
        folder = self.path_to_comp+'/'+str(user.operation_system_type)+'/User_storage/'+str(user.login)
        for the_file in os.listdir(folder):
            file_path = os.path.join(folder, the_file)
            try:
                if os.path.isfile(file_path):
                    os.unlink(file_path)
                elif os.path.isdir(file_path): shutil.rmtree(file_path)
            except Exception as e:
                print(e)
        os.rmdir(folder)
        self.user_storage_size = self.storage_size*0.7

    def __clear_user_s_system_storage(self, user):
        folder = self.path_to_comp+'/'+str(user.operation_system_type)+'/System_storage/'+str(user.login)
        for the_file in os.listdir(folder):
            file_path = os.path.join(folder, the_file)
            try:
                if os.path.isfile(file_path):
                    os.unlink(file_path)
                elif os.path.isdir(file_path): shutil.rmtree(file_path)
            except Exception as e:
                print(e)
        os.rmdir(folder)
        self.system_storage_size = self.storage_size*0.3

    #Done
    def add_new_user_direcrory(self,user):
        os.chdir(self.path_to_comp+'/'+str(user.operation_system_type)+'/System_storage')
        os.mkdir(str(user.login))
        os.chdir(self.path_to_comp+'/'+str(user.operation_system_type)+'/System_storage/'+str(user.login)+'/')#
        writing_user_info_to_storage = open('User_info.txt','w')
        writing_user_info_to_storage.write(str(user.get_user_info()))

        os.chdir(self.path_to_comp+'/'+str(user.operation_system_type)+'/User_storage')
        os.mkdir(str(user.login))


    def delete_user(self, user):
        self.__clear_user_s_storage(user)
        self.__clear_user_s_system_storage(user)

        


class Commands_realization:

    #Done
    def clear_file(self, file_name, path):
        os.chdir(path=path)
        open(file_name, 'w').close()

    #Done
    def delete_file(self, file_name, path):
        os.chdir(path=path)
        os.remove(str(file_name))

    #Done
    def create_file(self, file_name, path):
        os.chdir(path=path)
        file = open(str(file_name), "w")
        file.close()

    #Done
    def overwrite_file(self, file_name, path):
        os.chdir(path=path)
        file = open(str(file_name), "w")
        file.write(str(input()))
        file.close()

    #Done
    def add_data_to_end(self, file_name, path):
        os.chdir(path=path)
        file = open(str(file_name), "a")
        file.write(str(input()))
        file.close()
    
    #Done
    def view_file_data(self, file_name, path):
        os.chdir(path=path)
        file = open(str(file_name), "r")
        print(file.read())
        file.close()


class Сommand_settings:
    def __init__(self, commands):
        self.commands = commands

    def get_commands(self):
        return self.commands

    def get_command(self, command):
        if command in self.commands.keys():
            return self.commands[command]
        else:
            print('No such command!')

    def add_command(self, new_command):
        if new_command not in self.commands.keys():
            self.commands[new_command.keys()] = new_command[new_command.keys()]
        else:
            print('This command already exists!')

    def del_command(self, command):
        del self.commands[command]


class Linux_commands(Сommand_settings):
    def __init__(self):
        self.commands = {'clear file': 'clearing file',
                          'rm': 'remove file',
                          'touch': 'create file',
                          'echo >': 'overwrite file',
                          'echo >>': 'add data to end',
                          'cat': 'view file data'}

class Win_commands(Сommand_settings):
    def __init__(self):
        self.commands = {'cat /dev/null': 'clearing file',
                        'del': 'remove file',
                        'type null >': 'create file',
                        'echo >': 'overwrite file',
                        'echo >>': 'add data to end',
                        'cat': 'view file data'}

class macOS_commands(Сommand_settings):
    def __init__(self):
        self.commands = {'echo -n': 'clearing file',
                          'rm': 'remove file',
                          'nano': 'create file',
                          'echo >': 'overwrite file',
                          'echo >>': 'add data to end',
                          'cat': 'view file data'}


class Operation_system:
    def __init__(self, system_type):
        self.type = system_type
        self.commands = None
        self.commands_sourse = Commands_realization()
        if system_type.lower() == 'linux':
            self.type = system_type
            self.commands = Linux_commands()
        elif system_type.lower() == 'windows':
            self.type = system_type
            self.commands = Win_commands()
        elif system_type.lower() == 'macosx':
            self.type = system_type
            self.commands = macOS_commands()
        else:
            print('Invalid operating system name!')
    
    #Done
    def run_command(self, command, path):
        if self.commands.get_command(command) == 'clearing file':
            self.commands_sourse.clear_file(file_name=input(),path=path)
        elif self.commands.get_command(command) =='remove file':
            self.commands_sourse.delete_file(file_name=input(),path=path)
        elif self.commands.get_command(command) =='create file':
            self.commands_sourse.create_file(file_name=input(),path=path)
        elif self.commands.get_command(command) =='overwrite file':
            self.commands_sourse.overwrite_file(file_name=input(),path=path)
        elif self.commands.get_command(command) =='add data to end':
            self.commands_sourse.add_data_to_end(file_name=input(),path=path)
        elif self.commands.get_command(command) =='view file data':
            self.commands_sourse.view_file_data(file_name=input(),path=path)


#first_pc = Computer(10)
#sec_pc = Computer(100)
#third_pc = Computer(1000)
#Saver(first_pc, sec_pc, third_pc)

p1 = Parser()
p1.update_data()
data = p1.get_data()
p1.upload_data_to_program()