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
import os


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


class Computer:
    def __init__(self, password, system_type, storage_size):
        self.password = password
        self.system_type = system_type
        self.user_storage = Storage(storage_size, system_type)
        self.keyboard = Keyboard()
        self.turn_status = False

    def turn_status(self):
        if self.status is True:
            self.status = False
        else:
            self.status = True

    def use_command(self):
        return self.keyboard.enter_command()


class Keyboard:
    def enter_command(self):
        return str(input())

# добавить набор команд для работы с хранилищем
# прописать взаимодействие с хранилищем


# как разделить storage?
# говнокод(конструкторы)
class Storage:
    def __init__(self, size, system_type):
        self.user_storage = User_storage(size*0.7)
        self.system_storage = System_storage(size*0.3, 'Linux')

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
        self.system_type = system_type
        self.comands = {}
        #  may be use lowercase()?
        if system_type == 'Linux' or 'linux' or 'Penguin':
            self.comands = {}
        elif system_type == 'Windows' or 'Win' or 'win':
            self.comands = {}
        elif system_type == 'macOS' or 'macos' or 'MacOS':
            self.comands = {}

    def get_memory_info(self):
        return {'Free memory :': self.free_memory, 'Used memory:': self.used_memory}

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
    def __init__(self, system_type, commands):
        self.commands = commands  # should be a dict (key-command,value-access)
        self.system_type = system_type

    def get_system_type(self):
        return self.system_type

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
class Linux__commands(Сommand_settings):
    def __init__(self, commands):
        super().__init__(system_type, commands)
        self.commands = {'shutdown': 'sudo'}


class Win_commands:
    def __init__(self, system_type, commands):
        super().__init__(system_type, commands)
        self.commands = {'shutdown': 'sudo'}


class macOS_commands:
    def __init__(self, system_type, commands):
        super().__init__(system_type, commands)
        self.commands = {'shutdown': 'sudo'}


first_user = User('Siarhei', ('Win', 'Linux', 'macOS'))
#  first_pc = Computer('my_password', 'Linux', 100)
storage = Storage(10, 'Linux')
first_computer = Computer('1234', 'linux', 10)
first_user.use_command(first_computer)
