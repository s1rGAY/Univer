from view.view import ViewComponent
from datetime import datetime

class ControllerComponent:
    def __init__(self, model):
        self.model = model
        self.view = ViewComponent(table=self.model.table, controller=self,)
        self._observers = []
        self.subscribe(self.view)

    def refresh(self):
        self.model.refresh_trains()

    def get_screen(self):
        return self.view.build()

    def dialog(self, window_type, dialog):
        self.open_dialog(window_type, dialog)
        
    def input_train(self, data):
        for i in range(len(data)):
            value = None
            if i == 0:
                try:
                    value = int(data[i])
                except ValueError:
                    value = 0
            elif i>0 and i<3:
                try:
                    value = str(data[i])
                except ValueError:
                    value = 'Heaven'
            else:
                try:
                    value = datetime.strptime(data[i], "%d/%m/%Y %H:%M:%S")
                except ValueError:
                    value = datetime.now()
        
            data[i] = value

        self.model.add_new_train(row=data)

    def filter_trains(self, data):
        self.model.filter_trains(filters=data)

    def delete_trains(self, data):
        deleted = self.model.delete_trains(filters=data)
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
