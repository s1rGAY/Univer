from __future__ import with_statement
import json

from numpy import save

from abstractions.observer import Observer
from abstractions.logger import AbstractLogger
from Lab1.saver import Saver


class SnapshotService(Observer):
    def __init__(self):
        self.__computer = None

    def handle(self, computer, logger: AbstractLogger) -> None:
        self.__computer = computer

        logger.disable_logging()

        self.__save_computer__()  # добавлено, переделать внутренности

        logger.enable_logging()

    def __save_computer__(self, *objects) -> None:
        saver = Saver(objects)
        saver.save_state(objects)
