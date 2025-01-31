import pygame
import os

# Global Constants
TITLE = "Next Level Coder CO"
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1100
FPS = 30
IMG_DIR = os.path.join(os.path.dirname(__file__), "..", "assets")

# Assets Constants
ICON = pygame.image.load(os.path.join(IMG_DIR, "DinoWallpaper.png"))

RUNNING = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun2.png")),
]

RUNNING_SHIELD = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun1Shield.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun2.png")),
]

RUNNING_HAMMER = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck1Hammer.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun2.png")),
]

JUMPING = pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoJump.png"))
JUMPING_SHIELD = pygame.image.load(
    os.path.join(IMG_DIR, "Dino/DinoJumpShield.png"))
JUMPING_HAMMER = pygame.image.load(
    os.path.join(IMG_DIR, "Dino/DinoJumpHammer.png"))

DUCKING = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck2.png")),
]

DUCKING_SHIELD = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck1Shield.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck2.png")),
]

DUCKING_HAMMER = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck1Hammer.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck2.png")),
]

SMALL_CACTUS = [
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/SmallCactus1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/SmallCactus2.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/SmallCactus3.png")),
]
LARGE_CACTUS = [
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/LargeCactus1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/LargeCactus2.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/LargeCactus3.png")),
]

BIRD = [
    pygame.image.load(os.path.join(IMG_DIR, "Bird/Bird1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Bird/Bird2.png")),
]

CLOUD = pygame.image.load(os.path.join(IMG_DIR, 'Other/Cloud.png'))
SHIELD = pygame.image.load(os.path.join(IMG_DIR, 'Other/shield.png'))
HAMMER = pygame.image.load(os.path.join(IMG_DIR, 'Other/hammer.png'))

BG = pygame.image.load(os.path.join(IMG_DIR, 'Other/Track.png'))

HEART = pygame.image.load(os.path.join(IMG_DIR, 'Other/SmallHeart.png'))

DEFAULT_TYPE = "default"
SHIELD_TYPE = "shield"


# ---------- START NEW POWER-UP ----------
COIN_TYPE = "coin"

COIN = pygame.image.load(os.path.join(IMG_DIR, 'Other/Coin/24.png'))

RUNNING_COIN = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRunYellow1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRunYellow2.png")),
]

JUMPING_COIN = pygame.image.load(
    os.path.join(IMG_DIR, "Dino/DinoJumpYellow.png"))

DUCKING_COIN = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuckYellow1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuckYellow2.png")),
]
# ---------- END NEW POWER-UP ----------

# ---------- sound game ----------
pygame.mixer.init()  # Initialize audio but get error
MUSIC_GAME = pygame.mixer.music.load(os.path.join(IMG_DIR, 'Sounds/music.ogg'))
# SOUND_UP = pygame.image.load(os.path.join(IMG_DIR, 'Sound/volume_up.png'))
# SOUND_DOWN = pygame.image.load(os.path.join(IMG_DIR, 'Sound/volume_down.png'))
# SOUND_MAX = pygame.image.load(os.path.join(IMG_DIR, 'Sound/volume_max.png'))
# SOUND_MUTED = pygame.image.load(
#     os.path.join(IMG_DIR, 'Sound/volume_muted.png'))

# ---------- END sound game ----------

COLOR_BLACK = (0, 0, 0)
FONT = 'D:/Estudios/jala/juego/NextLevelCoder-CO_VII-23/dino_runner/assets/font/Lumanosimo-Regular.ttf'
