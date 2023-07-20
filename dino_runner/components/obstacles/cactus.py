"""cactus obstacle module"""
import random
from dino_runner.components.obstacles.obstacle import Obstacle
from dino_runner.utils.constants import LARGE_CACTUS, SMALL_CACTUS


class Cactus(Obstacle):
    """
    Cactus class inherits from Obstacle
    """

    def __init__(self):
        image_list = SMALL_CACTUS + LARGE_CACTUS
        select_image = random.choice(image_list)
        super().__init__(select_image)
        self.rect.y = 390 - self.rect.h
