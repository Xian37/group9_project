import pygame
from Game_Objects.game_object import GameObject
from Game_Objects.enemy import Enemy
from Game_Objects.player import Player
from Game_Objects.Player.Monkey import Monkey
from constants import *


class HealthItem(GameObject):
    def __init__(self, x, y, size, color):
        super().__init__(x, y, size, color)
        self.image_health = pygame.image.load(health_path)
        self.image_health = pygame.transform.scale(
            self.image_health, (TILE_SIZE, TILE_SIZE))

    def apply(self, target):
        if isinstance(target, Player):
            if isinstance(target, Monkey):
                target.health = min(target.health + 50, 125)
            else:
                target.health = min(target.health + 50, 100)
        elif isinstance(target, Enemy):
            target.health = min(target.health + 50, 100)

    def draw(self, screen):
        # pygame.draw.circle(screen, self.color, (self.x + self.size // 2, self.y + self.size // 2), self.size // 2)
        screen.blit(self.image_health, (self.x, self.y))
