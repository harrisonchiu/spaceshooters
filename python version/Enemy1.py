import pygame, random, math
from Load import *
from Player import *

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
        if self.rect.x > WIDTH * 1.1 or self.rect.x < 0 - 60 or self.rect.y > HEIGHT * 1.1 or self.health <= 0:
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
            self.rect = self.image.get_rect()

            # Randomize Location and Speed Again
            self.rect.x = random.randint(2, WIDTH - self.rect.width - 2)
            self.rect.y = random.randint(-2000, -50)
            self.speedy = random.randint(5, 10)
            self.speedx = random.randint(-3, 3)
            self.health = 100
asteroid = Asteroid()

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

            # Movement Path
            self.rect.x += self.speed # Function equation solved for 'Y' based on X location
            self.rect.y = math.sqrt(-(self.rect.x + 400) ** 2 + 600000) - 100

            # Shoots 3 times
            if self.rect.y == HEIGHT/2 or self.rect.y == HEIGHT/4 or self.rect.y == HEIGHT * 2/3:
              self.shoot()
            if self.rect.y <= 0: # Removes itself from game
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
