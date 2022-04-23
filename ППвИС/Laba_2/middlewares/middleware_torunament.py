from datetime import datetime


class MiddlewareTournament:
  def __init__(self):
    self.parameters = ["id", "name_tournament", "date", "type_tournament", "fio", "price_tournament", "price"]
    pass

  def contain(self, values):
    for value in values:
      if self.parameters.count(value) == 0:
        return False
    return True

  def checkDTO(self, tournamentDTO): # Data Transfer Object
    for cell in tournamentDTO:
      if tournamentDTO[cell] == "":
        return False
    try:
      int(tournamentDTO["price_tournament"])
      datetime.strptime(tournamentDTO["date"], "%Y-%m-%d")
    except BaseException:
      return False
    return True

  def isNumber(self, value):
    try:
      int(value)
      return True
    except BaseException:
      return False    