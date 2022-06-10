class Сommand_settings:
    def __init__(self, commands):
        self.commands = commands

    def get_commands(self):
        return self.commands

    def get_command(self, command):
        if command in self.commands.keys():
            return self.commands[command]
        else:
            return False

    def add_command(self, new_command):
        if new_command not in self.commands.keys():
            self.commands[new_command.keys()] = new_command[new_command.keys()]
        else:
            print('This command already exists!')

    def del_command(self, command):
        del self.commands[command]
