from re import M
from kivy.core.text import Label


import kivy
from matplotlib.pyplot import text
from utility.windows.windows import InputWindow
from utility.windows.windows import FilterWindow
from utility.windows.windows import DeleteWindow
from utility.windows.windows import SaveWindow
from utility.windows.windows import UploadWindow


from kivy.properties import ObjectProperty
from kivy.lang import Builder

from kivy.uix.screenmanager import Screen
from kivy.uix.button import Button
from kivy.uix.pagelayout import PageLayout

 
from kivymd.uix.snackbar import Snackbar


class MainWidget():
    def init(self, info='Def string'):
        self.info = info
        
        self.fg = PageLayout()

        btn1 = Button(text =self.info)
        btn2 = Button(text =self.info)
        btn3 = Button(text =self.info)

        lab1 = Label(text=self.info)

        self.fg.add_widget(btn1)
        self.fg.add_widget(btn2)    
        self.fg.add_widget(btn3)
        self.fg.add_widget(lab1)

    def get(self):
        return self.fg
        

class ViewComponent(Screen):
    controller = ObjectProperty()

    def __init__(self, **kw):
        super().__init__(**kw)
        self.widget = MainWidget('dsdsfsdfds')
        self.table = self.widget.get()
        self.screen = Screen()



    def open_dialog(self, window_type: str):
        if window_type == 'input':
            self.dialog = InputWindow(view=self)
        elif window_type == 'filter':
            self.dialog = FilterWindow(view=self)
        elif window_type == 'delete':
            self.dialog = DeleteWindow(view=self)
        elif window_type == 'save':
            self.dialog = SaveWindow(view=self)
        elif window_type == 'upload':
            self.dialog = UploadWindow(view=self)

        self.dialog.open()
        self.controller.open_dialog(window_type, self.dialog)

    def close_dialog(self, dialog_data: list = []):
        if self.dialog.mode == 'input':
            self.controller.input_train(dialog_data)
        elif self.dialog.mode == 'filter':
            self.controller.filter_trains(dialog_data)
        elif self.dialog.mode == 'delete':
            deleted = self.controller.delete_trains(dialog_data)
            Snackbar(text=f'{deleted} trains are deleted.').open()
        elif self.dialog.mode == 'upload':
            self.controller.upload_from_file(dialog_data)
        elif self.dialog.mode == 'save':
            self.controller.save_in_file(dialog_data)

        self.dialog = None

    def on_controller_change(self, data):
        self.close_dialog(data)

    def refresh(self):
        self.controller.refresh()

    def build(self):
        self.add_widget(self.table)
        return self

#Builder.load_file('/home/siarhei/Programming/IIT/Univer/ППвИС/lab_4/view/view.kv')