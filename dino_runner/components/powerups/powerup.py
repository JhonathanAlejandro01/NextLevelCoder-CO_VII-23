import random
from pygame.sprite import Sprite

from dino_runner.utils.constants import DEFAULT_TYPE, SCREEN_WIDTH


class PowerUp(Sprite):
    def __init__(self, frames):
        self.frames = frames
        self.image = self.frames[0]
        self.rect = self.image.get_rect()
        self.rect.x = SCREEN_WIDTH + 40
        self.rect.y = random.randint(200, 250)
        self.type = DEFAULT_TYPE
        self.frame_index = 0  # Índice actual de la lista de imágenes
        # Velocidad de la animación (ajustar según la velocidad deseada)
        self.animation_speed = 10
        self.current_frame = 0  # Contador para controlar el cambio de imagen

    def update(self, game_speed):
        self.rect.x -= game_speed
        if self.current_frame >= self.animation_speed:
            self.current_frame = 0
            self.frame_index = (self.frame_index + 1) % len(self.frames)
            self.image = self.frames[self.frame_index]
        return self.rect.x > 0  # true if image is still on the screen, false otherwise

    def draw(self, screen):
        screen.blit(self.image, self.rect)
