import pygame
from Game_Objects.game_object import GameObject
from constants import *

class Player(GameObject):
    def __init__(self, x, y, size, color, speed, player_path, name='You'):
        super().__init__(x, y, size, color, name=name)
        self.speed = speed
        # Initialize with maximum bombs #if didnt -1 it will have 3 bombs (X)
        self.bombs = MAX_BOMBS-1
        self.invincible = False
        self.bomb_replenish_timer = 0  # Timer for bomb replenishment
        self.image = pygame.image.load(player_path)
        self.image = pygame.transform.scale(self.image, (self.size, self.size))
        self.bomb_image = pygame.image.load(bomb_path)
        self.bomb_image = pygame.transform.scale(self.bomb_image, (60, 60))

    def move(self, dx, dy, map_data):
        new_x = self.x + dx
        new_y = self.y + dy
        if self.can_move(new_x, new_y, map_data):
            self.x = new_x
            self.y = new_y

    def can_move(self, x, y, map_data):
        if x < MARGIN_WIDTH or y < 0 or x + self.size > SCREEN_WIDTH or y + self.size > SCREEN_HEIGHT:
            return False
        try:
            if (map_data[int((y - 10) // TILE_SIZE)][int((x - MARGIN_WIDTH) // TILE_SIZE)] != 0 or
                map_data[int((y - 10) // TILE_SIZE)][int((x - MARGIN_WIDTH + self.size - 1) // TILE_SIZE)] != 0 or
                map_data[int((y + self.size - 1 - 10) // TILE_SIZE)][int(((x - MARGIN_WIDTH) // TILE_SIZE))] != 0 or
                    map_data[int((y + self.size - 1 - 10) // TILE_SIZE)][int(((x - MARGIN_WIDTH + self.size - 1) // TILE_SIZE))] != 0):
                return False
        except IndexError:
            return False  # If any index is out of bounds, movement is not allowed
        return True

    def can_place_bomb(self):
        return self.bombs > 0  # Check if the player has bombs to place

    def replenish_bomb(self, game_over):
        if self.bombs < MAX_BOMBS and not game_over:
            if self.bomb_replenish_timer <= 0:
                self.bombs += 1
                self.bomb_replenish_timer = BOMB_REPLENISH_TIME
            else:
                self.bomb_replenish_timer -= 1 / 30  # Assuming 30 FPS

    def draw_bomb_inventory(self, screen):
        slot_size = 80
        slot_x = 10
        slot_y_start = 10
        for i in range(1,MAX_BOMBS+1):
            slot_y = slot_y_start + (i-1) * (slot_size + 10)
            pygame.draw.rect(screen, BLACK, (slot_x, slot_y, slot_size, slot_size), 2)
            if i < self.bombs:
                screen.blit(self.bomb_image, (slot_x+10, slot_y+10))
                # pygame.draw.circle(
                # screen, BLACK, (slot_x + slot_size // 2, slot_y + slot_size // 2), slot_size // 4)
            elif i == self.bombs:
                font = pygame.font.Font(None, 24)
                remaining_time = max(int(self.bomb_replenish_timer), 0)
                timer_text = font.render(str(remaining_time), True, BLACK)
                screen.blit(self.bomb_image, (slot_x+10, slot_y+10))
                # screen.blit(timer_text, (slot_x + slot_size // 2 - timer_text.get_width() //
                #           2, slot_y + slot_size // 2 - timer_text.get_height() // 2))

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))
        self.draw_health_bar(screen)
        self.draw_name(screen)