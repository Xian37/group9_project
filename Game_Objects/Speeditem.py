import pygame
from Game_Objects.game_object import GameObject
from constants import *
from Game_Objects.enemy import Enemy
from Game_Objects.player import Player

class SpeedItem(GameObject):
    def __init__(self, x, y, size, color):
        super().__init__(x, y, size, color)
        self.image_speed = pygame.image.load(speed_path)
        self.image_speed = pygame.transform.scale(self.image_speed, (TILE_SIZE, TILE_SIZE))

    def apply(self, target):
        if isinstance(target, Player):
            target.speed = 7.5  # Increase player speed by 50%
            # Set a timer to reset player speed back to normal after 5 seconds
            pygame.time.set_timer(USEREVENT + 1, 5000)
        elif isinstance(target, Enemy):
            target.speed = 7.5  # Increase enemy speed by 50%
            # Set a timer to reset enemy speed back to normal after 5 seconds
            pygame.time.set_timer(USEREVENT + 2, 5000)

    def draw(self, screen):
        screen.blit(self.image_speed, (self.x, self.y))