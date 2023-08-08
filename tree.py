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
        self.rect = pygame.Rect(pos.x, pos.y, self.objsize, self.objsize)
        self.mask = "obj"

    def update(self, dt, events):
        pass

    def draw(self, window, camera):
        window.blit(Tree.sprites[self.treeType], camera.cameraPos(self.pos))