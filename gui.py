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
        self.ekey = image_load("assets/gui/e_key.png")
        self.nextText = self.font.render("Next up ", True, (0, 0, 0))
        self.wooden_axe = image_load("assets/objs/wooden_axe.png")
        self.wooden_pick = image_load("assets/objs/wooden_pick.png")
        self.stone_axe = image_load("assets/objs/stone_axe.png")
        self.stone_pick = image_load("assets/objs/stone_pick.png")
        self.home = image_load("assets/gui/home.png")
        self.winText = self.font.render("You  Survived  the  Thunderstorm", True, (255, 255, 255))
        self.nextItem = self.wooden_axe
        self.requirements = {
            "wooden_axe": {
                "stick": 15,
                "flower": 5,
            },
            "wooden_pick": {
                "stick": 20,
                "flower": 10,
            },
            "stone_pick": {
                "rock": 15,
                "flower": 10,
            },
            "stone_axe": {
                "rock": 30,
                "flower": 15,
            },
            "dam": {
                "stick": 100,
                "flower": 20,
                "apple": 15,
                "rock": 20,
            },
        }
        self.requirementsUI = {
            "wooden_axe": [
                [self.stick, self.getNum(15)],
                [self.flower, self.getNum(5)],
            ],
            "wooden_pick": [
                [self.stick, self.getNum(20)],
                [self.flower, self.getNum(10)],
            ],
            "stone_pick": [
                [self.rock, self.getNum(15)],
                [self.flower, self.getNum(10)],
            ],
            "stone_axe": [
                [self.rock, self.getNum(30)],
                [self.flower, self.getNum(15)],
            ],
            "dam": [
                [self.stick, self.getNum(100)],
                [self.flower, self.getNum(20)],
                [self.apple, self.getNum(15)],
                [self.rock, self.getNum(20)],
            ],
        }
        self.stage = "wooden_axe"
        self.ready = False
        self.hungerBar = image_load("assets/gui/hunger_bar.png")
        self.hungerLevel = 100
        self.hungerSize = pygame.Vector2(494, 26)
        self.hungerRect = pygame.Rect(0, 0, 494, 26)
        self.hungerSurf = pygame.Surface((494, 26))
        self.hungerSurf.set_alpha(128)
        self.hungerText = self.font.render("Hunger", True, (0, 0, 0))
        self.timer = 36000
        self.displayTime = self.font.render(str(int(self.timer // 3600)) + " " + str(int(self.timer % 3600 // 60)), True, (0, 0, 0))
        self.winScene = False
        self.winTimer = 600
        self.gameFinished = False
        self.winSurf = pygame.Surface((640, 480))
        self.winSurf.set_alpha(0)
        self.deathScene = False
        self.deathSurf = pygame.Surface((640, 480))
        self.deathText = self.font.render("", True, (0, 0, 0))
        self.deathTimer = 300

    def getNum(self, num):
        return self.font.render(str(num), True, (0, 0, 0))

    def update(self, dt, events, inventory):
        if self.winScene:
            self.winTimer -= dt
            self.winSurf.set_alpha(int(600 - self.winTimer))
            if self.winTimer < 0:
                self.gameFinished = True
        elif self.deathScene:
            self.deathTimer -= dt
            if self.deathTimer < 0:
                self.gameFinished = True
        else:
            self.stickCount = self.font.render(str(inventory.items["stick"]), True, (0, 0, 0))
            self.rockCount = self.font.render(str(inventory.items["rock"]), True, (0, 0, 0))
            self.appleCount = self.font.render(str(inventory.items["apple"]), True, (0, 0, 0))
            self.flowerCount = self.font.render(str(inventory.items["flower"]), True, (0, 0, 0))
            done = True
            for key, val in self.requirements[self.stage].items():
                if inventory.items[key] < val:
                    done = False
            if done:
                self.ready = True
            if self.ready:
                if events["keys"][pygame.K_e]:
                    self.ready = False
                    for key, val in self.requirements[self.stage].items():
                        inventory.take(key, val)
                    if self.stage == "wooden_axe":
                        self.stage = "wooden_pick"
                        self.nextItem = self.wooden_pick
                        inventory.add("wooden_axe")
                    elif self.stage == "wooden_pick":
                        self.stage = "stone_pick"
                        self.nextItem = self.stone_pick
                        inventory.add("wooden_pick")
                    elif self.stage == "stone_pick":
                        self.stage = "stone_axe"
                        self.nextItem = self.stone_axe
                        inventory.add("stone_pick")
                    elif self.stage == "stone_axe":
                        self.stage = "dam"
                        inventory.add("stone_axe")
                        self.nextItem = self.home
                    elif self.stage == "dam":
                        self.winScene = True

            if self.hungerLevel < 25:
                if inventory.items["apple"] > 0:
                    inventory.take("apple", 1)
                    self.hungerLevel = 100
            if self.hungerLevel < 1:
                self.deathScene = True
                self.deathText = self.font.render("You  Died  of  Hunger", True, (255, 255, 255))
                self.deathTextLocation = pygame.Vector2(180, 220)
            self.hungerLevel -= dt / 100
            self.hungerSize = pygame.Vector2(494 / 100 * self.hungerLevel, 26)
            self.hungerRect.width = self.hungerSize.x
            if self.timer > 0:
                self.timer -= dt
                self.displayTime = self.font.render(str(int(self.timer // 3600)) + "   " + str(int(self.timer % 3600 // 60)), True, (0, 0, 0))
            else:
                self.deathScene = True
                self.deathText = self.font.render("You  Did  Not  Survive  the  Thunderstorm", True, (255, 255, 255))
                self.deathTextLocation = pygame.Vector2(20, 220)

    def draw(self, window):
        if self.winScene:
            self.winSurf.fill((0, 0, 0))
            if self.winTimer < 600-255:
                self.winSurf.blit(self.winText, (80, 220))
            window.blit(self.winSurf, (0, 0))
        elif self.deathScene:
            self.deathSurf.fill((0, 0, 0))
            self.deathSurf.blit(self.deathText, self.deathTextLocation)
            window.blit(self.deathSurf, (0, 0))
        else:
            window.blit(self.stick, (10, 10))
            window.blit(self.stickCount, (50, 10))
            window.blit(self.rock, (10, 50))
            window.blit(self.rockCount, (50, 50))
            window.blit(self.flower, (10, 90))
            window.blit(self.flowerCount, (50, 90))
            window.blit(self.apple, (10, 130))
            window.blit(self.appleCount, (50, 130))
            if self.stage == "wooden_axe":
                pass
            elif self.stage == "wooden_pick":
                window.blit(self.wooden_axe, (10, 170))
            elif self.stage == "stone_pick":
                window.blit(self.wooden_axe, (10, 170))
                window.blit(self.wooden_pick, (10, 210))
            elif self.stage == "stone_axe":
                window.blit(self.wooden_axe, (10, 170))
                window.blit(self.wooden_pick, (10, 210))
                window.blit(self.stone_pick, (10, 250))
            elif self.stage == "dam":
                window.blit(self.wooden_axe, (10, 170))
                window.blit(self.wooden_pick, (10, 210))
                window.blit(self.stone_pick, (10, 250))
                window.blit(self.stone_axe, (10, 290))
            if self.ready:
                window.blit(self.ekey, (440, 10))
            window.blit(self.nextText, (480, 10))
            window.blit(self.nextItem, (600, 10))
            for i in range(len(self.requirementsUI[self.stage])):
                window.blit(self.requirementsUI[self.stage][i][0], (480, 50 + 40 * i))
                window.blit(self.requirementsUI[self.stage][i][1], (520, 50 + 40 * i))
            window.blit(self.hungerBar, (70, 440))
            self.hungerSurf.fill((0, 0, 0))
            pygame.draw.rect(self.hungerSurf, (128, 128, 128), self.hungerRect)
            window.blit(self.hungerSurf, (73, 443))
            window.blit(self.hungerText, (270, 410))
            window.blit(self.displayTime, (280, 10))


class MenuGUI:
    def __init__(self):
        self.menu = image_load("assets/gui/menu.png")

    def update(self):
        pass

    def draw(self, window):
        window.blit(self.menu, (0, 0))
