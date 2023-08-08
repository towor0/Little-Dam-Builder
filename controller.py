import random

import pygame
from bub import Bub
from camera import Camera
from map import Map
from gui import GUI, MenuGUI
from helper import point_pos


class Controller:
    def __init__(self):
        self.menu = MenuController()
        self.game = GameController()

    def update(self, dt, events):
        if not self.menu.started:
            self.menu.update(dt, events)
        else:
            self.game.update(dt, events)
            if self.game.gui.gameFinished:
                self.menu = MenuController()
                self.game = GameController()

    def draw(self, window):
        if not self.menu.started:
            self.menu.draw(window)
        else:
            self.game.draw(window)


class GameController:
    def __init__(self):
        self.bub = Bub(pygame.Vector2(32 * 64, 32 * 64))
        self.camera = Camera(self.bub.pos)
        self.map = Map()
        self.gui = GUI()

    def update(self, dt, events):
        self.bub.collision.update_objects("tile", self.map.layer[0])
        self.bub.collision.update_objects("obj", self.map.layer[1])
        self.bub.update(dt, events)
        self.camera.update(dt, events, self.bub.rect.center)
        self.map.update(dt, events, self.camera, self.bub)
        self.gui.update(dt, events, self.bub.inventory)

    def draw(self, window):
        self.map.draw(window, self.camera)
        self.map.drawDrops(window, self.camera)
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
        if not bubDrawn:
            self.bub.draw(window, self.camera)
        self.map.drawParticles(window, self.camera)
        self.gui.draw(window)


class MenuController:
    def __init__(self):
        self.map = Map()
        self.bub = Bub(pygame.Vector2(-10000, -10000))
        self.camera = Camera(pygame.Vector2(32 * 64, 24 * 64))
        self.navPos = pygame.Vector2(32 * 64, 24 * 64)
        self.navTime = 10
        self.navSpeed = point_pos(1, random.randint(0, 360))
        self.gui = MenuGUI()
        self.started = False

    def update(self, dt, events):
        self.map.update(dt, events, self.camera, self.bub)
        self.camera.update(dt, events, self.navPos)
        if self.navTime < 0:
            self.navTime = random.randint(50, 500)
            self.navSpeed = point_pos(1, random.randint(0, 360))
        self.navTime -= dt
        self.navPos += self.navSpeed * dt
        if events["keys"][pygame.K_RETURN]:
            self.started = True


    def draw(self, window):
        self.map.draw(window, self.camera)
        for obj in self.map.layer[1]:
            obj.draw(window, self.camera)
        self.gui.draw(window)

