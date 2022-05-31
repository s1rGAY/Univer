from view.view import ViewComponent
from view.popup import PopupWindow
from kivymd.uix.snackbar import Snackbar


class ControllerComponent:
    def __init__(self, model):
        self.model = model
        self.view = ViewComponent(controller=self)
        self.dialog = None

    def get_screen(self):
        return self.view.build()

    def open_dialog(self, title, action):
        self.dialog = PopupWindow(
            controller=self,
            title=title,
            action=action,
        )

        self.dialog.open()

    def close_dialog(self, data):
        converted_data = None
        try:
            converted_data = str(data).split(', ')
            self.action_on_computer(self.dialog.action, converted_data)
        except ValueError:
            Snackbar(text='Error! Invalid data given.').open()

        self.dialog = None
        self.view.update_label()

    def action_on_computer(self, action, additional_data=None):

        if action == 'OnComputer':  # DONE
            if self.model.computer.get_power_status() is False:
                self.model.computer.turn_computer_power_status(additional_data[0], additional_data[1])
        elif action == 'OffComputer':  # DONE
            if self.model.computer.get_power_status():
                self.model.computer.turn_computer_power_status()
        elif action == 'AddUser':  # DONE
            self.model.computer.add_user(additional_data[0],
                                         additional_data[1],
                                         additional_data[2])
        elif action == 'DelUser':  # DONE
            self.model.computer.del_user(additional_data[0],
                                         additional_data[1])
        elif action == 'ChangeUser':  # DONE
            self.model.computer.change_logged_user(additional_data[0],
                                                   additional_data[1],)
        elif action == 'InnputCommand':  # DONE
            self.model.computer.enter_command(additional_data)

    def update_computer_information(self):
        return self.model.update_computer_information()
