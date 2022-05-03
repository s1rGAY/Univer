from abc import ABC, abstractclassmethod, abstractmethod


class Observer(ABC):
    @abstractmethod
    def on_model_change(self, data):
        """Method is called when on the observer when model is changing"""
