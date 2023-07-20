

import random
from dino_runner.components.items.item import Item
from dino_runner.utils.constants import CLOUD, SCREEN_WIDTH


class Cloud(Item):
    def __init__(self):
        select_image = CLOUD
        position_x = SCREEN_WIDTH + 40
        position_y = random.randint(20, 70)
        super().__init__(select_image, position_x, position_y)
