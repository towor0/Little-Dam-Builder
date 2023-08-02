import pygame
import os


def image_load(p):
    path = os.path.join(*p.split("/"))
    image = pygame.image.load(path).convert_alpha()
    return image
