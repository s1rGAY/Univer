import os

from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder

from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton


class DialogContent(BoxLayout):
    pass


class InputDialogContent(DialogContent):
    pass


class FilterDialogContent(DialogContent):
    pass


class DeleteDialogContent(DialogContent):
    pass


class UploadDialogContent(DialogContent):
    pass


class SaveDialogContent(DialogContent):
    pass


class DialogWindow(MDDialog):
    def __init__(self, **kwargs):
        super().__init__(
            title=kwargs['title'],
            type='custom',
            content_cls=kwargs['content_cls'],
            buttons=[
                MDFlatButton(text='OK', theme_text_color='Custom', on_release=self.close),
            ],
        )
        self.mode = kwargs['mode']
        self.view = kwargs['view']

    def close(self, obj):
        self.dismiss()
        self.view.close_dialog()

#Сделано, но без глубокой переработки
class InputWindow(DialogWindow):
    def __init__(self, **kwargs):
        super().__init__(
            title='Fill new train data:',
            content_cls=InputDialogContent(),
            mode='input',
            view=kwargs['view'],
        )

    def close(self, obj):
        self.dismiss()
        self.view.close_dialog(
            [
                self.content_cls.ids.input_train_number.text,
                self.content_cls.ids.input_depart_st.text,
                self.content_cls.ids.input_arriv_st.text,
                self.content_cls.ids.input_data_of_depart.text,
                self.content_cls.ids.input_data_of_arriv.text
            ]
        )

#Не смотрел(класс для фильтрации данных)
class FilterWindow(DialogWindow):
    def __init__(self, **kwargs):
        super().__init__(
                title='''Filter trains:''',
                content_cls=FilterDialogContent(),
                mode="filter",
                view=kwargs["view"],
        )

    def close(self, obj):
        self.dismiss()
        self.view.close_dialog(
            [
                self.content_cls.ids.find_train_number.text,
                self.content_cls.ids.find_depart_st.text,
                self.content_cls.ids.find_arriv_st.text,
                self.content_cls.ids.find_data_of_depart.text,
                self.content_cls.ids.find_data_of_arriv.text,
                self.content_cls.ids.find_time_of_travel.text
            ]
        )

#Окно сделано, но не работает удаление
class DeleteWindow(DialogWindow):
    def __init__(self, **kwargs):
        super().__init__(
                title="Delete trains: ",
                content_cls=DeleteDialogContent(),
                mode="delete",
                view=kwargs["view"],
        )
    
    #закртытие вводимых окон?
    def close(self, obj):
        self.dismiss()
        self.view.close_dialog(
            [
                self.content_cls.ids.del_train_number.text,
                self.content_cls.ids.del_depart_st.text,
                self.content_cls.ids.del_arriv_st.text,
                self.content_cls.ids.del_data_of_depart.text,
                self.content_cls.ids.del_data_of_arriv.text,
                self.content_cls.ids.del_time_of_travel.text
            ]
        )

#Не делал
class SaveWindow(DialogWindow):
    def __init__(self, **kwargs):
        super().__init__(
                title="Saving: ",
                content_cls=SaveDialogContent(),
                mode="save",
                view=kwargs["view"],
        )

    def close(self, obj):
        self.dismiss()
        self.view.close_dialog(self.content_cls.ids.save_path.text)

#Не делал
class UploadWindow(DialogWindow):
    def __init__(self, **kwargs):
        super().__init__(
                title="Upload: ",
                content_cls=UploadDialogContent(),
                mode="upload",
                view=kwargs["view"],
        )

    def close(self, obj):
        self.dismiss()
        self.view.close_dialog(self.content_cls.ids.upload_path.text)


Builder.load_file('/home/siarhei/Programming/IIT/Univer/ППвИС/true_lab_2/src/utility/windows/windows.kv')
