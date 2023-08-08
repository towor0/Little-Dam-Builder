import pygame
import random


class Camera:
    def __init__(self, pos):
        self.rect = pygame.Rect(0, 0, 640, 480)
        self.rect.center = pos
        self.targety = pos.x
        self.targetx = pos.y
        self.shaketime = 0
        self.centerpos = pygame.Vector2(pos.x, pos.y)
        self.smooth = 9
        self.limit = pygame.Rect(0, 0, 64 * 64, 64 * 64)

    def shake(self, time):
        self.shaketime += time

    def update(self, dt, events, focus):
        # camera smoothening
        self.targetx, self.targety = focus
        self.centerpos.y += (self.targety - self.centerpos.y) / self.smooth
        self.centerpos.x += (self.targetx - self.centerpos.x) / self.smooth
        # apply camera shakes
        if self.shaketime > 0:
            self.shaketime -= dt
            self.centerpos.x += random.randint(-4, 4)
            self.centerpos.y += random.randint(-4, 4)
        self.rect.centerx = self.centerpos.x
        self.rect.centery = self.centerpos.y
        if self.rect.x < self.limit.x:
            self.rect.x = self.limit.x
        if self.rect.right > self.limit.x + self.limit.width:
            self.rect.right = self.limit.x + self.limit.width
        if self.rect.y < self.limit.y:
            self.rect.y = self.limit.y
        if self.rect.bottom > self.limit.y + self.limit.height:
            self.rect.bottom = self.limit.y + self.limit.height

    def cameraPos(self, pos):
        return pygame.Vector2(pos.x - self.rect.x, pos.y - self.rect.y)

    def backgroundPos(self, effect):
        return pygame.Vector2(-self.rect.x/effect, -self.rect.y/effect)
