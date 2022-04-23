# Interface обработчика 
class Handler:
    def __init__(self, parser):
        self.parser = parser
        pass

    def init_sourse(self, filename):
        pass    

    def read_from_sourse(self):
        pass

    def update_sourse(self, data, path):
        # пишешь обработчик который обновляет данные в self.filename из data
        pass

