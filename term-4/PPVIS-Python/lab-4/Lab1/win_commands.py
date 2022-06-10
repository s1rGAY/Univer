from Lab1.command_settings import Сommand_settings

class Win_commands(Сommand_settings):
    def __init__(self):
        self.commands = {'cat /dev/null': 'clearing file',
                        'del': 'remove file',
                        'type null >': 'create file',
                        'echo >': 'overwrite file',
                        'echo >>': 'add data to end',
                        'cat': 'view file data'}
