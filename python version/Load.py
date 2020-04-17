import pygame, random
from os import path
pygame.init()

""" MANDATORY VARS """

WIDTH = 640 # Window
HEIGHT = 720 # Size
TITLE = "untitled"
screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption(TITLE)
clock = pygame.time.Clock()
save_dir = path.dirname(__file__)
enemy_dir = path.join(path.dirname(__file__), 'EnemySprites')
snd_dir = path.join(path.dirname(__file__), 'Sound')
visuals_dir = path.join(path.dirname(__file__), 'GeneralVisuals')
player_dir = path.join(path.dirname(__file__), 'Player')

""" GLOBAL VARS """
all_sprites = pygame.sprite.Group()
spawncoins = pygame.sprite.Group()
bullets = pygame.sprite.Group()
asteroids = pygame.sprite.Group()
enemies1 = pygame.sprite.Group()
enemy1bullets = pygame.sprite.Group()
enemies2 = pygame.sprite.Group()
enemy2bullets = pygame.sprite.Group()
enemy2shields = pygame.sprite.Group()
enemies3 = pygame.sprite.Group()
enemy3bullets = pygame.sprite.Group()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 230, 118)

running = True
wavetimer = 0
scene = 1
save = {}
coins = 0
score = 0


""" LOAD ALL IMAGES """
# BACKGROUNDS
menuBack = pygame.image.load(path.join(visuals_dir, "BackMenu.jpg")).convert()
hangarBack = pygame.image.load(path.join(visuals_dir, "BackHangar.png")).convert()
pausedBack = pygame.image.load(path.join(visuals_dir, "BackPaused.png")).convert_alpha()
background = pygame.image.load(path.join(visuals_dir, "BackGame.png")).convert()
scrollBack = 0
# BUTTONS
playL = pygame.image.load(path.join(visuals_dir, "PlayLight.png")).convert_alpha() # Play
playD = pygame.image.load(path.join(visuals_dir, "PlayDark.png")).convert_alpha()
hangarL = pygame.image.load(path.join(visuals_dir, "HangarLight.png")).convert_alpha() # Hangar
hangarD = pygame.image.load(path.join(visuals_dir, "HangarDark.png")).convert_alpha()
helpL = pygame.image.load(path.join(visuals_dir, "HelpLight.png")).convert_alpha() # Help
helpD = pygame.image.load(path.join(visuals_dir, "HelpDark.png")).convert_alpha()
backL = pygame.image.load(path.join(visuals_dir, "BackLight.png")).convert_alpha() # Back
backD = pygame.image.load(path.join(visuals_dir, "BackDark.png")).convert_alpha()
soundL = pygame.image.load(path.join(visuals_dir, "SoundLight.png")).convert_alpha() # Sound
soundD = pygame.image.load(path.join(visuals_dir, "SoundDark.png")).convert_alpha()
muteL = pygame.image.load(path.join(visuals_dir, "MuteLight.png")).convert_alpha() # Mute
muteD = pygame.image.load(path.join(visuals_dir, "MuteDark.png")).convert_alpha()
menuL = pygame.image.load(path.join(visuals_dir, "MenuLight.png")).convert_alpha() # Menu
menuD = pygame.image.load(path.join(visuals_dir, "MenuDark.png")).convert_alpha()
# HANGAR
stats_img = pygame.image.load(path.join(visuals_dir, "stats.png")).convert_alpha() # Stats Bar
font = pygame.font.Font(path.join(visuals_dir, "future.ttf"), 18) # Future Font
select_img = pygame.image.load(path.join(visuals_dir, "select.png")).convert_alpha() # Select Highlight
# GAME VISUALS
explosion_anim = {}
explosion_anim['large'] = []
explosion_anim['small'] = []
for i in range(9):
    filename = 'regularExplosion0{}.png'.format(i)
    img = pygame.image.load(path.join(visuals_dir, filename)).convert_alpha()
    img_large = pygame.transform.scale(img, (75, 75)) # Large Explosion
    explosion_anim['large'].append(img_large)
    img_small = pygame.transform.scale(img, (32, 32)) # Small Explosion
    explosion_anim['small'].append(img_small)
coin_img = pygame.image.load(path.join(visuals_dir, "coin.png")).convert()
# PLAYER
player_img = pygame.image.load(path.join(player_dir, "player.png")).convert_alpha()
bullet_img = pygame.image.load(path.join(player_dir, "playerlaser.png")).convert_alpha()
fire1_img = pygame.image.load(path.join(player_dir, "playerfire1.png")).convert_alpha()
fire2_img = pygame.image.load(path.join(player_dir, "playerfire2.png")).convert_alpha()
fire3_img = pygame.image.load(path.join(player_dir, "playerfire3.png")).convert_alpha()
shield_img = pygame.image.load(path.join(player_dir, "playershield.png")).convert_alpha()
# ASTEROIDS
asteroid1_img = pygame.image.load(path.join(enemy_dir, "asteroid1.png")).convert_alpha()
asteroid2_img = pygame.image.load(path.join(enemy_dir, "asteroid2.png")).convert_alpha()
asteroid3_img = pygame.image.load(path.join(enemy_dir, "asteroid3.png")).convert_alpha()
asteroid4_img = pygame.image.load(path.join(enemy_dir, "asteroid4.png")).convert_alpha()
asteroid5_img = pygame.image.load(path.join(enemy_dir, "asteroid5.png")).convert_alpha()
asteroid6_img = pygame.image.load(path.join(enemy_dir, "asteroid6.png")).convert_alpha()
asteroid7_img = pygame.image.load(path.join(enemy_dir, "asteroid7.png")).convert_alpha()
asteroid8_img = pygame.image.load(path.join(enemy_dir, "asteroid8.png")).convert_alpha()
# ENEMY 1
enemy1type1_img = pygame.image.load(path.join(enemy_dir, "enemy1type1.png")).convert_alpha()
enemy1type23_img = pygame.image.load(path.join(enemy_dir, "enemy1type23.png")).convert_alpha()
enemy1laser1_img = pygame.image.load(path.join(enemy_dir, "enemy1laser1.png")).convert_alpha()
# ENEMY 2
enemy2_img = pygame.image.load(path.join(enemy_dir, "enemy2.png")).convert_alpha()
enemy2laser1_img = pygame.image.load(path.join(enemy_dir, "enemy2laser1.png")).convert_alpha()
enemy2shield_img = pygame.image.load(path.join(enemy_dir, "enemy2shield.png")).convert_alpha()
# ENEMY 3
enemy3type1_img = pygame.image.load(path.join(enemy_dir, "enemy3type1.png")).convert()
enemy3type2_img = pygame.image.load(path.join(enemy_dir, "enemy3type2.png")).convert()
enemy3type3_img = pygame.image.load(path.join(enemy_dir, "enemy3type3.png")).convert()
enemy3laser1_img = pygame.image.load(path.join(enemy_dir, "enemy3laser1.png")).convert()

""" LOAD GAME SOUNDS """
# USE CHANNELS ONLY IF OTHERWISE SOUND WOULD NOT BE PLAYED
channel0 = pygame.mixer.Channel(0) # Player, explosions
channel1 = pygame.mixer.Channel(1) # Enemy1
channel2 = pygame.mixer.Channel(2) # Enemy2
channel3 = pygame.mixer.Channel(3) # Enemy3
channel4 = pygame.mixer.Channel(4) # Enemy4
channel5 = pygame.mixer.Channel(5) # Enemy5
channel6 = pygame.mixer.Channel(6) # Enemy6
channel7 = pygame.mixer.Channel(7) # Other Game Mechanics
# BACKGROUND MUSIC
def Music():
    song = random.randint(1,4)
    if song == 1:
        pygame.mixer.music.load(path.join(snd_dir, 'stay.ogg'))
        pygame.mixer.music.set_volume(0.8)
    elif song == 2:
        pygame.mixer.music.load(path.join(snd_dir, 'untitled.ogg'))
        pygame.mixer.music.set_volume(0.3)
    elif song == 3:
        pygame.mixer.music.load(path.join(snd_dir, 'ftl.ogg'))
        pygame.mixer.music.set_volume(0.3)
    elif song == 4:
        pygame.mixer.music.load(path.join(snd_dir, 'miami.ogg'))
        pygame.mixer.music.set_volume(0.3)
    pygame.mixer.music.play(5) # plays 6 times
explosion1_snd = pygame.mixer.Sound(path.join(snd_dir, 'explosion1.wav'))
explosion2_snd = pygame.mixer.Sound(path.join(snd_dir, 'explosion2.wav'))
explosion3_snd = pygame.mixer.Sound(path.join(snd_dir, 'explosion3.wav'))
explosion4_snd = pygame.mixer.Sound(path.join(snd_dir, 'explosion4.wav'))
explosion5_snd = pygame.mixer.Sound(path.join(snd_dir, 'explosion5.wav'))
coin_snd = pygame.mixer.Sound(path.join(snd_dir, 'coin.ogg'))
playerlaser_snd = pygame.mixer.Sound(path.join(snd_dir, 'playerlaser.wav'))
enemy2shield1_snd = pygame.mixer.Sound(path.join(snd_dir, 'enemy2shield1.wav'))
enemy2shield2_snd = pygame.mixer.Sound(path.join(snd_dir, 'enemy2shield2.wav'))
enemy2shield3_snd = pygame.mixer.Sound(path.join(snd_dir, 'enemy2shield3.wav'))
