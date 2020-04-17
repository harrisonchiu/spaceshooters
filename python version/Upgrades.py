import pygame, random
from Load import *

class Upgrades(): #HANGAR SCENE
    def __init__(self):
        self.background = pygame.transform.scale(hangarBack, (756, 1344))
        self.image = pygame.transform.scale(player_img, (171, 150))
        self.rect = self.image.get_rect()
        self.rect.x = WIDTH/2 - self.rect.width/2
        self.rect.y = 550 - self.rect.height/2

        self.stats = pygame.transform.scale(stats_img, (640, 400))
        self.backL = pygame.transform.scale(backL, (120, 34))
        self.backD = pygame.transform.scale(backD, (120, 34))
        self.back = False

        self.dmgLvl = 1 # LASER DAMAGE
        self.dmgBought = 15
        self.dmgCost = 10
        self.dmgSelect = False
        self.damage = 50
        self.firerateLvl = 1 # FIRE RATE
        self.firerateBought = 15
        self.firerateCost = 100
        self.firerateSelect = False
        self.fireDelay = 300
        self.gunsLvl = 1 # AMOUNT OF LASER SHOOTERS
        self.gunsBought = 15
        self.gunsCost = 1000
        self.gunsSelect = False
        self.guns = 1
        self.spLvl = 1 # SKILL POINTS MULTIPLIER
        self.spBought = 15
        self.spCost = 100
        self.spSelect = False
        self.spX = 1
        self.coinLvl = 1 # COIN MULTIPLIER
        self.coinBought = 15
        self.coinCost = 100
        self.coinSelect = False
        self.coinX = 1
        self.coins = coins

        self.next = False
        self.prev = False
        self.scrolling = False

    def run(self):
        mx = pygame.mouse.get_pos()[0]
        my = pygame.mouse.get_pos()[1]

        screen.blit(self.background, (0, 0))
        screen.blit(self.image, (self.rect.x, self.rect.y))
        screen.blit(self.stats, (0, 0))
        screen.blit(self.backL, (260, 650))

        # Laser Damage
        if my <= 90:
            self.select = pygame.transform.scale(select_img, (640, 90))
            screen.blit(self.select, (0, 0))
            self.dmgSelect = True
            self.firerateSelect = False
            self.gunsSelect = False
            self.spSelect = False
            self.coinSelect = False
        # Fire Rate
        elif my > 90 and my <= 165:
            self.select = pygame.transform.scale(select_img, (640, 75))
            screen.blit(self.select, (0, 90))
            self.firerateSelect = True
            self.dmgSelect = False
            self.gunsSelect = False
            self.spSelect = False
            self.coinSelect = False
        # Laser Guns
        elif my > 165 and my <= 240:
            self.select = pygame.transform.scale(select_img, (640, 76))
            screen.blit(self.select, (0, 165))
            self.gunsSelect = True
            self.firerateSelect = False
            self.dmgSelect = False
            self.spSelect = False
            self.coinSelect = False
        # SP Rate
        elif my > 240 and my <= 318:
            self.select = pygame.transform.scale(select_img, (640, 75))
            screen.blit(self.select, (0, 242))
            self.spSelect = True
            self.gunsSelect = False
            self.firerateSelect = False
            self.dmgSelect = False
            self.coinSelect = False
        # Coin Drop
        elif my > 318 and my <= 393:
            self.select = pygame.transform.scale(select_img, (640, 75))
            screen.blit(self.select, (0, 319))
            self.coinSelect = True
            self.spSelect = False
            self.gunsSelect = False
            self.firerateSelect = False
            self.dmgSelect = False
        else:
            self.coinSelect = False
            self.spSelect = False
            self.gunsSelect = False
            self.firerateSelect = False
            self.dmgSelect = False

        # Laser Damage
        self.dmgtext = font.render(str(self.dmgLvl) + ": " + str(self.damage) + " dmg", 1, (WHITE))
        screen.blit(self.dmgtext, (143, 52))
        pygame.draw.rect(screen, (GREEN), (270, 54, self.dmgBought, 16))
        if self.dmgBought > 300:
            self.dmgBought = 15
            self.dmgLvl += 1

        # Fire Rate
        self.fireratetext = font.render(str(self.firerateLvl) + ": " + str(self.fireDelay) + " ms", 1, (WHITE))
        screen.blit(self.fireratetext, (143, 128))
        pygame.draw.rect(screen, (GREEN), (270, 130, self.firerateBought, 16))
        if self.firerateBought > 300:
            if self.firerateLvl == 3:
                self.firerateLvl = "max"
            elif self.firerateLvl != "max":
                self.firerateBought = 15
                self.firerateLvl += 1

        # Guns
        if self.guns == 1:
            self.guntext = font.render(str(self.gunsLvl) + " : " + str(self.guns) + " gun", 1, (255,255,255))
        elif self.guns > 1 and self.guns < 5:
            self.guntext = font.render(str(self.gunsLvl) + " : " + str(self.guns) + " guns", 1, (255,255,255))
        elif self.guns == 5:
            self.guntext = font.render(str(self.gunsLvl) + ": " + str(self.guns) + " guns", 1, (255,255,255))
        screen.blit(self.guntext, (135, 205))
        pygame.draw.rect(screen, (GREEN), (270, 207, self.gunsBought, 16))
        if self.gunsBought > 300:
            self.gunsLvl = "max"

        # SP Rate
        self.sptext = font.render(str(self.spLvl) + ": " + str(self.spX * 100) + "%", 1, (WHITE))
        screen.blit(self.sptext, (143, 282))
        pygame.draw.rect(screen, (GREEN), (270, 284, self.spBought, 16))
        if self.spBought > 300:
            self.spBought = 15
            self.spLvl += 1

        # Coin Drops
        self.cointext = font.render(str(self.coinLvl) + ": " + str(self.coinX * 100) + "%", 1, (WHITE))
        screen.blit(self.cointext, (143, 359))
        pygame.draw.rect(screen, (GREEN), (270, 361, self.coinBought, 16))
        if self.coinBought > 300:
            self.coinLvl = "max"

        # Purchase Info
        if self.dmgSelect:
            self.info = font.render("Increases weapon damage", 1, (255,255,255))
            self.costtext = font.render("Cost: " + str(self.dmgCost), 1, (255,255,255))
        elif self.firerateSelect and self.firerateLvl != "max":
            self.info = font.render("Increases weapon fire rate", 1, (255,255,255))
            self.costtext = font.render("Cost: " + str(self.firerateCost), 1, (255,255,255))
        elif self.gunsSelect and self.gunsLvl != "max":
            self.info = font.render("Increases amount of laser guns", 1, (255,255,255))
            self.costtext = font.render("Cost: " + str(self.gunsCost), 1, (255,255,255))
        elif self.spSelect:
            self.info = font.render("Increases the SP earned", 1, (255,255,255))
            self.costtext = font.render("Cost: " + str(self.spCost), 1, (255,255,255))
        elif self.coinSelect and self.coinLvl != "max":
            self.info = font.render("Increases the coins' worth", 1, (255,255,255))
            self.costtext = font.render("Cost: " + str(self.coinCost), 1, (255,255,255))
        else:
            self.info = font.render(" ", 1, (255,255,255)) # if not in selection collision or is max lvl, show nothing
            self.costtext = font.render(" ", 1, (255,255,255))
        self.coinstext = font.render("Coins: " + str(self.coins), 1, (WHITE))
        screen.blit(self.info, (270, 400))
        screen.blit(self.costtext, (87, 420))
        screen.blit(self.coinstext, (87, 400))

        # Back Button
        if mx >= 260 and mx <= 380 and my >= 650 and my <= 680:
            screen.blit(self.backD, (260, 650))
            self.back = True
        else:
            self.back = False
upgrades = Upgrades()

class Coin(pygame.sprite.Sprite):
    def __init__(self, center):
        super().__init__()
        self.image = pygame.transform.scale(coin_img,(30, 30))
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.radius = 15

        self.angle = 0
        self.direction = random.randint(0,1)
        self.rotateTime = 0
        self.rotateSpeed = random.randint(3, 6)

        self.speedX = random.randint(-1,1)
        self.speedY = random.randint(1,2)
        self.time = 0

    def update(self):
        self.new = pygame.transform.scale(coin_img,(30, 30))
        self.image = pygame.transform.rotate(self.new, self.angle)
        self.image.set_colorkey(BLACK)
        self.rotateTime += 1
        if self.direction == 0:
            if self.rotateTime > self.rotateSpeed:
                self.angle += 1
                self.rotateTime = 0
        if self.direction == 1:
            if self.rotateTime > self.rotateSpeed:
                self.angle -= 1
                self.rotateTime = 0

        self.time += 1
        if self.time >= 5:
            self.rect.x += self.speedX
            self.rect.y += self.speedY
            self.time = 0

        if self.rect.x >= WIDTH + self.rect.width or self.rect.x <= 0 - self.rect.width:
            self.kill()
        if self.rect.y >= HEIGHT + self.rect.height or self.rect.y <= 0 - self.rect.height:
            self.kill()

def CoinDrop(center):
    coinCenter = center
    dropAmount = random.randint(1, 5)
    coin1 = Coin(coinCenter)
    coin2 = Coin(coinCenter)
    coin3 = Coin( (coinCenter[0] + 10, coinCenter[1] - 20) )
    coin4 = Coin( (coinCenter[0], coinCenter[1] - 20) )
    coin5 = Coin( (coinCenter[0] + 25, coinCenter[1] + 25) )
    if dropAmount < 6:
        all_sprites.add(coin1)
        spawncoins.add(coin1)
        if dropAmount < 5:
            all_sprites.add(coin2)
            spawncoins.add(coin2)
            if dropAmount < 4:
                all_sprites.add(coin3)
                spawncoins.add(coin3)
                if dropAmount < 3:
                    all_sprites.add(coin4)
                    spawncoins.add(coin4)
                    if dropAmount < 2:
                        all_sprites.add(coin5)
                        spawncoins.add(coin5)
