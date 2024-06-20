import pygame
from Game_Objects.game_object import GameObject
from constants import flame_path, TILE_SIZE


class Flame(GameObject):
    def __init__(self, x, y, size, color, created_time):
        super().__init__(x, y, size, color, health=0)
        self.created_time = created_time
        self.image = pygame.image.load(flame_path)
        self.image = pygame.transform.scale(self.image, (TILE_SIZE, TILE_SIZE))

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))
