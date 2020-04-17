#!/usr/bin/env python3
import sys
import pygame
from pygame.locals import QUIT, MOUSEBUTTONDOWN, MOUSEMOTION, MOUSEBUTTONUP, KEYDOWN, K_SPACE, K_ESCAPE, K_UP, K_LEFT, K_RIGHT, K_DOWN
import pyautogui
import random

pygame.init()
window_x, window_y = pyautogui.size()
window, string_x = (int(window_x/2), window_y), window_x/8
surface = pygame.display.set_mode(window)
fpsclock = pygame.time.Clock()
pink = (255, 182, 193)
bingo_string = pygame.font.SysFont(None, 72)
number_string = pygame.font.SysFont(None, 100)


class Bingo_Card(object):

    def __init__(self):
        self.switch, self.count = True,  1
        self.mainloope()

    def generate_num(self, x, y, number):
        for i in range(1, 6):
            if (i * 100 <= x <= (i + 1) * 100):
                surface.blit(
                    number_string.render(str(number), True, (0, 106, 182)), (x, y))

    def draw_normal_object(self):
        for i in range(1, 7):
            pygame.draw.line(surface, (255, 0, 0),
                             (100*i, 100), (100*i, 600), 5)
            pygame.draw.line(surface, (255, 0, 0),
                             (100, 100*i), (600, 100*i), 5)
        surface.blit(bingo_string.render("BINGO CARD", True,
                                         (0, 128, 0)), (string_x, 50))
        pygame.draw.circle(surface, (255, 0, 0), (350, 350), 50)

    def mainloope(self):
        while True:
            for get in pygame.event.get():
                if(get.type == KEYDOWN):
                    if(get.key == K_SPACE):
                        self.switch = False if self.count % 2 == 1 else True
                        self.count = self.count + 1 if self.count < 10 else 1
                    elif(get.key == K_ESCAPE):
                        pygame.quit()
                        sys.exit()

            if(self.switch):
                surface.fill(pink)
                num_list, number2, used_index = [], [], []
                for i in range(1, 6):
                    for j in range(1, 6):
                        number1 = random.randint(15*(j - 1) + 1, 15*j)
                        if(number1 not in num_list):
                            self.generate_num(100*j+20, 100*i+30, number1)
                        else:
                            number2 = range(15*(j-1)+1, 15*j)
                            number2 = list(
                                set(number2) - set(num_list)-set(used_index))
                            x = random.randint(0, len(number2)-1)
                            self.generate_num(
                                100*j+20, 100*i+30, number2[x])
                            used_index.append(number2[x])

                        num_list.append(number1)

            self.draw_normal_object()
            fpsclock.tick(40)
            pygame.display.update()


Bingo_Card()
