"""Bird obstacle module"""
from dino_runner.components.obstacles.obstacle import Obstacle
from dino_runner.utils.constants import BIRD


class Bird(Obstacle):
    """
    Bird class inherits from Obstacle
    """

    def __init__(self):
        self.image = BIRD[0]
        super().__init__(self.image)
        self.rect.y = 300
        self.step_index = 0

    def update(self):
        if self.step_index >= 10:
            self.step_index = 0

    def fly(self):
        self.image = BIRD[0] if self.step_index < 5 else BIRD[1]
        self.rect = self.image.get_rect()
        # self.rect.x = self.POS_X
        # self.rect.y = self.POS_Y
        self.step_index += 1
