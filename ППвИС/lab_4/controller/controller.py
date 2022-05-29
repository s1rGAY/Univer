from view.view import ViewComponent

class ControllerComponent():
    def __init__(self, model):
        self.model = model

        self.view = ViewComponent()

    def get_screen(self):
        return self.view.build()

    def add_computer(self):
        #добавлерние компьютера
        pass

    def turn_status(self):
        self.model.turn_computer_power_status()

    def get_computer_name(self):
        return self.model.get_computer_name()

    #Rebuilded without view
    def add_user(self,user_login, user_password, user_systme_type):
        if self.model.get_power_status():
            self.model.add_user(self, user_login, user_password, user_systme_type)
        else:
            print('\nComputer status - OFF\n')








    #Надо решить проблему с видом и чеком
    def del_user(self):
        if self.model.get_power_status():
            print('\n DELETING A USER \nTo remove user you must know it\'s login and password.')
            
            permission_data = self.model.__check_access_rights()
            if permission_data[0] == True:
                self.storage._delete_user(permission_data[1])
                self.users.remove(permission_data[1])

        else:
            print('Computer status - OFF')

    









    def re_login(self):
        self.model.__loggin()
    

    def enter_command(self, command):
        self.model(command)

    def print_free_space_in_storage(self):
        return self.model.free_user_memory()

    
    #допилить
    def save_system_state(self):
        #Сохранить состояние системы.
        pass

    #допилить
    def load_last_saved_state(self):
        #Загрузить последнее сохраненное состояние.
        pass
