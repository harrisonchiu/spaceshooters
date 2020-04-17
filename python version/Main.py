import pygame, sys, ast
from os import path
from Load import *
from Scenes import *
from Upgrades import *
from Player import *
from Enemy1 import *
from Enemy2 import *
from Enemy3 import *
pygame.init()

""" LOADING AND SAVING DATA """
with open(path.join(save_dir, "save.txt"), 'r') as f:
    save = ast.literal_eval(f.read())
    score = save['score']
    upgrades.coins = save['coins']

    upgrades.dmgLvl = save['dmgLvl']
    upgrades.dmgBought = save['dmgBought']
    upgrades.dmgCost = save['dmgCost']
    upgrades.damage = save['damage']

    upgrades.firerateLvl = save['firerateLvl']
    upgrades.firerateBought = save['firerateBought']
    upgrades.firerateCost = save['firerateCost']
    upgrades.fireDelay = save['fireDelay']

    upgrades.gunsLvl = save['gunsLvl']
    upgrades.gunsBought = save['gunsBought']
    upgrades.gunsCost = save['gunsCost']
    upgrades.guns = save['guns']

    upgrades.spLvl = save['spLvl']
    upgrades.spBought = save['spBought']
    upgrades.spCost = save['spCost']
    upgrades.spX = save['spX']

    upgrades.coinLvl = save['coinLvl']
    upgrades.coinBought = save['coinBought']
    upgrades.coinCost = save['coinCost']
    upgrades.coinX = save['coinX']
def Save():
    save['score'] = score
    save['coins'] = upgrades.coins

    save['dmgLvl'] = upgrades.dmgLvl
    save['dmgBought'] = upgrades.dmgBought
    save['dmgCost'] = upgrades.dmgCost
    save['damage'] = upgrades.damage

    save['firerateLvl'] = upgrades.firerateLvl
    save['firerateBought'] = upgrades.firerateBought
    save['firerateCost'] = upgrades.firerateCost
    save['fireDelay'] = upgrades.fireDelay

    save['gunsLvl'] = upgrades.gunsLvl
    save['gunsBought'] = upgrades.gunsBought
    save['gunsCost'] = upgrades.gunsCost
    save['guns'] = upgrades.guns

    save['spLvl'] = upgrades.spLvl
    save['spBought'] = upgrades.spBought
    save['spCost'] = upgrades.spCost
    save['spX'] = upgrades.spX

    save['coinLvl'] = upgrades.coinLvl
    save['coinBought'] = upgrades.coinBought
    save['coinCost'] = upgrades.coinCost
    save['coinX'] = upgrades.coinX

    with open(path.join(save_dir, "save.txt"), 'w') as f:
        f.write(str(save))

""" SPAWNING ENEMIES """
def e1(type):
    enemy1Type1 = Enemy1(1)
    enemy1Type2 = Enemy1(2)
    enemy1Type3 = Enemy1(3)
    if type == 1:
        enemies1.add(enemy1Type1)
        all_sprites.add(enemy1Type1)
    if type == 2:
        enemies1.add(enemy1Type2)
        all_sprites.add(enemy1Type2)
    if type == 3:
        enemies1.add(enemy1Type3)
        all_sprites.add(enemy1Type3)
def e2():
    enemy2 = Enemy2()
    enemies2.add(enemy2)
    all_sprites.add(enemy2)
def e3(type):
    x = random.randint(50, WIDTH - 50)
    y = random.randint(-700, -50)
    enemy3Type1 = Enemy3(x, y, 1)
    enemy3Type2 = Enemy3(x, y, 2)
    enemy3Type3 = Enemy3(x, y, 3)
    if type == 1:
        enemies3.add(enemy3Type1)
        all_sprites.add(enemy3Type1)
    if type == 2:
        enemies3.add(enemy3Type2)
        all_sprites.add(enemy3Type2)
    if type == 3:
        enemies3.add(enemy3Type3)
        all_sprites.add(enemy3Type3)

def Wave():
    if wavetimer == 1:
        all_sprites.add(player)
        asteroids.add(asteroid)
        all_sprites.add(asteroid)
    if wavetimer == 100:
        e1(1)
    if wavetimer == 200:
        e1(2), e1(1)
    if wavetimer == 300:
        e3(1)
    if wavetimer == 350:
        e3(1),e3(2),e3(3)
    if wavetimer == 800:
        e2(),e3(1),e3(1),e3(1),e3(1)
    if wavetimer == 1000:
        e3(1),e3(1),e3(3),e3(3),e3(2),e3(2)
    if wavetimer == 1200:
        e1(1),e1(2),e1(3)
    if wavetimer == 2000:
        e3(3),e3(3),e3(3),e3(3),e3(3),e3(3),e3(3)
    if wavetimer == 3000:
        e3(2),e3(2),e3(2),e3(1),e3(1),e3(3),e3(3)
        e2()
    if wavetimer == 4000:
        e1(1),e1(2),e3(1),e3(1),e3(3),e3(3)
    if wavetimer == 4500:
        e3(2),e3(2),e3(2),e3(1),e3(1),e3(3),e3(3)



""" RUN GAME """
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Save()
            running = False
        if scene == 1 and event.type == pygame.MOUSEBUTTONUP and event.button == 1: # MENU MOUSE CLICK
            if menu.play == True:
                scene = 0
                menu.play = False
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
        if scene == -100 and event.type == pygame.MOUSEBUTTONUP and event.button == 1: # PAUSED MOUSE CLICK
            if paused.menu == True:
                scene = 1
                gametime = 0
                paused.menu = False
                paused.isPaused = False
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
        if scene == 2 and event.type == pygame.MOUSEBUTTONUP and event.button == 1: # HANGAR MOUSE CLICK
            if upgrades.coins >= upgrades.dmgCost and upgrades.dmgSelect == True:
                upgrades.coins -= upgrades.dmgCost
                upgrades.dmgBought += 15
                upgrades.dmgCost += 100
                upgrades.damage += 1
            if upgrades.coins >= upgrades.firerateCost and upgrades.firerateSelect == True and upgrades.firerateLvl != "max":
                upgrades.coins -= upgrades.firerateCost
                upgrades.firerateBought += 15
                upgrades.firerateCost += 100
                upgrades.fireDelay -= 4
            if upgrades.coins >= upgrades.gunsCost and upgrades.gunsSelect == True and upgrades.gunsLvl != "max":
                upgrades.coins -= upgrades.gunsCost
                upgrades.gunsBought += 75
                upgrades.gunsCost += 100
                upgrades.guns += 1
            if upgrades.coins >= upgrades.spCost and upgrades.spSelect == True:
                upgrades.coins -= upgrades.spCost
                upgrades.spBought += 15
                upgrades.spCost += 100
                upgrades.spX += 0.25
            if upgrades.coins >= upgrades.coinCost and upgrades.coinSelect == True and upgrades.coinLvl != "max":
                upgrades.coins -= upgrades.coinCost
                upgrades.coinBought += 30
                upgrades.coinCost += 100
                upgrades.coinX += 1
            if upgrades.back == True:
                scene = 1
                upgrades.back = False
    """~~~~~~~~~~~~~~~~~~~~~~~~~~~"""
    if menu.musicPlay == True:
        pygame.mixer.music.unpause()
    if menu.musicPlay == False:
        pygame.mixer.music.pause()
    """~~~~~~~~~~~~~~~~~~~~~~~~~~~"""
    if scene == 1: # MENU
        menu.run()
    if scene == 2: # UPGRADES (HANGAR)
        upgrades.run()
    if scene == 9000:
        scene = 1
    """~~~~~~~~~~~~~~~~~~~~~~~~~~~"""
    if scene == 0: # GAMPLAY
        wavetimer += 1
        Wave()
        key = pygame.key.get_pressed()
        if key[pygame.K_ESCAPE]:
            scene = -100
        if paused.isPaused == False:
            all_sprites.update()


        """COIN COLLISIONS"""
        hits = pygame.sprite.spritecollide(player, spawncoins, True, pygame.sprite.collide_circle)
        if hits:
            coin_snd.set_volume(0.2)
            coin_snd.play()
            coins += 2 * upgrades.coinX  # coin worth x player coin multiplier

        """ASTEROID COLLISIONS"""
        # P1 bullet hits asteroid
        hits = pygame.sprite.groupcollide(asteroids, bullets, False, True)
        for hit in hits:
            hit.health -= upgrades.damage * len(hits[hit])
            if hit.health <= 0:
                expl = Explosion(hit.rect.center, 'large')
                all_sprites.add(expl)
                CoinDrop(hit.rect.center)
        # P1 hits asteroid
        hits = pygame.sprite.spritecollide(player, asteroids, False, pygame.sprite.collide_circle)
        for hit in hits:
            hit.health = 0
            expl = Explosion(hit.rect.center, 'small')
            all_sprites.add(expl)

        """ENEMY1 COLLISIONS"""
        # P1 bullet hits enemy1
        hits = pygame.sprite.groupcollide(enemies1, bullets, False, True)
        for hit in hits:
            hit.health -= upgrades.damage * len(hits[hit])
            if hit.health <= 0:
                expl = Explosion(hit.rect.center, 'large')
                all_sprites.add(expl)
                CoinDrop(hit.rect.center)
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

        """ENEMY2 COLLISIONS"""
        # P1 bullet hits enemy2
        hits = pygame.sprite.groupcollide(enemies2, bullets, False, True)
        for hit in hits:
            hit.health -= upgrades.damage * len(hits[hit])
            if hit.health <= 0:
                expl = Explosion(hit.rect.center, 'large')
                all_sprites.add(expl)
                CoinDrop(hit.rect.center)
        # NO P1 SHIP HIT ENEMY2 BECAUSE ENEMY2 HAS SHIELD
        # Enemy2 bullet hits P1
        hits = pygame.sprite.spritecollide(player, enemy2bullets, True, pygame.sprite.collide_circle)
        for hit in hits:
            expl = Explosion( (hit.rect.center[0], hit.rect.y + hit.rect.height), 'small')
            all_sprites.add(expl)

        """ENEMY3 COLLISIONS"""
        # P1 bullet hits ENEMY3
        hits = pygame.sprite.groupcollide(enemies3, bullets, False, True)
        for hit in hits:
            hit.health -= upgrades.damage * len(hits[hit])
            if hit.health <= 0:
                expl = Explosion(hit.rect.center, 'large')
                all_sprites.add(expl)
                CoinDrop(hit.rect.center)
        hits = pygame.sprite.spritecollide(player, enemies3, True)
        for hit in hits:
            scene = 9000
            expl = Explosion(hit.rect.center, 'large')
            all_sprites.add(expl)
        hits = pygame.sprite.spritecollide(player, enemy3bullets, True, pygame.sprite.collide_circle)
        for hit in hits:
            expl = Explosion( (hit.rect.center[0], hit.rect.y + hit.rect.height), 'small')
            all_sprites.add(expl)
    """~~~~~~~~~~~~~~~~~~~~~~~~~~~"""
    if scene == 0 or scene == -100: # DRAW SPRITES & BACKGROUND
        screen.fill(BLACK)
        screen.blit(background, (0, scrollBack))
        screen.blit(background, (0, scrollBack - 1920))
        scrollBack += 0.1
        if scrollBack >= 1920:
            scrollBack = 0
        all_sprites.draw(screen)
        Hud()
    if scene == -100: # PAUSED
        paused.isPaused = True
        paused.run()
    #if scene == 9000:

    """~~~~~~~~~~~~~~~~~~~~~~~~~~~"""
    pygame.display.flip()
    clock.tick(120)
pygame.quit()
sys.exit()
