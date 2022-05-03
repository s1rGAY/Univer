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


class InputWindow(DialogWindow):
    def __init__(self, **kwargs):
        super().__init__(
            title='Fill new student data:',
            content_cls=InputDialogContent(),
            mode='input',
            view=kwargs['view'],
        )

    def close(self, obj):
        self.dismiss()
        self.view.close_dialog(
            [
                self.content_cls.ids.input_name.text,
                self.content_cls.ids.input_group.text,
                self.content_cls.ids.input_1_semester.text,
                self.content_cls.ids.input_2_semester.text,
                self.content_cls.ids.input_3_semester.text,
                self.content_cls.ids.input_4_semester.text,
                self.content_cls.ids.input_5_semester.text,
                self.content_cls.ids.input_6_semester.text,
                self.content_cls.ids.input_7_semester.text,
                self.content_cls.ids.input_8_semester.text,
                self.content_cls.ids.input_9_semester.text,
                self.content_cls.ids.input_10_semester.text,
            ]
        )


class FilterWindow(DialogWindow):
    def __init__(self, **kwargs):
        super().__init__(
                title='''#Note: if you don't need some term of search, just don't fill it.\nFilter students:''',
                content_cls=FilterDialogContent(),
                mode="filter",
                view=kwargs["view"],
        )

    def close(self, obj):
        self.dismiss()
        self.view.close_dialog(
            [
                self.content_cls.ids.filter_name.text,
                self.content_cls.ids.filter_group.text,
                self.content_cls.ids.filter_count_lower.text,
                self.content_cls.ids.filter_count_upper.text,
            ]
        )


class DeleteWindow(DialogWindow):
    def __init__(self, **kwargs):
        super().__init__(
                title="#Note: if you don't need some term of search, just don't fill it.\nDelete students: ",
                content_cls=DeleteDialogContent(),
                mode="delete",
                view=kwargs["view"],
        )

    def close(self, obj):
        self.dismiss()
        self.view.close_dialog(
            [
                self.content_cls.ids.delete_name.text,
                self.content_cls.ids.delete_group.text,
                self.content_cls.ids.delete_count_lower.text,
                self.content_cls.ids.delete_count_upper.text,
            ]
        )


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


Builder.load_file('/home/evgeny/source/repos/ideal-giggle/src/utility/windows/windows.kv')
