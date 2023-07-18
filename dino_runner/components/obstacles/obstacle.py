"""generic obstacle module"""
from pygame.sprite import Sprite
from dino_runner.utils.constants import (
    SCREEN_WIDTH
)


class Obstacle(Sprite):
    """
    generic obstacle class
    Inherits from the Sprite class
    """

    def __init__(self, image):
        """
        construction method
        Get image as an argument
        """
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = SCREEN_WIDTH

    def update(self, game_speed):
        """
        Method update obstacle
        Get game_speed as an argument
        """
        self.rect.x -= game_speed
        return self.rect.x > 0  # true image is still on the screen, false otherwise

    def draw(self, screen):
        """
        method of drawing on screen
        Get screen as an argument
        """
        screen.blit(self.image, self.rect)
