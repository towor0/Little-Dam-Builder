import pygame
from helper import image_load
import random


class Stick:
    sprite = image_load("assets/objs/stick.png")

    def __init__(self, pos):
        self.vel = pygame.Vector2(random.randint(-3, 3), random.randint(-8, -1))
        self.ground = pos.y + random.randint(-100, 100)
        self.pos = pygame.Vector2(pos.x + random.randint(-16, 16), pos.y + random.randint(-16, 16))
        self.rect = pygame.Rect(self.pos.x, self.pos.y, 16, 16)
        self.grounded = False
        self.collected = False

    def update(self, dt, events, bub):
        if not self.grounded:
            self.pos += self.vel * dt
            self.vel.y += dt / 4
            if self.pos.y > self.ground and self.vel.y > 0:
                self.grounded = True
            self.rect.x = self.pos.x
            self.rect.y = self.pos.y
        else:
            if self.rect.colliderect(bub.rect):
                self.collected = True
                bub.inventory.add("stick")

    def draw(self, window, camera):
        window.blit(Stick.sprite, camera.cameraPos(self.pos))


class Apple:
    sprite = image_load("assets/objs/apple.png")

    def __init__(self, pos):
        self.vel = pygame.Vector2(random.randint(-3, 3), random.randint(-8, -1))
        self.ground = pos.y + random.randint(-100, 100)
        self.pos = pygame.Vector2(pos.x + random.randint(-16, 16), pos.y + random.randint(-16, 16))
        self.rect = pygame.Rect(self.pos.x, self.pos.y, 16, 16)
        self.grounded = False
        self.collected = False

    def update(self, dt, events, bub):
        if not self.grounded:
            self.pos += self.vel * dt
            self.vel.y += dt / 4
            if self.pos.y > self.ground and self.vel.y > 0:
                self.grounded = True
            self.rect.x = self.pos.x
            self.rect.y = self.pos.y
        else:
            if self.rect.colliderect(bub.rect):
                self.collected = True
                bub.inventory.add("apple")

    def draw(self, window, camera):
        window.blit(Apple.sprite, camera.cameraPos(self.pos))


class Flower:
    sprite = image_load("assets/objs/flower.png")

    def __init__(self, pos):
        self.vel = pygame.Vector2(random.randint(-3, 3), random.randint(-8, -1))
        self.ground = pos.y + random.randint(-100, 100)
        self.pos = pygame.Vector2(pos.x + random.randint(-16, 16), pos.y + random.randint(-16, 16))
        self.rect = pygame.Rect(self.pos.x, self.pos.y, 16, 16)
        self.grounded = False
        self.collected = False

    def update(self, dt, events, bub):
        if not self.grounded:
            self.pos += self.vel * dt
            self.vel.y += dt / 4
            if self.pos.y > self.ground and self.vel.y > 0:
                self.grounded = True
            self.rect.x = self.pos.x
            self.rect.y = self.pos.y
        else:
            if self.rect.colliderect(bub.rect):
                self.collected = True
                bub.inventory.add("flower")

    def draw(self, window, camera):
        window.blit(Flower.sprite, camera.cameraPos(self.pos))

class Rock:
    sprite = image_load("assets/objs/rock.png")

    def __init__(self, pos):
        self.vel = pygame.Vector2(random.randint(-3, 3), random.randint(-8, -1))
        self.ground = pos.y + random.randint(-100, 100)
        self.pos = pygame.Vector2(pos.x + random.randint(-16, 16), pos.y + random.randint(-16, 16))
        self.rect = pygame.Rect(self.pos.x, self.pos.y, 16, 16)
        self.grounded = False
        self.collected = False

    def update(self, dt, events, bub):
        if not self.grounded:
            self.pos += self.vel * dt
            self.vel.y += dt / 4
            if self.pos.y > self.ground and self.vel.y > 0:
                self.grounded = True
            self.rect.x = self.pos.x
            self.rect.y = self.pos.y
        else:
            if self.rect.colliderect(bub.rect):
                self.collected = True
                bub.inventory.add("rock")

    def draw(self, window, camera):
        window.blit(Rock.sprite, camera.cameraPos(self.pos))
