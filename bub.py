import pygame
from helper import image_load


class Bub:
    def __init__(self, pos):
        self.sprite = {
            "land": {
                "01": image_load("assets/bub/bub_down.png"),
                "11": image_load("assets/bub/bub_downright.png"),
                "-11": image_load("assets/bub/bub_downleft.png"),
                "10": image_load("assets/bub/bub_right.png"),
                "-10": image_load("assets/bub/bub_left.png"),
                "0-1": image_load("assets/bub/bub_up.png"),
                "1-1": image_load("assets/bub/bub_upright.png"),
                "-1-1": image_load("assets/bub/bub_upleft.png"),
            },
            "water": {
                "01": image_load("assets/bub/bub_water_down.png"),
                "11": image_load("assets/bub/bub_water_downright.png"),
                "-11": image_load("assets/bub/bub_water_downleft.png"),
                "10": image_load("assets/bub/bub_water_right.png"),
                "-10": image_load("assets/bub/bub_water_left.png"),
                "0-1": image_load("assets/bub/bub_water_up.png"),
                "1-1": image_load("assets/bub/bub_water_upright.png"),
                "-1-1": image_load("assets/bub/bub_water_upleft.png"),
            },
        }
        self.pos = pos
        self.offset = pygame.Vector2(0, 0)
        self.rect = pygame.Rect(self.pos.x, self.pos.y, 32, 32)
        self.vel = pygame.Vector2(0, 0)
        self.speed = 4
        self.waterspeed = 3
        self.mode = "land"
        self.collision = self.CollisionHandler(self.pos)
        self.dir = "01"
        self.inventory = self.Inventory()

    class Inventory:
        def __init__(self):
            self.items = {
                "stick": 0,
                "rock": 0,
                "flower": 0,
                "apple": 0,
                "wooden_axe": 0,
                "wooden_pick": 0,
                "stone_axe": 0,
                "stone_pick": 0,
            }

        def add(self, name):
            self.items[name] += 1

        def take(self, name, num):
            self.items[name] -= num

    class CollisionHandler:
        def __init__(self, pos):
            self.collision_mask = {
                "obj": [],
                "tile": [],
                "drop": []
            }
            self.collision = []
            self.pos = pos
            self.rect = pygame.Rect(pos.x, pos.y, 32, 32)
            self.air_time = 0

        def update(self, dt, events):
            self.air_time += dt

        def update_player(self, pos):
            self.pos = pos
            self.rect = pygame.Rect(pos.x, pos.y, 32, 32)

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
            self.update_collision("obj")
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
            self.update_collision("obj")
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
        dirChange = False
        if events["keys"][pygame.K_d]:
            movementDirection["horizontal"] += 1
        if events["keys"][pygame.K_w]:
            movementDirection["vertical"] -= 1
        if events["keys"][pygame.K_a]:
            movementDirection["horizontal"] -= 1
        if events["keys"][pygame.K_s]:
            movementDirection["vertical"] += 1
        if movementDirection["vertical"] != 0 and movementDirection["horizontal"] != 0:
            if self.mode == "land":
                cvel.x += 0.71 * movementDirection["horizontal"] * self.speed
                cvel.y += 0.71 * movementDirection["vertical"] * self.speed
            else:
                cvel.x += 0.71 * movementDirection["horizontal"] * self.waterspeed
                cvel.y += 0.71 * movementDirection["vertical"] * self.waterspeed
        else:
            if self.mode == "land":
                cvel.x += movementDirection["horizontal"] * self.speed
                cvel.y += movementDirection["vertical"] * self.speed
            else:
                cvel.x += 0.71 * movementDirection["horizontal"] * self.waterspeed
                cvel.y += 0.71 * movementDirection["vertical"] * self.waterspeed
        dir = str(movementDirection["horizontal"]) + str(movementDirection["vertical"])
        if dir != "00":
            self.dir = dir
        if self.mode == "water":
            cvel.x -= 1
        return cvel * dt

    def update(self, dt, events):
        cvel = self.move(dt, events)
        self.collision.update(dt, events)
        cvel += self.vel
        self.rect, self.pos, facing, self.mode = self.collision.get_pos(cvel)

    def draw(self, window, camera):
        window.blit(self.sprite[self.mode][self.dir], camera.cameraPos(self.pos - self.offset))
