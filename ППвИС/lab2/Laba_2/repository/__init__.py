from .tournament_repository import FileXmlHandler
from .parsers.parser import TournamentXmlParser
from .interfaces import Handler

# Здесь используются два принципа( хотя и очень тупой реализацией, но все же) 
# 1: IoC ( inversion of control ) - инверсия управления
# 2: DI ( dependency injection ) - внедрение зависмостей
#
#  Эти классы не знаю о друг жруге ничего, а просто используют друг друга
#  идет независимость классов друг от друга
#  в любой момент мы можем заменить эти классы, если это нужно