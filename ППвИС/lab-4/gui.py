from kivymd.app import MDApp

from kivy.core.window import Window
from abstractions.vehicle import AbstractVehicle

from controller.controller import ControllerComponent
from model.model import ModelComponent


def run_gui_interface(car: AbstractVehicle, logger):
    CarGraphicApplication(car, logger).run()


class CarGraphicApplication(MDApp):
    def __init__(self, car, logger, **kw):
        super().__init__(**kw)
        self.model = ModelComponent(car, logger)
        self.controller = ControllerComponent(self.model)
        self.theme_cls.theme_style = 'Light'

    def build(self):
        Window.size = (1500, 1000)
        return self.controller.get_screen()
