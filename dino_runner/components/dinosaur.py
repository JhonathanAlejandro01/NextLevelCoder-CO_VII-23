"""Module Dinosaur"""
import pygame
from pygame.sprite import Sprite
from dino_runner.utils.constants import (
    DEAD,
    DUCKING_SHIELD,
    RUNNING_SHIELD,
    JUMPING_SHIELD,
    RUNNING,
    DUCKING,
    JUMPING,
    DEFAULT_TYPE,
    SHIELD_TYPE
)
# pylint: disable=no-member


class Dinosaur(Sprite):
    """
    Class to represent a single instance of the game character "Dino"
    """

    POS_X = 80
    POS_Y = 300
    DUCK_POS_Y = 340
    JUMP_VELOCITY = 8.5

    def __init__(self):
        self.running_img = {DEFAULT_TYPE: RUNNING, SHIELD_TYPE: RUNNING_SHIELD}
        self.jumping_img = {DEFAULT_TYPE: JUMPING, SHIELD_TYPE: JUMPING_SHIELD}
        self.ducking_img = {DEFAULT_TYPE: DUCKING, SHIELD_TYPE: DUCKING_SHIELD}
        self.dead_img = DEAD
        self.type = DEFAULT_TYPE
        self.image = self.running_img[self.type][0]
        self.rect = self.image.get_rect()
        self.rect.x = self.POS_X
        self.rect.y = self.POS_Y
        self.step_index = 0
        self.running = True
        self.ducking = False
        self.jumping = False
        self.jumping_velocity = self.JUMP_VELOCITY

    def update(self, user_input):
        """
        Update the dinosaur's state based on input from player
        """
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
        """
        Draw dinosaur on screen
        """
        screen.blit(self.image, self.rect)

    def run(self):
        """
        Method for running dinosaur
        """
        self.image = self.running_img[self.type][self.step_index // 5]
        self.rect = self.image.get_rect()
        self.rect.x = self.POS_X
        self.rect.y = self.POS_Y
        self.step_index += 1

    def jump(self):
        """
        This method is called when the player presses up arrow, space, i or w key to start ducking
        """
        self.image = self.jumping_img[self.type]
        if self.jumping:
            self.rect.y -= int(self.jumping_velocity * 4)
            self.jumping_velocity -= 0.8
        if self.jumping_velocity < -self.JUMP_VELOCITY:
            self.rect.y = self.POS_Y
            self.jumping = False
            self.jumping_velocity = self.JUMP_VELOCITY

    def duck(self):
        """
        This method is called when the player presses down arrow key to start ducking
        """
        self.image = self.ducking_img[self.type][self.step_index // 5]
        self.rect = self.image.get_rect()
        self.rect.x = self.POS_X
        self.rect.y = self.DUCK_POS_Y
        self.step_index += 1

    def dead(self):
        self.image = self.dead
        self.rect = self.image.get_rect()
        self.rect.x = self.POS_X
        self.rect.y = self.POS_Y
        self.step_index += 1
