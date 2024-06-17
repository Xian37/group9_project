import pygame
from Game_Objects.game_object import GameObject
from Game_Objects.player import Player
from constants import *

class Fox(Player):
    def __init__(self, x, y, size, color, speed, role1_fox):
        super().__init__(x, y, size, color, speed ,health = 100, player_path = role1_fox, name='You')      

    def draw_health_block(self, screen):
        rainbow_image = pygame.image.load(rainbow_path)
        font = pygame.font.Font(None, 45)
        block_x = 10
        block_y = 265
        bar_width = 80
        bar_height = 525
        outline_rect = pygame.Rect(block_x - 3, block_y - 3, bar_width + 3, bar_height + 3)
        fill_rect = pygame.Rect(block_x, block_y + bar_height-(self.health / 100) * bar_height, bar_width, (self.health / 100) * bar_height)
        rainbow_image = pygame.transform.scale(rainbow_image, (80,525*(self.health / 100)))
        if self.invincible == True:
            #pygame.draw.rect(screen, BLACK, fill_rect)
            screen.blit(rainbow_image, fill_rect)
        else:
            pygame.draw.rect(screen, RED, fill_rect)
        pygame.draw.rect(screen, BLACK, outline_rect, 3)
        screen.blit(font.render(str(self.health)+"%", True, BLACK), (10, 210))