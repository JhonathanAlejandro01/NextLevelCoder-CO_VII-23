"""Module handle obstacles in general"""
from dino_runner.components.obstacles.cactus import Cactus


class ObstacleManager:
    """
    Manages the obstacles in a level and their movement speeds based on player's
    """

    def __init__(self):
        self.has_obstacle = False
        self.obstacle = None

    def update(self, game):
        """
        Updates obstacle position according to current time step (based on players' velocity).
        """
        if not self.has_obstacle:
            self.create_obstacle()
        self.has_obstacle = self.obstacle.update(game.game_speed)

    def create_obstacle(self):
        """
        Creates an instance of cactus as one type of obstacle for now. In future this can
        be extended with more types or difficulty levels.
        """
        self.obstacle = Cactus()
        self.has_obstacle = True

    def draw(self, screen):
        """
        Draw the obstacle on the screen
        """
        if self.has_obstacle:
            self.obstacle.draw(screen)
