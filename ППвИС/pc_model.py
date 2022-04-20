#from webbrowser import MacOSX
import json
from multiprocessing.reduction import sendfds
import os
import shutil
import jsons

path = '/home/siarhei/Programming/IIT/Univer/ППвИС/Computers_data'


class Parser:
    def __init__(self, path):
        self.data = None
        self.loc_path = path+'/data.json'
        with open(self.loc_path,'r') as load_data:
            self.data = json.loads(load_data.read())

    def update_data(self):
        with open(self.loc_path,'r') as load_data:
            self.data = json.loads(load_data.read())

    def get_data(self):
        return self.data

class Saver:
    def __init__(self, *objects):
        
        with open(path+'/data.json','w') as write_file:
            write_file.write(jsons.dumps(objects, strip_nulls = True,
            strip_privates = True, strip_properties = True))

    def save_state(self, *objects):
        with open(path+'/data.json','w') as write_file:
            write_file.write(jsons.dumps(objects, strip_nulls = True,
            strip_privates = True, strip_properties = True))

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

class User:
    def __init__(self, login, password, operation_system_type):
        self.login = login
        self.password = password
        self.operation_system_type = operation_system_type
    
    def _set_login(self, login):
        self.login = login

    def get_login(self):
        return self.login

    def _set_password(self, password):
        self.password = password
    
    def _get_password(self):
        return self.password
        
    def _set_operation_system_type(self, operation_system_type):
        self.operation_system_type = operation_system_type

    def get_operation_system_type(self):
        return self.operation_system_type

    def get_all_user_info(self):
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

    #инпут - норм ?
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
        
        if os.path.exists(self.path_to_comp)!=True:
            os.chdir(path=path)
            os.mkdir(self.path_to_comp)
            
            for i in operation_systems:
                os.chdir(self.path_to_comp) #заходим в папку компа

                os.mkdir(i._get_system_type())
                os.chdir(self.path_to_comp+'/'+str(i._get_system_type()))# в папку операционки

                os.mkdir('System_storage')
                os.chdir((self.path_to_comp+'/'+str(i._get_system_type())+'/System_storage'))# /операционка/System_storage

                writing_commands_to_storage = open('Commands_and_descriptions.txt', 'w')
                writing_commands_to_storage.write(str(i._get_system_type())) # записываем команды
                self.system_storage_size -= 1
                
                os.chdir(self.path_to_comp+'/'+str(i._get_system_type()))
                os.mkdir('User_storage') # операционка + User_strorage

                if i._get_system_type() == users[0].get_operation_system_type():
                    os.chdir((self.path_to_comp+'/'+str(i._get_system_type())+'/System_storage'))
                    os.mkdir(users[0].get_login()) # операционка/System_storage + Login
                    os.chdir((self.path_to_comp+'/'+str(i._get_system_type())+'/System_storage/'+users[0].get_login()))#
                    writing_user_info_to_storage = open('User_info.txt','w')
                    writing_user_info_to_storage.write(str(users[0].get_all_user_info()))
                    self.system_storage_size -= 1

                    os.chdir(self.path_to_comp+'/'+str(i._get_system_type())+'/User_storage')
                    os.mkdir(users[0].get_login())


    def get_all_storage_info(self):
        return {self.storage_size:' storage size.',
                self.system_storage_size : ' free system memory.',
                self.user_storage_size :' free user memory'}
    
    def get_storage_size(self):
        return self.storage_size

    def get_free_system_storage_size(self):
        return self.system_storage_size

    def get_free_user_storage_size(self):
        return self.user_storage_size


    def __clear_user_s_storage(self, user):
        folder = self.path_to_comp+'/'+str(user.get_operation_system_type())+'/User_storage/'+str(user.get_login())
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
        folder = self.path_to_comp+'/'+str(user.get_operation_system_type())+'/System_storage/'+str(user.get_login())
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


    def _add_new_user_directory(self,user):
        if os.path.exists(self.path_to_comp+'/'+str(user.get_operation_system_type())+'/System_storage/'+str(user.get_login()))!=True:
            path_to_user_syst = self.path_to_comp+'/'+str(user.get_operation_system_type())
            user_login = user.get_login()

            os.chdir(path_to_user_syst+'/System_storage')
            os.mkdir(str(user_login))
            os.chdir(path_to_user_syst+'/System_storage/'+str(user_login)+'/')#
            writing_user_info_to_storage = open('User_info.txt','w')
            writing_user_info_to_storage.write(str(user.get_all_user_info()))

            os.chdir(path_to_user_syst+'/User_storage')
            os.mkdir(str(user_login))


    def _delete_user(self, user):
        self.__clear_user_s_storage(user)
        self.__clear_user_s_system_storage(user)
        


class Commands_realization:

    def clear_file(self, file_name, path):
        os.chdir(path=path)
        open(file_name, 'w').close()

    def delete_file(self, file_name, path):
        os.chdir(path=path)
        os.remove(str(file_name))

    def create_file(self, file_name, path):
        os.chdir(path=path)
        file = open(str(file_name), "w")
        file.close()

    def overwrite_file(self, file_name, path):
        os.chdir(path=path)
        file = open(str(file_name), "w")
        file.write(str(input()))
        file.close()

    def add_data_to_end(self, file_name, path):
        os.chdir(path=path)
        file = open(str(file_name), "a")
        file.write(str(input()))
        file.close()
    
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
            return False

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
    
    def _get_system_type(self):
        return self.type

    def _get_command(self, command):
        return self.commands.get_command(command)

    def _get_all_commands(self):
        return self.commands.get_commands

    def _delete_command(self,command):
        return self.commands.del_command(command)

    def _run_command(self, command, path):
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
        else:
            print('\nNo such command!\n')


