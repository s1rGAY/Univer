from abc import ABC, abstractmethod


# class that describes display of fuel tank
class AbstractFuelTankDisplay(ABC):

    @property
    @abstractmethod
    def fill_level(self):
        """Indicates fill level(float)"""

    @property
    @abstractmethod
    def is_on_reserve(self):
        """Boolean value which indicates whether
        fuel is below certain border"""

    @property
    @abstractmethod
    def is_full(self):
        """Boolean value which indicates whether tank is full"""
