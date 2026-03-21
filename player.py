# Модулі
from pygame import *

class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y

        self.speed = 7
        self.gravity = 0.5
        self.velocity_y = 0
        self.jump_speed = -15
        self.on_ground = False
        self.direction = "right"

        self.image = image.load("assets/images/levels/player/player.png").convert_alpha()
        self.image = transform.smoothscale(self.image, (80, 140))
        self.image_right = self.image
        self.image_left = transform.flip(self.image_right, True, False)

        self.rect = self.image.get_rect()
        self.rect.topleft = (self.x, self.y)

    def move(self, platforms):
        keys = key.get_pressed()
        dx = 0
        dy = 0

        if keys[K_LEFT]:
            dx = -self.speed
            self.direction = "left"
            
        if keys[K_RIGHT]:
            dx = self.speed
            self.direction = "right"

        if keys[K_a] and self.on_ground:
            self.velocity_y = self.jump_speed
            self.on_ground = False

        self.velocity_y += self.gravity
        if self.velocity_y > 10:
            self.velocity_y = 10
        dy += self.velocity_y

        self.on_ground = False
        for platform in platforms:
            if platform.colliderect(self.rect.x, self.rect.y + dy, self.rect.width, self.rect.height):
                if self.velocity_y > 0:
                    dy = platform.top - self.rect.bottom
                    self.velocity_y = 0
                    self.on_ground = True
                elif self.velocity_y < 0:
                    dy = platform.bottom - self.rect.top
                    self.velocity_y = 0

            if platform.colliderect(self.rect.x + dx, self.rect.y, self.rect.width, self.rect.height):
                dx = 0

        return dx, dy

    def show(self, window):
        if self.direction == "right":
            window.blit(self.image_right, self.rect)
        elif self.direction == "left":
            window.blit(self.image_left, self.rect)
