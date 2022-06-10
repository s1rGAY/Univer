from Lab1.command_settings import Сommand_settings

class macOS_commands(Сommand_settings):
    def __init__(self):
        self.commands = {'echo -n': 'clearing file',
                          'rm': 'remove file',
                          'nano': 'create file',
                          'echo >': 'overwrite file',
                          'echo >>': 'add data to end',
                          'cat': 'view file data'}

