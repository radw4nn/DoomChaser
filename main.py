import pygame, sys, random
from settings import *
from levels import *
from player import *
from raycast import *
from object_renderer import *
from sprite_object import *
from object_handler import *
from weapon import *
from sounds import *
from pathfinding import *


class Game:
    def __init__(self) -> None:
        pygame.init()  # Initialize Pygame
        pygame.mouse.set_visible(False)  # Hide the mouse cursor
        self.screen = pygame.display.set_mode(RES)  # Set up the display with defined resolution
        self.running = False  # Game running state

        self.FPSclock = pygame.time.Clock()  # Clock to manage frame rate
        self.delta_time = 1  # Time between frames, initialized to 1

        # Set up timer for global events
        self.global_trigger = False
        self.global_event = pygame.USEREVENT
        pygame.time.set_timer(self.global_event, 40)  # Trigger a custom event every 40 ms

        self.initialize_game()  # Initialize game components

    def initialize_game(self):
        # Initialize all game components
        self.map = Map(self)
        self.player = Player(self)
        self.object_renderer = ObjectRenderer(self)
        self.raycast = Raycast(self)
        self.object_handler = ObjectHandler(self)
        self.weapon = Weapon(self)
        self.sounds = Sound(self)
        self.pathfinding = Pathfinding(self)
        self.sounds.play_theme()  # Start playing the background theme

    def draw(self) -> None:
        # Draw game components on the screen
        # self.screen.fill(BLACK)  # Uncomment if you need a background color
        self.object_renderer.draw()  # Draw objects and walls
        self.weapon.draw()  # Draw the weapon
        # self.map.draw()  # Uncomment if you need to draw the map
        # self.player.draw()  # Uncomment if you need to draw the player

    def update(self) -> None:
        self.draw()  # Call draw method to render the screen
        self.delta_time = self.FPSclock.tick(FPS)  # Control the frame rate and update delta_time

        pygame.display.set_caption(f"FPS: {self.FPSclock.get_fps() :.1f}")  # Update window title with current FPS

        self.raycast.update()  # Update raycasting
        self.player.update()  # Update player state
        self.object_handler.update()  # Update object interactions

        # Update weapon state (must be after object handler to ensure NPCs detect hits)
        self.weapon.update()

        pygame.display.update()  # Refresh the display

    def events(self) -> None:
        self.global_trigger = False  # Reset global event trigger
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                pygame.quit()  # Quit Pygame
                sys.exit()  # Exit the program

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    self.initialize_game()  # Reset the game if 'R' is pressed

            elif event.type == self.global_event:
                self.global_trigger = True  # Set global trigger if the custom event occurs

            self.player.single_fire_event(event)  # Handle player-specific events

    def start(self):
        self.running = True
        while self.running:
            self.update()  # Update the game state
            self.events()  # Process user inputs and events


def main() -> None:
    game = Game()  # Create a Game instance
    game.start()  # Start the game loop


if __name__ == "__main__":
    main()  # Run the game if this script is executed
