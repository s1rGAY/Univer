from abc import ABC, abstractmethod
import string


class AbstractLogger(ABC):
    @abstractmethod
    def log(self, message: string):
        """Logging information to file."""

    @abstractmethod
    def disable_logging(self):
        """Disables logging"""

    @abstractmethod
    def enable_logging(self):
        """Enables logging"""
