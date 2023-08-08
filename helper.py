import pygame
import os
from math import sin, cos, radians, pi


def getPath(p):
    return os.path.join(*p.split("/"))


def image_load(p):
    image = pygame.image.load(getPath(p)).convert_alpha()
    return image


def point_pos(d, theta):
    theta_rad = pi/2 - radians(theta)
    return pygame.Vector2(d*cos(theta_rad), d*sin(theta_rad))