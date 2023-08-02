import pygame
import time
import sys
import os

# initialize pygame
pygame.init()
pygame.display.set_caption("Little Dam Builder")
clock = pygame.time.Clock()
prev_time = time.time()
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
window = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT)).convert_alpha()
running = True

# initialize controllers
from controller import Controller

controller = Controller()

# game loop
while running:
    clock.tick(60)  # frame cap
    now = time.time()
    dt = (now - prev_time) * 60
    prev_time = now
    events = {
        "events": pygame.event.get(),
        "keys": pygame.key.get_pressed(),
        "mod_keys": pygame.key.get_mods(),
        "mouse_pos": pygame.mouse.get_pos(),
    }
    for event in events["events"]:
        if event.type == pygame.QUIT:
            running = False
    # update all instances
    controller.update(dt, events)
    # draw all instances
    window.fill((100, 200, 255))
    controller.draw(window)
    screen.blit(window, (0, 0))
    pygame.display.flip()

# quit
pygame.quit()
sys.exit()
