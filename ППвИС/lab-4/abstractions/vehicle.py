from abc import ABC, abstractmethod


# Abstract class that describes vehicles
class AbstractVehicle(ABC):

    @property
    @abstractmethod
    def engine_is_running(self):
        """Indicates whether engine is running or not"""

    @abstractmethod
    def engine_start(self):
        """Starts an engine"""

    @abstractmethod
    def engine_stop(self):
        """Stops an engine"""

    @abstractmethod
    def refuel(self, liters: float):
        """Refuel vehicle by certain amount of fuel(in liters)"""

    @abstractmethod
    def running_idle(self):
        """Method which runs vehicle until certain event"""

    @abstractmethod
    def free_wheel(self):
        """Method which runs vehicle in mode where fuel doesn't consume"""

    @abstractmethod
    def brake_by(self, speed: float):
        """Method which launches breaking in vehicle"""

    @abstractmethod
    def accelerate(self, speed: float):
        """Method which launches acceleration in vehicle"""
