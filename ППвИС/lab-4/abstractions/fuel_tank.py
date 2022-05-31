from abc import ABC, abstractmethod


class AbstractFuelTank(ABC):
    @property
    @abstractmethod
    def fill_level(self):
        """Indicates amount of fuel(in liters)"""

    @property
    @abstractmethod
    def is_on_reserve(self):
        """Boolean property which indicates whether
        amount of fuel is below certain border"""

    @property
    @abstractmethod
    def is_full(self):
        """Indicates whether tank is full"""

    @abstractmethod
    def consume(self, liters: float):
        """Updates amount of fuel"""

    @abstractmethod
    def refuel(self, liters: float):
        """Updates amount of fuel."""
