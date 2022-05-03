from abc import ABC, abstractmethod


class Observable(ABC):
    @abstractmethod
    def subscribe(self, observer):
        """Attach an observer to observable instance"""

    @abstractmethod
    def unsubscribe(self, observer):
        """Detaches an observer from observable instance"""

    @abstractmethod
    def notify(self, data):
        """Notifies all observers about changes"""
