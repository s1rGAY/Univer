import xml.sax
from xml.dom import minidom
from datetime import datetime
from random import randint


# Парсер xml файлов
class TournamentXmlParser(xml.sax.ContentHandler):
 
    def __init__(self):
        self.CurrentData = ''
        self.return_value = {
          "id" : 123123,
          "name_tournament" : "",
          "date" : 0,
          "type_tournament" : "asdasds",
          "fio" : "asdsa adsasd asdasd",
          "price_tournament" : 1232
        }
        self.tournaments = list()
        
    # Call when an element starts
    def startElement(self,tag,attributes):
        self.CurrentData=tag
        if tag == 'tournament':
            title = attributes['title']
            self.return_value.update({'id': str(randint(1, 100000))})
            self.return_value.update({'name_tournament':  title})
           

    # Call when an elements ends
    def endElement(self,tag):
        if self.CurrentData == 'prize':
            self.CurrentData = ''
            #print('flag: ', self.return_value)
            new_tournament = {
              "id" : str(self.return_value["id"]),
              "name_tournament" : self.return_value["name_tournament"],
              "date" : self.return_value["date"],
              "type_tournament" : self.return_value["type_tournament"],
              "fio" : self.return_value["fio"],
              "price_tournament" : int(self.return_value["price_tournament"]),
              "price": int (int(self.return_value["price_tournament"]) * 0.6)
            }
            self.tournaments.append(new_tournament)
        else: 
            self.CurrentData = '' 
        
   # Call when a character is read
    def characters(self, content):
        if self.CurrentData == 'date':
            deadline = datetime.strptime(content, "%Y-%m-%d")
            self.return_value.update({'date': deadline})
        elif self.CurrentData == 'kind':
            self.return_value.update({'type_tournament': content})
        elif self.CurrentData == 'winner':
            self.return_value.update({'fio': content})
        elif self.CurrentData == 'prize':
            self.return_value.update({'price_tournament': content})
    
    def getTournaments(self):
      return self.tournaments
