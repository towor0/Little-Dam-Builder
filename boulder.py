import pygame
from helper import image_load

class Boulder:
    sprites = image_load("assets/objs/boulder.png")

    def __init__(self, pos):
        self.pos = pos
        self.objsize = 128
        self.rect = pygame.Rect(pos.x + 2, pos.y + 86, 124, 36)
        self.clickRect = pygame.Rect(pos.x, pos.y, 128, 128)
        self.mask = "obj"
        self.status = "active"
        self.hitcount = 100

    def update(self, dt, events, camera, bub):
        pass

    def getCenter(self):
        return self.pos + pygame.Vector2(42+23, 106+5)

    def draw(self, window, camera):
        window.blit(Boulder.sprites, camera.cameraPos(self.pos))