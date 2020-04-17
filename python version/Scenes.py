import pygame
from Load import *

class Menu():
    def __init__(self):
        self.image = pygame.transform.scale(menuBack, (1440, 900))
        self.playL = pygame.transform.scale(playL, (120, 34))
        self.playD = pygame.transform.scale(playD, (120, 34))
        self.play = False

        self.hangarL = pygame.transform.scale(hangarL, (120, 34))
        self.hangarD = pygame.transform.scale(hangarD, (120, 34))
        self.hangar = False

        self.helpL = pygame.transform.scale(helpL, (120, 34))
        self.helpD = pygame.transform.scale(helpD, (120, 34))
        self.help = False

        self.soundL = pygame.transform.scale(soundL, (120, 34))
        self.soundD = pygame.transform.scale(soundD, (120, 34))
        self.muteL = pygame.transform.scale(muteL, (120, 34))
        self.muteD = pygame.transform.scale(muteD, (120, 34))
        self.music = False
        self.musicPlay = True
        Music()

    def run(self):
        mx = pygame.mouse.get_pos()[0]
        my = pygame.mouse.get_pos()[1]

        screen.blit(self.image, (-400, 0)) # Light Images
        screen.blit(self.playL, (274, 300))
        screen.blit(self.hangarL, (274, 360))
        screen.blit(self.helpL, (274, 420))
        if self.musicPlay == True:
            screen.blit(self.soundL, (274, 480))
        if self.musicPlay == False:
            screen.blit(self.muteL, (274, 480))

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
menu = Menu()

class Paused():
    def __init__(self):
        self.image = pygame.transform.scale(pausedBack, (WIDTH, HEIGHT))
        self.isPaused = False

        self.menuL = pygame.transform.scale(menuL, (120, 34))
        self.menuD = pygame.transform.scale(menuD, (120, 34))
        self.menu = False

        self.soundL = pygame.transform.scale(soundL, (120, 34))
        self.soundD = pygame.transform.scale(soundD, (120, 34))
        self.muteL = pygame.transform.scale(muteL, (120, 34))
        self.muteD = pygame.transform.scale(muteD, (120, 34))
        self.music = False

        self.backL = pygame.transform.scale(backL, (120, 34))
        self.backD = pygame.transform.scale(backD, (120, 34))
        self.back = False

    def run(self):
        mx = pygame.mouse.get_pos()[0]
        my = pygame.mouse.get_pos()[1]

        screen.blit(self.image, (0, 0))
        screen.blit(self.menuL, (274, 300))
        screen.blit(self.backL, (274, 420))
        if menu.musicPlay == True:
            screen.blit(self.soundL, (274, 360))
        if menu.musicPlay == False:
            screen.blit(self.muteL, (274, 360))

        if mx >= 274 and mx <= 394 and my >= 300 and my <= 334: # Menu dark and click detection
            screen.blit(self.menuD, (274, 300))
            self.menu = True
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
paused = Paused()

class GameOver():
    def __init__(self):
        self.image = pygame.transform.scale(pausedBack, (WIDTH, HEIGHT))

        self.menuL = pygame.transform.scale(menuL, (120, 34))
        self.menuD = pygame.transform.scale(menuD, (120, 34))
        self.menu = False
