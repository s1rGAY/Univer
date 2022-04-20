class User:
    def __init__(self, login, password, operation_system_type):
        self.login = login
        self.password = password
        self.operation_system_type = operation_system_type
    
    def _set_login(self, login):
        self.login = login

    def get_login(self):
        return self.login

    def _set_password(self, password):
        self.password = password
    
    def _get_password(self):
        return self.password
        
    def _set_operation_system_type(self, operation_system_type):
        self.operation_system_type = operation_system_type

    def get_operation_system_type(self):
        return self.operation_system_type

    def get_all_user_info(self):
        return self.login, self.password, self.operation_system_type

    def change_user_info(self):
        print('Please, enter password :')
        password = input()
        if password is self.password:
            print('What would you change?')
            param = input()
            if param == 'login':
                print('Please, enter new Login : ')
                self.login = str(input())
            elif param == 'password':
                print('Please, enter new Password : ')
                self.password = str(input())
            else:
                print('No such param')
        else:
            print('Access denied!')