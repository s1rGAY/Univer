from model.command_settings import Сommand_settings

class Linux_commands(Сommand_settings):
    def __init__(self):
        self.commands = {'clear file': 'clearing file',
                          'rm': 'remove file',
                          'touch': 'create file',
                          'echo >': 'overwrite file',
                          'echo >>': 'add data to end',
                          'cat': 'view file data'}
