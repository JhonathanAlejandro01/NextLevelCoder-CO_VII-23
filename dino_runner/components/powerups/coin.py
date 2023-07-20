
import pygame
from dino_runner.components.powerups.powerup import PowerUp
from dino_runner.utils.constants import COIN, COIN_TYPE


class Coin(PowerUp):
    def __init__(self):
        self.image = COIN
        self.frames = self.get_frames()
        super().__init__(self.frames)
        self.type = COIN_TYPE

    # Función para dividir la hoja de sprites en cuadros individuales

    def get_frames(self):
        # Dimensiones de cada cuadro del sprite
        frame_width = COIN.get_width()
        frame_height = COIN.get_height() // 24
        frames = []
        for y in range(0, self.image.get_height(), frame_height):
            for x in range(0, self.image.get_width(), frame_width):
                frame = self.image.subsurface(
                    pygame.Rect(x, y, frame_width, frame_height))
                frames.append(frame)
        return frames
