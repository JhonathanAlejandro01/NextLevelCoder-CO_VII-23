

from dino_runner.components.items.cloud import Cloud


class ItemManager:
    def __init__(self):
        self.has_items = False
        self.item = None

    def update(self, game):
        if not self.has_items:
            self.create_item()
        self.has_items = self.item.update(game.game_speed)

    def create_item(self):
        self.item = Cloud()
        self.has_items = True

    def draw(self, screen):
        self.item.draw(screen)
