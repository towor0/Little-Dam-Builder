import pygame
from helper import image_load


class Bub:
    def __init__(self):
        self.sprite = image_load("assets/bub/bub.png")
        self.pos = pygame.Vector2(0, 0)
        self.rect = pygame.Rect(self.pos.x, self.pos.y, 64, 64)
        self.vel = pygame.Vector2(0, 0)
        self.speed = 4

    def move(self, dt, events):
        cvel = pygame.Vector2(0, 0)
        movementDirection = {
            "vertical": 0,
            "horizontal": 0
        }
        if events["keys"][pygame.K_d]:
            movementDirection["horizontal"] += 1
        if events["keys"][pygame.K_a]:
            movementDirection["horizontal"] -= 1
        if events["keys"][pygame.K_w]:
            movementDirection["vertical"] -= 1
        if events["keys"][pygame.K_s]:
            movementDirection["vertical"] += 1
        if movementDirection["vertical"] != 0 and movementDirection["horizontal"] != 0:
            cvel.x += 0.71 * movementDirection["horizontal"] * self.speed
            cvel.y += 0.71 * movementDirection["vertical"] * self.speed
        else:
            cvel.x += movementDirection["horizontal"] * self.speed
            cvel.y += movementDirection["vertical"] * self.speed
        cvel += self.vel
        self.pos += cvel
        self.rect.x = self.pos.x
        self.rect.y = self.pos.y

    def update(self, dt, events):
        self.move(dt, events)

    def draw(self, window, camera):
        window.blit(self.sprite, camera.cameraPos(self.pos))
