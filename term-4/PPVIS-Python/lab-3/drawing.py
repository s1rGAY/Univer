#отрисовка всех элементов
import pygame
from settings import *
from map import mini_map
from collections import deque
from random import randrange
import sys

path = '/home/siarhei/Programming/IIT/Univer/ППвИС/lab_3/'

class Drawing:
    def __init__(self, sc, sc_map, player, clock):
        self.sc = sc #основная поверхность
        self.sc_map = sc_map
        self.player = player
        self.clock = clock
        self.font = pygame.font.SysFont('Arial', 36, bold=True) #отображение кол-ва кадров
        self.font_win = pygame.font.Font(path+'font/font.ttf', 144)
        
        #атрибут для текстур
        # словарь, тк удобнее потом писать запрос на вывод
        self.textures = {1: pygame.image.load(path+'img/wall6.png').convert(),
                         2: pygame.image.load(path+'img/wall5.png').convert(),
                         3: pygame.image.load(path+'img/wall3.png').convert(),
                         4: pygame.image.load(path+'img/wall7.png').convert(),
                         'S': pygame.image.load(path+'img/sky3.png').convert(),
                         }
        # menu
        self.menu_trigger = True
        self.menu_picture = pygame.image.load(path+'img/bg.jpg').convert()
        # weapon parameters
        self.weapon_base_sprite = pygame.image.load(path+'sprites/weapons/shotgun/base/0.png').convert_alpha()
        self.weapon_shot_animation = deque([pygame.image.load(f'/home/siarhei/Programming/IIT/Univer/ППвИС/lab_3/sprites/weapons/shotgun/shot/{i}.png')
                                 .convert_alpha() for i in range(10)])
        self.weapon_rect = self.weapon_base_sprite.get_rect()
        self.weapon_pos = (HALF_WIDTH - self.weapon_rect.width // 2, HEIGHT - self.weapon_rect.height)
        self.shot_length = len(self.weapon_shot_animation)
        self.shot_length_count = 0
        self.shot_animation_trigger = True
        self.shot_animation_speed = 3
        self.shot_animation_count = 0
        self.shot_sound = pygame.mixer.Sound(path+'sound/awp1.mp3')
        # shot SFX
        self.sfx = deque([pygame.image.load(f'/home/siarhei/Programming/IIT/Univer/ППвИС/lab_3/sprites/weapons/sfx/{i}.png').convert_alpha() for i in range(9)])
        self.sfx_length_count = 0
        self.sfx_length = len(self.sfx)

    #отрисовка фона
    def background(self):
        sky_offset = -10 * math.degrees(self.player.angle) % WIDTH
        #в зависимости от смещения разные кадры неба
        self.sc.blit(self.textures['S'], (sky_offset, 0))
        self.sc.blit(self.textures['S'], (sky_offset - WIDTH, 0))
        self.sc.blit(self.textures['S'], (sky_offset + WIDTH, 0))
        pygame.draw.rect(self.sc, DARKGRAY, (0, HALF_HEIGHT, WIDTH, HALF_HEIGHT))

    #отрисовка главной проекции
    def world(self, world_objects):
        for obj in sorted(world_objects, key=lambda n: n[0], reverse=True): #для отрисовки
            if obj[0]:
                _, object, object_pos = obj
                self.sc.blit(object, object_pos)

    #получение fps
    def fps(self, clock):
        display_fps = str(int(clock.get_fps())) #получаем из clock
        render = self.font.render(display_fps, 0, DARKORANGE) #цвет
        self.sc.blit(render, FPS_POS) #размещение (FPS_POS - settings)

    def win(self):
        render = self.font_win.render('YOU WIN!!!', 1, (randrange(40, 120), 0, 0))
        rect = pygame.Rect(0, 0, 1000, 300)
        rect.center = HALF_WIDTH, HALF_HEIGHT
        pygame.draw.rect(self.sc, BLACK, rect, border_radius=50)
        self.sc.blit(render, (rect.centerx - 430, rect.centery - 140))
        pygame.display.flip()
        self.clock.tick(15)

    #отрисовка миникарты
    def mini_map(self):
        self.sc_map.fill(BLACK) #Фон карты
        map_x, map_y = self.player.x // MAP_SCALE, self.player.y // MAP_SCALE #маштабирование позиции
        
        # отрисовка карты и игрока
        pygame.draw.line(self.sc_map, YELLOW, (map_x, map_y), (map_x + 8 * math.cos(self.player.angle),
                                                               map_y + 8 * math.sin(self.player.angle)), 2)
        pygame.draw.circle(self.sc_map, RED, (int(map_x), int(map_y)), 4)
        for x, y in mini_map:
            pygame.draw.rect(self.sc_map, DARKBROWN, (x, y, MAP_TILE, MAP_TILE))
        self.sc.blit(self.sc_map, MAP_POS) #расположение по дефолту

    def player_weapon(self, shot_projections):
        if self.player.shot:
            if not self.shot_length_count:
                self.shot_sound.play()
            self.shot_projection = min(shot_projections)[1] // 2
            self.bullet_sfx()
            shot_sprite = self.weapon_shot_animation[0]
            self.sc.blit(shot_sprite, self.weapon_pos)
            self.shot_animation_count += 1
            if self.shot_animation_count == self.shot_animation_speed:
                self.weapon_shot_animation.rotate(-1)
                self.shot_animation_count = 0
                self.shot_length_count += 1
                self.shot_animation_trigger = False
            if self.shot_length_count == self.shot_length:
                self.player.shot = False
                self.shot_length_count = 0
                self.sfx_length_count = 0
                self.shot_animation_trigger = True
        else:
            self.sc.blit(self.weapon_base_sprite, self.weapon_pos)

    def bullet_sfx(self):
        if self.sfx_length_count < self.sfx_length:
            sfx = pygame.transform.scale(self.sfx[0], (self.shot_projection, self.shot_projection))
            sfx_rect = sfx.get_rect()
            self.sc.blit(sfx, (HALF_WIDTH - sfx_rect.width // 2, HALF_HEIGHT - sfx_rect.height // 2))
            self.sfx_length_count += 1
            self.sfx.rotate(-1)

    def menu(self):
        pygame.mixer.music.load(path+'sound/win.mp3')
        pygame.mixer.music.play()
        button_font = pygame.font.Font(path+'font/font.ttf', 72)
        label_font = pygame.font.Font(path+'font/font1.otf', 400)
        start = button_font.render('GOOOO', 1, pygame.Color('lightgray'))
        button_start = pygame.Rect(0, 0, 400, 150)
        button_start.center = HALF_WIDTH, HALF_HEIGHT
        exit = button_font.render('EXIT', 1, pygame.Color('lightgray'))
        button_exit = pygame.Rect(0, 0, 400, 150)
        button_exit.center = HALF_WIDTH, HALF_HEIGHT + 200

        while self.menu_trigger:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.sc.blit(self.menu_picture, (0, 0), (0 % WIDTH, HALF_HEIGHT, WIDTH, HEIGHT))

            pygame.draw.rect(self.sc, BLACK, button_start, border_radius=25, width=10)
            self.sc.blit(start, (button_start.centerx - 130, button_start.centery - 70))

            pygame.draw.rect(self.sc, BLACK, button_exit, border_radius=25, width=10)
            self.sc.blit(exit, (button_exit.centerx - 85, button_exit.centery - 70))

            color = randrange(40)
            label = label_font.render('SEREGA', 1, (color, color, color))
            self.sc.blit(label, (15, -30))

            mouse_pos = pygame.mouse.get_pos()
            mouse_click = pygame.mouse.get_pressed()
            if button_start.collidepoint(mouse_pos):
                pygame.draw.rect(self.sc, BLACK, button_start, border_radius=25)
                self.sc.blit(start, (button_start.centerx - 130, button_start.centery - 70))
                if mouse_click[0]:
                    self.menu_trigger = False
            elif button_exit.collidepoint(mouse_pos):
                pygame.draw.rect(self.sc, BLACK, button_exit, border_radius=25)
                self.sc.blit(exit, (button_exit.centerx - 85, button_exit.centery - 70))
                if mouse_click[0]:
                    pygame.quit()
                    sys.exit()

            pygame.display.flip()
            self.clock.tick(20)






