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
# to include this variable in order to the use of invincible item and speed item.
USEREVENT = 0

MARGIN_WIDTH = 100
SCREEN_WIDTH, SCREEN_HEIGHT = 1060+10, 790+10
GAME_WIDTH = SCREEN_WIDTH - MARGIN_WIDTH
ADD_ITEM_EVENT = pygame.USEREVENT + 5
start_image_path = "Game_Picture/start.png"
game_over_path = "Game_Picture/gameover.png"
game_win_path = "Game_Picture/gamewin.png"
# player_path = "Game_Picture/cucu.png"
bomb_path = "Game_Picture/bomb.png"
flame_path = "Game_Picture/flame.png"
rainbow_path = "Game_Picture/rainbow.jpeg"

# Items
health_path = "Game_Picture/health.png"
speed_path = "Game_Picture/speed.png"
invincible_path = "Game_Picture/star.png"
landmine_path = "Game_Picture/landmine.png"

# Map Desert
desert_road_path = "Game_Picture/sand.jpg"
desert_wall_path = "Game_Picture/cactus.png"
desert_ob_path = "Game_Picture/rock.png"

# Map Ocean
ocean_road_path_1 = "Game_Picture/sea_background_1.jpg"
ocean_road_path_2 = "Game_Picture/sea_background_2.jpg"
ocean_road_path_3 = "Game_Picture/sea_background_3.jpg"
ocean_road_path_4 = "Game_Picture/sea_background_4.jpg"
ocean_wall_path_1 = "Game_Picture/coral2.png"
ocean_ob_path = "Game_Picture/rock.png"

# Map Forest
forest_road_path = "Game_Picture/grass.jpg"
forest_wall_path = "Game_Picture/forest.png"
forest_ob_path = "Game_Picture/forest2.png"

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GRAY = (200, 200, 200)
GREEN = (0, 255, 0)
ORANGE = (255, 165, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
LIGHTBLUE = (117, 210, 210)
DARKBLUE = (2, 2, 85)

# Map Path
map1_img = "Game_Picture/forest2.png"
map2_img = "Game_Picture/sea.png"
map3_img = "Game_Picture/desert.png"

# Role Path

role1_fox = "Game_Picture/fox2.png"
role2_monkey = "Game_Picture/monkey.png"
role3_cucu = "Game_Picture/cucu.png"

# Enemy Path

fox_enemy = "Game_Picture/panda.png"
monkey_enemy = "Game_Picture/blond_guy.png"
cucu_enemy = "Game_Picture/mi.png"

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Bomber Man')
programIcon = pygame.image.load('Game_Picture/bomb.png')
pygame.display.set_icon(programIcon)

map1_image = pygame.image.load(map1_img)
map1_image = pygame.transform.scale(pygame.image.load(map1_img), (250, 250))
map2_image = pygame.image.load(map2_img)
map2_image = pygame.transform.scale(pygame.image.load(map2_img), (250, 250))
map3_image = pygame.image.load(map3_img)
map3_image = pygame.transform.scale(pygame.image.load(map3_img), (250, 250))

role1_image = pygame.image.load(role1_fox)
role1_image = pygame.transform.scale(pygame.image.load(role1_fox), (250, 250))
role2_image = pygame.image.load(role2_monkey)
role2_image = pygame.transform.scale(
    pygame.image.load(role2_monkey), (250, 250))
role3_image = pygame.image.load(role3_cucu)
role3_image = pygame.transform.scale(pygame.image.load(role3_cucu), (250, 250))

start_image = pygame.image.load(start_image_path)
gameover_image = pygame.image.load(game_over_path)
gamewin_image = pygame.image.load(game_win_path)
rainbow_image = pygame.image.load(rainbow_path)
block_x = 10
block_y = 265
bar_width = 80
bar_height = 525
outline_rect = pygame.Rect(block_x, block_y, bar_width, bar_height)
round = 0
