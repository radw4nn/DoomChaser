import pygame
from settings import *  # Importing constants or settings from a settings module

_ = False  # Placeholder for empty tiles (assuming False is used to represent empty tiles)

# Definition of TILEMAP: A 2D list representing the map with different tile types.
TILEMAP = [
    # Each row represents a line of tiles in the game map.
    # Different numbers represent different types of tiles.
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 5, 1, 1, 1, 1, 5, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 1, _, _, _, _, _, _, _, _, _, 1],
    [1, _, _, _, _, _, _, _, _, _, 3, 3, 3, 3, 3, 3, 3, 3, 3, _, _, _, _, _, 1, _, 1, _, 1, 1, 1, 1],
    [2, 2, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 1, _, _, _, 1, _, 1, _, _, _, _, 1],
    [2, 1, _, _, 1, _, _, 1, 1, 1, 4, 1, 1, 1, 1, 1, _, _, _, _, 1, 1, _, _, 1, _, 1, 1, 1, _, 1, 1],
    [2, _, _, _, 1, _, _, _, 5, _, 1, _, _, _, _, 1, _, 5, _, _, 1, _, _, _, 1, _, _, 1, _, _, _, 1],
    [2, _, _, _, 1, _, _, _, _, _, 1, _, _, _, _, 1, _, _, _, _, 1, _, _, _, 4, 3, 3, 3, 1, 1, 1, 1],
    [2, _, _, _, 1, _, _, _, _, _, 1, _, 4, 4, _, 1, _, _, _, _, _, _, 1, _, _, _, _, _, _, _, _, 1],
    [2, _, _, _, 1, _, 5, _, 5, _, 1, _, _, 4, _, 1, _, _, 1, _, _, _, 1, _, _, _, _, _, 2, _, _, 1],
    [2, _, _, _, 1, 5, _, _, _, _, 1, _, _, _, _, 3, _, 5, 1, _, _, _, _, _, _, 3, _, 2, 2, 2, _, 1],
    [1, _, _, _, 1, _, _, _, _, _, 1, _, _, _, _, 3, _, _, 1, _, _, _, 1, _, _, 3, _, _, 2, _, _, 1],
    [1, _, _, _, 1, _, _, 5, _, _, _, _, _, _, _, 3, _, _, 1, _, _, _, 5, 1, _, 3, _, _, _, _, _, 1],
    [1, _, _, _, 1, _, _, _, _, _, _, 1, 1, _, _, 3, _, 1, 4, 1, 1, _, _, _, _, 3, _, _, _, _, _, 1],
    [1, 1, _, 1, 4, 1, 1, 1, 1, 1, 5, 1, 3, 3, 3, 4, _, 1, _, _, _, _, _, _, _, 3, _, _, 2, _, _, 1],
    [1, _, _, _, _, _, _, 1, _, _, _, _, _, _, _, _, _, 1, _, _, _, _, _, _, _, 3, _, _, 2, _, _, 1],
    [1, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 1],
    [1, 3, 3, 3, 5, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 1, 1, 1, 1]
]


class Map:
    def __init__(self, game) -> None:
        self.game = game  # Reference to the game object
        self.tilemap = TILEMAP  # Initialize with TILEMAP
        self.world_map = {}  # Dictionary to store the world map data

        self.get_world_map(self.tilemap)  # Populate the world_map with tile data

    def get_world_map(self, tilemap) -> None:
        """
        Converts the tilemap into a world_map dictionary where the keys are
        (x, y) coordinates and the values are the tile types.
        """
        for i, row in enumerate(tilemap):
            for j, col in enumerate(row):
                if col:  # Only add tiles that are not empty
                    self.world_map[(j, i)] = col

    def draw(self) -> None:
        """
        Draws the map on the screen by iterating through world_map and
        drawing a rectangle for each tile.
        """
        # Draw each tile as a rectangle on the screen
        [pygame.draw.rect(self.game.screen, (255, 255, 255),
                          (pos[0] * TILESIZE, pos[1] * TILESIZE, TILESIZE, TILESIZE), 2)
         for pos in self.world_map]
