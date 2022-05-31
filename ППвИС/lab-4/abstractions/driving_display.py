from abc import ABC, abstractmethod


# class that describes actual information on vehicle speed and other parameters
class AbstractDrivingDisplay(ABC):

    @property
    @abstractmethod
    def actual_speed(self):
        """Indicates actual speed of vehicle."""

    @property
    @abstractmethod
    def actual_consumption(self):
        """Indicates current consumption rate."""
