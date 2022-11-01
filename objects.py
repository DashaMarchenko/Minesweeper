import pygame
import random

class Menu:
    def __init__(self, screen, display, caption = 'Minesweeper',
                 menu_items = ['Beginner', 'Intermediate', 'Advanced', 'Exit']):
        self.screen = screen
        self.check = 0
        self.display = display
        self.caption = caption
        self.menu_items = menu_items
        self.caption_font = pygame.font.SysFont('arial', 50)
        self.caption_render = self.caption_font.render(self.caption, False, pygame.Color(255, 255, 255))
        self.caption_rect = self.caption_render.get_rect(center=(self.display.current_w // 2, 250))
        self.items_font = pygame.font.SysFont('arial', 30)

    def draw(self):
        self.screen.blit(self.caption_render, self.caption_rect)
        self.items = []
        self.items_rect = []
        for i in range(len(self.menu_items)):
            if i == self.check:
                self.items.append(self.items_font.render(self.menu_items[i], False, pygame.Color (50, 168, 82)))
            else:
                self.items.append(self.items_font.render(self.menu_items[i], False, pygame.Color(255, 255, 255)))
            self.items_rect.append(self.items[i].get_rect(center = (self.display.current_w // 2,
                                                                    int((self.display.current_h //2)*(0.897 + i*0.106)))))
            self.screen.blit(self.items[i], self.items_rect[i])


def game_field(n, n1, mins, screen=None):
    mas = [[0 for _ in range(n)] for j in range(n1)]
    for i in range(mins):
        mas[random.randint(0, n1 - 1)][random.randint(0, n - 1)] = 1
    if screen != None:
        for i in range(len(mas)):
            for j in range(len(mas[i - 1])):
                pygame.draw.rect(screen, (255, 255, 255), (3 + j * 66, 3 + i * 66, 63, 63))

        pygame.draw.rect(screen, (255, 0, 0), (3 + 20 * 66, 3 + 12 * 66, 63, 63))

    return mas

