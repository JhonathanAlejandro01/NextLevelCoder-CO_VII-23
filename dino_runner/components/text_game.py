
import pygame

from dino_runner.utils.constants import FONT


class TextGame:
    def __init__(self):
        self.letter_type = pygame.font.Font(FONT, 40)

    def update(self, text, color):
        self.size = self.letter_type.render(text, True, color)
        self.rect = self.size.get_rect()
        self.rect.x = 150
        self.rect.y = 100

    def draw(self, screen):
        screen.blit(self.size, self.rect)
