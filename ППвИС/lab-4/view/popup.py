from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder

from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton


kivy = '''
<TextInputField@MDTextField>:
    size_hint: 0.5, 0.1
    input_type: 'text'

<PopupContent>:
    orientation: 'vertical'
    spacing: '10dp'
    height: '75dp'
    size_hint_y: None

    data: input_data

    TextInputField:
        id: input_data
        hint_text: 'Please input required data'

'''


class PopupContent(BoxLayout):
    pass


class PopupWindow(MDDialog):
    def __init__(self, **kwargs):
        super().__init__(
            title=kwargs['title'],
            type='custom',
            content_cls=PopupContent(),
            buttons=[
                MDFlatButton(
                    text='Confirm',
                    theme_text_color='Primary',
                    on_release=self.close
                ),
            ],
        )

        self.action = kwargs['action']
        self.controller = kwargs['controller']

    def close(self, obj):
        self.dismiss()
        self.controller.close_dialog(self.content_cls.ids.input_data.text)


Builder.load_string(kivy)
