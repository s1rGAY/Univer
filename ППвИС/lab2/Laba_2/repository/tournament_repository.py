import xml.sax
from xml.dom import minidom 
from logger import Logger

# custom import 
from .interfaces import Handler

# Обработчик xml файлов принимает в себя парсер того же типа
class FileXmlHandler:
    def __init__(self, parser):
        self.parser = parser
        self.logger = Logger()
        pass

    def init_sourse(self, filename):
        self.filename = filename
    
    def read_from_sourse(self):
        try:
            parser = xml.sax.make_parser() #creating an XMLReader
            parser.setFeature(xml.sax.handler.feature_namespaces,0) #turning off namespaces
            Parser = self.parser
            parser.setContentHandler(Parser) #overriding default ContextHandler
            print(self.filename)
            parser.parse(self.filename)
            self.logger.debug(f"File parse is success")
            return Parser.tournaments
        except:
             return None

    def update_sourse(self, data, path):
        self.logger.warning('UPDATE!!!!!!!!!!!!!!!!!!!!!')
        root = minidom.Document()
        xml = root.createElement('competitions') 
        root.appendChild(xml)
        for i in data:
            self.logger.info("cell " + str(i))
            tournament_child = root.createElement('tournament')
            tournament_child.setAttribute('title', i['name_tournament'])
            xml.appendChild(tournament_child)
            self.logger.info("added tournament")

            date_child = root.createElement('date')
            tournament_child.appendChild(date_child)
            date_text = root.createTextNode(str(i['date'])[:10])
            date_child.appendChild(date_text)
            self.logger.info("added date")

            type_child = root.createElement('kind')
            tournament_child.appendChild(type_child)
            type_text = root.createTextNode(i['type_tournament'])
            type_child.appendChild(type_text)
            self.logger.info("added kind")


            fio_child = root.createElement('winner')
            tournament_child.appendChild(fio_child)
            fio_text = root.createTextNode(i['fio'])
            fio_child.appendChild(fio_text)
            self.logger.info("added winner")


            prize_child = root.createElement('prize')
            tournament_child.appendChild(prize_child)
            prize_text = root.createTextNode(str(i['price_tournament']))
            prize_child.appendChild(prize_text)
            self.logger.info("added prize")



        xml_str = root.toprettyxml(indent ="\t") 
        save_path_file = path

        try:
          f = open(save_path_file, "w", encoding='utf-8')
        except FileNotFoundError:
          self.logger.info(f"File {path} is created")

        f = open(save_path_file, "w", encoding='utf-8')
        f.write(xml_str)
        
