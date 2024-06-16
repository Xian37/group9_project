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
from Game_Objects.game import Game
# Initialize Pygame
pygame.init()


def main():
    font = pygame.font.Font(None, 100)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    num = "1"
                    running = False
                elif event.key == pygame.K_2:
                    num = "2"
                    running = False
                elif event.key == pygame.K_3:
                    num = "3"
                    running = False
        screen.fill(WHITE)
        screen.blit(map1_image, (100, 300))
        screen.blit(map2_image, (400, 300))
        screen.blit(map3_image, (700, 300))

        map_name1 = font.render('FOREST', True, BLACK)
        map_name2 = font.render('OCEAN', True, BLACK)
        map_name3 = font.render('DESERT', True, BLACK)
        title1 = font.render('---- 1 ----', True, BLACK)
        title2 = font.render('---- 2 ----', True, BLACK)
        title3 = font.render('---- 3 ----', True, BLACK)
        screen.blit(map_name1, (100, 600))
        screen.blit(map_name2, (400, 600))
        screen.blit(map_name3, (700, 600))
        screen.blit(title1, (100, 200))
        screen.blit(title2, (400, 200))
        screen.blit(title3, (700, 200))
        pygame.display.flip()
    game = Game(num)
    clock = pygame.time.Clock()
    while True:
        if game.game_over or game.game_won:
            game.draw()
            pygame.display.update()
            break

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_SPACE and not game.game_over and not game.game_won and game.player.can_place_bomb():
                    bomb_x = (game.player.x - MARGIN_WIDTH) // TILE_SIZE * \
                        TILE_SIZE + MARGIN_WIDTH
                    bomb_y = (game.player.y - 10) // TILE_SIZE * TILE_SIZE + 10
                    if not any(bomb.x == bomb_x and bomb.y == bomb_y for bomb in game.bombs):
                        game.bombs.append(
                            Bomb(bomb_x, bomb_y, TILE_SIZE, RED, time.time(), bomb_path))
                        game.player.bombs -= 1  # Decrease bomb count
            if event.type == USEREVENT + 1:
                game.player.speed = 5  # Reset player speed
            if event.type == USEREVENT + 2:
                for enemy in game.enemies:
                    enemy.speed = 5  # Reset enemy speed
            if event.type == USEREVENT + 3:
                game.player.invincible = False  # Reset player invincibility
            if event.type == USEREVENT + 4:
                for enemy in game.enemies:
                    enemy.invincible = False  # Reset enemy invincibility
        keys = pygame.key.get_pressed()
        if not game.game_over and not game.game_won:
            if keys[K_LEFT]:
                game.player.move(-game.player.speed, 0, game.map_data)
            if keys[K_RIGHT]:
                game.player.move(game.player.speed, 0, game.map_data)
            if keys[K_UP]:
                game.player.move(0, -game.player.speed, game.map_data)
            if keys[K_DOWN]:
                game.player.move(0, game.player.speed, game.map_data)

        game.update()
        game.draw()
        pygame.display.update()
        clock.tick(30)

    # Secondary loop to keep the game over or win screen displayed
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        # Redraw the final screen
        game.draw()
        pygame.display.update()


if __name__ == "__main__":
    main()