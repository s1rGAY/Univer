from view.view import ViewComponent


class ControllerComponent:
    def __init__(self, model):
        self.model = model
        self.view = ViewComponent(table=self.model.table, controller=self,)
        self._observers = []
        self.subscribe(self.view)

    def refresh(self):
        self.model.refresh_students()

    def get_screen(self):
        return self.view.build()

    def dialog(self, window_type, dialog):
        self.open_dialog(window_type, dialog)

    def input_student(self, data):
        # pipeline to handle invalid characters in inputs
        for i in range(1, len(data)):
            value = None
            try:
                value = int(data[i])
            except ValueError:
                value = 0

            data[i] = value
        self.model.add_new_student(row=data)

    def filter_students(self, data):
        self.model.filter_students(filters=data)

    def delete_students(self, data):
        deleted = self.model.delete_students(filters=data)
        return deleted

    def upload_from_file(self, data):
        self.model.read_data(path=data)

    def save_in_file(self, data):
        self.model.write_data_to_file(path=data)

    def open_dialog(self, dialog, mode):
        self.dialog = dialog

    def close_dialog(self, dialog_data: list = []):
        data = dialog_data
        self.model.notify(data)
        self.dialog = data

    def subscribe(self, observer):
        self._observers.append(observer)

    def unsubscribe(self, observer):
        self._observers.remove(observer)

    def notify(self, data):
        for x in self._observers:
            x.on_controller_change(data)
