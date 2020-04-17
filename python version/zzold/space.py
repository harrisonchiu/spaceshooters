import pygame, random, sys, math, ast
from os import path

""" INITIALIZE PYGAME """
pygame.init()

WIDTH = 640 # Window
HEIGHT = 720 # Size
screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption("Rogue Two: Guarding The Galaxy")
clock = pygame.time.Clock()
savedir = path.dirname(__file__)
img_dir = path.join(path.dirname(__file__), 'img')
snd_dir = path.join(path.dirname(__file__), 'snd')
menu_dir = path.join(path.dirname(__file__), 'menu')

""" LOAD IMAGES """
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)

# Menu
menubackground = pygame.image.load(path.join(menu_dir, "menuback.jpg")).convert()
playLight = pygame.image.load(path.join(menu_dir, "PlayLight.png")).convert_alpha()
playDark = pygame.image.load(path.join(menu_dir, "PlayDark.png")).convert_alpha()
hangarLight = pygame.image.load(path.join(menu_dir, "HangarLight.png")).convert_alpha()
hangarDark = pygame.image.load(path.join(menu_dir, "HangarDark.png")).convert_alpha()
helpLight = pygame.image.load(path.join(menu_dir, "HelpLight.png")).convert_alpha()
helpDark = pygame.image.load(path.join(menu_dir, "HelpDark.png")).convert_alpha()
backLight = pygame.image.load(path.join(menu_dir, "BackLight.png")).convert_alpha()
backDark = pygame.image.load(path.join(menu_dir, "BackDark.png")).convert_alpha()
soundLight = pygame.image.load(path.join(menu_dir, "SoundLight.png")).convert_alpha()
soundDark = pygame.image.load(path.join(menu_dir, "SoundDark.png")).convert_alpha()
muteLight = pygame.image.load(path.join(menu_dir, "MuteLight.png")).convert_alpha()
muteDark = pygame.image.load(path.join(menu_dir, "MuteDark.png")).convert_alpha()
# Hangar
hangarbackground = pygame.image.load(path.join(menu_dir, "hangarback.png")).convert()
player1 = pygame.image.load(path.join(menu_dir, "player1.png")).convert_alpha()
player2 = pygame.image.load(path.join(menu_dir, "player2.png")).convert_alpha()
player3 = pygame.image.load(path.join(menu_dir, "player3.png")).convert_alpha()
player4 = pygame.image.load(path.join(menu_dir, "player4.png")).convert_alpha()
player5 = pygame.image.load(path.join(menu_dir, "player5.png")).convert_alpha()
player6 = pygame.image.load(path.join(menu_dir, "player6.png")).convert_alpha()
player7 = pygame.image.load(path.join(menu_dir, "player7.png")).convert_alpha()
player8 = pygame.image.load(path.join(menu_dir, "player8.png")).convert_alpha()
player9 = pygame.image.load(path.join(menu_dir, "player9.png")).convert_alpha()
player10 = pygame.image.load(path.join(menu_dir, "player10.png")).convert_alpha()
stats_img = pygame.image.load(path.join(menu_dir, "stats.png")).convert_alpha()
font = pygame.font.Font(path.join(menu_dir, "future.ttf"), 18)
select_img = pygame.image.load(path.join(menu_dir, "select.png")).convert_alpha()
# Paused
pausedback = pygame.image.load(path.join(menu_dir, "pausedback.png")).convert_alpha()
menuLight = pygame.image.load(path.join(menu_dir, "MenuLight.png")).convert_alpha()
menuDark = pygame.image.load(path.join(menu_dir, "MenuDark.png")).convert_alpha()
# General Game Visuals
background = pygame.image.load(path.join(img_dir, "background2.png")).convert()
background2 = pygame.image.load(path.join(img_dir, "background2.png")).convert()
scrollingY = 0
explosion_anim = {}
explosion_anim['large'] = []
explosion_anim['small'] = []
for i in range(9):
    filename = 'regularExplosion0{}.png'.format(i)
    img = pygame.image.load(path.join(img_dir, filename)).convert()
    img.set_colorkey(BLACK)

    img_large = pygame.transform.scale(img, (75, 75)) # Large Explosion
    explosion_anim['large'].append(img_large)

    img_small = pygame.transform.scale(img, (32, 32)) # Small Explosion
    explosion_anim['small'].append(img_small)
coin_img = pygame.image.load(path.join(img_dir, "coin.png")).convert()
shield_icon = pygame.image.load(path.join(img_dir, "iconshield.png")).convert_alpha()
beam_icon = pygame.image.load(path.join(img_dir, "iconbeam.png")).convert_alpha()
time_icon = pygame.image.load(path.join(img_dir, "icontime.png")).convert_alpha()
# Player
player_img = pygame.image.load(path.join(img_dir, "player1.png")).convert()
player2_img = pygame.image.load(path.join(img_dir, "player2.png")).convert_alpha()
bullet_img = pygame.image.load(path.join(img_dir, "player1laser.png")).convert()
playerfire_img = pygame.image.load(path.join(img_dir, "player1fire.png")).convert_alpha()
shield_img = pygame.image.load(path.join(img_dir, "player1shield1.png")).convert_alpha()

# Asteroids
asteroid1_img = pygame.image.load(path.join(img_dir, "asteroid1.png")).convert()
asteroid2_img = pygame.image.load(path.join(img_dir, "asteroid2.png")).convert()
asteroid3_img = pygame.image.load(path.join(img_dir, "asteroid3.png")).convert()
asteroid4_img = pygame.image.load(path.join(img_dir, "asteroid4.png")).convert()
asteroid5_img = pygame.image.load(path.join(img_dir, "asteroid5.png")).convert()
asteroid6_img = pygame.image.load(path.join(img_dir, "asteroid6.png")).convert()
asteroid7_img = pygame.image.load(path.join(img_dir, "asteroid7.png")).convert()
asteroid8_img = pygame.image.load(path.join(img_dir, "asteroid8.png")).convert()
# Enemy1
enemy1type1_img = pygame.image.load(path.join(img_dir, "enemy1type1.png")).convert()
enemy1type23_img = pygame.image.load(path.join(img_dir, "enemy1type23.png")).convert()
enemy1laser1_img = pygame.image.load(path.join(img_dir, "enemy1laser1.png")).convert()
# Enemy2
enemy2_img = pygame.image.load(path.join(img_dir, "enemy2.png")).convert()
enemy2laser1_img = pygame.image.load(path.join(img_dir, "enemy2laser1.png")).convert()
enemy2shield_img = pygame.image.load(path.join(img_dir, "enemy2shield.png")).convert_alpha()
# Enemy3
enemy3type1_img = pygame.image.load(path.join(img_dir, "enemy3type1.png")).convert()
enemy3type2_img = pygame.image.load(path.join(img_dir, "enemy3type2.png")).convert()
enemy3type3_img = pygame.image.load(path.join(img_dir, "enemy3type3.png")).convert()
enemy3laser1_img = pygame.image.load(path.join(img_dir, "enemy3laser1.png")).convert()





""" GLOBAL VARS """
save = {}
scene = 1
coins = 0
score = 0
ship = 1
damage = 50
fireDelay = 300
guns = 1
sps = 1
drops = 1


with open(path.join(savedir, "save.txt"), 'r') as f:
    save = ast.literal_eval(f.read())
    ship = save['ship']

""" MENU AND OTHER SCENES """
### SCENE 0 == GAMEPLAY // SCENE >= 1 == MENU AND SCENES // SCENE 9000 == GAMEOVER // SCENE -100 == PAUSE ###
class Menu():
    def __init__(self):
        self.image = pygame.transform.scale(menubackground, (1440, 900))
        self.playL = pygame.transform.scale(playLight, (120, 34))
        self.playD = pygame.transform.scale(playDark, (120, 34))
        self.play = False

        self.hangarL = pygame.transform.scale(hangarLight, (120, 34))
        self.hangarD = pygame.transform.scale(hangarDark, (120, 34))
        self.hangar = False

        self.helpL = pygame.transform.scale(helpLight, (120, 34))
        self.helpD = pygame.transform.scale(helpDark, (120, 34))
        self.help = False

        self.soundL = pygame.transform.scale(soundLight, (120, 34))
        self.soundD = pygame.transform.scale(soundDark, (120, 34))
        self.muteL = pygame.transform.scale(muteLight, (120, 34))
        self.muteD = pygame.transform.scale(muteDark, (120, 34))
        self.music = False
        self.musicPlay = True
        Music()

    def run(self):
        screen.blit(self.image, (-400, 0)) # Light Images
        screen.blit(self.playL, (274, 300))
        screen.blit(self.hangarL, (274, 360))
        screen.blit(self.helpL, (274, 420))
        if self.musicPlay == True:
            screen.blit(self.soundL, (274, 480))
        if self.musicPlay == False:
            screen.blit(self.muteL, (274, 480))

        mx = pygame.mouse.get_pos()[0]
        my = pygame.mouse.get_pos()[1]
        if mx >= 274 and mx <= 394 and my >= 300 and my <= 334: # Play dark and click detection
            screen.blit(self.playD, (274, 300))
            self.play = True
        elif mx >= 274 and mx <= 394 and my >= 360 and my <= 394: # Hangar dark and click detection
            screen.blit(self.hangarD, (274, 360))
            self.hangar = True
        elif mx >= 274 and mx <= 394 and my >= 420 and my <= 454: # Help dark and click detection
            screen.blit(self.helpD, (274, 420))
            self.help = True
        elif mx >= 274 and mx <= 394 and my >= 480 and my <= 514:
            self.music = True
            if self.musicPlay == True:
                screen.blit(self.soundD, (274, 480))
            if self.musicPlay == False:
                screen.blit(self.muteD, (274, 480))
        else:
            self.play = False
            self.hangar = False
            self.help = False
            self.music = False

class Hangar():
    def __init__(self):
        self.load = 0
        self.background = pygame.transform.scale(hangarbackground, (756, 1344))
        if ship == 1:
            self.image = pygame.transform.scale(player1, (112, 75))
        if ship == 2:
            self.image = pygame.transform.scale(player2, (115, 85))
        if ship == 3:
            self.image = pygame.transform.scale(player3, (113, 107))
        if ship == 4:
            self.image = pygame.transform.scale(player4, (114, 82))
        if ship == 5:
            self.image = pygame.transform.scale(player5, (121, 91))
        if ship == 6:
            self.image = pygame.transform.scale(player6, (113, 93))
        if ship == 7:
            self.image = pygame.transform.scale(player7, (113, 178))
        if ship == 8:
            self.image = pygame.transform.scale(player8, (135, 85))
        if ship == 9:
            self.image = pygame.transform.scale(player9, (115, 98))
        if ship == 10:
            self.image = pygame.transform.scale(player10, (171, 150))
        self.rect = self.image.get_rect()
        self.rect.x = WIDTH/2 - self.rect.width/2
        self.rect.y = 550 - self.rect.height/2
        self.ship = ship

        self.stats = pygame.transform.scale(stats_img, (640, 400))
        self.backL = pygame.transform.scale(backLight, (120, 34))
        self.backD = pygame.transform.scale(backDark, (120, 34))
        self.back = False

        self.dmgLvl = 1 # LASER DAMAGE
        self.dmgBought = 15
        self.dmgCost = 10
        self.dmgSelect = False
        self.firerateLvl = 1 # FIRE RATE (HAS MAX LVL)
        self.firerateBought = 15
        self.firerateCost = 100
        self.firerateSelect = False
        self.gunsLvl = 1 # AMOUNT OF LASER SHOOTERS
        self.gunsBought = 15
        self.gunsCost = 1000
        self.gunsSelect = False
        self.spLvl = 1 # SKILL POINTS INCREASE RATE (SHIELD, POWERFUL BEAM)
        self.spBought = 15
        self.spCost = 100
        self.spSelect = False
        self.dropLvl = 1 # COIN DROP RATE
        self.dropBought = 15
        self.dropCost = 100
        self.dropSelect = False

        self.next = False
        self.prev = False
        self.transSpeed = 5
        self.scrolling = False
        self.ship = ship

    def run(self):
        mx = pygame.mouse.get_pos()[0]
        my = pygame.mouse.get_pos()[1]
        self.load += 1

        screen.blit(self.background, (0, 0)) # Background
        screen.blit(self.image, (self.rect.x, self.rect.y)) # Player Ship
        screen.blit(self.stats, (0, 0)) # Stats Board
        screen.blit(self.backL, (260, 650))

        # Laser Damage
        if my <= 90:
            self.select = pygame.transform.scale(select_img, (640, 90))
            screen.blit(self.select, (0, 0))
            self.dmgSelect = True
            self.firerateSelect = False
            self.gunsSelect = False
            self.spSelect = False
            self.dropSelect = False
        # Fire Rate
        elif my > 90 and my <= 165:
            self.select = pygame.transform.scale(select_img, (640, 75))
            screen.blit(self.select, (0, 90))
            self.firerateSelect = True
            self.dmgSelect = False
            self.gunsSelect = False
            self.spSelect = False
            self.dropSelect = False
        # Laser Guns
        elif my > 165 and my <= 240:
            self.select = pygame.transform.scale(select_img, (640, 76))
            screen.blit(self.select, (0, 165))
            self.gunsSelect = True
            self.firerateSelect = False
            self.dmgSelect = False
            self.spSelect = False
            self.dropSelect = False
        # SP Rate
        elif my > 240 and my <= 318:
            self.select = pygame.transform.scale(select_img, (640, 75))
            screen.blit(self.select, (0, 242))
            self.spSelect = True
            self.gunsSelect = False
            self.firerateSelect = False
            self.dmgSelect = False
            self.dropSelect = False
        # Coin Drop
        elif my > 318 and my <= 393:
            self.select = pygame.transform.scale(select_img, (640, 75))
            screen.blit(self.select, (0, 319))
            self.dropSelect = True
            self.spSelect = False
            self.gunsSelect = False
            self.firerateSelect = False
            self.dmgSelect = False
        else:
            self.dropSelect = False
            self.spSelect = False
            self.gunsSelect = False
            self.firerateSelect = False
            self.dmgSelect = False

        # Laser Damage
        self.dmgtext = font.render(str(self.dmgLvl) + ": " + str(damage) + " dmg", 1, (255,255,255))
        screen.blit(self.dmgtext, (143, 52))
        pygame.draw.rect(screen, (0,230,118), (270, 54, self.dmgBought, 16))
        if self.dmgBought > 300:
            self.dmgBought = 15
            self.dmgLvl += 1

        # Fire Rate
        self.fireratetext = font.render(str(self.firerateLvl) + ": " + str(fireDelay) + " ms", 1, (255,255,255))
        screen.blit(self.fireratetext, (143, 128))
        pygame.draw.rect(screen, (0,230,118), (270, 130, self.firerateBought, 16))
        if self.firerateBought > 300:
            if self.firerateLvl == 3:
                self.firerateLvl = "max"
            elif self.firerateLvl != "max":
                self.firerateBought = 15
                self.firerateLvl += 1

        # Guns
        if guns == 1:
            self.guntext = font.render(str(self.gunsLvl) + " : " + str(guns) + " gun", 1, (255,255,255))
        elif guns > 1 and guns < 5:
            self.guntext = font.render(str(self.gunsLvl) + " : " + str(guns) + " guns", 1, (255,255,255))
        elif guns == 5:
            self.guntext = font.render(str(self.gunsLvl) + ": " + str(guns) + " guns", 1, (255,255,255))
        screen.blit(self.guntext, (135, 205))
        pygame.draw.rect(screen, (0,230,118), (270, 207, self.gunsBought, 16))
        if self.gunsBought > 300:
            self.gunsLvl = "max"

        # SP Rate
        self.sptext = font.render(str(self.spLvl) + ": " + str(player.sps * 100) + "%", 1, (255,255,255))
        screen.blit(self.sptext, (143, 282))
        pygame.draw.rect(screen, (0,230,118), (270, 284, self.spBought, 16))
        if self.spBought > 300:
            self.spBought = 15
            self.spLvl += 1

        # Coin Drops
        self.droptext = font.render(str(self.dropLvl) + ": " + str(drops* 100) + "%", 1, (255,255,255))
        screen.blit(self.droptext, (143, 359))
        pygame.draw.rect(screen, (0,230,118), (270, 361, self.dropBought, 16))
        if self.dropBought > 300:
            self.dropLvl = "max"

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
        elif self.dropSelect and self.dropLvl != "max":
            self.info = font.render("Increases the coins' worth", 1, (255,255,255))
            self.costtext = font.render("Cost: " + str(self.dropCost), 1, (255,255,255))
        else:
            self.info = font.render(" ", 1, (255,255,255)) # if not in selection collision or is max lvl, show nothing
            self.costtext = font.render(" ", 1, (255,255,255))
        self.coinstext = font.render("Coins: " + str(coins), 1, (255, 255, 255))
        screen.blit(self.info, (270, 400))
        screen.blit(self.costtext, (87, 420))
        screen.blit(self.coinstext, (87, 400))

        # Back Button
        if mx >= 260 and mx <= 380 and my >= 650 and my <= 680:
            screen.blit(self.backD, (260, 650))
            self.back = True
        else:
            self.back = False

        # Ship Select
        key = pygame.key.get_pressed()
        if key[pygame.K_n] and self.ship != 10:
            self.next = True
        if self.next == True:
            self.rect.x -= self.transSpeed
            if self.rect.x < -200:
                self.ship += 1
                self.scrolling = True
                if self.ship == 1:
                    self.image = pygame.transform.scale(player1, (112, 75))
                if self.ship == 2:
                    self.image = pygame.transform.scale(player2, (115, 85))
                if self.ship == 3:
                    self.image = pygame.transform.scale(player3, (113, 107))
                if self.ship == 4:
                    self.image = pygame.transform.scale(player4, (114, 82))
                if self.ship == 5:
                    self.image = pygame.transform.scale(player5, (121, 91))
                if self.ship == 6:
                    self.image = pygame.transform.scale(player6, (113, 93))
                if self.ship == 7:
                    self.image = pygame.transform.scale(player7, (113, 178))
                if self.ship == 8:
                    self.image = pygame.transform.scale(player8, (135, 85))
                if self.ship == 9:
                    self.image = pygame.transform.scale(player9, (115, 98))
                if self.ship == 10:
                    self.image = pygame.transform.scale(player10, (171, 150))

                self.rect = self.image.get_rect()
                self.rect.y = 550 - self.rect.height/2
                self.rect.x = 840

            if self.rect.x < WIDTH/2 - self.rect.width/2 and self.scrolling == True:
                self.next = False
                self.scrolling = False
                self.rect.x = WIDTH/2 - self.rect.width/2

class Paused():
    def __init__(self):
        self.image = pygame.transform.scale(pausedback, (WIDTH, HEIGHT))
        self.isPaused = False

        self.menuL = pygame.transform.scale(menuLight, (120, 34))
        self.menuD = pygame.transform.scale(menuDark, (120, 34))
        self.menu = False

        self.soundL = pygame.transform.scale(soundLight, (120, 34))
        self.soundD = pygame.transform.scale(soundDark, (120, 34))
        self.muteL = pygame.transform.scale(muteLight, (120, 34))
        self.muteD = pygame.transform.scale(muteDark, (120, 34))
        self.music = False

        self.backL = pygame.transform.scale(backLight, (120, 34))
        self.backD = pygame.transform.scale(backDark, (120, 34))
        self.back = False

    def run(self):
        screen.blit(self.image, (0, 0))
        screen.blit(self.menuL, (274, 300))
        screen.blit(self.backL, (274, 420))
        if menu.musicPlay == True:
            screen.blit(self.soundL, (274, 360))
        if menu.musicPlay == False:
            screen.blit(self.muteL, (274, 360))

        mx = pygame.mouse.get_pos()[0]
        my = pygame.mouse.get_pos()[1]
        if mx >= 274 and mx <= 394 and my >= 300 and my <= 334: # Menu dark and click detection
            screen.blit(self.menuD, (274, 300))
            self.menu = True
            self.isPaused = False
        elif mx >= 274 and mx <= 394 and my >= 360 and my <= 394: # Music dark and click detection
            self.music = True
            if menu.musicPlay == True:
                screen.blit(self.soundD, (274, 360))
            if menu.musicPlay == False:
                screen.blit(self.muteD, (274, 360))
        elif mx >= 274 and mx <= 394 and my >= 420 and my <= 454: # Back dark and click detection
            screen.blit(self.backD, (274, 420))
            self.back = True
        else:
            self.menu = False
            self.music = False
            self.back = False


# HUD: COINS, HP, CHARGE, SP, SCORE
""" PLAYER AND OTHER MAJOR GAME MECHANICS """
# DIFFERENT PLAYER SHIPS ONLY DIFFER IN HEALTH, SPEED (TO AN EXTENT), LOOKS (INCLUDING BULLETS), AND SKILLS
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() # NAME: Endurance, Ranger (from Interstellar); K-2SO; Krestel Cruiserp # WHICH SHIP
        if hangar.ship == 1:
            self.image = pygame.transform.scale(player_img, (50, 38))
            self.speed = 2
            self.maxHp = 100
            self.maxCharge = 100
        if hangar.ship == 2:
            self.image = pygame.transform.scale(player2_img, (57, 42))
            self.speed = 2
            self.maxHp = 150
            self.maxCharge = 125
        if hangar.ship == 3:
            self.image = pygame.transform.scale(player2_img, (56, 53))
            self.speed = 2
            self.maxHp = 200
            self.maxCharge = 150
        if hangar.ship == 4:
            self.image = pygame.transform.scale(player4, (57, 41))
            self.speed = 2
            self.maxHp = 250
            self.maxCharge = 175
        if hangar.ship == 5:
            self.image = pygame.transform.scale(player5, (60, 45))
            self.speed = 3
            self.maxHp = 300
            self.maxCharge = 200
        if hangar.ship == 6:
            self.image = pygame.transform.scale(player6, (56, 46))
            self.speed = 3
            self.maxCharge = 250
        if hangar.ship == 7:
            self.image = pygame.transform.scale(player7, (56, 89))
            self.speed = 3
            self.maxHp = 400
            self.maxCharge = 275
        if hangar.ship == 8:
            self.image = pygame.transform.scale(player8, (67, 42))
            self.speed = 3
            self.maxHp = 450
            self.maxCharge = 300
        if hangar.ship == 9:
            self.image = pygame.transform.scale(player9, (57, 49))
            self.speed = 3
            self.maxHp = 500
            self.maxCharge = 350
        if hangar.ship == 10:
            self.image = pygame.transform.scale(player10, (85, 75))
            self.speed = 4
            self.maxHp = 700
            self.maxCharge = 400
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.radius = 20

        """Changeable Vars"""
        self.rect.x = WIDTH/2 - self.rect.width/2 # Spawn
        self.rect.y = HEIGHT - self.rect.height*3 # Location
        self.fireDelayTimer = 0
        self.ready = True

        """Skills Vars"""
        self.beam = False
        self.beamTime = 0
        self.time = False
        self.timeTimer = 0
        self.timeMulti = 1
        self.sp
        self.drops = drops # COIN MULTIPLIER


        self.health = self.maxHp
        self.charge = self.maxCharge

    def update(self):
        """Player Key Movement"""
        key = pygame.key.get_pressed()
        if key[pygame.K_w] and self.rect.y > 3:
            self.rect.y -= self.speed * self.timeMulti
        elif key[pygame.K_s] and self.rect.y < HEIGHT - self.rect.height - 3:
            self.rect.y += self.speed * self.timeMulti
        if key[pygame.K_d] and self.rect.x < WIDTH - self.rect.width - 3:
            self.rect.x += self.speed * self.timeMulti
        elif key[pygame.K_a] and self.rect.x > 3:
            self.rect.x -= self.speed * self.timeMulti

        """Player Shoot Action"""
        if key[pygame.K_SPACE] and fireDelayTimer >= fireDelay and self.ready == True and self.beam == False:
            self.shoot()
            self.fireDelayTimer = 0
        self.fireDelayTimer += 5 * self.timeMulti
        if self.charge <= 0: # Can't shoot if no charge
            self.charge = 0
            self.ready = False
        if self.ready == False: # Charges slowly if used all
            self.charge += 0.25
        elif self.fireDelayTimer >= fired * 3: # Charges if not shooting
            self.charge += 0.6
        if self.charge >= self.maxCharge: # If fully charged, can shoot
            self.charge = self.maxCharge
            self.ready = True

        """Player SP Beam"""
        if key[pygame.K_1] and self.sp >= 100:
            self.sp = 0
            self.beam = True
        if self.beam == True:
            self.beamTime += 1
            if self.beamTime >= 700:
                self.beam = False
                self.beamTime = 0
        if key[pygame.K_SPACE] and self.beam == True: # Regular shoot button but beam
            self.shoot()

        """Player SP Shield"""
        if key[pygame.K_2] and sp>= 100:
            sp= 0
            shield = Shield()
            all_sprites.add(shield)
            shields.add(shield)

        if key[pygame.K_3]:
            self.time = True
        if self.time == True:
            self.timeMulti = 3
            self.timeTimer += 1
            if self.timeTimer >= 300:
                self.time = False
                self.timeTimer = 0
                self.timeMulti = 1

    def shoot(self):
        """Shoot"""
        if guns == 1:
            bullet1 = Bullet(self.rect.x + self.rect.width/2 - 4, self.rect.y - self.rect.height/2 - 50) # MIDDLE
            all_sprites.add(bullet1)
            bullets.add(bullet1)
        if guns == 2:
            bullet1 = Bullet(self.rect.x + self.rect.width/4 - 5, self.rect.y - self.rect.height/4 - 50) # LEFT
            bullet2 = Bullet(self.rect.x + self.rect.width - self.rect.width/4 - 1, self.rect.y - self.rect.height/4 - 50) # RIGHT
            all_sprites.add(bullet1)
            bullets.add(bullet1)
            all_sprites.add(bullet2)
            bullets.add(bullet2)
        if guns == 3:
            bullet1 = Bullet(self.rect.x - 6, self.rect.y - 50) # FAR LEFT
            bullet2 = Bullet(self.rect.x + self.rect.width/2 - 4, self.rect.y - self.rect.height/2 - 50) # MIDDLE
            bullet3 = Bullet(self.rect.x + self.rect.width, self.rect.y - 50) # FAR RIGHT
            all_sprites.add(bullet1)
            bullets.add(bullet1)
            all_sprites.add(bullet2)
            bullets.add(bullet2)
            all_sprites.add(bullet3)
            bullets.add(bullet3)
        if guns == 4:
            bullet1 = Bullet(self.rect.x - 6, self.rect.y - 50) # FAR LEFT
            bullet2 = Bullet(self.rect.x + self.rect.width/4 - 5, self.rect.y - self.rect.height/4 - 50) # LEFT
            bullet3 = Bullet(self.rect.x + self.rect.width - self.rect.width/4 - 1, self.rect.y - self.rect.height/4 - 50) # RIGHT
            bullet4 = Bullet(self.rect.x + self.rect.width, self.rect.y - 50) # FAR RIGHT
            all_sprites.add(bullet1)
            bullets.add(bullet1)
            all_sprites.add(bullet2)
            bullets.add(bullet2)
            all_sprites.add(bullet3)
            bullets.add(bullet3)
            all_sprites.add(bullet4)
            bullets.add(bullet4)
        if guns == 5:
            bullet1 = Bullet(self.rect.x - 6, self.rect.y - 50) # FAR LEFT
            bullet2 = Bullet(self.rect.x + self.rect.width/4 - 5, self.rect.y - self.rect.height/4 - 50) # LEFT
            bullet3 = Bullet(self.rect.x + self.rect.width/2 - 4, self.rect.y - self.rect.height/2 - 50) # MIDDLE
            bullet4 = Bullet(self.rect.x + self.rect.width - self.rect.width/4 - 1, self.rect.y - self.rect.height/4 - 50) # RIGHT
            bullet5 = Bullet(self.rect.x + self.rect.width, self.rect.y - 50) # FAR RIGHT
            all_sprites.add(bullet1)
            bullets.add(bullet1)
            all_sprites.add(bullet2)
            bullets.add(bullet2)
            all_sprites.add(bullet3)
            bullets.add(bullet3)
            all_sprites.add(bullet4)
            bullets.add(bullet4)
            all_sprites.add(bullet5)
            bullets.add(bullet5)
        # Shooting uses charge
        if self.beam == False:
            if hangar.firerateLvl == 1:
                self.charge -= 15
            if hangar.firerateLvl == 2:
                self.charge -= 10
            if hangar.firerateLvl == 3:
                self.charge -= 8
            if hangar.firerateLvl == "max":
                self.charge -= 5
        # Plays a sound
        playerlaser_snd.play()
        playerlaser_snd.set_volume(0.3)
        # Show gun fire
        fire = BulletFire()
        all_sprites.add(fire)

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.transform.scale(bullet_img, (7, 30)) # Image
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        """Changeable Vars"""
        self.speed = 15

    def update(self):
        """Movement"""
        self.rect.y -= self.speed
        if self.rect.y < 0: # Remove from game if out of game
            self.kill()

class BulletFire(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.transform.scale(playerfire_img, (10, 18)) # Image
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = player.rect.center[0] - 5
        self.rect.y = player.rect.y - 18
        self.time = 0

    def update(self):
        self.rect.x = player.rect.center[0] - 5
        self.rect.y = player.rect.y - 18
        if self.time > 10:
            self.kill()
        self.time += 1

class Shield(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.transform.scale(shield_img, (135, 135))
        self.rect = self.image.get_rect()
        self.rect.x = player.rect.center[0] - self.rect.width/2
        self.rect.y = player.rect.center[1] - self.rect.height/2
        self.radius = 50

        self.energy = 100

    def update(self):
        self.rect.x = player.rect.center[0] - self.rect.width/2
        self.rect.y = player.rect.center[1] - self.rect.height/2
        self.energy -= 1
        if self.energy <= 0:
            self.kill()


""" GAME MECHANICS """
class Explosion(pygame.sprite.Sprite):
    def __init__(self, center, size):
        super().__init__()
        self.size = size
        self.image = explosion_anim[self.size][0]
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.frame = 0
        self.lastUpdate = pygame.time.get_ticks()
        self.frameRate = 50 # Bigger this number, longer the animation

        """5 Different Explosion Sounds"""
        self.randsnd = random.randint(1,5) # Produce random sound for each type of explosion
        if self.randsnd == 1:
           explosion1_snd.play()
           explosion1_snd.set_volume(0.2)
        if self.randsnd == 2:
           explosion2_snd.play()
           explosion2_snd.set_volume(0.2)
        if self.randsnd == 3:
           explosion3_snd.play()
           explosion3_snd.set_volume(0.2)
        if self.randsnd == 4:
           explosion4_snd.play()
           explosion4_snd.set_volume(0.1)
        if self.randsnd == 5:
           explosion5_snd.play()
           explosion5_snd.set_volume(0.1)

    def update(self):
        """Explosion Picture Change"""
        now = pygame.time.get_ticks()
        if now - self.lastUpdate > self.frameRate:
            self.lastUpdate = now
            self.frame += 1
            if self.frame == len(explosion_anim[self.size]):
                self.kill()
            else:
                center = self.rect.center
                self.image = explosion_anim[self.size][self.frame]
                self.rect = self.image.get_rect()
                self.rect.center = center

class Coin(pygame.sprite.Sprite):
    def __init__(self, center):
        super().__init__()
        self.image = pygame.transform.scale(coin_img,(30, 30))
        self.image.set_colorkey(BLACK)
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
def CoinDrop(hit):
    dropAmount = random.randint(1, 5)
    coin1 = Coin(hit.rect.center)
    coin2 = Coin(hit.rect.center)
    coin3 = Coin( (hit.rect.center[0] + 10, hit.rect.center[1] - 20) )
    coin4 = Coin( (hit.rect.center[0], hit.rect.center[1] - 20) )
    coin5 = Coin( (hit.rect.center[0] + 25, hit.rect.center[1] + 25) )
    if dropAmount == 1:
        all_sprites.add(coin1)
        spawncoins.add(coin1)
    if dropAmount == 2:
        all_sprites.add(coin1)
        spawncoins.add(coin1)
        all_sprites.add(coin2)
        spawncoins.add(coin2)
    if dropAmount == 3:
        all_sprites.add(coin1)
        spawncoins.add(coin1)
        all_sprites.add(coin2)
        spawncoins.add(coin2)
        all_sprites.add(coin3)
        spawncoins.add(coin3)
    if dropAmount == 4:
        all_sprites.add(coin1)
        spawncoins.add(coin1)
        all_sprites.add(coin2)
        spawncoins.add(coin2)
        all_sprites.add(coin3)
        spawncoins.add(coin3)
        all_sprites.add(coin4)
        spawncoins.add(coin4)
    if dropAmount == 5:
        all_sprites.add(coin1)
        spawncoins.add(coin1)
        all_sprites.add(coin2)
        spawncoins.add(coin2)
        all_sprites.add(coin3)
        spawncoins.add(coin3)
        all_sprites.add(coin4)
        spawncoins.add(coin4)
        all_sprites.add(coin5)
        spawncoins.add(coin5)
def Hud():
    HP_LENGTH = 100
    HP_HEIGHT = 20
    hp = int(max( min(player.health/player.maxHp * HP_LENGTH, HP_LENGTH), 0 ))
    pygame.draw.rect( screen, RED, (55, 690, hp, HP_HEIGHT) )
    pygame.draw.rect( screen, WHITE, (55, 690, HP_LENGTH, HP_HEIGHT), 3 )
    hpText = font.render("HP:", 1, (WHITE))
    screen.blit(hpText, (20, 690))

    CHARGE_LENGTH = 100
    CHARGE_HEIGHT = 20
    ch = int(max( min(player.charge/player.maxCharge * HP_LENGTH, HP_LENGTH), 0 ))
    pygame.draw.rect( screen, (0, 255, 255), (285, 690, ch, CHARGE_HEIGHT) )
    pygame.draw.rect( screen, WHITE, (285, 690, CHARGE_LENGTH, CHARGE_HEIGHT), 3 )
    chText = font.render("Charge:", 1, (WHITE))
    screen.blit(chText, (195, 690))

    SP_LENGTH = 100
    SP_HEIGHT = 20
    spAmount = player.sp
    if sp > 100:
        sp = 100
    pygame.draw.rect( screen, GREEN, (515, 690, sp, SP_HEIGHT) )
    pygame.draw.rect( screen, WHITE, (515, 690, SP_LENGTH, SP_HEIGHT), 3 )
    spText = font.render("SP:", 1, (WHITE))
    screen.blit(spText, (480, 690))

    # Skills available
    shieldico = pygame.transform.scale(shield_icon, (30, 29))
    beamico = pygame.transform.scale(beam_icon, (30, 29))
    timeico = pygame.transform.scale(time_icon, (30, 29))
    if hangar.ship >= 1:
        screen.blit(shieldico, (600, 640))
    if hangar.ship >= 4:
        screen.blit(beamico, (600, 605))
    if hangar.ship >= 7:
        screen.blit(timeico, (600, 570))



""" ASTEROID """
class Asteroid(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        """6 Types of Asteroids"""
        self.type = random.randint(1,8)
        if self.type == 1:
            self.image = pygame.transform.scale(asteroid1_img, (45, 41))
        if self.type == 2:
            self.image = pygame.transform.scale(asteroid2_img, (45, 41))
        if self.type == 3:
            self.image = pygame.transform.scale(asteroid3_img, (45, 41))
        if self.type == 4:
            self.image = pygame.transform.scale(asteroid4_img, (45, 41))
        if self.type == 5:
            self.image = pygame.transform.scale(asteroid5_img, (45, 41))
        if self.type == 6:
            self.image = pygame.transform.scale(asteroid6_img, (45, 41))
        if self.type == 7:
            self.image = pygame.transform.scale(asteroid7_img, (45, 41))
        if self.type == 8:
            self.image = pygame.transform.scale(asteroid8_img, (45, 41))
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.radius = 19

        # Random Spawn, Speed, Health
        self.rect.x = random.randint(2, WIDTH - self.rect.width - 2)
        self.rect.y = random.randint(-1000, -5)
        self.speedy = random.randint(5, 10)
        self.speedx = random.randint(-3, 3)
        self.health = 100

    def update(self):
        """Movement"""
        self.rect.y += self.speedy
        self.rect.x += self.speedx

        """Respawn"""
        if self.rect.x >= WIDTH or self.rect.x <= 0 or self.rect.y >= HEIGHT or self.rect.y <= 0 or self.health <= 0:
            self.type = random.randint(1,8)
            if self.type == 1:
                self.image = pygame.transform.scale(asteroid1_img, (45, 41))
            if self.type == 2:
                self.image = pygame.transform.scale(asteroid2_img, (45, 41))
            if self.type == 3:
                self.image = pygame.transform.scale(asteroid3_img, (45, 41))
            if self.type == 4:
                self.image = pygame.transform.scale(asteroid4_img, (45, 41))
            if self.type == 5:
                self.image = pygame.transform.scale(asteroid5_img, (45, 41))
            if self.type == 6:
                self.image = pygame.transform.scale(asteroid6_img, (45, 41))
            if self.type == 7:
                self.image = pygame.transform.scale(asteroid7_img, (45, 41))
            if self.type == 8:
                self.image = pygame.transform.scale(asteroid8_img, (45, 41))
            self.image.set_colorkey(BLACK)
            self.rect = self.image.get_rect()

            # Randomize Location and Speed Again
            self.rect.x = random.randint(2, WIDTH - self.rect.width - 2)
            self.rect.y = random.randint(-1000, -5)
            self.speedy = random.randint(5, 10)
            self.speedx = random.randint(-3, 3)
            self.health = 100


""" SPACE AC130 """
class Enemy1(pygame.sprite.Sprite):
    def __init__(self, type):
        super().__init__()
        self.type = type
        """Each Type is Slightly Different"""
        if self.type == 1: # TYPE 1 -- TOP
           self.image = pygame.transform.scale(enemy1type1_img, (60, 55)) # Default Enemy1
           self.rect = self.image.get_rect()
           self.angle = 0
           self.rect.x = 0
        if self.type == 2: # TYPE 2 -- LEFT
           self.image = pygame.transform.scale(enemy1type23_img, (68, 55)) # Different starting angle
           self.image = pygame.transform.rotate(self.image, 180)
           self.rect = self.image.get_rect()
           self.angle = 90
           self.rect.x = 0
        if self.type == 3: # TYPE 3 -- RIGHT
           self.image = pygame.transform.scale(enemy1type23_img, (68, 55)) # Different starting angle and location
           self.image = pygame.transform.rotate(self.image, 180)
           self.rect = self.image.get_rect()
           self.angle = 270
           self.rect.x = 640
        self.image.set_colorkey(BLACK)
        self.rect.y = 0

        """Changeable Vars"""
        self.speed = 1 # Lowest integer speed
        self.health = 100
        self.timer = 0 # Timer tells when to turn ship

    def update(self):
        """Type 1 Movement"""
        if self.type == 1:
            # Rotate Ship
            self.timer += 1
            if self.timer >= 5: # Angle changes every so often
                self.angle += 1
                self.timer = 0
            self.smaller = pygame.transform.scale(enemy1type1_img, (60, 55))
            self.image = pygame.transform.rotate(self.smaller, self.angle)
            self.image.set_colorkey(BLACK)

            # Movement Path
            self.rect.x += self.speed # Function equation solved for 'Y' based on X location
            self.rect.y = math.sqrt(self.rect.x * (-self.rect.x + WIDTH * 1.15)) - 100

            # Shoots 3 times
            if self.rect.x == WIDTH/4 or self.rect.x == WIDTH/2 or self.rect.x == WIDTH - WIDTH/4:
               self.shoot() # Shoots once at 3 locations
            if self.rect.x > WIDTH:
               self.kill() # Removes itself from game

        """Type 2 Movement"""
        if self.type == 2:
           # Rotate ship
           self.timer += 1
           if self.timer >= 5:
              self.angle += 1
              self.timer = 0
           self.smaller = pygame.transform.scale(enemy1type23_img, (68, 55))
           self.image = pygame.transform.rotate(self.smaller, self.angle)
           self.image.set_colorkey(BLACK)

           # Movement Path
           self.rect.x += self.speed # Function equation solved for 'Y' based on X location
           self.rect.y = math.sqrt(-(self.rect.x + 400) ** 2 + 600000) - 100

           # Shoots 3 times
           if self.rect.y == HEIGHT/2 or self.rect.y == HEIGHT/4 or self.rect.y == HEIGHT * 2/3:
              self.shoot()
           if self.rect.y < 0 - self.rect.height: # Removes itself from game
              self.kill()

        """Type 3 Movement"""
        if self.type == 3:
           # Rotate Ship
           self.timer += 1
           if self.timer >= 5:
              self.angle -= 1
              self.timer = 0
           self.smaller = pygame.transform.scale(enemy1type1_img, (68, 55))
           self.image = pygame.transform.rotate(self.smaller, self.angle)
           self.image.set_colorkey(BLACK)

           # Movement Path
           self.rect.x -= self.speed # Function equation solved for 'Y' based on X location
           self.rect.y = math.sqrt(-(self.rect.x - 1000) ** 2 + 600000) - 100

           # Shoots 3 times
           if self.rect.y == HEIGHT/2 or self.rect.y == HEIGHT/4 or self.rect.y == HEIGHT * 2/3:
              self.shoot()
           if self.rect.y < 0 - self.rect.height: # Removes itself from game
              self.kill()

        """Destroyed"""
        if self.health <= 0: # Removes itself from game if destroyed
           self.kill()

    def shoot(self):
        """Shoot"""
        enemy1bullet = Enemy1Bullet(self.rect.x + self.rect.width/2, self.rect.y + self.rect.height) # Shoot location
        all_sprites.add(enemy1bullet)
        enemy1bullets.add(enemy1bullet)

class Enemy1Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.transform.scale(enemy1laser1_img, (25, 24))
        self.rect = self.image.get_rect()
        self.image.set_colorkey(BLACK)
        self.rect.x = x
        self.rect.y = y

        self.dx = player.rect.x - self.rect.x # X-Distance
        self.dy = player.rect.y - self.rect.y # Y-Distance
        self.dist = math.sqrt(self.dx ** 2 + self.dy ** 2) # Total Distance between Enemy1 and Player
        self.dx = (self.dx / self.dist) * 15 # This controls
        self.dy = (self.dy / self.dist) * 15 # the speed of bullet

    def update(self):
        # Moving
        self.rect.x += self.dx
        self.rect.y += self.dy

        # Remove from game if out of game
        if self.rect.x >= WIDTH or self.rect.x <= 0 or self.rect.y >= HEIGHT or self.rect.y <= 0:
            self.kill()


""" TANK """
class Enemy2(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.transform.scale(enemy2_img, (82, 84))
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()

        """Changeable Vars"""
        self.rect.x = WIDTH/2
        self.rect.y = -200
        self.speed = 1
        self.health = 1000
        self.charge = 0
        self.fullCharge = 300

        self.shield() # Activates Shield

    def update(self):
        """Follow Player Horizontally"""
        if self.rect.x + 41 < player.rect.x + 25: # If left to the player move right
            self.speed = 1
        elif self.rect.x + 41 > player.rect.x + 25: # If right to the player move left
            self.speed = -1
        elif self.rect.x + 41 == player.rect.x + 25: # Otherwise stay
            self.speed = 0
            if self.charge >= self.fullCharge: # If charge is ready and is in range of player --> shoot
                self.shoot()
                self.charge = 0
        self.charge += 1 # Constantly charging
        self.rect.x += self.speed # and ready to move

        """Stops Moving Vertically After a Point"""
        if self.rect.y < 100: # Acts as a bullet wall for other enemies
            self.rect.y += 1

        """Destroyed"""
        if self.health <= 0: # Remove itself from the game
            self.kill()

    def shoot(self):
        """Shoot Right Side Bullet"""
        enemy2bullet1 = Enemy2Bullet(self.rect.x + self.rect.width/3 - 11, self.rect.y + self.rect.height - 30)
        all_sprites.add(enemy2bullet1)
        enemy2bullets.add(enemy2bullet1)

        """Shoot Left Side Bullet"""
        enemy2bullet2 = Enemy2Bullet(self.rect.x + self.rect.width*2/3, self.rect.y + self.rect.height - 30)
        all_sprites.add(enemy2bullet2)
        enemy2bullets.add(enemy2bullet2)

    def shield(self):
        """Physical Shield Against Player"""
        enemy2shield = Enemy2Shield() # Prevents player from going to the sides to avoid the ship's attacks
        all_sprites.add(enemy2shield)
        enemy2shields.add(enemy2shield)

class Enemy2Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.transform.scale(enemy2laser1_img, (13, 57))
        self.rect = self.image.get_rect()
        self.image.set_colorkey(BLACK)
        self.rect.x = x
        self.rect.y = y

        """Changeable Vars"""
        self.speed = 4

    def update(self):
        """Movement"""
        self.rect.y += self.speed

        """Remove from game"""
        if self.rect.x >= WIDTH or self.rect.x <= 0 or self.rect.y >= HEIGHT or self.rect.y <= 0:
            self.kill()

class Enemy2Shield(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.transform.scale(enemy2shield_img, (640, 50))
        self.rect = self.image.get_rect()
        self.image.set_colorkey(BLACK)

    def update(self):
        self.rect.y = enemy2.rect.y + enemy2.rect.height # Always infront of Enemy2

        """Check for Collision"""
        self.hit = pygame.sprite.spritecollide(player, enemy2shields, False)

        if self.hit: # The forcefield moves the player back
           player.rect.y += 10
           self.randsnd = random.randint(1,3) # Random sound
           # Checks if Channel2 is not playing (Don't want sound effect player over each other)
           if channel2.get_busy() != 1:
              if self.randsnd == 1:
                 channel2.play(enemy2shield1_snd) # Plays random sound
              if self.randsnd == 2:
                 channel2.play(enemy2shield2_snd)
              if self.randsnd == 3:
                 channel2.play(enemy2shield3_snd)

        if enemy2.health <= 0: # Destroys shield if source is gone
            self.kill()


""" STANDARD ATTACKER """
class Enemy3(pygame.sprite.Sprite):
    def __init__(self, x, y, type):
        super().__init__()
        self.type = type
        if self.type == 1: # Straight Down Shooting Straight
            self.image = pygame.transform.scale(enemy3type1_img, (51, 42))
            self.chargeRate = 1 # Standard charging rate
            self.chargeCost = 120 # How much each shot cost in energy (This creates delay between each shot)
            self.chargeReady = True
        if self.type == 2: # Top Sniping Then Zoom Away
            self.image = pygame.transform.scale(enemy3type2_img, (51, 42))
            self.timer = 0
            self.timerlimit = 1000
        if self.type == 3: # Side Sniping Moving Straight Down
            self.image = pygame.transform.scale(enemy3type3_img, (51, 42))
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.charge = 500 # Max charge
        self.speed = 1
        self.health = 100


    def update(self):
        """STRAIGHT DOWN SHOOTING STRAIGHT"""
        if self.type == 1:
            self.rect.y += self.speed # Always moving
            self.charge += self.chargeRate # Always charging

            if self.rect.y > 0: # Only shoot if passed a point
               self.shoot()
            if self.charge > 500: # Max amount of charge --> Ready to shoot and not charging
                self.chargeRate = 0
                self.charge = 500
                self.chargeReady = True
            elif self.charge < 500 and self.charge > 0 and self.chargeReady == True:
                self.chargeRate = 1 # Charges slowly when shooting
            if self.charge <= 0: # If no more charge --> Not ready to shoot and faster charge rate
                self.chargeReady = False
                self.chargeRate = 3

        """TOP SNIPING THEN ZOOM AWAY"""
        if self.type == 2:
            self.rect.y += self.speed
            self.timer += 1
            self.charge -= 2 # Time till it shoots
            if self.rect.y > 50 and self.timer < self.timerlimit: # Stops at a point if not time to go away
                self.speed = 0
            if self.charge <= 0: # Shoot
                self.shoot()
                self.charge = 500
            if self.timer > self.timerlimit: # Accelerates away
                self.speed += 0.2

        """SIDE SNIPING MOVING STRAIGHT DOWN"""
        if self.type == 3:
            self.rect.y += self.speed
            self.charge -= 3
            if self.charge <= 0:
                self.shoot()
                self.charge = 500

        """REMOVE FROM GAME"""
        if self.health <= 0 or self.rect.x >= WIDTH or self.rect.x <= 0 or self.rect.y >= HEIGHT or self.rect.y <= 0:
            self.kill()

    def shoot(self):
        """TYPE 1 BURST SHOT"""
        if self.type == 1:
            if self.charge % 100 == 0 and self.chargeReady == True:
                self.charge -= self.chargeCost
                enemy3bullet = Enemy3Bullet(self.rect.center[0] - 10, self.rect.center[1], 1) # Shoot location
                all_sprites.add(enemy3bullet)
                enemy3bullets.add(enemy3bullet)

        """TYPE 2 & 3 AT LAST PLAYER LOCATION"""
        if self.type == 2 or self.type == 3:
            enemy3bullet = Enemy3Bullet(self.rect.center[0] - 10, self.rect.center[1], 2) # Shoot location
            all_sprites.add(enemy3bullet)
            enemy3bullets.add(enemy3bullet)

class Enemy3Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, type):
        super().__init__()
        self.image = pygame.transform.scale(enemy3laser1_img, (20, 20))
        self.rect = self.image.get_rect()
        self.image.set_colorkey(BLACK)
        self.rect.x = x
        self.rect.y = y
        self.type = type

        self.speed = 4
        self.dx = player.rect.center[0] - self.rect.center[0] + 50 # X-Distance
        self.dy = player.rect.center[1] - self.rect.center[1] # Y-Distance
        self.dist = math.sqrt(self.dx ** 2 + self.dy ** 2) # Total Distance between Enemy1 and Player
        self.dx = (self.dx / self.dist) * 5 # This controls
        self.dy = (self.dy / self.dist) * 5 # the speed of bullet

    def update(self):
        """Movement"""
        if self.type == 1: # Type 1 only moves in a straight path at constant speed
            self.rect.y += self.speed
        if self.type == 2 or self.type == 3: # Type 2 and 3 goes to player's last location
            self.rect.x += self.dx
            self.rect.y += self.dy

        """Remove from game"""
        if self.rect.x >= WIDTH or self.rect.x <= 0 or self.rect.y >= HEIGHT or self.rect.y <= 0:
            self.kill()


""" SPRITE LISTS """
all_sprites = pygame.sprite.Group()
spawncoins = pygame.sprite.Group()
bullets = pygame.sprite.Group()
shields = pygame.sprite.Group()
asteroids = pygame.sprite.Group()
enemies1 = pygame.sprite.Group()
enemy1bullets = pygame.sprite.Group()
enemies2 = pygame.sprite.Group()
enemy2bullets = pygame.sprite.Group()
enemy2shields = pygame.sprite.Group()
enemies3 = pygame.sprite.Group()
enemy3bullets = pygame.sprite.Group()

menu = Menu()
hangar = Hangar()
paused = Paused()
player = Player()
shield = Shield()
asteroid = Asteroid()
enemy1Type1 = Enemy1(1)
enemy1Type2 = Enemy1(2)
enemy1Type3 = Enemy1(3)
enemy2 = Enemy2()
enemy3Type1 = Enemy3(WIDTH/2, -10, 1) # X, Y, Type
enemy3Type2 = Enemy3(WIDTH/2, -10, 2)
enemy3Type3 = Enemy3(WIDTH/2, -10, 3)

""" ADD SPRITES (WAVES & LEVELS) """
# ASTEROID
"""all_sprites.add(asteroid)
asteroids.add(asteroid)"""
# ENEMY1 -- TYPE ALL
"""all_sprites.add(enemy1Type1)
enemies1.add(enemy1Type1)"""
"""all_sprites.add(enemy1Type2)
enemies1.add(enemy1Type2)"""
"""all_sprites.add(enemy1Type3)
enemies1.add(enemy1Type3)"""
# ENEMY2
"""all_sprites.add(enemy2)
enemies2.add(enemy2)"""
# ENEMY3
"""all_sprites.add(enemy3Type3)
enemies3.add(enemy3Type3)"""


""" LOADING DATA """
#save = {}
with open(path.join(savedir, "save.txt"), 'r') as f:
    save = ast.literal_eval(f.read())
    score = save['score']
    coins = save['coins']

    hangar.dmgLvl = save['dmgLvl']
    hangar.dmgBought = save['dmgBought']
    hangar.dmgCost = save['dmgCost']
    damage = save['damage']

    hangar.firerateLvl = save['firerateLvl']
    hangar.firerateBought = save['firerateBought']
    hangar.firerateCost = save['firerateCost']
    fireDelay = save['fireDelay']

    hangar.gunsLvl = save['gunsLvl']
    hangar.gunsBought = save['gunsBought']
    hangar.gunsCost = save['gunsCost']
    guns = save['guns']

    hangar.spLvl = save['spLvl']
    hangar.spBought = save['spBought']
    hangar.spCost = save['spCost']
    sps = save['sp']

    hangar.dropLvl = save['dropLvl']
    hangar.dropBought = save['dropBought']
    hangar.dropCost = save['dropCost']
    drops = save['drops']

""" SAVING DATA """
def Save():
    save['score'] = score
    save['coins'] = coins
    save['ship'] = hangar.ship

    save['dmgLvl'] = hangar.dmgLvl
    save['dmgBought'] = hangar.dmgBought
    save['dmgCost'] = hangar.dmgCost
    save['damage'] = damage

    save['firerateLvl'] = hangar.firerateLvl
    save['firerateBought'] = hangar.firerateBought
    save['firerateCost'] = hangar.firerateCost
    save['fireDelay'] = fireDelay

    save['gunsLvl'] = hangar.gunsLvl
    save['gunsBought'] = hangar.gunsBought
    save['gunsCost'] = hangar.gunsCost
    save['guns'] = guns

    save['spLvl'] = hangar.spLvl
    save['spBought'] = hangar.spBought
    save['spCost'] = hangar.spCost
    save['sp'] = sps

    save['dropLvl'] = hangar.dropLvl
    save['dropBought'] = hangar.dropBought
    save['dropCost'] = hangar.dropCost
    save['drops'] = drops

    with open(path.join(savedir, "save.txt"), 'w') as f:
        f.write(str(save))


""" MAIN GAME """
running = True
while running:
    print(hangar.ship)
    player.sp += 5
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Save()
            running = False
        if scene == 1 and event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            if menu.play == True:
                scene = 0
                menu.play = False
                player = Player()
                all_sprites.add(player)
            if menu.hangar == True:
                scene = 2
                menu.hangar = False
            if menu.help == True:
                scene = 3
                menu.help = False
            if menu.music == True:
                if menu.musicPlay == True:
                    menu.musicPlay = False
                elif menu.musicPlay == False:
                    menu.musicPlay = True
        if scene == 2 and event.type == pygame.MOUSEBUTTONUP and event.button == 1 and hangar.load > 75:
            if coins >= hangar.dmgCost and hangar.dmgSelect == True:
                coins -= hangar.dmgCost
                hangar.dmgBought += 15
                hangar.dmgCost += 100
                damage += 1
            if coins >= hangar.firerateCost and hangar.firerateSelect == True and hangar.firerateLvl != "max":
                coins -= hangar.firerateCost
                hangar.firerateBought += 15
                hangar.firerateCost += 100
                fireDelay -= 4
            if coins >= hangar.gunsCost and hangar.gunsSelect == True and hangar.gunsLvl != "max":
                coins -= hangar.gunsCost
                hangar.gunsBought += 75
                hangar.gunsCost += 100
                guns += 1
            if coins >= hangar.spCost and hangar.spSelect == True:
                coins -= hangar.spCost
                hangar.spBought += 15
                hangar.spCost += 100
                player.sps += 0.25
            if coins >= hangar.dropCost and hangar.dropSelect == True and hangar.dropLvl != "max":
                coins -= hangar.dropCost
                hangar.dropBought += 30
                hangar.dropCost += 100
                drops+= 1
            if hangar.back == True:
                scene = 1
                hangar.back = False
                hangar.load = 0
        if scene == -100 and event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            if paused.menu == True:
                scene = 1
                paused.menu = False
                for sprite in all_sprites:
                    sprite.kill()
            if paused.music == True:
                if menu.musicPlay == True:
                    menu.musicPlay = False
                elif menu.musicPlay == False:
                    menu.musicPlay = True
            if paused.back == True:
                scene = 0
                paused.isPaused = False

    if menu.musicPlay == True:
        pygame.mixer.music.unpause()
    if menu.musicPlay == False:
        pygame.mixer.music.pause()

    if scene == 1:
        menu.run()

    if scene == 2:
        hangar.run()

    if scene == 0:
        """GLOBAL GAME CONTROLS"""
        # Pause Game
        key = pygame.key.get_pressed()
        if key[pygame.K_ESCAPE]:
            paused.isPaused = True
            scene = -100
            pygame.mixer.music.pause()
        # If Not Paused, Update all Sprites
        if paused.isPaused == False:
            all_sprites.update()


        """COIN COLLISIONS"""
        hits = pygame.sprite.spritecollide(player, spawncoins, True, pygame.sprite.collide_circle)
        if hits:
            coin_snd.set_volume(0.2)
            coin_snd.play()
            coins += 2 * drops# coin worth x player coin multiplier


        """ASTEROID COLLISIONS"""
        # P1 bullet hits asteroid
        hits = pygame.sprite.groupcollide(asteroids, bullets, False, True)
        for hit in hits:
            hit.health -= damage * len(hits[hit])
            if hit.health <= 0:
                expl = Explosion(hit.rect.center, 'large')
                all_sprites.add(expl)
                CoinDrop()
        # P1 hits asteroid
        hits = pygame.sprite.spritecollide(player, asteroids, True, pygame.sprite.collide_circle)
        for hit in hits:
            hit.health = 0
            #scene = 9000
            expl = Explosion(hit.rect.center, 'small')
            all_sprites.add(expl)
        # Asteroid hits P1 Shield
        hits = pygame.sprite.groupcollide(shields, asteroids, False, True, pygame.sprite.collide_circle)
        for hit in hits:
            enemy2shield2_snd.play()


        """ENEMY1 COLLISIONS"""
        # P1 bullet hits enemy1
        hits = pygame.sprite.groupcollide(enemies1, bullets, False, True)
        for hit in hits:
            hit.health -= damage * len(hits[hit])
            if hit.health <= 0:
                expl = Explosion(hit.rect.center, 'large')
                all_sprites.add(expl)
                CoinDrop()
        # P1 hits enemy1
        hits = pygame.sprite.spritecollide(player, enemies1, True)
        for hit in hits:
            scene = 9000
            expl = Explosion(hit.rect.center, 'large')
            all_sprites.add(expl)
        # Enemy1 bullets hit P1
        hits = pygame.sprite.spritecollide(player, enemy1bullets, True, pygame.sprite.collide_circle)
        for hit in hits:
            expl = Explosion(hit.rect.center, 'small')
            all_sprites.add(expl)
        hits = pygame.sprite.groupcollide(shields, enemy1bullets, False, True, pygame.sprite.collide_circle)
        for hit in hits:
            enemy2shield2_snd.play()


        """ENEMY2 COLLISIONS"""
        # P1 bullet hits enemy2
        hits = pygame.sprite.groupcollide(enemies2, bullets, False, True)
        for hit in hits:
            hit.health -= damage * len(hits[hit])
            if hit.health <= 0:
                expl = Explosion(hit.rect.center, 'large')
                all_sprites.add(expl)
                CoinDrop()
        # NO P1 SHIP HIT ENEMY2 BECAUSE ENEMY2 HAS SHIELD
        # Enemy2 bullet hits P1
        hits = pygame.sprite.spritecollide(player, enemy2bullets, True, pygame.sprite.collide_circle)
        for hit in hits:
            expl = Explosion( (hit.rect.center[0], hit.rect.y + hit.rect.height), 'small')
            all_sprites.add(expl)
        # Enemy2 bullet hits P1 SHIELD
        hits = pygame.sprite.groupcollide(shields, enemy2bullets, False, True, pygame.sprite.collide_circle)
        for hit in hits:
            enemy2shield2_snd.play()

    if scene == 0 or scene == -100:
        """WINDOW VARS"""
        screen.fill(BLACK)
        screen.blit(background, (0, scrollingY))
        screen.blit(background2, (0, scrollingY - 1920))
        scrollingY += 0.1
        if scrollingY >= 1920:
            scrollingY = 0
        all_sprites.draw(screen)
        Hud()

    if scene == -100:
        paused.run()

    pygame.display.flip()
    if player.time == True:
        clock.tick(30)
    else:
        clock.tick(120)
pygame.quit()
sys.exit()
