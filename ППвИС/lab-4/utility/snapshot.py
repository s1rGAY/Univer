from __future__ import with_statement
import json

from abstractions.observer import Observer
from abstractions.logger import AbstractLogger


# изначально создает модель ????
class SnapshotService(Observer):
    def __init__(self):

        self.__computer = None  # добавлено для компа

    def handle(self, computer, logger: AbstractLogger) -> None:
        self.__computer = computer

        logger.disable_logging()

        self.__save_computer__()  # добавлено, переделать внутренности

        logger.enable_logging()

    # что здесь делать??????
    def __save_computer__(self) -> None:
        # get car parts
        # self.__driving_display: AbstractDrivingDisplay = #self.__car.__getattribute__('__get_driving_display__')

        # dictionary = #{
        #    "fill_level": self.__fuel_tank_display.fill_level,
        #    "actual_speed": self.__driving_display.actual_speed,
        #    "actual_consumption": self.__driving_display.actual_consumption,
        #    "engine_is_running": self.__car.engine_is_running,
        '''}'''

        data = json.dumps(dictionary={}, indent=4)
        with open('car_configuration.json', 'w', encoding='UTF-8') as json_file:
            json_file.write(data)
