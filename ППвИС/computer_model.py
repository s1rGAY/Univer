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
from distutils.command.sdist import sdist
import os


class User:
    def __init_(self, name, system, accses_level):
        self.name = name
        self.accses_level = accses_level
        self.system = system  # кортеж систем, которыми может пользоваться user

    def turn_on_comuter(Computer):
        Computer.turn_status()

    def use_command(self):
        Keyboard.enter_command(self.accses_level)


class Computer:
    def __init__(self, password, root_password, system_name, Storage):
        self.password = password
        self.root_password = root_password
        self.storage = Storage()
        self.status = False  # pc is switched off
        self.system_name = system_name
        if system_name == 'windows':
            self.comands = ['shutdown']
        elif system_name == 'macOS':
            self.comands = ['shutdown']
        elif system_name == 'linux':
            self.comands = ['poweroff']
        else:
            print("Such a system isn't available")

    def turn_status(self):
        if self.status is True:
            self.status = False
        else:
            self.status = True


class Keyboard:
    def enter_command(accses_level):
        command = str(input())

# добавить набор команд для работы с хранилищем
# прописать взаимодействие с хранилищем


# как разделить storage?

class Storage:
    def __init__(self, size):
        self.size = size
        self.free_memory = size

        self.user_storage = User_storage(size)
        self.system_storage = System_storage(size)

        if isinstance(self, User_storage):
            self.access_lvl = 'User'
            self.user_size = self.size * 0.7
        elif isinstance(self, System_storage):
            self.access_lvl = 'Administrator'
            self.system_size = self.size * 0.3
            self.

    def clear_storage(self):
        self.free_memory = self.size
        # прописать удаление файлов


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


class User_storage(Storage):
    pass


class System_storage(Storage):
    #  должна хранить root файлы и команды
    pass
