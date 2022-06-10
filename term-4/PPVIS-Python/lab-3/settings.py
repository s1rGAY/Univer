import math

# общие параметры
WIDTH = 1200
HEIGHT = 800
HALF_WIDTH = WIDTH // 2
HALF_HEIGHT = HEIGHT // 2
DOUBLE_WIDTH = 2 * WIDTH
DOUBLE_HEIGHT = 2 * HEIGHT
PENTA_HEIGHT = 5 * HEIGHT
FPS = 60
TILE = 100 #размер квадрата карты
FPS_POS = (WIDTH - 65, 5) #позиция для fps

# параметры для карты
MINIMAP_SCALE = 5 #маштабирующий коэф для карты
MAP_RES = (WIDTH // MINIMAP_SCALE, HEIGHT // MINIMAP_SCALE) #для квадрата
MAP_SCALE = 2 * MINIMAP_SCALE # 1 -> 12 x 8, 2 -> 24 x 16, 3 -> 36 x 24
MAP_TILE = TILE // MAP_SCALE
MAP_POS = (0, HEIGHT - HEIGHT // MINIMAP_SCALE)

# параметры лучей
FOV = math.pi / 3 #угол обзора
HALF_FOV = FOV / 2 #основной луч
NUM_RAYS = 300 #количество лучей
MAX_DEPTH = 800 #дальность прорисовки
DELTA_ANGLE = FOV / NUM_RAYS #угол между лучами
DIST = NUM_RAYS / (2 * math.tan(HALF_FOV)) #расстояние до объекта
PROJ_COEFF = 3 * DIST * TILE #проекция (на 3 чтоб стена не была так сильно растянута)
SCALE = WIDTH // NUM_RAYS #маштабирующий коэф

# параметры спрайтов(фикс для скрытия)
DOUBLE_PI = math.pi * 2
CENTER_RAY = NUM_RAYS // 2 - 1
FAKE_RAYS = 200 #для дополнительного отображения(после половины)
FAKE_RAYS_RANGE = NUM_RAYS - 1 + 2 * FAKE_RAYS

# параметры текстур
TEXTURE_WIDTH = 1200
TEXTURE_HEIGHT = 1200
HALF_TEXTURE_HEIGHT = TEXTURE_HEIGHT // 2 #маштабирующий коэф для квадрата карты
TEXTURE_SCALE = TEXTURE_WIDTH // TILE

# параметры для игрока
player_pos = (HALF_WIDTH // 4, HALF_HEIGHT - 50)
player_angle = 0
player_speed = 5
player_rotation_speed = 0.02

#это база
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (220, 0, 0)
GREEN = (0, 80, 0)
BLUE = (0, 0, 255)
DARKGRAY = (40, 40, 40)
PURPLE = (120, 0, 120)
SKYBLUE = (0, 186, 255)
YELLOW = (220, 220, 0)
SANDY = (244, 164, 96)
DARKBROWN = (97, 61, 25)
DARKORANGE = (255, 140, 0)