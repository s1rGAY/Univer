from kivy.properties import ObjectProperty

from sys import exit

from kivymd.color_definitions import colors
from kivymd.uix.screen import MDScreen
from kivymd.uix.screen import Screen
from kivymd.uix.snackbar import Snackbar
from kivymd.uix.button import MDFlatButton
from kivymd.uix.button import MDFillRoundFlatButton
from kivymd.uix.stacklayout import MDStackLayout
from kivymd.uix.label import MDLabel

from view.popup import PopupWindow


class ViewComponent(MDScreen):
    controller = ObjectProperty()

    def __init__(self, **kw):
        super().__init__(**kw)
        self.screen = Screen()
        self.stack_layout = MDStackLayout(orientation='lr-tb')

        self.car_label = MDLabel(
            text='',
            halign='center',
            theme_text_color='Primary'
        )

        # Done
        default_size_hint = (.25, .1)
        self.on_computer = MDFlatButton(
            text='ON Computer',
            size_hint=default_size_hint,
            on_press=self.on_button_press,
        )
        self.off_computer = MDFlatButton(
            text='OFF Computer',
            size_hint=default_size_hint,
            on_press=self.on_button_press,
        )
        self.add_user = MDFlatButton(
            text='Add User',
            size_hint=default_size_hint,
            on_press=self.on_button_press,
        )
        self.del_user = MDFlatButton(
            text='Del User',
            size_hint=default_size_hint,
            on_press=self.on_button_press,
        )
        self.change_user = MDFlatButton(
            text='Change User',
            size_hint=default_size_hint,
            on_press=self.on_button_press,
        )
        self.enter_command = MDFlatButton(
            text='Enter a command',
            size_hint=default_size_hint,
            on_press=self.on_button_press,
        )
        self.exit_button = MDFillRoundFlatButton(
            text='Exit',
            size_hint=default_size_hint,
            md_bg_color=colors['Green']['A700'],
            on_press=self.on_button_press,
        )

        self.stack_layout.add_widget(self.on_computer)
        self.stack_layout.add_widget(self.off_computer)
        self.stack_layout.add_widget(self.add_user)
        self.stack_layout.add_widget(self.del_user)
        self.stack_layout.add_widget(self.change_user)
        self.stack_layout.add_widget(self.enter_command)
        self.stack_layout.add_widget(self.exit_button)

        self.screen.add_widget(self.car_label)
        self.screen.add_widget(self.stack_layout)

        # обновление автозапуска
        self.update_label()

    def build(self):
        return self.screen

    # обнова инфы для экрана
    def update_label(self):
        self.car_label.text = self.controller.update_computer_information()

    def on_button_press(self, button):
        button_text = button.text

        popup_title = None
        action = None

        if button_text == 'Exit':
            exit()
        elif button_text == 'ON Computer':
            action = 'OnComputer'
            popup_title = 'Sign in: \n\nLogin, password'
        elif button_text == 'OFF Computer':
            action = 'OffComputer'
        elif button_text == 'Add User':
            popup_title = 'Enter information for new User: \n\nLogin, password, operation system'
            action = 'AddUser'
        elif button_text == 'Del User':
            popup_title = 'Enter del User\'s information: \n\nLogin, password'
            action = 'DelUser'
        elif button_text == 'Change User':
            popup_title = 'Enter User\'s information: \n\nLogin, password'
            action = 'ChangeUser'
        elif button_text == 'Enter a command':
            popup_title = 'Enter a command'
            action = 'InnputCommand'

        if action and popup_title:
            self.controller.open_dialog(popup_title, action)
        else:
            self.controller.action_on_computer(action)
            self.update_label()
