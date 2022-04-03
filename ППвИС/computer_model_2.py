#from webbrowser import MacOSX
from multiprocessing.reduction import sendfds
import os

#probably Done
class User:
    def __init__(self, login, password, access_lvl, system_type):
        self.login = login
        self.password = password
        self.access_lvl = access_lvl
        self.operation_system = Operation_system(system_type)
    
    def get_user_info(self):
        return self.login, self.password, self.access_lvl, self.operation_system.type

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
            elif param == 'access_lvl':
                print('Please, enter new access_lvl : ')
                self.access_lvl = str(input())
            else:
                print('No such param')
        else:
            print('Access denied!')

class Computer:
    def __init__(self, storage_size):
        #тк комп создается впервые нужно задать хотя бы 1 пользователя
        #storage_size - кол-во возможных файлов
        print('Enter info in order: \n Computer Name \n Login \n Password \n Access_lvl \n System_type')
        self.computer_name = input()
        self.users = [User(input(),input(),input(),input())]
        self.storage = Storage(storage_size, self.computer_name, self.users)
        self.keyboard = Keyboard()

    def add_user(self):
        #тк комп с юзером уже есть, надо просто добавить нового через self.storage
        print('Enter info in order:\n Login \n Password \n Access_lvl \n System_type')
        self.users.append(User[input(),input(),input(),input()])
        self.storage.add_new_user_direcrory(self.users[-1])
    
    def del_user(self):
        print('Enter user login : ')
        login = input()
        #проверка на существование


#добавить проверку на существования уже такого компа
#добавить фиксацию размера хранилища
path = '/home/siarhei/Programming/IIT/Univer/ППвИС/Computers_data'
class Storage:
    def __init__(self, size, computer_name, users):
        self.path_to_comp = (path+'/'+computer_name)

        #приводится к int тк работает по принципу подсчета кол-ва файлов
        #user_storage_size = 100, создаем в дериктории 1 файл, user_storage_size = 99
        self.storage_size = size
        self.user_storage_size = int(size*0.7)
        self.system_storage_size = int(size*0.3)

        os.chdir(path=path)
        os.mkdir(self.path_to_comp)
        os.chdir(self.path_to_comp)
        
        '''
        системное хранилище должно хранить инфу о всех пользователях(по папкам)
        список команд (в этих же папках, тк это зависит от параметра пользователя system_type)
        '''
        os.mkdir('System_storage')
        os.chdir((self.path_to_comp+'/System_storage'))
        os.mkdir(users[0].login)
        os.chdir((self.path_to_comp+'/System_storage/'+users[0].login))

        writing_commands_to_storage = open('Commands_and_descriptions.txt', 'w')
        writing_commands_to_storage.write(str(users[0].operation_system.get_commands()))
        writing_user_info_to_storage = open('User_info.txt','w')
        writing_user_info_to_storage.write(str(users[0].get_user_info()))



        '''
        хранит все файлы и тд созданные пользователем
        '''
        os.chdir((self.path_to_comp))
        os.mkdir('User_storage')
        os.chdir((self.path_to_comp+'/User_storage'))
        os.mkdir(users[0].login)
        os.chdir((self.path_to_comp+'/User_storage/'+users[0].login))

    #допилить удаление всех файлов в пользлвательской директории
    def clear_user_storage(self):
        os.chdir(self.path_to_comp)
        os.removedirs('User_storage')
        self.user_storage_size = self.storage_size*0.7
    #аналога с удалением файлов систему не будет!(ну мб с только с линуксом) )

    def get_storage_info(self):
        return {self.storage_size:' storage size.',
                self.system_storage_size : ' free system memory.',
                self.user_storage_size :' free user memory'}
    
    def add_new_user_direcrory(self,login):
        os.chdir((self.path_to_comp+'/System_storage'))
        os.mkdir(login.login)
        os.chdir((self.path_to_comp+'/System_storage/'+login.login))

        writing_commands_to_storage = open('Commands_and_descriptions.txt', 'w')
        writing_commands_to_storage.write(str(login.operation_system.get_commands()))

        writing_user_info_to_storage = open('User_info.txt','w')
        writing_user_info_to_storage.write(str(login.get_user_info()))

    #разобраться с удалением в OS
    def delete_user_directory(self, user):
        pass
                
#~ мб добавить раскаладки
class Keyboard:
    def typing():
        return input()

#переделать exeption на адекватный
#перемотреть весь класс(взять из прошлой реализации)
class Сommand_settings:
    def __init__(self, commands):
        self.commands = commands  # should be a dict (key-command,value-access)

    def get_commands(self):
        return self.commands

    def get_command(self, command):
        if command in self.commands.keys():
            return self.commands[command]
        else:
            print('Exception!')

    def add_command(self, new_command):  # should be a dict (value-access)
        if new_command not in self.commands.keys():
            self.commands[new_command.keys()] = new_command[new_command.keys()]
        else:
            print('Exception!')

    def del_command(self, command):  # just a command
        del self.commands[command]

class Linux_commands(Сommand_settings):
    def __init__(self):
        self.commands = {'shoutdown': 'off',
                          'clear_file': 'clearing file',
                          'rm': 'remove file',
                          'touch': 'create file',
                          'echo >': 'overwrite file',
                          'echo >>': 'add data to end',
                          'cat': 'view file data'}

class Win_commands(Сommand_settings):
    def __init__(self):
        self.commands = {'shoutdown': 'off',
                        'cat /dev/null': 'clearing file',
                        'del': 'remove file',
                        'type null >': 'create file',
                        'echo >': 'overwrite file',
                        'echo >>': 'add data to end',
                        'cat': 'view file data'}

class macOS_commands(Сommand_settings):
    def __init__(self):
        self.commands = {'shoutdown': 'off',
                          'echo -n': 'clearing file',
                          'rm': 'remove file',
                          'nano': 'create file',
                          'echo >': 'overwrite file',
                          'echo >>': 'add data to end',
                          'cat': 'view file data'}

#добавить управление и взаимодействие юзера
class Operation_system:
    def __init__(self, system_name):
        self.type = system_name

        if system_name.lower() == 'linux':
            self.commands = Linux_commands()
        elif system_name.lower() == 'windows':
            self.commands = Win_commands()
        elif system_name == 'macosx':
            self.command == macOS_commands()
        else:
            print('Invalid operating system name!')
    
    def get_commands(self):
        return self.commands.get_commands()
