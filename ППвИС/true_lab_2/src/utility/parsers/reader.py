#if len(self.train_data) == 5: - возможные проблемы
#тк не добавил загрузку времени пути

import xml.sax as sax


class XmlReader(sax.ContentHandler):
    def __init__(self) -> None:
        super().__init__()
        self.table_data = []
        self.train_data = []
        self.parser = sax.make_parser()

    def startElement(self, name, attrs):
        self.current = name
        if name == 'train':
            pass

    def characters(self, content):
        if self.current == 'train_number':
            self.train_number = content
        elif self.current == 'depart_st':
            self.depart_st = content
        elif self.current == 'arriv_st':
            self.arriv_st = content
        elif self.current == 'data_of_departure':
            self.data_of_departure = content
        elif self.current == 'data_of_arrival':
            self.data_of_arrival = content

    def endElement(self, name):
        if self.current == 'train_number':
            self.train_data.append(self.train_number)
        elif self.current == 'depart_st':
            self.train_data.append(self.depart_st)
        elif self.current == 'arriv_st':
            self.train_data.append(self.arriv_st)
        elif self.current == 'data_of_departure':
            self.train_data.append(self.data_of_departure)
        elif self.current == 'data_of_arrival':
            self.train_data.append(self.data_of_arrival)

        if len(self.train_data) == 5:
            self.table_data.append(tuple(self.train_data))
            self.train_data = []

        self.current = ''
