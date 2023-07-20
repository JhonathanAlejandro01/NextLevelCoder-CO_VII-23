from pygame.sprite import Sprite


class Item(Sprite):

    def __init__(self, image, x_axis, y_axis):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x_axis
        self.rect.y = y_axis

    def update(self, game_speed):
        self.rect.x -= game_speed
        return self.rect.x > 0

    def draw(self, screen):
        screen.blit(self.image, self.rect)
