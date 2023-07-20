import pygame

# from dino_runner.utils.constants import SOUND_DOWN, SOUND_MUTED, SOUND_UP


class Music:
    def __init__(self):
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(0.3)
        # self.image = SOUND_DOWN

    # def update(self, user_input, screen):
    #     # down volume
    #     if user_input[pygame.K_MINUS] and pygame.mixer.music.get_volume() > 0.0:
    #         pygame.mixer.music.set_volume(
    #             pygame.mixer.music.get_volume() - 0.01)
    #         screen.blit(SOUND_DOWN, (850, 25))
    #     elif user_input[pygame.K_MINUS] and pygame.mixer.music.get_volume() == 0.0:
    #         screen.blit(SOUND_MUTED, (850, 25))

    #     # up volume
    #     if user_input[pygame.K_PLUS] and pygame.mixer.music.get_volume() < 1.0:
    #         pygame.mixer.music.set_volume(
    #             pygame.mixer.music.get_volume() + 0.01)
    #         screen.blit(SOUND_UP, (850, 25))
    #     elif user_input[pygame.K_PLUS] and pygame.mixer.music.get_volume() == 1.0:
    #         screen.blit(SOUND_UP, (850, 25))

    #     # disable SOUND
    #     elif user_input[pygame.K_m]:
    #         pygame.mixer.music.set_volume(0.0)
    #         screen.blit(sonido_mute, (850, 25))

    #     # reactivate SOUND
    #     elif user_input[pygame.K_COMMA]:
    #         pygame.mixer.music.set_volume(1.0)
    #         screen.blit(sonido_max, (850, 25))

    # def draw(self, screen):
    #     screen.blit(self.image, self.rect)
