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
        self.bub.update(dt, events)
        self.map.update(dt, events)
        self.camera.update(dt, events, self.bub.rect.center)

    def draw(self, window):
        self.map.draw(window, self.camera)
        self.bub.draw(window, self.camera)

