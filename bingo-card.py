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
yellow = (255, 255, 133)

bingo_string = pygame.font.SysFont(None, 72)
number_string = pygame.font.SysFont(None, 100)


def generate_num(x, y, number):
    for i in range(1, 6):
        if (i * 100 <= x <= (i + 1) * 100):
            surface.blit(
                number_string.render(str(number), True, (0, 255, 255)), (x, y))


def main():
    swtich, count = True,  1
    while True:
        for get in pygame.event.get():
            if(get.type == KEYDOWN):
                if(get.key == K_SPACE):
                    swtich = False if count % 2 == 1 else True
                    count = count + 1 if count < 10 else 1
                elif(get.key == K_ESCAPE):
                    pygame.quit()
                    sys.exit()

        if(swtich):
            surface.fill(yellow)
            index = 0
            num_list = []
            for i in range(1, 6):
                for j in range(1, 6):
                    number1 = random.randint(15*(j - 1) + 1, 15*j)
                    if(number1 not in num_list):
                        num_list.append(number1)
                        generate_num(20+100*j, 30+100*i, number1)
                    else:
                        index = index + 1
                        number2 = range(15*(j-1), 15*j)
                        number2 = list(set(number2) - set(num_list))
                        generate_num(20+100*j, 30+100*i, number2[index])

        for i in range(1, 7):
            pygame.draw.line(surface, (255, 0, 0),
                             (100*i, 100), (100*i, 600), 5)
            pygame.draw.line(surface, (255, 0, 0),
                             (100, 100*i), (600, 100*i), 5)

        surface.blit(bingo_string.render("BINGO CARD", True,
                                         (0, 255, 255)), (string_x, 50))

        pygame.draw.circle(surface, (255, 0, 0), (350, 350), 50)
        fpsclock.tick(40)
        pygame.display.update()


main()
