from datetime import datetime
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.button import Button

# custom module
from service import TournamentService
from middlewares import MiddlewareTournament
from logger import Logger

class TournamentController:
  def __init__(self, service: TournamentService):
    self.service = service
    self.middleware = MiddlewareTournament()
    self.viewer = None
    self.current_filter = None
    self.logger = Logger()

  def init_viewer(self, viewer):
    self.viewer = viewer

  def getAllRecords(self):
    return  self.service.find(self.current_filter) 

  def filterDataSearch_1(self):
    inputOne = self.viewer["SEARCH"]["search_1th"]["input_column"].text

    compare = {
      "ID": "id",
      "Название турнира": "name_tournament",
      "Дата проведения": "date",
      "Название вида спорта": "type_tournament",
      "ФИО победителя": "fio",
      "Размер призовых турнира": "price_tournament",
      "Название турнира": "name_tournament",
      "Заработок победителя (60% от размера призовых)": "price",
    }

    for key in compare:
      if inputOne == key:
        inputOne = compare[key]

    inputTwo = self.viewer["SEARCH"]["search_1th"]["input_elem"].text
    if self.current_filter == None:
      self.current_filter = dict()
    if self.middleware.contain([inputOne]):
      if (inputOne == "price" or inputOne == "price_tournament"):
        if self.middleware.isNumber(inputTwo) is False:
            self.viewer["SETTINGS"]["logStatus"].text = 'Inputs in filter is uncorrectly...'
            return
        else:
          self.current_filter[inputOne] = int(inputTwo)
      else:
        self.current_filter[inputOne] = inputTwo
      self.rewrite()
      return
    self.viewer["SETTINGS"]["logStatus"].text = 'Inputs in filter is uncorrectly...'

  def filterDataSearch_2(self):
    input_fio = self.viewer["SEARCH"]["search_2th"]["input_fio"].text
    if self.current_filter == None:
      self.current_filter = dict()
    self.current_filter["fio"] = input_fio
    self.rewrite()

  def filterDataSearch_3(self):
    input_min = self.viewer["SEARCH"]["search_3th"]["input_min"].text
    input_max = self.viewer["SEARCH"]["search_3th"]["input_max"].text
    
    if input_min == "":
      input_min = None
    if input_max == "":
      input_max = None

    if (input_max == None or self.middleware.isNumber(input_max) is True) and (input_min == None or self.middleware.isNumber(input_min) is True):
      if self.current_filter == None:
        self.current_filter = dict()
      self.current_filter["price_tournament_limited"] = {
        "min": None,
        "max": None,
      }
      if input_min != None:
        self.current_filter["price_tournament_limited"]["min"] = int(input_min)
      if input_max != None:
        self.current_filter["price_tournament_limited"]["max"] = int(input_max)

      self.rewrite()
    self.viewer["SETTINGS"]["logStatus"].text = 'Inputs in filter is uncorrectly...'
    



  def clearFilter(self):
    self.current_filter = None

  def rightClick(self):
    if self.viewer["CURRENT"] * self.viewer["ROWS"] < len(self.getAllRecords()):
      self.viewer["CURRENT"] += 1
      self.rewrite()

  def leftClick(self):
    if self.viewer["CURRENT"] > 1:
      self.viewer["CURRENT"] -= 1
      self.rewrite()

  def rightDoubleClick(self):
    self.viewer["CURRENT"] = len(self.getAllRecords()) // self.viewer["ROWS"] + 1
    print(self.viewer["CURRENT"])
    self.rewrite()

  def leftDoubleClick(self):
    self.viewer["CURRENT"] = 1
    self.rewrite()



  def openFile(self):
    path = self.viewer["OPEN"]["input_path"].text
    if self.service.read_from_sourse(path) == False:
      self.viewer["SETTINGS"]["logStatus"].text = 'Error in upload, can you check path...'
    else:
      self.updateDropDown()
      self.rewrite()

  def saveData(self):
    path = self.viewer["SAVE"]["input_way"].text
    name_file = self.viewer["SAVE"]["file_name"].text
    if self.service.update_to_file(path + name_file) == False:
      self.viewer["SETTINGS"]["logStatus"].text = 'Error in save, can you check path or correct of data...'
    else:
      self.viewer["SETTINGS"]["logStatus"].text = 'Data was saved successfully...'
    

  def insertData(self):
    parametrs = {
          "id": "some",
          "name_tournament" : None,
          "date" : None,
          "type_tournament" : None,
          "fio" : None,
          "price_tournament" : None,
          "price": "some",
    }

    parametrs["name_tournament"] = self.viewer["ADD"]["input_1"].text
    parametrs["date"] = self.viewer["ADD"]["input_2"].text
    parametrs["type_tournament"] = self.viewer["ADD"]["input_3"].text
    parametrs["fio"] = self.viewer["ADD"]["input_4"].text
    #parametrs["price_tournament"] = self.viewer["ADD"]["input_5"].text

    if self.middleware.checkDTO(parametrs) is True:
      parametrs["price_tournament"] = int(self.viewer["ADD"]["input_5"].text)
      parametrs["date"] = datetime.strptime(parametrs["date"], "%Y-%m-%d")
    else:
      self.viewer["SETTINGS"]["logStatus"].text = 'Uncorrect data, can you check...'
      return

    if self.service.insertOne(parametrs) is True:
      self.rewrite()
      self.viewer["SETTINGS"]["logStatus"].text = 'Data was added successfully...'
      self.updateDropDown()
    else:
      self.viewer["SETTINGS"]["logStatus"].text = 'Error in insert data, can you data again...'



  def updateDropDown(self):
    type_tournaments = self.service.peekTournamentTypes()
    self.viewer["ADD"]["dropDown"].clear_widgets()
    for index in type_tournaments:
          btn = Button(text=index, size_hint_y=None, height=44)
          btn.bind(on_release=lambda btn: self.viewer["ADD"]["dropDown"].select(btn.text))
          self.viewer["ADD"]["dropDown"].add_widget(btn)




  def rewrite(self):
    self.viewer["SETTINGS"]["logStatus"].text = ""
    self.viewer["gridTable"].clear_widgets()

    amount = 0
    count = 0

    if self.viewer["CURRENT"] * self.viewer["ROWS"] > len(self.getAllRecords()):
        amount = len(self.getAllRecords())
        count = (self.viewer["CURRENT"] * self.viewer["ROWS"] - len(self.getAllRecords()))
        print(count)
    else:
        amount = self.viewer["CURRENT"] * self.viewer["ROWS"]

    for i in range((self.viewer["CURRENT"] - 1) * self.viewer["ROWS"], amount):
        for j in self.getAllRecords()[i]:
            self.viewer["gridTable"].add_widget(Label(text = str(self.getAllRecords()[i][j])))

    if count < self.viewer["ROWS"]:
        for i in range(0, count):
            for j in range(0, self.viewer["COLUMNS"]):
                self.viewer["gridTable"].add_widget(Label(text = ""))



  def filterDataDelete_1(self):
    self.viewer["CURRENT"] = 1
    inputOne = self.viewer["DELETE"]["delete_1th"]["input_column"].text

    compare = {
      "ID": "id",
      "Название турнира": "name_tournament",
      "Дата проведения": "date",
      "Название вида спорта": "type_tournament",
      "ФИО победителя": "fio",
      "Размер призовых турнира": "price_tournament",
      "Название турнира": "name_tournament",
      "Заработок победителя (60% от размера призовых)": "price",
    }

    for key in compare:
      if inputOne == key:
        inputOne = compare[key]

    inputTwo = self.viewer["DELETE"]["delete_1th"]["input_elem"].text
    if self.current_filter == None:
      self.current_filter = dict()
    if self.middleware.contain([inputOne]):
      if (inputOne == "price" or inputOne == "price_tournament"):
        if self.middleware.isNumber(inputTwo) is False:
            self.viewer["SETTINGS"]["logStatus"].text = 'Inputs in filter is uncorrectly...'
            return
        else:
          self.current_filter[inputOne] = int(inputTwo)
      else:
        self.current_filter[inputOne] = inputTwo
      self.removeByFilter()         
      self.clearFilter()
      self.rewrite()
      return
    else:
      self.viewer["SETTINGS"]["logStatus"].text = 'Inputs in filter is uncorrectly...'

  def filterDataDelete_2(self):
    self.viewer["CURRENT"] = 1
    input_fio = self.viewer["DELETE"]["delete_2th"]["input_fio"].text
    if self.current_filter == None:
      self.current_filter = dict()
    self.current_filter["fio"] = input_fio
    self.removeByFilter()
    self.clearFilter()
    self.rewrite()

  def filterDataDelete_3(self):
    self.viewer["CURRENT"] = 1
    input_min = self.viewer["DELETE"]["delete_3th"]["input_min"].text
    input_max = self.viewer["DELETE"]["delete_3th"]["input_max"].text
    
    if input_min == "":
      input_min = None
    if input_max == "":
      input_max = None

    if (input_max == None or self.middleware.isNumber(input_max) is True) and (input_min == None or self.middleware.isNumber(input_min) is True):
      if self.current_filter == None:
        self.current_filter = dict()
      self.current_filter["price_tournament_limited"] = {
        "min": None,
        "max": None,
      }
      if input_min != None:
        self.current_filter["price_tournament_limited"]["min"] = int(input_min)
      if input_max != None:
        self.current_filter["price_tournament_limited"]["max"] = int(input_max)
      self.removeByFilter()
      self.clearFilter()
      self.rewrite()
    self.viewer["SETTINGS"]["logStatus"].text = 'Inputs in filter is uncorrectly...'
    

  def removeByFilter(self):
    try:
      self.service.findAndDelete(self.current_filter)
      self.viewer["SETTINGS"]["logStatus"].text = 'Delete is successfaly...'
    except BaseException:
      self.viewer["SETTINGS"]["logStatus"].text = 'Error in delete...'
