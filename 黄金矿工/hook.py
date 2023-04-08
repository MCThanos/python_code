import pygame
import time
from math import sin, cos, pi


def hook(screen, i, run, j):
    if run == True:
        image_surface_hook1 = pygame.image.load(".\图片\钩子.jpg").convert()
        image_surface_hook1.set_colorkey((255, 255, 255))
        image_surface_hook = pygame.transform.rotate(image_surface_hook1, i + 270)
        screen.blit(image_surface_hook, (350, 160))
        time.sleep(0.1)
    if run == False:
        image_surface_hook1 = pygame.image.load(".\图片\钩子.jpg").convert()
        image_surface_hook1.set_colorkey((255, 255, 255))
        image_surface_hook = pygame.transform.rotate(image_surface_hook1, i + 270)
        screen.blit(image_surface_hook, (350 - 0.5 * cos(i / 180 * pi) * j, 160 + 0.5 * sin(i / 180 * pi) * j))

def back(i, j):
    if (350 - 0.5 * cos(i / 180 * pi) * j) <= 0:
        return 1
    elif (160 + 0.5 * sin(i / 180 * pi) * j) >= 850:
        return 1
    elif 580>=(350 - 0.5 * cos(i / 180 * pi) * j)>=480 and 280>=(160 + 0.5 * sin(i / 180 * pi) * j)>=210:
        return 1
    elif 180 >= (350 - 0.5 * cos(i / 180 * pi) * j) >= 80 and 530 >= (160 + 0.5 * sin(i / 180 * pi) * j) >= 460:
        return 1
    elif 80>=(350 - 0.5 * cos(i / 180 * pi) * j)>=0 and 380>=(160 + 0.5 * sin(i / 180 * pi) * j)>=310:
        return 1
    elif 380 >= (350 - 0.5 * cos(i / 180 * pi) * j) >= 280 and 580 >= (160 + 0.5 * sin(i / 180 * pi) * j) >= 510:
        return 1
    elif 280 >= (350 - 0.5 * cos(i / 180 * pi) * j) >= 180 and 680 >= (160 + 0.5 * sin(i / 180 * pi) * j) >= 610:
        return 1
    elif 580 >= (350 - 0.5 * cos(i / 180 * pi) * j) >= 480 and 430 >= (160 + 0.5 * sin(i / 180 * pi) * j) >= 360:
        return 1
    else:
        return 0


