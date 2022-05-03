from kivymd.app import MDApp
from kivymd.uix.datatables import MDDataTable

from contoller.controller import ControllerComponent
from model.model import ModelComponent

from kivy.core.window import Window
from kivy.metrics import dp

#создание основной таблицы
class TableApplication(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.table = MDDataTable(
            pos_hint={'center_x': 0.5, 'center_y': 0.54},
            size_hint={0.9, 0.8},
            use_pagination=True,
            rows_num=6,
            column_data=[
                ('Train number', dp(30)),
                ('Departure station', dp(30)),
                ('Arrival station', dp(30)),
                ('Date and time of departure', dp(50)),
                ('Date and time of arrival', dp(50)),
                ('Travel time', dp(40))
            ]
        )
        self.model = ModelComponent(table=self.table)
        self.controller = ControllerComponent(self.model)

    #запуск окна с размерами пикселей
    def build(self):
        Window.size = (1600, 1000)
        return self.controller.get_screen()


TableApplication().run()
