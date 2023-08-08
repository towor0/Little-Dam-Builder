import pygame
from helper import image_load, getPath


class GUI:
    def __init__(self):
        self.font = pygame.font.Font(getPath("assets/ARCADECLASSIC.TTF"), 32)
        self.stick = image_load("assets/objs/stick.png")
        self.stickCount = self.font.render("0", True, (0, 0, 0))
        self.rock = image_load("assets/objs/rock.png")
        self.rockCount = self.font.render("0", True, (0, 0, 0))
        self.flower = image_load("assets/objs/flower.png")
        self.flowerCount = self.font.render("0", True, (0, 0, 0))
        self.apple = image_load("assets/objs/apple.png")
        self.appleCount = self.font.render("0", True, (0, 0, 0))

    def update(self, inventory):
        self.stickCount = self.font.render(str(inventory.items["stick"]), True, (0, 0, 0))
        self.rockCount = self.font.render(str(inventory.items["rock"]), True, (0, 0, 0))
        self.appleCount = self.font.render(str(inventory.items["apple"]), True, (0, 0, 0))
        self.flowerCount = self.font.render(str(inventory.items["flower"]), True, (0, 0, 0))

    def draw(self, window):
        window.blit(self.stick, (10, 10))
        window.blit(self.stickCount, (50, 10))
        window.blit(self.rock, (10, 50))
        window.blit(self.rockCount, (50, 50))
        window.blit(self.flower, (10, 90))
        window.blit(self.flowerCount, (50, 90))
        window.blit(self.apple, (10, 130))
        window.blit(self.appleCount, (50, 130))

