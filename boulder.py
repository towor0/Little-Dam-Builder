import pygame
from helper import image_load

class Boulder:
    sprites = image_load("assets/objs/boulder.png")

    def __init__(self, pos):
        self.pos = pos
        self.objsize = 128
        self.rect = pygame.Rect(pos.x, pos.y, self.objsize, self.objsize)
        self.mask = "obj"

    def update(self, dt, events):
        pass

    def draw(self, window, camera):
        window.blit(Boulder.sprites, camera.cameraPos(self.pos))