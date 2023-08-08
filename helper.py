import pygame
import os


def getPath(p):
    return os.path.join(*p.split("/"))


def image_load(p):
    image = pygame.image.load(getPath(p)).convert_alpha()
    return image
