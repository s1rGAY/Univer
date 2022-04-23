from commands_realization import Commands_realization
from linux_commands import Linux_commands
from win_commands import Win_commands
from macos_commands import macOS_commands

class Operation_system:
    def __init__(self, system_type):
        self.type = system_type
        self.commands = None
        self.commands_sourse = Commands_realization()
        if system_type.lower() == 'linux':
            self.type = system_type
            self.commands = Linux_commands()
        elif system_type.lower() == 'windows':
            self.type = system_type
            self.commands = Win_commands()
        elif system_type.lower() == 'macosx':
            self.type = system_type
            self.commands = macOS_commands()
        else:
            print('Invalid operating system name!')
    
    def _get_system_type(self):
        return self.type

    def _get_command(self, command):
        return self.commands.get_command(command)

    def _get_all_commands(self):
        return self.commands.get_commands

    def _delete_command(self,command):
        return self.commands.del_command(command)

    def _run_command(self, command, path):
        if self.commands.get_command(command) == 'clearing file':
            self.commands_sourse.clear_file(file_name=input(),path=path)
        elif self.commands.get_command(command) =='remove file':
            self.commands_sourse.delete_file(file_name=input(),path=path)
        elif self.commands.get_command(command) =='create file':
            self.commands_sourse.create_file(file_name=input(),path=path)
        elif self.commands.get_command(command) =='overwrite file':
            self.commands_sourse.overwrite_file(file_name=input(),path=path)
        elif self.commands.get_command(command) =='add data to end':
            self.commands_sourse.add_data_to_end(file_name=input(),path=path)
        elif self.commands.get_command(command) =='view file data':
            self.commands_sourse.view_file_data(file_name=input(),path=path)
        else:
            print('\nNo such command!\n')
