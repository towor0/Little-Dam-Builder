import pygame
from helper import image_load

class Tree:
    sprites = {
        1: image_load("assets/objs/tree.png"),
        2: image_load("assets/objs/tree_apple.png"),
        3: image_load("assets/objs/tree_flower.png"),
    }

    def __init__(self, pos, tT):
        self.treeType = tT
        self.pos = pos
        self.objsize = 128
        self.rect = pygame.Rect(pos.x + 42, pos.y + 106, 46, 11)
        self.clickRect = pygame.Rect(pos.x, pos.y, 128, 128)
        self.mask = "obj"
        self.status = "active"
        self.hitcount = 500

    def update(self, dt, events, camera, bub):
        if self.status == "active":
            if events["mouse_pressed"][0]:
                point = camera.mouseToGamePos(events["mouse_pos"])
                if self.clickRect.collidepoint(point.x, point.y):
                    if camera.getDistance(self.pos + pygame.Vector2(42+23, 106+5)) < 100:
                        self.hitcount -= dt
                        camera.shake(dt, 2)
                        if self.hitcount < 1:
                            self.status = "destroyed"

    def getCenter(self):
        return self.pos + pygame.Vector2(42+23, 106+5)

    def draw(self, window, camera):
        if self.status == "active":
            window.blit(Tree.sprites[self.treeType], camera.cameraPos(self.pos))