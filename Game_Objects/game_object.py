import pygame
from constants import *

class GameObject:
    def __init__(self, x, y, size, color, health=100, name=''):
        self.x = x
        self.y = y
        self.size = size
        self.color = color
        self.health = health
        self.name = name

    def draw(self, screen):
        pygame.draw.rect(screen, self.color,
                         (self.x, self.y, self.size, self.size))
        self.draw_health_bar(screen)
        self.draw_name(screen)

    def draw_health_bar(self, screen):
        if self.health > 0:
            bar_x = self.x
            bar_y = self.y - 10
            bar_width = self.size
            bar_height = 5
            fill = (self.health / 100) * bar_width
            outline_rect = pygame.Rect(bar_x, bar_y, bar_width, bar_height)
            fill_rect = pygame.Rect(bar_x, bar_y, fill, bar_height)
            pygame.draw.rect(screen, RED, fill_rect)
            pygame.draw.rect(screen, BLACK, outline_rect, 1)

    def draw_name(self, screen):
        font = pygame.font.Font(None, 24)
        text = font.render(self.name, True, BLACK)
        screen.blit(text, (self.x, self.y - 25))