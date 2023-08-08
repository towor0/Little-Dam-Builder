import pygame
from bub import Bub
from camera import Camera
from map import Map


class Controller:
    def __init__(self):
        self.game = GameController()

    def update(self, dt, events):
        self.game.update(dt, events)

    def draw(self, window):
        self.game.draw(window)


class GameController:
    def __init__(self):
        self.bub = Bub()
        self.camera = Camera(self.bub.pos)
        self.map = Map()

    def update(self, dt, events):
        self.bub.collision.update_objects("tile", self.map.layer[0])
        self.bub.collision.update_objects("obj", self.map.layer[1])
        self.bub.update(dt, events)
        self.camera.update(dt, events, self.bub.rect.center)
        self.map.update(dt, events, self.camera)

    def draw(self, window):
        self.map.draw(window, self.camera)
        bubDrawn = False
        for obj in self.map.layer[1]:
            if not bubDrawn:
                if obj.rect.bottom > self.bub.rect.bottom:
                    self.bub.draw(window, self.camera)
                    obj.draw(window, self.camera)
                    bubDrawn = True
                else:
                    obj.draw(window, self.camera)
            else:
                obj.draw(window, self.camera)

