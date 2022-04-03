'''
Задание
Модель ЭВМ(компьютера)
Предметная область: взаимодействие пользователя с компьютером.

Важные сущности: компьютер, клавиатура, пин код(пароль), хранилище
(память компьютера), операция просмотра хранилища, операции взаимодействия
(добавление данных, удаление и тд), ?команды?, ?хранилище банкнот?.


Шаги выполнения:

декомпозировать поведение системы на состояния, построить диаграмму состояний
спроектировать классы с учетом принципов SOLID, построить диаграмму классов

Общие требования к выполнению:
сохранять состояние программной системы между запусками программы
использовать UMLверсии2.xдля построения диаграммы классов и диаграммы состояний
использовать стандарт PEP8
использовать механизм исключений для обработки ошибочных ситуаций
программная система должна быть разработана с интерфейсом командной строки(CLI)

Дополнительные требования:
использовать аннотацию типов
разработать unit тесты
'''

# from calendar import r
import collections
from distutils.command.sdist import sdist
from inspect import CO_ASYNC_GENERATOR
import string
import os

from cachetools import FIFOCache


class User:
    def __init__(self, name, systems):
        self.name = name
        self.system = systems  # кортеж систем, которыми может пользоваться user

    def turn_comuter_status(Computer):
        Computer.turn_status()

    def use_command(self, Computer):
        Computer.use_command()

    def get_user_info(self):
        return(self.name, self.system)

#парсер для данных из папки с инфой компа
def parser():
    pass

class Computer:
    def __init__(self, password, system_type, storage_size):
        self.password = password
        self.system_type = system_type
        self.storage = Storage(storage_size, system_type)
        self.keselfyboard = Keyboard()
        self.status = False

    def login(User):
        if parser() is True:
            # если такой пользователь есть у компа => можно запускать
            pass
            #добавить проверку passw
        else:
            #пользователя нету => доступ запрещен
            pass

    def _check_status(self):
        return self.status

    def turn_status(self):
        if self.status is True:
            self.status = False
        else:
            self.status = True

    def get_system_type(self):
        return self.system_type

    def get_storage_info(self):
        return self.storage.get_memory_info()

    def use_command(self):
        if self._check_status() is True:
            command = self.keselfyboard.enter_command()
            if self.storage.system_storage.find_command(command):
                # реализация команд
                # через класс! В котором посто будут функции с этими командами
                pass
            else:
                print('Exeption! No such command.')
            


    def get_status(self):
        return self.status


class Keyboard:
    def enter_command(self):
        return str(input())

# добавить набор команд для работы с хранилищем
# прописать взаимодействие с хранилищем


# как разделить storage?
# говнокод(конструкторы)
# странаня иерархия
class Storage:
    def __init__(self, size, system_type):
        self.user_storage = User_storage(size*0.7)
        self.system_storage = System_storage(size*0.3, system_type)

    def get_memory_info(self):
        return {'User storage : ': self.user_storage.get_memory_info(),
                'System storage : ': self.system_storage.get_memory_info()}

    def clear_storage():
        pass


class User_storage(Storage):
    def __init__(self, size):
        self.free_memory = size
        self.used_memory = 0

    def get_memory_info(self):
        return {'Free memory :': self.free_memory, 'Used memory:': self.used_memory}

    #  прописать организацию файлов


class System_storage(Storage):
    def __init__(self, size, system_type):
        self.free_memory = size
        self.used_memory = 0
        self.system_type = (system_type.lower())  # возможные проблемы
        self.source_commands_realization = File_handling()
        self.comands = {}
        #добавить перегрузку для 1 параметра
        if self.system_type == 'linux':
            self.comands = Linux_commands({'':''})
        elif system_type == 'windows' or 'win':
            self.comands = Win_commands({'':''})
        elif system_type == 'macos':
            self.comands = macOS_commands({'':''})

    def get_memory_info(self):
        return {'Free memory :': self.free_memory, 'Used memory:': self.used_memory}

    def find_command(self, command):
        return (command in self.commands.keys())
    
    def get_command(command):
        pass


class File_handling:
    def clear_file(file_name):
        os.system(r' >file_name')  # ???????????????????????????

    def delete_file(file_name):
        os.remove(str(file_name))

    def create_file(file_name):
        file = open(str(file_name), "w")
        file.close()

    def overwrite_file(file_name):
        file = open(str(file_name), "w")
        file.write(str(input()))
        file.close()

    def add_data_to_end(file_name):
        file = open(str(file_name), "a")
        file.write(str(input()))
        file.close()

    def view_file_data(file_name):
        file = open(str(file_name), "r")
        file.read()
        file.close()


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


#  нужен фикс с конструктором
class Linux_commands(Сommand_settings):
    def __init__(self, commands):
        linux_commands = {'shoutdown': 'off',
                          'clear_file': 'clearing file',
                          'rm': 'remove file',
                          'touch': 'create file',
                          'echo >': 'overwrite file',
                          'echo >>': 'add data to end',
                          'cat': 'view file data'}
        super().__init__({**linux_commands, **commands})
#переставить версия питона на 3.9 для записи linux_commands | commands

class Win_commands(Сommand_settings):
    def __init__(self, commands):
        win_commands = {'shoutdown': 'off',
                        'cat /dev/null': 'clearing file',
                        'del': 'remove file',
                        'type null >': 'create file',
                        'echo >': 'overwrite file',
                        'echo >>': 'add data to end',
                        'cat': 'view file data'}
        super().__init__({**win_commands, **commands})


class macOS_commands(Сommand_settings):
    def __init__(self, commands):
        macos_commands = {'shoutdown': 'off',
                          'echo -n': 'clearing file',
                          'rm': 'remove file',
                          'nano': 'create file',
                          'echo >': 'overwrite file',
                          'echo >>': 'add data to end',
                          'cat': 'view file data'}
        super().__init__({**macos_commands, **commands})

    def __init__(self, commands):
        super().__init__(commands)


siarhei = User('Siarei','linux')
print(str(siarhei.get_user_info())+ '\t')


siarhei_pc = Computer(12345, 'linux', 100)
print(str(siarhei_pc.get_status()) + '\t')
print(str(siarhei_pc.get_storage_info()) + '\t')
print(str(siarhei_pc.get_system_type()) + '\t')