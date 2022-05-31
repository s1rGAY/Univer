from abc import ABC, abstractmethod
from abstractions.observer import Observer


class Observable(ABC):
    @abstractmethod
    def subscribe(self, observer: Observer) -> None:
        """Attach an observer to observable instance"""

    @abstractmethod
    def unsubscribe(self, observer: Observer) -> None:
        """Detach an observer to observable instance"""

    @abstractmethod
    def notify(self) -> None:
        """Notify all observables"""
