import pygame
from Load import *
from Player import *


""" TANK """
class Enemy2(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.transform.scale(enemy2_img, (82, 84))
        self.rect = self.image.get_rect()

        """Changeable Vars"""
        self.rect.x = WIDTH/2
        self.rect.y = -200
        self.speed = 1
        self.health = 1000
        self.charge = 0
        self.fullCharge = 300
        self.enemy2shield = Enemy2Shield(self.rect.y + self.rect.height * 3.5)

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
        if self.rect.y == -5:
            self.shield()

        """Destroyed"""
        if self.health <= 0: # Remove itself from the game
            self.kill()
            all_sprites.remove(self.enemy2shield)
            enemy2shields.remove(self.enemy2shield)

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
        all_sprites.add(self.enemy2shield)
        enemy2shields.add(self.enemy2shield)
        enemy2shield1_snd.play()

class Enemy2Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.transform.scale(enemy2laser1_img, (13, 57))
        self.rect = self.image.get_rect()
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
    def __init__(self, y):
        super().__init__()
        self.image = pygame.transform.scale(enemy2shield_img, (640, 50))
        self.rect = self.image.get_rect()
        self.rect.y = y

    def update(self):
        if self.rect.y < 190:
            self.rect.y += 1 # Always infront of Enemy2

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
