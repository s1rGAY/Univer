from kivymd.app import MDApp
from kivymd.uix.datatables import MDDataTable

from contoller.controller import ControllerComponent
from model.model import ModelComponent

from kivy.core.window import Window
from kivy.metrics import dp


class TableApplication(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.table = MDDataTable(
            pos_hint={'center_x': 0.5, 'center_y': 0.54},
            size_hint={0.9, 0.8},
            use_pagination=True,
            rows_num=13,
            column_data=[
                ('Full name', dp(30)),
                ('Group', dp(20)),
                ('1', dp(15)),
                ('2', dp(15)),
                ('3', dp(15)),
                ('4', dp(15)),
                ('5', dp(15)),
                ('6', dp(15)),
                ('7', dp(15)),
                ('8', dp(15)),
                ('9', dp(15)),
                ('10', dp(15)),
                ('Total', dp(15)),
            ],
        )
        self.model = ModelComponent(table=self.table)
        self.controller = ControllerComponent(self.model)

    def build(self):
        Window.size = (1280, 800)
        return self.controller.get_screen()


TableApplication().run()
