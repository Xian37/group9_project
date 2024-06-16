import pygame
import random
import time
from Game_Objects.game_object import GameObject
from Game_Objects.bomb import Bomb
from constants import *

class Enemy(GameObject):
    def __init__(self, x, y, size, color, speed, direction, enemy_path, name):
        super().__init__(x, y, size, color, name=name)
        self.speed = speed
        self.direction = direction
        self.invincible = False
        self.bomb_cooldown = 0
        self.image = pygame.image.load(enemy_path)
        self.image = pygame.transform.scale(self.image, (self.size, self.size))

    def move(self, map_data, bombs):
        dx = 0
        dy = 0
        distance = 0
        for bomb in bombs:
            distance = ((self.x - bomb.x) ** 2 + (self.y - bomb.y) ** 2) ** 0.5
        if distance < TILE_SIZE * 3:
            directions = {
                'left': (-self.speed, 0),
                'right': (self.speed, 0),
                'up': (0, -self.speed),
                'down': (0, self.speed)
            }
            self.avoid_bombs(bombs, map_data)
            dx, dy = directions[self.direction]
        else:
            directions = {
                'left': (-self.speed, 0),
                'right': (self.speed, 0),
                'up': (0, -self.speed),
                'down': (0, self.speed)
            }

            if random.random() < 0.80:  # 80% probability to keep the same direction
                dx, dy = directions[self.direction]
            else:  # 20% probability to change direction
                self.direction = random.choice(['left', 'right', 'up', 'down'])
                dx, dy = directions[self.direction]
        new_x = self.x + dx
        new_y = self.y + dy
        if self.can_move(new_x, new_y, map_data):
            self.x = new_x
            self.y = new_y
        else:
            # If can't move in the current direction, choose another random direction
            self.direction = random.choice(['left', 'right', 'up', 'down'])

    def can_move(self, x, y, map_data):
        if x < MARGIN_WIDTH or y < 0 or x + self.size > SCREEN_WIDTH or y + self.size > SCREEN_HEIGHT:
            return False
        try:
            if (map_data[int((y - 10) // TILE_SIZE)][int((x - MARGIN_WIDTH) // TILE_SIZE)] != 0 or
                map_data[int(((y - 10) // TILE_SIZE))][int((x - MARGIN_WIDTH + self.size - 1) // TILE_SIZE)] != 0 or
                map_data[int((y + self.size - 1 - 10) // TILE_SIZE)][int((x - MARGIN_WIDTH) // TILE_SIZE)] != 0 or
                    map_data[int((y + self.size - 1 - 10) // TILE_SIZE)][int((x - MARGIN_WIDTH + self.size - 1) // TILE_SIZE)] != 0):
                return False
        except IndexError:
            return False  # If any index is out of bounds, movement is not allowed
        return True

    def place_bomb(self, bombs, player, enemies):
        enemies_exclude = enemies[:]
        enemies_exclude.remove(self)
        enemies_exclude.append(player)
        if self.bomb_cooldown <= 0:
            target = player if random.random() < 0.5 else random.choice(enemies_exclude)
            if self.is_near_target(target):
                bomb_x = (self.x - MARGIN_WIDTH) // TILE_SIZE * \
                    TILE_SIZE + MARGIN_WIDTH
                bomb_y = (self.y - 10) // TILE_SIZE * TILE_SIZE + 10
                if not any(bomb.x == bomb_x and bomb.y == bomb_y for bomb in bombs):
                    bombs.append(Bomb(bomb_x, bomb_y, TILE_SIZE,
                                 RED, time.time(), bomb_path))
                    self.bomb_cooldown = 200  # Cooldown period before placing another bomb
        else:
            self.bomb_cooldown -= 1

    def is_near_target(self, target):
        distance = ((self.x - target.x) ** 2 + (self.y - target.y) ** 2) ** 0.5
        return distance < TILE_SIZE * 3

    def avoid_bombs(self, bombs, map_data):
        for bomb in bombs:
            distance = ((self.x - bomb.x) ** 2 + (self.y - bomb.y) ** 2) ** 0.5
            Dx = bomb.x - self.x
            Dy = bomb.y - self.y
            if distance < TILE_SIZE * 3:
                if Dx > 0:
                    if Dy > 0:
                        if Dx > Dy:
                            self.direction = 'down' 
                        else:
                            self.direction = 'left'
                    else:
                        if Dx > Dy:
                            self.direction = 'up'
                        else:
                            self.direction = 'left'
                else:
                    if Dy > 0:
                        if Dx > Dy:
                            self.direction = 'down'
                        else:
                            self.direction = 'right'
                    else:
                        if Dx > Dy:
                            self.direction = 'up'
                        else:
                            self.direction = 'right'

        '''for bomb in bombs:
            distance = ((self.x - bomb.x) ** 2 + (self.y - bomb.y) ** 2) ** 0.5
            if distance < TILE_SIZE * 4:
                directions = ['left', 'right', 'up', 'down']
                safe_direction = None
                for direction in directions:
                    dx, dy = {
                        'left': (-self.speed, 0),
                        'right': (self.speed, 0),
                        'up': (0, -self.speed),
                        'down': (0, self.speed)
                    }[direction]
                    new_x = self.x + dx
                    new_y = self.y + dy
                    if self.can_move(new_x, new_y, map_data):
                        safe_direction = direction
                        break
                if safe_direction:
                    self.direction = safe_direction'''
   # def draw(self, screen):
    #    pygame.draw.rect(screen, self.color, (self.x, self.y, self.size, self.size))
     #   self.draw_health_bar(screen)
      #  self.draw_name(screen)

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))
        self.draw_health_bar(screen)
        self.draw_name(screen)
    