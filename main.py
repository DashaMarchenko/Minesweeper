import sys
import time
import pygame
import random
from objects import *

pygame.init()


display = pygame.display.Info()
screen = pygame.display.set_mode((display.current_w, display.current_h))
screen.fill((0, 0, 0))
clock = pygame.time.Clock()
menu = Menu(screen, display)
game_state = 'menu'
mas1 = game_field(9, 9, 10)
mas2 = game_field(15, 11, 40)
mas3 = game_field(18, 13, 100)
flag = False
count_mines = 0


def listener():
    global game_state, mas1, mas2, mas3, flag, count_mines
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                if game_state == 'menu':
                    sys.exit()
                else:
                    screen.fill((0, 0, 0))
                    game_state = 'menu'
                    count_mines = 0
                    flag = False

            if event.key == pygame.K_UP and game_state == 'menu':
                if menu.check > 0: menu.check -= 1
            elif event.key == pygame.K_DOWN and game_state == 'menu':
                if menu.check < 3: menu.check += 1
            if event.key == pygame.K_RETURN and game_state == 'menu':
                if menu.check == 0:
                    game_state = 'game'
                    screen.fill((0, 0, 0))
                    game_field(9, 9, 10, screen)
                elif menu.check == 1:
                    game_state = 'game'
                    screen.fill((0, 0, 0))
                    game_field(15, 11, 40, screen)
                elif menu.check == 2:
                    game_state = 'game'
                    screen.fill((0, 0, 0))
                    game_field(18, 13, 100, screen)
                elif menu.check == 3:
                    sys.exit()

        if game_state == 'game' and event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                x = (event.pos[0] - 3) // 66
                y = (event.pos[1] - 3) // 66
                if menu.check == 0: mas, mines = mas1, 10
                elif menu.check == 1: mas, mines = mas2, 40
                elif menu.check == 2: mas, mines = mas3, 100

                if x == 20 and y == 12 and not flag: flag = True
                elif x == 20 and y == 12 and flag: flag = False
                elif y <= len(mas) and x <= len(mas[0]) and not mas[y][x] == 1 and not flag:
                    pygame.draw.rect(screen, (0, 0, 0), (3 + x * 66, 3 + 66 * y, 63, 63))
                    suma = 0
                    if y != 0: suma += mas[y - 1][x]
                    if y != len(mas) - 1: suma += mas[y + 1][x]
                    if x != 0: suma += mas[y][x - 1]
                    if x != len(mas[0]) - 1: suma += mas[y][x + 1]
                    if y != 0 and x != len(mas[0]) - 1: suma += mas[y - 1][x + 1]
                    if y != 0 and x != 0: suma += mas[y - 1][x - 1]
                    if x != 0 and y != len(mas) - 1: suma += mas[y + 1][x - 1]
                    if x != len(mas[0]) - 1 and y != len(mas) - 1: suma += mas[y + 1][x + 1]
                    sum_font = pygame.font.SysFont('arial', 50)
                    if suma == 1: color = (50, 100, 168)
                    elif suma == 2: color = (50, 168, 82)
                    elif suma == 3: color = (235, 204, 5)
                    elif suma == 4: color = (121, 50, 168)
                    elif suma == 5: color = (168, 50, 50)
                    elif suma == 6: color = (235, 100, 5)
                    elif suma == 0 or suma == 7 or suma == 8: color = (255, 255, 255)
                    sum_render = sum_font.render(str(suma), True, pygame.Color(color))
                    sum_rect = sum_render.get_rect(center=(36 + x * 66, 36 + 66 * y))
                    screen.blit(sum_render, sum_rect)
                elif y <= len(mas) and x <= len(mas[0]) and mas[y][x] == 1 and not flag:
                    game_state = 'lose'
                    game_over_font = pygame.font.SysFont('arial', 100)
                    game_over_render = game_over_font.render('GAME OVER', True, pygame.Color((168, 50, 50)))
                    game_over_rect = game_over_render.get_rect(center=(display.current_w//2, display.current_h//2))
                    screen.blit(game_over_render, game_over_rect)
                elif y <= len(mas) and x <= len(mas[0]) and mas[y][x] == 1 and flag:
                    if mas[y][x] == 1:
                        count_mines += 1
                        pygame.draw.rect(screen, (255, 0, 0), (3 + x * 66, 3 + 66 * y, 63, 63))
                        if count_mines == mines:
                            game_state = 'win'
                            game_over_font = pygame.font.SysFont('arial', 100)
                            game_over_render = game_over_font.render('YOU WIN', True, pygame.Color((168, 50, 50)))
                            game_over_rect = game_over_render.get_rect(
                                center=(display.current_w // 2, display.current_h // 2))
                            screen.blit(game_over_render, game_over_rect)


while True:
    listener()

    if game_state == 'menu':
        menu.draw()

    pygame.display.update()
    clock.tick(60)
