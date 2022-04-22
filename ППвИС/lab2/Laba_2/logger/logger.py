class Logger:
  def __init__(self):
    # something
    pass

  def info(self, message):
    print('\033[32m INFO\033[0m ', message)

  def error(self, message):
    print('\033[31m ERROR\033[0m ', message)

  def debug(self, message):
    print('\033[37m DEBUG\033[0m ', message)

  def warning(self, message):
    print('\033[33m WARNING\033[0m ', message)
