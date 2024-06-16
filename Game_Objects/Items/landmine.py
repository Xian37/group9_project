import pygame
import sys
import time
import random
from Game_Objects.game_object import GameObject
from Game_Objects.flame import Flame
from constants import *

class LandmineItem(GameObject):
    def __init__(self, x, y, size, color, placed_time):
        super().__init__(x, y, size, color, health = 0)
        self.placed_time = placed_time
        self.explosion_timer = 0  # Initialize explosion timer attribute
        self.hidden = False  # Initialize hidden attribute
        self.image_landmine = pygame.image.load(landmine_path).convert_alpha()  # Replace landmine_image_path with the actual path to your image
        self.image_landmine = pygame.transform.scale(self.image_landmine, (TILE_SIZE, TILE_SIZE))  # Scale the image to match the tile size
        self.touch = False

    def explode(self, map_data, flames, player, enemies, invincible=False):
        #self.explosion_timer = 0
        self.hidden = False
        bomb_x, bomb_y = (
            self.x - MARGIN_WIDTH) // TILE_SIZE, (self.y - 10) // TILE_SIZE
        explosion_range = 1
        # Up, Down, Right, Left
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        affected_positions = [(bomb_x, bomb_y)]

        # Draw the center of the explosion
        flames.append(Flame(self.x, self.y, TILE_SIZE, ORANGE, time.time()))

        for dx, dy in directions:
            for step in range(1, explosion_range + 1):
                check_x, check_y = bomb_x + dx * step, bomb_y + dy * step
                if 0 <= check_x < len(map_data[0]) and 0 <= check_y < len(map_data):
                    if map_data[int(check_y)][int(check_x)] == 1:
                        map_data[int(check_y)][int(check_x)] = 0
                        flames.append(Flame(check_x * TILE_SIZE + MARGIN_WIDTH,
                                            check_y * TILE_SIZE + 10, TILE_SIZE, ORANGE, time.time()))
                        break
                    elif map_data[int(check_y)][int(check_x)] == 2:  # Check if it's an obstacle
                        # Obstacles should not be affected by explosions
                        break
                    affected_positions.append((check_x, check_y))
                    flames.append(Flame(check_x * TILE_SIZE + MARGIN_WIDTH,
                                            check_y * TILE_SIZE + 10, TILE_SIZE, ORANGE, time.time()))
                else:
                    break

        if ((player.x - MARGIN_WIDTH) // TILE_SIZE, (player.y - 10) // TILE_SIZE) in affected_positions:
            if not player.invincible:
                player.health -= HEALTH_DECREMENT
                if player.health <= 0:
                    player.health = 0

        for enemy in enemies[:]:
            if ((enemy.x - MARGIN_WIDTH) // TILE_SIZE, (enemy.y - 10) // TILE_SIZE) in affected_positions:
                if not enemy.invincible:
                    enemy.health -= HEALTH_DECREMENT
                    if enemy.health <= 0:
                        enemies.remove(enemy)

    def draw(self, screen):
        if not self.hidden:
            screen.blit(self.image_landmine, (self.x, self.y))