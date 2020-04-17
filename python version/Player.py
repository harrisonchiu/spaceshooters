import pygame, random
from Load import *
from Upgrades import *

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() # NAME: Endurance, Ranger (from Interstellar); K-2SO; Krestel Cruiserp # WHICH SHIP
        self.image = pygame.transform.scale(player_img, (55, 46))
        self.rect = self.image.get_rect()
        self.radius = 28
        #pygame.draw.circle(self.image, RED, (self.rect.center), self.radius)

        """Changeable Vars"""
        self.rect.x = WIDTH/2 - self.rect.width/2 # Spawn
        self.rect.y = HEIGHT - self.rect.height*3 # Location
        self.fireDelayTimer = 0
        self.ready = True
        self.speed = 2
        self.maxHp = 700
        self.maxCharge = 400
        self.health = self.maxHp
        self.charge = self.maxCharge

        """Skills Vars"""
        self.beam = False
        self.beamTime = 0
        self.time = False
        self.timeTimer = 0
        self.timeMulti = 1
        self.sp = 0

    def update(self):
        """Player Key Movement"""
        key = pygame.key.get_pressed()
        if key[pygame.K_w] and self.rect.y > 3: # [W]
            self.rect.y -= self.speed * self.timeMulti
        elif key[pygame.K_s] and self.rect.y < HEIGHT - self.rect.height - 3: # [S]
            self.rect.y += self.speed * self.timeMulti
        if key[pygame.K_d] and self.rect.x < WIDTH - self.rect.width - 3: # [D]
            self.rect.x += self.speed * self.timeMulti
        elif key[pygame.K_a] and self.rect.x > 3: # [A]
            self.rect.x -= self.speed * self.timeMulti

        """Player Shoot Action"""
        # Normal Shoot
        if key[pygame.K_SPACE] and self.fireDelayTimer >= upgrades.fireDelay and self.ready == True and self.beam == False:
            self.shoot()
            self.fireDelayTimer = 0
        self.fireDelayTimer += 5 * self.timeMulti

        if self.charge <= 0: # Can't shoot if no charge
            self.charge = 0
            self.ready = False
        if self.ready == False: # Charges slowly if used all
            self.charge += 0.25
        elif self.fireDelayTimer >= upgrades.fireDelay * 3: # Charges if not shooting
            self.charge += 0.6
        if self.charge >= self.maxCharge: # If fully charged, can shoot
            self.charge = self.maxCharge
            self.ready = True


        """Player SP Beam"""
        if key[pygame.K_1] and self.sp >= 100: # Activate Beam
            self.sp = 0
            self.beam = True
        if self.beam == True: # Beam Duration
            self.beamTime += 1
            if self.beamTime >= 700:
                self.beam = False
                self.beamTime = 0
        if key[pygame.K_SPACE] and self.beam == True: # Beam Shoot
            self.shoot()


        """Player SP Time"""
        if key[pygame.K_2] and self.sp >= 100: # Activate Time Bend
            self.time = True
        if self.time == True: # Time Duration
            self.timeMulti = 3
            self.timeTimer += 1
            if self.timeTimer >= 300:
                self.time = False
                self.timeTimer = 0
                self.timeMulti = 1

    def shoot(self):
        """Shoot"""
        if upgrades.guns == 1:
            bullet1 = Bullet(self.rect.x + self.rect.width/2 - 4, self.rect.y - self.rect.height/2 - 50) # MIDDLE
            all_sprites.add(bullet1)
            bullets.add(bullet1)
        elif upgrades.guns == 2:
            bullet1 = Bullet(self.rect.x + self.rect.width/4 - 5, self.rect.y - self.rect.height/4 - 50) # LEFT
            bullet2 = Bullet(self.rect.x + self.rect.width - self.rect.width/4 - 1, self.rect.y - self.rect.height/4 - 50) # RIGHT
            all_sprites.add(bullet1)
            bullets.add(bullet1)
            all_sprites.add(bullet2)
            bullets.add(bullet2)
        elif upgrades.guns == 3:
            bullet1 = Bullet(self.rect.x - 6, self.rect.y - 50) # FAR LEFT
            bullet2 = Bullet(self.rect.x + self.rect.width/2 - 4, self.rect.y - self.rect.height/2 - 50) # MIDDLE
            bullet3 = Bullet(self.rect.x + self.rect.width, self.rect.y - 50) # FAR RIGHT
            all_sprites.add(bullet1)
            bullets.add(bullet1)
            all_sprites.add(bullet2)
            bullets.add(bullet2)
            all_sprites.add(bullet3)
            bullets.add(bullet3)
        elif upgrades.guns == 4:
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
        elif upgrades.guns == 5:
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
            if upgrades.firerateLvl == 1:
                self.charge -= 15
            if upgrades.firerateLvl == 2:
                self.charge -= 10
            if upgrades.firerateLvl == 3:
                self.charge -= 8
            if upgrades.firerateLvl == "max":
                self.charge -= 5
        # Plays a sound
        playerlaser_snd.play()
        playerlaser_snd.set_volume(0.3)
        # Shoot firerateLvl
        fire = BulletFire()
        all_sprites.add(fire)
player = Player()

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.transform.scale(bullet_img, (7, 27))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = 15

    def update(self):
        self.rect.y -= self.speed
        if self.rect.y < -30: # Remove from game if out of game
            self.kill()

class BulletFire(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.type = random.randint(1, 3)
        if self.type == 1:
            self.image = pygame.transform.scale(fire1_img, (11, 17))
        if self.type == 2:
            self.image = pygame.transform.scale(fire2_img, (15, 21))
        if self.type == 3:
            self.image = pygame.transform.scale(fire3_img, (13, 19))
        self.rect = self.image.get_rect()
        self.rect.x = player.rect.center[0] - self.rect.width/2
        self.rect.y = player.rect.y - 15
        self.time = 0

    def update(self):
        self.rect.x = player.rect.center[0] - self.rect.width/2
        self.rect.y = player.rect.y - 15
        self.time += 1
        if self.time > 10: # Remove from game if out of game
            self.kill()

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
    if spAmount > 100:
        spAmount = 100
    pygame.draw.rect( screen, GREEN, (515, 690, spAmount, SP_HEIGHT) )
    pygame.draw.rect( screen, WHITE, (515, 690, SP_LENGTH, SP_HEIGHT), 3 )
    spText = font.render("SP:", 1, (WHITE))
    screen.blit(spText, (480, 690))
