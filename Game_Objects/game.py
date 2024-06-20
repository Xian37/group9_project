import pygame
import sys
import time
import random
from pygame.locals import *
from constants import *
from Game_Objects.game_object import GameObject
from Game_Objects.player import Player
from Game_Objects.enemy import Enemy
from Game_Objects.bomb import Bomb
from Game_Objects.flame import Flame
from Game_Objects.Items.Health_Item import HealthItem
from Game_Objects.Items.Invincible_Item import InvincibleItem
from Game_Objects.Items.Speed_Item import SpeedItem
from Game_Objects.Items.Landmine_Item import LandmineItem
from Game_Objects.Player.Cucu import Cucu
from Game_Objects.Player.Monkey import Monkey
from Game_Objects.Player.Fox import Fox


class Game:
    def __init__(self, map_num, role_num):
        self.map_num = map_num
        map_filename = "Map/Map" + map_num + ".txt"
        with open(map_filename, 'r') as f:
            self.map_data = [list(map(int, line.strip().split()))
                             for line in f]
        if role_num == "1":
            self.player = Fox(MARGIN_WIDTH + TILE_SIZE, 10 +
                              TILE_SIZE, ENTITY_SIZE-10, BLACK, 5, role1_fox)
            self.enemy_path = fox_enemy
        elif role_num == "2":
            self.player = Monkey(MARGIN_WIDTH + TILE_SIZE, 10 +
                                 TILE_SIZE, ENTITY_SIZE - 10, BLACK, 5, role2_monkey)
            self.enemy_path = monkey_enemy
        elif role_num == "3":
            self.player = Cucu(MARGIN_WIDTH + TILE_SIZE, 10 +
                               TILE_SIZE, ENTITY_SIZE - 10, BLACK, 5, role3_cucu)
            self.enemy_path = cucu_enemy

        if map_num == "1":
            wall_path = forest_wall_path
            ob_path = forest_ob_path
            road_path = forest_road_path
        elif map_num == "2":
            wall_path = ocean_wall_path_1
            ob_path = ocean_ob_path
            road_path = ocean_road_path_2
        elif map_num == "3":
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
        self.start_time = time.time()
        self.game_time = 0
        self.winner = None
        self.game_over = False
        self.image_wall = pygame.image.load(wall_path).convert_alpha()
        self.image_wall = pygame.transform.scale(
            self.image_wall, (TILE_SIZE, TILE_SIZE))
        self.image_obstacle = pygame.image.load(ob_path).convert_alpha()
        self.image_obstacle = pygame.transform.scale(
            self.image_obstacle, (TILE_SIZE, TILE_SIZE))
        self.image_road = pygame.image.load(road_path).convert_alpha()
        self.image_road = pygame.transform.scale(
            self.image_road, (TILE_SIZE, TILE_SIZE))
        self.generate_health_items()
        self.generate_speed_items()
        self.generate_invincible_items()
        self.generate_landmines()
        # self.image = pygame.image.load(player_path)
        # self.image = pygame.transform.scale(self.image, (self.size, self.size))

    def is_position_occupied(self, x, y):
        for item in self.health_items + self.speed_items + self.invincible_items + self.landmines:
            if abs(item.x - x) < TILE_SIZE and abs(item.y - y) <= TILE_SIZE:
                return True
        for enemy in self.enemies:
            if abs(enemy.x - x) < TILE_SIZE and abs(enemy.y - y) <= TILE_SIZE:
                return True
        if abs(self.player.x - x) < TILE_SIZE and abs(self.player.y - y) <= TILE_SIZE:
            return True
        return False

    def generate_enemies(self, count):
        enemies = []
        for i in range(count):
            while True:
                x = random.randint(1, GAME_WIDTH // TILE_SIZE-1)
                y = random.randint(1, SCREEN_HEIGHT // TILE_SIZE-1)
                if self.map_data[int(y)][int(x)] == 0:
                    direction = random.choice(['left', 'right', 'up', 'down'])
                    enemies.append(Enemy(int(x) * TILE_SIZE + MARGIN_WIDTH, int(y) * TILE_SIZE +
                                   10, ENTITY_SIZE-10, GREEN, 5, direction, self.enemy_path,  f'Enemy {i+1}'))
                    break
        return enemies

    def generate_health_items(self):
        for y, row in enumerate(self.map_data):
            for x, tile in enumerate(row):
                if tile == 0 and random.random() < 0.035:
                    item_x = x * TILE_SIZE + MARGIN_WIDTH
                    item_y = y * TILE_SIZE + 10
                    if not self.is_position_occupied(item_x, item_y):
                        health_item = HealthItem(
                            x * TILE_SIZE + MARGIN_WIDTH, y * TILE_SIZE + 10, TILE_SIZE, YELLOW)
                        self.health_items.append(health_item)

    def generate_speed_items(self):
        for y, row in enumerate(self.map_data):
            for x, tile in enumerate(row):
                if tile == 0 and random.random() < 0.05:
                    item_x = x * TILE_SIZE + MARGIN_WIDTH
                    item_y = y * TILE_SIZE + 10
                    if not self.is_position_occupied(item_x, item_y):
                        speed_item = SpeedItem(
                            x * TILE_SIZE + MARGIN_WIDTH, y * TILE_SIZE + 10, TILE_SIZE, YELLOW)
                        self.speed_items.append(speed_item)

    def generate_invincible_items(self):
        for y, row in enumerate(self.map_data):
            for x, tile in enumerate(row):
                if tile == 0 and random.random() < 0.025:
                    item_x = x * TILE_SIZE + MARGIN_WIDTH
                    item_y = y * TILE_SIZE + 10
                    if not self.is_position_occupied(item_x, item_y):
                        invincible_item = InvincibleItem(
                            x * TILE_SIZE + MARGIN_WIDTH, y * TILE_SIZE + 10, TILE_SIZE, YELLOW)
                        self.invincible_items.append(invincible_item)

    def generate_landmines(self):
        for y, row in enumerate(self.map_data):
            for x, tile in enumerate(row):
                if tile == 0 and random.random() < 0.04:
                    item_x = x * TILE_SIZE + MARGIN_WIDTH
                    item_y = y * TILE_SIZE + 10
                    if not self.is_position_occupied(item_x, item_y):
                        landmine = LandmineItem(
                            x * TILE_SIZE + MARGIN_WIDTH, y * TILE_SIZE + 10, TILE_SIZE, YELLOW, time.time())
                        self.landmines.append(landmine)

    def generate_random_item(self):
        item_type = random.choice(
            ['health', 'speed', 'invincible', 'landmine'])
        while True:
            x = random.randint(0, len(self.map_data[0]) - 1)
            y = random.randint(0, len(self.map_data) - 1)
            if self.map_data[y][x] == 0:
                if item_type == 'health':
                    self.health_items.append(HealthItem(
                        x * TILE_SIZE + MARGIN_WIDTH, y * TILE_SIZE + 10, TILE_SIZE, YELLOW))
                elif item_type == 'speed':
                    self.speed_items.append(
                        SpeedItem(x * TILE_SIZE + MARGIN_WIDTH, y * TILE_SIZE + 10, TILE_SIZE, YELLOW))
                elif item_type == 'invincible':
                    self.invincible_items.append(InvincibleItem(
                        x * TILE_SIZE + MARGIN_WIDTH, y * TILE_SIZE + 10, TILE_SIZE, YELLOW))
                elif item_type == 'landmine':
                    self.landmines.append(LandmineItem(
                        x * TILE_SIZE + MARGIN_WIDTH, y * TILE_SIZE + 10, TILE_SIZE, YELLOW, time.time()))
                break

    def draw_map(self):
        for y, row in enumerate(self.map_data):
            for x, tile in enumerate(row):
                if tile == 1:
                    screen.blit(self.image_road, (x * TILE_SIZE +
                                MARGIN_WIDTH, y * TILE_SIZE + 10))
                    screen.blit(self.image_wall, (x * TILE_SIZE +
                                MARGIN_WIDTH, y * TILE_SIZE + 10))
                elif tile == 2:
                    screen.blit(self.image_road, (x * TILE_SIZE +
                                MARGIN_WIDTH, y * TILE_SIZE + 10))
                    screen.blit(self.image_obstacle, (x *
                                TILE_SIZE + MARGIN_WIDTH, y * TILE_SIZE + 10))
                elif tile == 0:
                    screen.blit(self.image_road, (x * TILE_SIZE +
                                MARGIN_WIDTH, y * TILE_SIZE + 10))

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
                    break  # Stop checking for other enemies if one has used the health item

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
                    break

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
                    break
        for landmine in self.landmines[:]:
            if (self.player.x > landmine.x - 30 and self.player.x < landmine.x + 30 and self.player.y > landmine.y - 30 and self.player.y < landmine.y + 30):
                if landmine.explosion_timer == 0:
                    landmine.explosion_timer = current_time
                    landmine.touch = True
            if current_time - landmine.explosion_timer >= LANDMINE_TIMER and landmine.touch:
                landmine.explode(self.map_data, self.flames,
                                 self.player, self.enemies)
                self.landmines.remove(landmine)
        for landmine in self.landmines[:]:
            for enemy in self.enemies:
                if (enemy.x > landmine.x - 30 and enemy.x < landmine.x + 30 and enemy.y > landmine.y - 30 and enemy.y < landmine.y + 30):
                    if landmine.explosion_timer == 0:
                        landmine.explosion_timer = current_time
                        landmine.touch = True
                if current_time - landmine.explosion_timer >= LANDMINE_TIMER and landmine.touch:
                    landmine.explode(self.map_data, self.flames,
                                     self.player, self.enemies)
                    self.landmines.remove(landmine)

        # Update player bomb replenishment
        self.player.replenish_bomb(self.game_over)

        if self.player.health <= 0:
            self.game_over = True

        if self.enemies == []:
            self.game_over = True

        # Check if time is up
        elapsed_time = current_time - self.start_time
        if elapsed_time > GAME_DURATION:
            self.game_over = True
            self.determine_winner()

    def draw(self):
        screen.fill(WHITE)
        outline_rect = pygame.Rect(100-3, 10-3, 970, 790)
        pygame.draw.rect(screen, BLACK, outline_rect, 3)
        self.draw_map()
        self.player.draw(screen)
        self.player.draw_bomb_inventory(screen)
        self.player.draw_health_block(screen)
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

        # Draw the timer
        if not self.game_over:
            self.draw_timer()

    def draw_timer(self):
        font = pygame.font.Font(None, 55)
        elapsed_time = time.time() - self.start_time
        remaining_time = max(GAME_DURATION - elapsed_time, 0)
        timer_text = font.render(f"Time: {int(remaining_time)}", True, BLACK)
        screen.blit(timer_text, (SCREEN_WIDTH - 175, 10))

    def display_game_over(self):
        screen.fill(LIGHTBLUE)
        # Large font for game over message
        font_large = pygame.font.Font(None, 74)
        # Smaller font for instructions
        font_small = pygame.font.Font(None, 54)

        if self.enemies:
            if self.player.health > 0:
                if self.player.health > max(enemy.health for enemy in self.enemies):
                    self.winner = 'You'
                    screen.blit(gamewin_image, (0, 150))
                else:
                    self.winner = 'Enemy'
                    screen.blit(gameover_image, (0, 150))
            else:
                self.winner = 'Enemy'
                screen.blit(gameover_image, (0, 150))
        else:
            self.winner = 'You'
            screen.blit(gamewin_image, (0, 150))

        # Render the game over message
        text_game_over = font_large.render(
            f"{self.winner} Wins! ", True, WHITE)
        text_game_over_rect = text_game_over.get_rect(
            center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))

        # Render the instruction text
        text_instructions1 = font_small.render(
            "Press 'R' to Restart ", True, WHITE)
        text_instructions1_rect = text_instructions1.get_rect(
            center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 75))
        text_instructions2 = font_small.render(
            "Press 'Q' to Quit ", True, WHITE)
        text_instructions2_rect = text_instructions2.get_rect(
            center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 125))

        # Blit the texts onto the screen
        screen.blit(text_game_over, text_game_over_rect)
        screen.blit(text_instructions1, text_instructions1_rect)
        screen.blit(text_game_over, text_game_over_rect)
        screen.blit(text_instructions2, text_instructions2_rect)

    def determine_winner(self):
        if self.player.health > 0:
            if self.enemies:
                highest_enemy_health = max(
                    enemy.health for enemy in self.enemies)
                if self.player.health > highest_enemy_health:
                    self.game_over = False
                else:
                    self.game_over = True
            else:
                self.game_over = False
        else:
            self.game_over = True

    def end_game(self):
        self.game_over = True
        self.end_time = time.time()
        self.game_time = min(self.end_time - self.start_time, 100)
