import pygame
import json
import os
from helper import image_load


class Map:
    def __init__(self):
        self.raw = []
        self.layer = []
        self.buildings = []
        self.size = 64
        self.tilesize = 64
        self.load_tiles()

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

    def update(self, dt, events):
        for tiles in self.layer:
            for tile in tiles:
                tile.update(dt, events)
        for build in self.buildings:
            build.update(dt, events)

    def draw(self, window, camera):
        for tiles in self.layer:
            for tile in tiles:
                tile.draw(window, camera)


class Tile:
    sprites = image_load("assets/map/tilesheet.png")

    def __init__(self, pos, tile):
        self.pos = pos
        self.tilesize = 64
        self.tile = (tile % 4 * self.tilesize, tile // 4 * self.tilesize)
        self.rect = pygame.Rect(pos.x, pos.y, self.tilesize, self.tilesize)
        self.mask = "tile"

    def update(self, dt, events):
        pass

    def draw(self, window, camera):
        window.blit(Tile.sprites, camera.cameraPos(self.pos), (self.tile[0], self.tile[1], self.tilesize, self.tilesize))