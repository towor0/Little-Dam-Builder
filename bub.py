import pygame
from helper import image_load


class Bub:
    def __init__(self):
        self.sprite = {
            "land": image_load("assets/bub/bub.png"),
            "water": image_load("assets/bub/bub_water.png")
        }
        self.pos = pygame.Vector2(64*32, 64*32)
        self.rect = pygame.Rect(self.pos.x, self.pos.y, 32, 32)
        self.vel = pygame.Vector2(0, 0)
        self.speed = 4
        self.mode = "land"
        self.collision = self.CollisionHandler(self.pos)

    class CollisionHandler:
        def __init__(self, pos):
            self.collision_mask = {
                "objects": [],
                "tile": []
            }
            self.collision = []
            self.pos = pos
            self.rect = pygame.Rect(pos.x, pos.y, 24, 32)
            self.air_time = 0

        def update(self, dt, events):
            self.air_time += dt

        def update_player(self, pos):
            self.pos = pos
            self.rect = pygame.Rect(pos.x, pos.y, 24, 32)

        def update_collision(self, mask):
            self.collision = []
            for obj in self.collision_mask[mask]:
                if self.rect.colliderect(obj.rect):
                    self.collision.append(obj)

        def update_objects(self, mask, objs):
            self.collision_mask[mask] = []
            for obj in objs:
                self.collision_mask[mask].append(obj)

        def get_collided(self, mask):
            return self.collision

        def get_pos(self, vel):
            mode = "land"
            facing = []
            self.update_player(self.pos + pygame.Vector2(vel.x, 0))
            self.update_collision("tile")
            for tile in self.collision:
                if tile.rect.collidepoint(self.rect.centerx, self.rect.centery):
                    if tile.tileNum == 3:
                        mode = "water"
            self.update_collision("objects")
            for obj in self.collision:
                if vel.x > 0:
                    self.rect.right = obj.rect.left
                    self.pos.x = self.rect.x
                    facing.append("right")
                elif vel.x < 0:
                    self.rect.left = obj.rect.right
                    self.pos.x = self.rect.x
                    facing.append("left")
            self.update_player(self.pos + pygame.Vector2(0, vel.y))
            self.update_collision("objects")
            for obj in self.collision:
                if vel.y > 0:
                    self.rect.bottom = obj.rect.top
                    self.air_time = 0
                    self.pos.y = self.rect.y
                    facing.append("bot")
                elif vel.y < 0:
                    self.rect.top = obj.rect.bottom
                    self.pos.y = self.rect.y
                    facing.append("top")
            if self.rect.right > 64 * 64:
                self.rect.right = 64 * 64
                self.pos.x = self.rect.x
            if self.rect.left < 0:
                self.rect.left = 0
                self.pos.x = self.rect.x
            if self.rect.top < 0:
                self.rect.top = 0
                self.pos.y = self.rect.y
            if self.rect.bottom > 64 * 64:
                self.rect.bottom = 64 * 64
                self.pos.y = self.rect.y
            return self.rect, self.pos, facing, mode

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
        return cvel

    def update(self, dt, events):
        cvel = self.move(dt, events)
        self.collision.update(dt, events)
        cvel += self.vel
        self.rect, self.pos, facing, self.mode = self.collision.get_pos(cvel)

    def draw(self, window, camera):
        window.blit(self.sprite[self.mode], camera.cameraPos(self.pos))
