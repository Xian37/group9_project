import pygame
import sys
import time
import random
from pygame.locals import *
from constants import*
from Game_Objects.game_object import GameObject
from Game_Objects.player import Player
from Game_Objects.enemy import Enemy
from Game_Objects.bomb import Bomb
from Game_Objects.flame import Flame
from Game_Objects.healthitem import HealthItem
from Game_Objects.Invincibleitem import InvincibleItem
from Game_Objects.Speeditem import SpeedItem
from Game_Objects.landmine import LandmineItem
class Game:
    def __init__(self,num):
        filename = "Map/Map" + num + ".txt"
        with open(filename, 'r') as f:
            self.map_data = [list(map(int, line.strip().split())) for line in f]
        if num == "1":
            self.player = Player(MARGIN_WIDTH + TILE_SIZE, 10 +
                                TILE_SIZE, ENTITY_SIZE-10, BLACK, 5, player_path)
            wall_path = forest_wall_path
            ob_path = forest_ob_path
            road_path = forest_road_path
        elif num == "2":
            self.player = Player(MARGIN_WIDTH ,10, ENTITY_SIZE - 10, BLACK, 5, player_path)
            wall_path = ocean_wall_path
            ob_path = ocean_ob_path
            road_path = ocean_road_path
        elif num == "3":
            self.player = Player(MARGIN_WIDTH ,10, ENTITY_SIZE - 10, BLACK, 5, player_path)
            wall_path = desert_wall_path
            ob_path = desert_ob_path
            road_path = desert_road_path
        self.enemies = self.generate_enemies(5)
        self.health_items = []
        self.speed_items = []
        self.invincible_items = []
        self.landmines = []
        self.bombs = []
        self.flames = []
        self.game_over = False
        self.game_won = False
        self.start_time = time.time()
        self.image_wall = pygame.image.load(wall_path).convert_alpha()
        self.image_wall = pygame.transform.scale(self.image_wall, (TILE_SIZE, TILE_SIZE))
        self.image_obstacle = pygame.image.load(ob_path).convert_alpha()
        self.image_obstacle = pygame.transform.scale(self.image_obstacle, (TILE_SIZE, TILE_SIZE))
        self.image_road = pygame.image.load(road_path).convert_alpha()
        self.image_road = pygame.transform.scale(self.image_road, (TILE_SIZE, TILE_SIZE))
        self.generate_health_items()
        self.generate_speed_items()
        self.generate_invincible_items()
        self.generate_landmines()
        # self.image = pygame.image.load(player_path)
        # self.image = pygame.transform.scale(self.image, (self.size, self.size))

    def generate_enemies(self, count):
        enemies = []
        for i in range(count):
            while True:
                x = random.randint(1, GAME_WIDTH // TILE_SIZE-1)
                y = random.randint(1, SCREEN_HEIGHT // TILE_SIZE-1)
                if self.map_data[int(y)][int(x)] == 0:
                    direction = random.choice(['left', 'right', 'up', 'down'])
                    enemies.append(Enemy(int(x) * TILE_SIZE + MARGIN_WIDTH, int(y) * TILE_SIZE +
                                   10, ENTITY_SIZE-10, GREEN, 5, direction, enemy_path,  f'Enemy {i+1}'))
                    break
        return enemies
    
    def generate_health_items(self):
            for y, row in enumerate(self.map_data):
                for x, tile in enumerate(row):
                    if tile == 0 and random.random() < 0.02:
                        health_item = HealthItem(x * TILE_SIZE + MARGIN_WIDTH, y * TILE_SIZE + 10, TILE_SIZE, YELLOW)
                        self.health_items.append(health_item)
                        
    def generate_speed_items(self):
        for y, row in enumerate(self.map_data):
            for x, tile in enumerate(row):
                if tile == 0 and random.random() < 0.04:
                    speed_item = SpeedItem(x * TILE_SIZE + MARGIN_WIDTH, y * TILE_SIZE + 10, TILE_SIZE, YELLOW)
                    self.speed_items.append(speed_item)
                    
    def generate_invincible_items(self):
        for y, row in enumerate(self.map_data):
            for x, tile in enumerate(row):
                if tile == 0 and random.random() < 0.01:
                    invincible_item = InvincibleItem(x * TILE_SIZE + MARGIN_WIDTH, y * TILE_SIZE + 10, TILE_SIZE, YELLOW)
                    self.invincible_items.append(invincible_item)
    def generate_landmines(self):
            for y, row in enumerate(self.map_data):
                for x, tile in enumerate(row):
                    if tile == 0 and random.random() < 0.1:
                        landmine = LandmineItem(x * TILE_SIZE + MARGIN_WIDTH, y * TILE_SIZE + 10, TILE_SIZE, YELLOW, time.time())
                        self.landmines.append(landmine)
    def draw_map(self):
        for y, row in enumerate(self.map_data):
            for x, tile in enumerate(row):
                if tile == 1:
                    # pygame.draw.rect(screen, GRAY, (x * TILE_SIZE + MARGIN_WIDTH, y * TILE_SIZE + 10, TILE_SIZE, TILE_SIZE))
                   # map_rect = map_image.get_rect(center = (x * TILE_SIZE + MARGIN_WIDTH, y * TILE_SIZE + 10))
                    # map_image = pygame.transform.scale(self.image, (self.size, self.size))
                    # screen.blit(pygame.image.load(map_image), map_rect)
                    screen.blit(self.image_road, (x * TILE_SIZE + MARGIN_WIDTH, y * TILE_SIZE + 10))
                    screen.blit(self.image_wall, (x * TILE_SIZE +
                                MARGIN_WIDTH, y * TILE_SIZE + 10))
                elif tile == 2:
                    screen.blit(self.image_road, (x * TILE_SIZE + MARGIN_WIDTH, y * TILE_SIZE + 10))
                    screen.blit(self.image_obstacle, (x * TILE_SIZE + MARGIN_WIDTH, y * TILE_SIZE + 10))
                elif tile == 0:
                    screen.blit(self.image_road, (x * TILE_SIZE + MARGIN_WIDTH, y * TILE_SIZE + 10))

    def update(self):
        for enemy in self.enemies:
            enemy.move(self.map_data, self.bombs)
            enemy.place_bomb(self.bombs, self.player, self.enemies)

        current_time = time.time()
        for bomb in self.bombs[:]:
            if current_time - bomb.placed_time > BOMB_TIMER:
                bomb.explode(self.map_data, self.flames,
                             self.player, self.enemies)
                self.bombs.remove(bomb)

        for flame in self.flames[:]:
            if current_time - flame.created_time > FLAME_DURATION:
                self.flames.remove(flame)
                
        for health_item in self.health_items[:]:
            if (self.player.x > health_item.x - 30 and self.player.x < health_item.x + 30 and self.player.y > health_item.y - 30 and self.player.y < health_item.y + 30):
                health_item.apply(self.player)
                self.health_items.remove(health_item)

        for health_item in self.health_items[:]:
            # Check if any enemy is in the same position as the health item
            for enemy in self.enemies:
                if (enemy.x > health_item.x - 30 and enemy.x < health_item.x + 30 and enemy.y > health_item.y - 30 and enemy.y < health_item.y + 30):
                    health_item.apply(enemy)
                    self.health_items.remove(health_item)
                    #break  # Stop checking for other enemies if one has used the health item

        for speed_item in self.speed_items[:]:
            if (self.player.x > speed_item.x - 30 and self.player.x < speed_item.x + 30 and self.player.y > speed_item.y - 30 and self.player.y < speed_item.y + 30):
                speed_item.apply(self.player)
                self.speed_items.remove(speed_item)

        for speed_item in self.speed_items[:]:
            # Check if any enemy is in the same position as the speed item
            for enemy in self.enemies:
                if (enemy.x > speed_item.x - 30 and enemy.x < speed_item.x + 30 and enemy.y > speed_item.y - 30 and enemy.y < speed_item.y + 30):
                    speed_item.apply(enemy)
                    self.speed_items.remove(speed_item)
                    #break
        
        for invincible_item in self.invincible_items[:]:
            if (self.player.x > invincible_item.x - 30 and self.player.x < invincible_item.x + 30 and self.player.y > invincible_item.y - 30 and self.player.y < invincible_item.y + 30):
                invincible_item.apply(self.player)
                self.invincible_items.remove(invincible_item)
        
        for invincible_item in self.invincible_items[:]:
            # Check if any enemy is in the same position as the invincible item
            for enemy in self.enemies:
                if (enemy.x > invincible_item.x - 30 and enemy.x < invincible_item.x + 30 and enemy.y > invincible_item.y - 30 and enemy.y < invincible_item.y + 30):
                    invincible_item.apply(enemy)
                    self.invincible_items.remove(invincible_item)
                    #break
        for landmine in self.landmines[:]:
            if (self.player.x > landmine.x - 30 and self.player.x < landmine.x + 30 and self.player.y > landmine.y - 30 and self.player.y < landmine.y + 30):
                if landmine.explosion_timer == 0:
                    landmine.explosion_timer = current_time
                    landmine.touch = True
            if current_time - landmine.explosion_timer >= LANDMINE_TIMER and landmine.touch:
                landmine.explode(self.map_data, self.flames, self.player, self.enemies)
                self.landmines.remove(landmine)
        for landmine in self.landmines[:]:
            for enemy in self.enemies:
                if (enemy.x > landmine.x - 30 and enemy.x < landmine.x + 30 and enemy.y > landmine.y - 30 and enemy.y < landmine.y + 30):
                    if landmine.explosion_timer == 0:
                        landmine.explosion_timer = current_time
                        landmine.touch = True
                if current_time - landmine.explosion_timer >= LANDMINE_TIMER and landmine.touch:
                    landmine.explode(self.map_data, self.flames, self.player, self.enemies)
                    self.landmines.remove(landmine)


        # Update player bomb replenishment
        self.player.replenish_bomb(self.game_over)

        if self.player.health <= 0:
            self.game_over = True

        if not self.enemies:
            self.game_won = True

        # Check if time is up
        elapsed_time = current_time - self.start_time
        if elapsed_time > GAME_DURATION:
            self.game_over = True
            self.determine_winner()

    def draw(self):
        screen.fill(WHITE)
        self.draw_map()
        self.player.draw(screen)
        self.player.draw_bomb_inventory(screen)
        for enemy in self.enemies:
            enemy.draw(screen)
        for bomb in self.bombs:
            bomb.draw(screen)
        for flame in self.flames:
            flame.draw(screen)
        for healthitem in self.health_items:
            healthitem.draw(screen)
        for speeditem in self.speed_items:
            speeditem.draw(screen)
        for invincibleitem in self.invincible_items:
            invincibleitem.draw(screen)
        for landmine in self.landmines:
            landmine.draw(screen)
        if self.game_over:
            self.display_game_over()
        elif self.game_won:
            self.display_game_won()

        # Draw the timer
        if not self.game_over and not self.game_won:
            self.draw_timer()

    def draw_timer(self):
        font = pygame.font.Font(None, 45)
        elapsed_time = time.time() - self.start_time
        remaining_time = max(GAME_DURATION - elapsed_time, 0)
        timer_text = font.render(f"Time: {int(remaining_time)}", True, BLACK)
        screen.blit(timer_text, (SCREEN_WIDTH - 150, 10))

    def display_game_over(self):
        font = pygame.font.Font(None, 74)
        if self.enemies:
            if self.player.health > 0:
                winner = 'You' if self.player.health > max(
                    enemy.health for enemy in self.enemies) else 'Enemy'
            else:
                winner = 'Enemy'
        else:
            winner = 'You'
        text = font.render(f"Game Over: {winner} Wins!", True, BLACK)
        screen.blit(text, (SCREEN_WIDTH//2 - text.get_width() //
                    2, SCREEN_HEIGHT//2 - text.get_height()//2))

    def display_game_won(self):
        font = pygame.font.Font(None, 74)
        text = font.render("You Win!", True, BLACK)
        screen.blit(text, (SCREEN_WIDTH//2 - text.get_width() //
                    2, SCREEN_HEIGHT//2 - text.get_height()//2))

    def determine_winner(self):
        if self.player.health > 0:
            if self.enemies:
                highest_enemy_health = max(
                    enemy.health for enemy in self.enemies)
                if self.player.health > highest_enemy_health:
                    self.game_won = True
                else:
                    self.game_over = True
            else:
                self.game_won = True
        else:
            self.game_over = True