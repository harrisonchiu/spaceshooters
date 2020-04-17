import pygame, math
from Load import *
from Player import *


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
        if self.health <= 0 or self.rect.x >= WIDTH or self.rect.x <= 0 or self.rect.y >= HEIGHT:
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
