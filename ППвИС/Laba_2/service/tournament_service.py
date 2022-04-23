from ast import Try
from random import randint
from repository import Handler
from logger import Logger
from datetime import datetime

# А это уже сервис (он не знает кто обрабатывает файлы и как (и то, что это вообще файлы))
# filename - может указывать на файл( а может и указывать на название базы данных(путь или что нибудь еще))
class TournamentService:
    def __init__(self, handler: Handler):
        self.list_of_tournaments = list()
        self.handler = handler
        self.logger = Logger()

    def read_from_sourse(self, filename):
        try:
          self.handler.init_sourse(filename)
          list_of_tournaments = self.handler.read_from_sourse()
          self.logger.debug(f"Success file upload: {list_of_tournaments}") # - ПОЧЕМУ ?! ШО НЕ ТАК
          if list_of_tournaments == None:
            return False
          self.list_of_tournaments = list_of_tournaments
        except Exception:
          return False
        return True

    def insertOne(self, data):
      try:
        data["id"] = str(randint(1, 100000))
        data["price"] = int(data["price_tournament"] * 0.6)
        self.list_of_tournaments.append(data)
        #self.logger.info('List is sucessfully updated' + str(self.list_of_tournaments))
      except BaseException:
        return False
      return True

    def update_to_file(self, path):
      try:
        print(path)
        print(self.list_of_tournaments)
        self.handler.update_sourse(self.list_of_tournaments, path)
        return True
      except FileNotFoundError:
        self.logger.error("some error in upload")
        return False
    
    def find(self, findBy: None):
      findedList = list()
      for cell in self.list_of_tournaments:
        flag = True
        if findBy is not None:
          for filter in findBy:
            if filter == "price_tournament_limited":
              if findBy["price_tournament_limited"]["max"] is not None:
                if cell["price_tournament"] > findBy["price_tournament_limited"]["max"]:
                  flag = False
                  break
              if findBy["price_tournament_limited"]["min"] is not None:
                if cell["price_tournament"] < findBy["price_tournament_limited"]["min"]:
                  flag = False
                  break
            elif filter == "fio":
              filtres = findBy[filter].split(" ")
              for i in filtres:
                if cell[filter].split(" ").count(i) == 0:
                  flag = False
                  break
            elif cell[filter] != findBy[filter]:
              flag = False
              break
            else:
              continue
        if flag is True:
          findedList.append(cell)
      return findedList

    def findAndDelete(self, filter):
      list_for_remove = self.find(filter)
      for cell in list_for_remove:
        self.findByIdAndDelete(cell["id"])
      return True

      # вернуть массив записей подходящих под критерии, которые описаны в findBy, иначе пустой массив
      # Например (это же словарь)
      #  В findBy могут быть такие как 
      #  date
      #  type_tournament    
      #  ищешь все записи подходящии под данное условие (чтобы были равны и date и type_tournament)

      # и да, кстати пользователь может в критерий посика внести id( index в массиве ) для поиска

      # дополнительный функционал: если критериев нет, то все данные выдаешь(ведь все подходят)

    def findById(self, index):
      resulted_list = list(filter(lambda x: x['id'] ==index, self.list_of_tournaments))
      return resulted_list if resulted_list else False
    

    def findByIdAndDelete(self, index):
      for i in self.list_of_tournaments:
        if i['id'] == index:
          self.list_of_tournaments.remove(i)
          return True
      return False

  
    def findByIdAndUpdate(self, index, data):
      # data может хранить не все поля, а только некоторые(которые нужно обновить)

      # вернуть true если все хорошо
      # false в ином
      pass

    def findBetween(self, data, minLimit, maxLimit):
      # Ищешь все записи по критерию, который находится в data
      # между minLimit и maxLimit
      # выдать все записи, подходящии данному критерию
      # иначе пустой массив
      pass

    def peekTournamentTypes(self):
      kind_of_sports=[]
      for i in self.list_of_tournaments:
        if kind_of_sports.count(i['type_tournament']) == 0:
          kind_of_sports.append(i['type_tournament'])
      return kind_of_sports if kind_of_sports else False
