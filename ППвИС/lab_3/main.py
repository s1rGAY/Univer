from player import Player
from sprite_objects import *
from ray_casting import ray_casting_walls
from drawing import Drawing
from interaction import Interaction

pygame.init()
sc = pygame.display.set_mode((WIDTH, HEIGHT), pygame.DOUBLEBUF)#настройка основного окна
clock = pygame.time.Clock()#установление кадров в секунду

sc_map = pygame.Surface(MAP_RES) #отрисовка миникарты на отдельной поверхности (уменьшнной в 5(коэф) раз)
sprites = Sprites()
player = Player(sprites)
drawing = Drawing(sc, sc_map, player, clock) #конструктор класса для рисования
interaction = Interaction(player, sprites, drawing)

drawing.menu()
pygame.mouse.set_visible(True)
interaction.play_music()

#цикл для итераций игры
while True:

    player.movement()
    drawing.background()
    walls, wall_shot = ray_casting_walls(player, drawing.textures)
    drawing.world(walls + [obj.object_locate(player) for obj in sprites.list_of_objects]) #вычисление параметров стен и возвращенные объекты
    drawing.fps(clock)
    drawing.mini_map()
    drawing.player_weapon([wall_shot, sprites.sprite_shot])

    interaction.interaction_objects()
    interaction.npc_action()
    interaction.clear_world()
    interaction.check_win()

    pygame.display.flip()#обновление вывода на каждой итерации
    clock.tick()#задержка для FPS