
import pygame
from dino_runner.components.powerups.powerup import PowerUp
from dino_runner.utils.constants import COIN, COIN_TYPE


class Coin(PowerUp):
    def __init__(self):
        select_image = COIN
        super().__init__(select_image)
        self.type = COIN_TYPE
