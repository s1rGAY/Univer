from kivymd.app import MDApp

from kivy.core.window import Window

from controller.controller import ControllerComponent
from model.model import ModelComponent


def run_gui_interface(computer, logger):
    ComputerGraphicApplication(computer, logger).run()


class ComputerGraphicApplication(MDApp):
    def __init__(self, computer, logger, **kw):
        super().__init__(**kw)
        self.model = ModelComponent(computer, logger)
        self.controller = ControllerComponent(self.model)
        self.theme_cls.theme_style = 'Light'

    def build(self):
        Window.size = (1500, 1000)
        return self.controller.get_screen()
