import pygame
from pygame.sprite import Sprite
from dino_runner.utils.constants import (
    RUNNING,
    DUCKING,
    JUMPING
)
# pylint: disable=no-member


class Dinosaur(Sprite):

    POS_X = 80
    POS_Y = 300
    DUCK_POS_Y = 340
    JUMP_VELOCITY = 8.5

    def __init__(self):
        self.image = RUNNING[0]
        self.rect = self.image.get_rect()
        self.rect.x = self.POS_X
        self.rect.y = self.POS_Y
        self.step_index = 0
        self.running = True
        self.ducking = False
        self.jumping = False
        self.jumping_velocity = self.JUMP_VELOCITY

    def update(self, user_input):
        if self.jumping:
            self.jump()
        if self.ducking:
            self.duck()
        if self.running:
            self.run()
        if (user_input[pygame.K_DOWN] or user_input[pygame.K_s] or user_input[pygame.K_k])\
                and not self.jumping:
            self.running = False
            self.ducking = True
            self.jumping = False
        elif user_input[pygame.K_UP] or user_input[pygame.K_i] or user_input[pygame.K_w]\
                or user_input[pygame.K_SPACE]:
            self.jumping = True
            self.running = False
            self.ducking = False
        elif not self.jumping:
            self.jumping = False
            self.running = True
            self.ducking = False

        if self.step_index >= 10:
            self.step_index = 0

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def run(self):
        self.image = RUNNING[0] if self.step_index < 5 else RUNNING[1]
        self.rect = self.image.get_rect()
        self.rect.x = self.POS_X
        self.rect.y = self.POS_Y
        self.step_index += 1

    def jump(self):
        self.image = JUMPING
        if self.jumping:
            self.rect.y -= self.jumping_velocity * 4
            self.jumping_velocity -= 0.8
        if self.jumping_velocity < -self.JUMP_VELOCITY:
            self.rect.y = self.POS_Y
            self.jumping = False
            self.jumping_velocity = self.JUMP_VELOCITY

    def duck(self):
        self.image = DUCKING[0] if self.step_index < 5 else DUCKING[1]
        self.rect = self.image.get_rect()
        self.rect.x = self.POS_X
        self.rect.y = self.DUCK_POS_Y
        self.step_index += 1
