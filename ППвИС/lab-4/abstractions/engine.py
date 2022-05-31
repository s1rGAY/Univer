from abc import ABC, abstractmethod


# class that commonly describes all engines
class AbstractEngine(ABC):

    @property
    @abstractmethod
    def is_running(self):
        """Indicates whether engine is running"""

    @abstractmethod
    def consume(self, liters: float):
        """Consumes certain amount of liters"""

    @abstractmethod
    def start(self):
        """Starts an engine"""

    @abstractmethod
    def stop(self):
        """Stops an engine"""
