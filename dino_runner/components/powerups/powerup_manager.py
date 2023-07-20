import random
from dino_runner.components.powerups.coin import Coin
from dino_runner.components.powerups.shield import Shield


class PowerUpManager:
    """
    Manages all aspects of a player's ability to collect power ups during their run through D
    - Creates new power-ups at regular intervals
    """

    def __init__(self):
        self.has_powerup = False
        self.powerup = None
        self.next_powerup_show = 100

    def update(self, game):
        """
        Updates the power-up manager's state based on current conditions in the given Game object
        """
        if not self.has_powerup and game.score == self.next_powerup_show:
            self.create_powerup()
            self.next_powerup_show += random.randint(200, 500)
        if self.has_powerup:
            self.has_powerup = self.powerup.update(game.game_speed)
            if game.player.rect.colliderect(self.powerup.rect):
                self.has_powerup = False
                game.player.type = self.powerup.type

    def create_powerup(self):
        list_powerups = [Shield(), Coin()]
        self.powerup = random.choice(list_powerups)
        self.has_powerup = True

    def draw(self, screen):
        if self.has_powerup:
            self.powerup.draw(screen)
