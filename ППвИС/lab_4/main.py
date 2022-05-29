'''import imp
from multiprocessing.sharedctypes import synchronized
from time import thread_time_ns

from matplotlib.container import Container
from lab_4.model.computer import Computer
from parser import Parser
from lab_4.utility.saver import Saver
from lab_4.utility.state_synchronization import StateSynchronization
'''
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

from kivy.core.window import Window

from controller.controller import ControllerComponent
from model.model import ModelComponent

from view.view import ViewComponent


class TableApplication(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.model = ModelComponent()
        self.controller = ControllerComponent(self.model)


    def build(self):
        Window.size = (1600, 1000)
        return self.controller.get_screen()


TableApplication().run()
