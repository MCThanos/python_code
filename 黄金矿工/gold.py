import pygame
from math import sin, cos, pi


def glod(screen, gold_x, gold_y, meet, bool1, bool2, bool3, bool4, bool5, bool6, i, j):
    image_surface_small_gold_2 = pygame.image.load(".\图片\小黄金.gif").convert()
    image_surface_big_gold_3 = pygame.image.load(".\图片\大黄金.gif").convert()
    image_surface_stone_1 = pygame.image.load(".\图片\矿石.png").convert()
    image_surface_stone_1.set_colorkey((255, 255, 255))
    image_surface_small_gold_5 = pygame.image.load(".\图片\小黄金.gif").convert()
    image_surface_big_gold_6 = pygame.image.load(".\图片\大黄金.gif").convert()
    image_surface_stone_4 = pygame.image.load(".\图片\矿石.png").convert()
    image_surface_stone_4.set_colorkey((255, 255, 255))
    if meet == 1:
        screen.blit(image_surface_stone_1, (350 - 0.5 * cos(i / 180 * pi) * j, 210 + 0.5 * sin(i / 180 * pi) * j))
        bool1 = False
    if meet == 2:
        screen.blit(image_surface_small_gold_2, (350 - 0.5 * cos(i / 180 * pi) * j, 210 + 0.5 * sin(i / 180 * pi) * j))
        bool2 = False
    if meet == 3:
        screen.blit(image_surface_big_gold_3, (350 - 0.5 * cos(i / 180 * pi) * j, 210 + 0.5 * sin(i / 180 * pi) * j))
        bool3 = False
    if meet == 4:
        screen.blit(image_surface_stone_4, (350 - 0.5 * cos(i / 180 * pi) * j, 210 + 0.5 * sin(i / 180 * pi) * j))
        bool4 = False
    if meet == 5:
        screen.blit(image_surface_small_gold_5, (350 - 0.5 * cos(i / 180 * pi) * j, 210 + 0.5 * sin(i / 180 * pi) * j))
        bool5 = False
    if meet == 6:
        screen.blit(image_surface_big_gold_6, (350 - 0.5 * cos(i / 180 * pi) * j, 210 + 0.5 * sin(i / 180 * pi) * j))
        bool6 = False
    if meet != 1 and bool1:
        screen.blit(image_surface_stone_1, (gold_x[1], gold_y[1]))
    if meet != 2 and bool2:
        screen.blit(image_surface_small_gold_2, (gold_x[2], gold_y[2]))
    if meet != 3 and bool3:
        screen.blit(image_surface_big_gold_3, (gold_x[3], gold_y[3]))
    if meet != 4 and bool4:
        screen.blit(image_surface_stone_4, (gold_x[4], gold_y[4]))
    if meet != 5 and bool5:
        screen.blit(image_surface_small_gold_5, (gold_x[5], gold_y[5]))
    if meet != 6 and bool6:
        screen.blit(image_surface_big_gold_6, (gold_x[6], gold_y[6]))
