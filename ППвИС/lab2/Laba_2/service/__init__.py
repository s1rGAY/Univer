from .tournament_service import TournamentService

from repository import FileXmlHandler, TournamentXmlParser
from logger import Logger
import datetime

parser = TournamentXmlParser()
handler = FileXmlHandler(parser)
service_tournament = TournamentService(handler)
# service_tournament.read_from_sourse('./data.xml')
# service_tournament.insertOne({'id':10101, 'name_tournament': 'NEW', 'date':'2000-10-1', 'type_tournament': 'NEW', 'fio': 'Кто-то там', 'price_tournament': '100'})
