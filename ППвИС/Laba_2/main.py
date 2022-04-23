from views import MyApp

from service import service_tournament
from controllers import TournamentController

if __name__ == "__main__":
  controller = TournamentController(service_tournament)
  MyApp(controller).run()