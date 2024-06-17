import pytest
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
from Game_Objects.game import Game  # Import the Game class from your game.py

# Mock constants or provide test-specific constants if needed
MAP_NUM = "1"
ROLE_NUM = "1"

@pytest.fixture
def setup_game():
    pygame.init()
    pygame.display.set_mode((800, 600))
    game_instance = Game(MAP_NUM, ROLE_NUM)
    yield game_instance
    pygame.quit()

def test_generate_enemies(setup_game):
    game = setup_game
    enemies = game.generate_enemies(5)
    assert len(enemies) == 5
    for enemy in enemies:
        assert isinstance(enemy, Enemy)

def test_generate_health_items(setup_game):
    game = setup_game
    game.generate_health_items()
    assert len(game.health_items) > 0
    for item in game.health_items:
        assert isinstance(item, HealthItem)

def test_generate_speed_items(setup_game):
    game = setup_game
    game.generate_speed_items()
    assert len(game.speed_items) > 0
    for item in game.speed_items:
        assert isinstance(item, SpeedItem)

def test_generate_invincible_items(setup_game):
    game = setup_game
    game.generate_invincible_items()
    assert len(game.invincible_items) > 0
    for item in game.invincible_items:
        assert isinstance(item, InvincibleItem)

def test_generate_landmines(setup_game):
    game = setup_game
    game.generate_landmines()
    assert len(game.landmines) > 0
    for landmine in game.landmines:
        assert isinstance(landmine, LandmineItem)

def test_generate_random_item(setup_game):
    game = setup_game
    initial_health_items = len(game.health_items)
    initial_speed_items = len(game.speed_items)
    initial_invincible_items = len(game.invincible_items)
    initial_landmines = len(game.landmines)

    # Call the method to generate a random item
    game.generate_random_item()

    # Check that at least one type of item has been added
    assert len(game.health_items) > initial_health_items or \
           len(game.speed_items) > initial_speed_items or \
           len(game.invincible_items) > initial_invincible_items or \
           len(game.landmines) > initial_landmines

    # Check the type of the last added item
    last_added_item = None
    if len(game.health_items) > initial_health_items:
        last_added_item = game.health_items[-1]
        assert isinstance(last_added_item, HealthItem)
    elif len(game.speed_items) > initial_speed_items:
        last_added_item = game.speed_items[-1]
        assert isinstance(last_added_item, SpeedItem)
    elif len(game.invincible_items) > initial_invincible_items:
        last_added_item = game.invincible_items[-1]
        assert isinstance(last_added_item, InvincibleItem)
    elif len(game.landmines) > initial_landmines:
        last_added_item = game.landmines[-1]
        assert isinstance(last_added_item, LandmineItem)

    # Optionally, you can further test the coordinates or placement logic of the item generated.
    # For simplicity, we're ensuring correct instance types here.

    # Additional assertions can be made based on specific game logic for placing items.
    # For example, ensuring the item is placed in a valid map tile.

    # Clean up any changes made during the test
    game.health_items = []
    game.speed_items = []
    game.invincible_items = []
    game.landmines = []

# Add more tests as needed for other methods in Game class
