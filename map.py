import pygame
import json
import os
from helper import image_load
from tree import Tree
from boulder import Boulder


class Map:
    def __init__(self):
        self.raw = []
        self.layer = []
        self.size = 64
        self.tilesize = 64
        self.objmapsize = 32
        self.objsize = 128
        self.load_tiles()
        self.load_objs()
        self.tileSheetAnim = 0

    def load_tiles(self):
        with open(os.path.join("assets", "map", "map.json")) as f:
            raw = json.load(f)
        for layer in raw["layers"]:
            templ = []
            rawtempl = []
            for i in range(len(layer["data"])):
                if layer["data"][i] != 0:
                    templ.append(Tile(pygame.Vector2(i % self.size * self.tilesize, i // self.size * self.tilesize),
                                      layer["data"][i] - 1))
                rawtempl.append(layer["data"][i] - 1)
                if i % self.size == self.size - 1:
                    self.raw.append(rawtempl)
                    rawtempl = []
            if len(templ) != 0:
                self.layer.append(templ)

    def load_objs(self):
        with open(os.path.join("assets", "map", "objmap.json")) as f:
            raw = json.load(f)
        for layer in raw["layers"]:
            templ = []
            rawtempl = []
            for i in range(len(layer["data"])):
                if layer["data"][i] != 0:
                    if layer["data"][i] in (1, 2, 3):
                        templ.append(Tree(pygame.Vector2(i % self.objmapsize * self.objsize, i //
                                                         self.objmapsize * self.objsize),
                                          layer["data"][i]))
                    elif layer["data"][i] == 4:
                        templ.append(Boulder(pygame.Vector2(i % self.objmapsize * self.objsize, i //
                                                         self.objmapsize * self.objsize)))
                rawtempl.append(layer["data"][i] - 1)
                if i % self.size == self.size - 1:
                    self.raw.append(rawtempl)
                    rawtempl = []
            if len(templ) != 0:
                self.layer.append(templ)

    def update(self, dt, events, camera):
        for tile in self.layer[0]:
            tile.update(dt, events)
        for obj in self.layer[1]:
            obj.update(dt, events, camera)
            if obj.status == "destroyed":
                self.layer[1].pop(self.layer[1].index(obj))
        if self.tileSheetAnim > 5:
            self.tileSheetAnim = 0
            Tile.nextSheet()
        else:
            self.tileSheetAnim += dt

    def draw(self, window, camera):
        for tile in self.layer[0]:
            tile.draw(window, camera)


class Tile:
    sprites = {
        1: image_load("assets/map/tilesheet1.png"),
        2: image_load("assets/map/tilesheet2.png"),
        3: image_load("assets/map/tilesheet3.png"),
        4: image_load("assets/map/tilesheet4.png"),
        5: image_load("assets/map/tilesheet5.png"),
        6: image_load("assets/map/tilesheet6.png"),
        7: image_load("assets/map/tilesheet7.png"),
        8: image_load("assets/map/tilesheet8.png"),
        9: image_load("assets/map/tilesheet9.png"),
        10: image_load("assets/map/tilesheet10.png"),
        11: image_load("assets/map/tilesheet11.png"),
        12: image_load("assets/map/tilesheet12.png"),
        13: image_load("assets/map/tilesheet13.png"),
        14: image_load("assets/map/tilesheet14.png"),
        15: image_load("assets/map/tilesheet15.png"),
        16: image_load("assets/map/tilesheet16.png")
    }
    sheet = 1

    @classmethod
    def nextSheet(cls):
        cls.sheet += 1
        if cls.sheet > 16:
            cls.sheet = 1

    def __init__(self, pos, tile):
        self.pos = pos
        self.tileNum = tile
        self.tilesize = 64
        self.tile = (tile % 4 * self.tilesize, tile // 4 * self.tilesize)
        self.rect = pygame.Rect(pos.x, pos.y, self.tilesize, self.tilesize)
        self.mask = "tile"

    def update(self, dt, events):
        pass

    def draw(self, window, camera):
        window.blit(Tile.sprites[Tile.sheet], camera.cameraPos(self.pos), (self.tile[0], self.tile[1], self.tilesize, self.tilesize))