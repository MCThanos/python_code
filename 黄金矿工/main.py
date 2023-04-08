import pygame
import sys
from pygame.locals import *
import hook as hook
from math import sin, cos, pi
import gold as gold


def run_game():
    pygame.init()
    screen = pygame.display.set_mode((768, 800))
    pygame.display.set_caption("黄金矿工")
    pygame.mixer.music.load('祖海-好运来.mp3')
    pygame.mixer.music.play()
    image_surface_sky = pygame.image.load(".\图片\天空.jpg").convert()
    image_surface_background = pygame.image.load(".\图片\背景.jpg").convert()
    image_surface_man = pygame.image.load(".\图片\矿工.jpg").convert()
    image_surface_man.set_colorkey((255, 255, 255))
    a = True
    b = False
    run = True
    i = 1
    j = 1
    back = 0
    meet = 0
    gold_x = [0, 550, 150, 50, 350, 250, 550]
    gold_y = [0, 250, 500, 350, 550, 650, 400]
    bool1 = True
    bool2 = True
    bool3 = True
    bool4 = True
    bool5 = True
    bool6 = True
    game = False
    while True:
        if (
                bool1 != True and bool2 != True and bool3 != True and bool4 != True and bool5 != True and bool6 != True) or game:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
            screen.fill((255, 255, 255))
            font = pygame.font.SysFont("freesansbold.ttf", 80)
            text = font.render("GAME OVER!", True, (0, 0, 0))
            screen.blit(text, (200, 300))
            pygame.mixer.music.stop()
            pygame.display.update()
        else:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
            key = pygame.key.get_pressed()
            if key[K_SPACE]:
                print('space')
                run = False
            screen.blit(image_surface_sky, (0, 0))
            screen.blit(image_surface_background, (0, 200))
            screen.blit(image_surface_man, (311.5, 48))
            back = back + int(hook.back(i, j))
            if i == 180 or i == 0:
                a, b = b, a
            if a == True and run == True:
                i = i + 1
            if b == True and run == True:
                i = i - 1
            if run == False and back == 0:
                j = j + 1
            if run == False and j >= 0 and back > 0:
                j = j - 1
            if (350 - 0.5 * cos(i / 180 * pi) * j) <= 0:
                game = True
            if (160 + 0.5 * sin(i / 180 * pi) * j) >= 750:
                game = True
            if 580 >= (350 - 0.5 * cos(i / 180 * pi) * j) >= 480 and 280 >= (160 + 0.5 * sin(i / 180 * pi) * j) >= 210:
                meet = 1
                bool1 = False
            if 180 >= (350 - 0.5 * cos(i / 180 * pi) * j) >= 80 and 530 >= (160 + 0.5 * sin(i / 180 * pi) * j) >= 460:
                meet = 2
                bool2 = False
            if 80 >= (350 - 0.5 * cos(i / 180 * pi) * j) >= 0 and 380 >= (160 + 0.5 * sin(i / 180 * pi) * j) >= 310:
                meet = 3
                bool3 = False
            if 380 >= (350 - 0.5 * cos(i / 180 * pi) * j) >= 280 and 580 >= (160 + 0.5 * sin(i / 180 * pi) * j) >= 510:
                meet = 4
                bool4 = False
            if 280 >= (350 - 0.5 * cos(i / 180 * pi) * j) >= 180 and 680 >= (160 + 0.5 * sin(i / 180 * pi) * j) >= 610:
                meet = 5
                bool5 = False
            if 580 >= (350 - 0.5 * cos(i / 180 * pi) * j) >= 480 and 430 >= (160 + 0.5 * sin(i / 180 * pi) * j) >= 360:
                meet = 6
                bool6 = False
            gold.glod(screen, gold_x, gold_y, meet, bool1, bool2, bool3, bool4, bool5, bool6, i, j)
            hook.hook(screen, i, run, j)
            pygame.display.update()
            if j == 0:
                a = True
                b = False
                run = True
                i = 1
                j = 1
                back = 0
                meet = 0


if __name__ == '__main__':
    run_game()
