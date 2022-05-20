'''import imp
from multiprocessing.sharedctypes import synchronized
from time import thread_time_ns

from matplotlib.container import Container
from lab_4.model.computer import Computer
from parser import Parser
from lab_4.utility.saver import Saver
from lab_4.utility.state_synchronization import StateSynchronization
'''
from kivymd.app import MDApp
from kivy.uix.boxlayout import BoxLayout

from kivymd.app import App
from kivymd.uix.datatables import MDDataTable
from kivy.core.window import Window
from kivy.metrics import dp

from controller.controller import ControllerComponent

from kivymd.theming import ThemeManager


class TableApplication(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.table = MDDataTable(
            pos_hint={'center_x': 0.5, 'center_y': 0.54},
            size_hint={0.9, 0.8},
            use_pagination=True,
            rows_num=15,
            column_data=[
                ('Train number', dp(40)),
                ('Departure station', dp(40)),
                ('Arrival station', dp(40)),
                ('Date and time of departure', dp(60)),
                ('Date and time of arrival', dp(60)),
                ('Travel time', dp(40))
            ]
        )
        self.model = ModelComponent(table=self.table)
        self.controller = ControllerComponent(self.model)


    def build(self):
        Window.size = (1600, 1000)
        return self.controller.get_screen()


TableApplication().run()
