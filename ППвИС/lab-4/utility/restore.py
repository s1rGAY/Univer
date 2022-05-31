# скачивание и востановление системы
from abstractions.logger import AbstractLogger
from models.computer import Computer

import json
from os.path import exists


# держит в себе параметры для сэйва ?
class RestoreService():
    def __init__(self):
        self.__computer_name: str = None
        self.__users: list = None

        self.__storage_size: int = None
        self.__coputer_power_status: bool = None

        self.__logged_user = None

    def restore_computer(self, logger: AbstractLogger):
        # read file
        if exists('car_configuration.json'):
            self.__read_file__()
            logger.disable_logging()

            # создаем класс на основе полученных данных из файла в Computer
            computer = Computer(10, 'ALexPC', 'Alex', '1', 'linux', logger)

            # restore car to it's initial condition
            # надо переделать во включенность компьютера
            if self.__coputer_power_status:
                computer.turn_computer_power_status()

            # переделать в залогиненного пользователя

            # refuel difference
            # мне наверное это не надо
            logger.enable_logging()
            return computer
        else:
            return None

    # заполнение данных файл -> класс
    def __read_file__(self) -> None:
        with open('computer_configuration.json', 'r') as json_file:
            data = json.load(json_file)
            self.__set_computer_name(data[0]['computer_name'])
            self.__set_users(data[0]['users'])
            self.__set_storage_size(data[0]['storage']['storage_size'])
            self.__set_computer_power_status(data[0]['comp_power_status'])
            self.__set_logged_user(data[0]['logged_user'])

    def __set_computer_name(self, computer_name):
        self.__computer_name = computer_name

    def __get_computer_name(self):
        return self.__computer_name

    def __set_users(self, users):
        self.__users = users

    def __get_users(self):
        return self.__users

    def __set_storage_size(self, sotorage_size):
        self.__storage_size = sotorage_size

    def __get_storage_size(self):
        return self.__storage_size

    def __set_computer_power_status(self, status):
        self.__coputer_power_status: bool = status

    def __get_computer_power_status(self):
        return self.__coputer_power_status

    def __set_logged_user(self, logged_user):
        self.__logged_user = logged_user

    def __get_logged_user(self):
        return self.__logged_user
