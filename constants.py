import pygame
TILE_SIZE = 60
ENTITY_SIZE = TILE_SIZE
BOMB_TIMER = 1
LANDMINE_TIMER = 1
FLAME_DURATION = 1
HEALTH_DECREMENT = 25
BOMB_REPLENISH_TIME = 3
MAX_BOMBS = 2
GAME_DURATION = 100
USEREVENT = 0 # to include this variable in order to the use of invincible item and speed item.

MARGIN_WIDTH = 100
SCREEN_WIDTH, SCREEN_HEIGHT = 1060+10, 790+10
GAME_WIDTH = SCREEN_WIDTH - MARGIN_WIDTH

player_path = "Game_Picture/cucu.png"
bomb_path = "Game_Picture/bomb.png"
enemy_path = "Game_Picture/mi.png"
flame_path = "Game_Picture/flame.png"
health_path = "Game_Picture/health.png"
speed_path = "Game_Picture/speed.png"
invincible_path = "Game_Picture/star.png"
landmine_path = "Game_Picture/landmine.png"

# Map Desert
desert_road_path = "Game_Picture/sand.jpg"
desert_wall_path = "Game_Picture/captus.png"
desert_ob_path = "Game_Picture/rock.png"

# Map Ocean
ocean_road_path = "Game_Picture/sand.jpg"
ocean_wall_path = "Game_Picture/forest.png"
ocean_ob_path = "Game_Picture/forest2.jpg"

# Map Forest
forest_road_path = "Game_Picture/grass.png"
forest_wall_path = "Game_Picture/forest.png"
forest_ob_path = "Game_Picture/forest2.jpg"

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GRAY = (200, 200, 200)
GREEN = (0, 255, 0)
ORANGE = (255, 165, 0)
BLUE = (0, 0, 255)
YELLOW = (255,255,0)

# Map Path
map1_img = "Game_Picture/forest2.jpg"
map2_img = "Game_Picture/sea.png"
map3_img = "Game_Picture/desert.png"

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Bomber Man')
programIcon = pygame.image.load('Game_Picture/bomb.png')
pygame.display.set_icon(programIcon)

map1_image = pygame.image.load(map1_img)
map1_image = pygame.transform.scale(map1_image, (250, 250))
map2_image = pygame.image.load(map2_img)
map2_image = pygame.transform.scale(map2_image, (250, 250))
map3_image = pygame.image.load(map3_img)
map3_image = pygame.transform.scale(map3_image, (250, 250))