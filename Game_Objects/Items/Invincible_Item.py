import pygame
from Game_Objects.game_object import GameObject
from constants import *
from Game_Objects.enemy import Enemy
from Game_Objects.player import Player


class InvincibleItem(GameObject):
    def __init__(self, x, y, size, color):
        super().__init__(x, y, size, color)
        self.image_invincible = pygame.image.load(invincible_path)
        self.image_invincible = pygame.transform.scale(
            self.image_invincible, (TILE_SIZE, TILE_SIZE))

    def apply(self, target):
        if isinstance(target, Player):
            target.invincible = True  # Set player invincible attribute to True
            # Set a timer to reset player invincibility after 3.5 seconds
            pygame.time.set_timer(USEREVENT + 3, 3500)
        elif isinstance(target, Enemy):
            target.invincible = True  # Set enemy invincible attribute to True
            # Set a timer to reset enemy invincibility after 3.5 seconds
            pygame.time.set_timer(USEREVENT + 4, 3500)

    def draw(self, screen):
        screen.blit(self.image_invincible, (self.x, self.y))
