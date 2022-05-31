from abstractions.logger import AbstractLogger


class ModelComponent():

    def __init__(self, computer, logger: AbstractLogger):
        self.computer = computer  # передача ранее созданной тачки УДАЛИТЬ
        self.logger: AbstractLogger = logger  # лог не надо трогать

    def on_computer(self):
        if self.computer.get_power_status() is False:
            self.car.turn_computer_power_status()

    def off_computer(self):
        if self.computer.get_power_status():
            self.computer.turn_computer_power_status()

    def add_user(self, user_login, user_password, user_systme_type):
        self.computer.add_user(self, user_login, user_password,
                               user_systme_type)

    def del_user(self):  # разобраться с чекингом/убрать его
        pass

    def free_user_memory(self):
        return self.computer.storage.get_free_user_storage_size()

    def enter_command(self, command):
        self.computer.enter_command(self, command)

    # переписать апдейт для компа
    def update_computer_information(self) -> str:
        self.logger.disable_logging()
        current_data: str = 'Computer name : '
        current_data += str(self.computer.get_computer_name())+'\n'

        current_data += 'Power status is'
        if self.computer.get_power_status():
            current_data += ' ON.\n'
            current_data += 'Logged user: ' + str(self.computer.get_logged_user().get_login()) + '\n'

            current_data += 'User operation system : ' + str(self.computer.get_logged_user().get_operation_system_type()) + '\n'
            current_data += 'Storage : ' + str(self.computer.free_user_memory())
        else:
            current_data += ' OFF.\n'

        self.logger.enable_logging()
        return current_data
