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
        self.hitcount = None
        self.particle = False

    def update(self, dt, events, camera, bub):
        self.particle = False
        if self.hitcount != None:
            if self.status == "active":
                if events["mouse_pressed"][0]:
                    point = camera.mouseToGamePos(events["mouse_pos"])
                    if self.clickRect.collidepoint(point.x, point.y):
                        if camera.getDistance(self.getCenter()) < 100:
                            self.particle = True
                            self.hitcount -= dt
                            camera.shake(dt, 2)
                            if self.hitcount < 1:
                                self.status = "destroyed"

    def getCenter(self):
        return self.pos + pygame.Vector2(64, 108)

    def draw(self, window, camera):
        window.blit(Boulder.sprites, camera.cameraPos(self.pos))