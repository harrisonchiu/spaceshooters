setup = function() {
    noStroke();
    createCanvas(384, 584);
};
// IMAGE VARIABLES
{
var battleSong; 
var myFont;
var tSW1Ship, tSW2Ship, t1Ship, t2Ship, t3Ship, t4Ship, t5Ship, t6Ship, t7Ship, t8Ship, t9Ship, t10Ship, t11Ship, t12Ship, tS1Ship, tS2Ship, tS3Ship, tS4Ship;
var tSWShipAegis, t1ShipAegis, t2ShipAegis, t3ShipAegis, t4ShipAegis, t5ShipAegis, t6ShipAegis, t7ShipAegis, t8ShipAegis, t9ShipAegis, t10ShipAegis, t11ShipAegis, t12ShipAegis, tS1ShipAegis, tS2ShipAegis, tS3ShipAegis, tS4ShipAegis;
var asteroid1;
var asteroid2;
var mine;
var mineExplosion;
var enemyA1, enemyA2, enemyA3, enemyA4;
var bossA;
var armorI, armorII, armorIII, armorIII2;
var damageI, damageII, damageIII;
var speedI, speedII, speedIII;
var gunT1, gunT2, gunT3;
var armorT1, armorT2, armorT3I, armorT3II;
var engineT1, engineT2, engineT3;
var selected;
var locked;
var holdingRack;
var armory;
var playerGUI;
var powerUp1, powerUp2, powerUp3;
var map1;
var menuBackground;
var gameoverScene;
var helpL;
var helpD;
var playL;
var playD;
var hangar;
var hangerL;
var hangerD;
var doorLeft;
var doorRight;
var armoryL;
var armoryD;
var menuL;
var menuD;
var shipsL;
var shipsD;
var backL;
var backD;
var resetL;
var resetD;
var shipSelect;
var explosion1, explosion2, explosion3, explosion4, explosion5, explosion6, explosion7, explosion8, explosion9, explosion10, bigExplosion;
var coalition;
} 
// Load Images
var preload = function() { 
    // Player ships
    tSW1Ship = loadImage("libraries/Graphics/Com Sci Graphics/Player Models/SW_1.gif");
    tSW2Ship = loadImage("libraries/Graphics/Com Sci Graphics/Player Models/SW_2.gif");
    t1Ship = loadImage("libraries/Graphics/Com Sci Graphics/Player Models/Tier_D_1_Ship.gif");
    t2Ship = loadImage("libraries/Graphics/Com Sci Graphics/Player Models/Tier_D_2_Ship.gif");
    t3Ship = loadImage("libraries/Graphics/Com Sci Graphics/Player Models/Tier_D_3_Ship.gif");
    t4Ship = loadImage("libraries/Graphics/Com Sci Graphics/Player Models/Tier_D_4_Ship.gif");
    t5Ship = loadImage("libraries/Graphics/Com Sci Graphics/Player Models/Tier_1_Ship.gif");
    t6Ship = loadImage("libraries/Graphics/Com Sci Graphics/Player Models/Tier_2_Ship.gif");
    t7Ship = loadImage("libraries/Graphics/Com Sci Graphics/Player Models/Tier_3_Ship.gif");
    t8Ship = loadImage("libraries/Graphics/Com Sci Graphics/Player Models/Tier_4_Ship.gif");
    t9Ship = loadImage("libraries/Graphics/Com Sci Graphics/Player Models/Tier_5_Ship.gif");
    t10Ship = loadImage("libraries/Graphics/Com Sci Graphics/Player Models/Tier_6_Ship.gif");
    t11Ship = loadImage("libraries/Graphics/Com Sci Graphics/Player Models/Tier_7_Ship.gif");
    t12Ship = loadImage("libraries/Graphics/Com Sci Graphics/Player Models/Tier_8_Ship.gif");
    tS1Ship = loadImage("libraries/Graphics/Com Sci Graphics/Player Models/Tier_S_1_Ship.gif");
    tS2Ship = loadImage("libraries/Graphics/Com Sci Graphics/Player Models/Tier_S_2_Ship.gif");
    tS3Ship = loadImage("libraries/Graphics/Com Sci Graphics/Player Models/Tier_S_3_Ship.gif");
    tS4Ship = loadImage("libraries/Graphics/Com Sci Graphics/Player Models/Tier_S_4_Ship.gif");
    
    //Player Ship Powerups
    tSWShipAegis = loadImage("libraries/Graphics/Com Sci Graphics/Player Aegis/SW_Aegis.gif");
    t1ShipAegis = loadImage("libraries/Graphics/Com Sci Graphics/Player Aegis/Tier_1_Aegis.gif");
    t2ShipAegis = loadImage("libraries/Graphics/Com Sci Graphics/Player Aegis/Tier_2_Aegis.gif");
    t3ShipAegis = loadImage("libraries/Graphics/Com Sci Graphics/Player Aegis/Tier_3_Aegis.gif");
    t4ShipAegis = loadImage("libraries/Graphics/Com Sci Graphics/Player Aegis/Tier_4_Aegis.gif");
    t5ShipAegis = loadImage("libraries/Graphics/Com Sci Graphics/Player Aegis/Tier_5_Aegis.gif");
    t6ShipAegis = loadImage("libraries/Graphics/Com Sci Graphics/Player Aegis/Tier_6_Aegis.gif");
    t7ShipAegis = loadImage("libraries/Graphics/Com Sci Graphics/Player Aegis/Tier_7_Aegis.gif");
    t8ShipAegis = loadImage("libraries/Graphics/Com Sci Graphics/Player Aegis/Tier_8_Aegis.gif");
    t9ShipAegis = loadImage("libraries/Graphics/Com Sci Graphics/Player Aegis/Tier_9_Aegis.gif");
    t10ShipAegis = loadImage("libraries/Graphics/Com Sci Graphics/Player Aegis/Tier_10_Aegis.gif");
    t11ShipAegis = loadImage("libraries/Graphics/Com Sci Graphics/Player Aegis/Tier_11_Aegis.gif");
    t12ShipAegis = loadImage("libraries/Graphics/Com Sci Graphics/Player Aegis/Tier_12_Aegis.gif");
    tS1ShipAegis = loadImage("libraries/Graphics/Com Sci Graphics/Player Aegis/Tier_S_1_Aegis.gif");
    tS2ShipAegis = loadImage("libraries/Graphics/Com Sci Graphics/Player Aegis/Tier_S_2_Aegis.gif");
    tS3ShipAegis = loadImage("libraries/Graphics/Com Sci Graphics/Player Aegis/Tier_S_3_Aegis.gif");
    tS4ShipAegis = loadImage("libraries/Graphics/Com Sci Graphics/Player Aegis/Tier_S_4_Aegis.gif");
    
    // Entities
    asteroid1 = loadImage("libraries/Graphics/Com Sci Graphics/Enemies/Asteroid1.gif");
    asteroid2 = loadImage("libraries/Graphics/Com Sci Graphics/Enemies/Asteroid2.gif");
    enemyA1 = loadImage("libraries/Graphics/Com Sci Graphics/Enemies/Enemy1.gif");
    enemyA2 = loadImage("libraries/Graphics/Com Sci Graphics/Enemies/Enemy3.gif");
    enemyA3 = loadImage("libraries/Graphics/Com Sci Graphics/Enemies/Enemy5.gif");
    enemyA4 = loadImage("libraries/Graphics/Com Sci Graphics/Enemies/Enemy7.gif");
    bossA = loadImage("libraries/Graphics/Com Sci Graphics/Enemies/Boss1.gif");
    mine = loadImage("libraries/Graphics/Com Sci Graphics/Enemies/Mine.gif");
    
    // Map
    map1 = loadImage("libraries/Graphics/Com Sci Graphics/Maps/MapLevel1.png");
    menuBackground = loadImage("libraries/Graphics/Com Sci Graphics/Maps/Menu.png");
    hangar = loadImage("libraries/Graphics/Com Sci Graphics/Menu/Hangar.png");
    playerGUI = loadImage("libraries/Graphics/Com Sci Graphics/Menu/PilotGUI.png");
    doorLeft = loadImage("libraries/Graphics/Com Sci Graphics/Menu/HangarDoorLeft.png");
    doorRight = loadImage("libraries/Graphics/Com Sci Graphics/Menu/HangarDoorRight.png");
    gameoverScene = loadImage("libraries/Graphics/Com Sci Graphics/Maps/Gameover.gif");
        
    // Text
    armoryL = loadImage("libraries/Graphics/Com Sci Graphics/Menu/ArmoryLight.png");
    armoryD = loadImage("libraries/Graphics/Com Sci Graphics/Menu/ArmoryDark.png");
    backL = loadImage("libraries/Graphics/Com Sci Graphics/Menu/BackLight.png");
    backD = loadImage("libraries/Graphics/Com Sci Graphics/Menu/BackDark.png");
    hangerL = loadImage("libraries/Graphics/Com Sci Graphics/Menu/HangarLight.png");
    hangerD = loadImage("libraries/Graphics/Com Sci Graphics/Menu/HangarDark.png");
    helpL = loadImage("libraries/Graphics/Com Sci Graphics/Menu/HelpLight.png");
    helpD = loadImage("libraries/Graphics/Com Sci Graphics/Menu/HelpDark.png");
    menuL = loadImage("libraries/Graphics/Com Sci Graphics/Menu/MenuLight.png");
    menuD = loadImage("libraries/Graphics/Com Sci Graphics/Menu/MenuDark.png");
    playL = loadImage("libraries/Graphics/Com Sci Graphics/Menu/PlayLight.png");
    playD = loadImage("libraries/Graphics/Com Sci Graphics/Menu/PlayDark.png");
    shipsL = loadImage("libraries/Graphics/Com Sci Graphics/Menu/ShipsLight.png");
    shipsD = loadImage("libraries/Graphics/Com Sci Graphics/Menu/ShipsDark.png");
    resetL = loadImage("libraries/Graphics/Com Sci Graphics/Menu/ResetLight.png");
    resetD = loadImage("libraries/Graphics/Com Sci Graphics/Menu/ResetDark.png");
    title = loadImage("libraries/Graphics/Com Sci Graphics/Menu/EagleSquadron.png");
    powerUp1 = loadImage("libraries/Graphics/Com Sci Graphics/Menu/PowerUp (1).png");
    powerUp2 = loadImage("libraries/Graphics/Com Sci Graphics/Menu/PowerUp (2).png");
    powerUp3 = loadImage("libraries/Graphics/Com Sci Graphics/Menu/PowerUp (3).png");
    shipSelect = loadImage("libraries/Graphics/Com Sci Graphics/Menu/ShipSelect.gif");
    armory = loadImage("libraries/Graphics/Com Sci Graphics/Menu/Armory.gif");
    armorI = loadImage("libraries/Graphics/Com Sci Graphics/Menu/ArmorUpgrade_I.gif");
    armorII = loadImage("libraries/Graphics/Com Sci Graphics/Menu/ArmorUpgrade_II.gif");
    armorIII = loadImage("libraries/Graphics/Com Sci Graphics/Menu/ArmorUpgrade_III_1.gif");
    armorIII2 = loadImage("libraries/Graphics/Com Sci Graphics/Menu/ArmorUpgrade_III_2.gif");
    speedI = loadImage("libraries/Graphics/Com Sci Graphics/Menu/SpeedUpgrade_I.gif");
    speedII = loadImage("libraries/Graphics/Com Sci Graphics/Menu/SpeedUpgrade_II.gif");
    speedIII = loadImage("libraries/Graphics/Com Sci Graphics/Menu/SpeedUpgrade_III.gif");
    damageI = loadImage("libraries/Graphics/Com Sci Graphics/Menu/DamageUpgrade_I.gif");
    damageII = loadImage("libraries/Graphics/Com Sci Graphics/Menu/DamageUpgrade_II.gif");
    damageIII = loadImage("libraries/Graphics/Com Sci Graphics/Menu/DamageUpgrade_III.gif");
    locked = loadImage("libraries/Graphics/Com Sci Graphics/Menu/Locked.gif");
    selected = loadImage("libraries/Graphics/Com Sci Graphics/Menu/Selected.gif");
    gunT1 = loadImage("libraries/Graphics/Com Sci Graphics/Menu/GunTier1.gif");
    gunT2 = loadImage("libraries/Graphics/Com Sci Graphics/Menu/GunTier2.gif");
    gunT3 = loadImage("libraries/Graphics/Com Sci Graphics/Menu/GunTier3.gif");
    armorT1 = loadImage("libraries/Graphics/Com Sci Graphics/Menu/ArmorTier1.gif");
    armorT2 = loadImage("libraries/Graphics/Com Sci Graphics/Menu/ArmorTier2.gif");
    armorT3I = loadImage("libraries/Graphics/Com Sci Graphics/Menu/ArmorTier3-1.gif");
    armorT3II = loadImage("libraries/Graphics/Com Sci Graphics/Menu/ArmorTier3-2.gif");
    engineT1 = loadImage("libraries/Graphics/Com Sci Graphics/Menu/EngineTier1.gif");
    engineT2 = loadImage("libraries/Graphics/Com Sci Graphics/Menu/EngineTier2.gif");
    engineT3 = loadImage("libraries/Graphics/Com Sci Graphics/Menu/EngineTier3.gif");
    holdingRack = loadImage("libraries/Graphics/Com Sci Graphics/Menu/HoldingRack.gif");
    
    //Fonts
    myFont = loadFont("libraries/Graphics/Com Sci Graphics/Font/Exo-MediumItalic.ttf");
    coalition = loadFont("libraries/Graphics/Com Sci Graphics/Font/Coalition_v2..ttf");
    
    //Audio
   battleSong = loadSound('libraries/Graphics/Com Sci Graphics/Audio/Ep.wav');
    
    // Explosion
    explosion1 = loadImage("libraries/Graphics/Com Sci Graphics/Animations/Explosion/explosion (1).png");
    explosion2 = loadImage("libraries/Graphics/Com Sci Graphics/Animations/Explosion/explosion (2).png");
    explosion3 = loadImage("libraries/Graphics/Com Sci Graphics/Animations/Explosion/explosion (3).png");        
    explosion4 = loadImage("libraries/Graphics/Com Sci Graphics/Animations/Explosion/explosion (4).png");
    explosion5 = loadImage("libraries/Graphics/Com Sci Graphics/Animations/Explosion/explosion (5).png");
    explosion6 = loadImage("libraries/Graphics/Com Sci Graphics/Animations/Explosion/explosion (6).png");
    explosion7 = loadImage("libraries/Graphics/Com Sci Graphics/Animations/Explosion/explosion (7).png");
    explosion8 = loadImage("libraries/Graphics/Com Sci Graphics/Animations/Explosion/explosion (8).png");
    explosion9 = loadImage("libraries/Graphics/Com Sci Graphics/Animations/Explosion/explosion (9).png");
    explosion10 = loadImage("libraries/Graphics/Com Sci Graphics/Animations/Explosion/explosion (10).png");
    bigExplosion = loadImage("libraries/Graphics/Com Sci Graphics/Animations/Explosion/Explosion.gif");
    mineExplosion = loadImage("libraries/Graphics/Com Sci Graphics/Animations/Explosion/mineExplosion.gif");
};

// Global Variables
var spawn;
var systemLoginId;
var admin = false;

//Animations
var explosions = function(x, y) {
    image(bigExplosion, x - 20, y - 20);
};

/** SCENES AND BUTTONS **/
var scene = 1;

// Menu Scene
var menu = function() { // Draw it
    // Background
    image(menuBackground, 0, 0);
    
    // Show title
    fill(255, 255, 255);
    textSize(35);
    textFont(coalition);
    text("STEEL TALONS", 20, 140, 500, 100);
    
    // Show play button
    image(playL, 145, 210);
    
    // Show hangar button
    image(hangerL, 145, 260);
    
    // Show help button
    image(helpL, 145, 310);
    
    // Highlight buttons when mouse in area
    if(mouseX >= 145 && mouseX <= 237 && mouseY >= 210 && mouseY <= 236) {        
        image(playD, 145, 210);
    }
    if(mouseX >= 145 && mouseX <= 237 && mouseY >= 260 && mouseY <= 286) {
        image(hangerD, 145, 260);
    }
    if(mouseX >= 145 && mouseX <= 237 && mouseY >= 310 && mouseY <= 336) {
        image(helpD, 145, 310);
    }
    
    // Highscore and unlocks goals
    textSize(20);
    textFont(myFont);
    text("Highscore: " + highscore, 20, 450, 364);
    text("Next unlock: ", 20, 500);
    if (highscore < 500) {
        text("Tier 2 Ships (Need Score of 500)", 130, 500, 210);
    }
    else if (highscore >= 500 && highscore < 2000) {
        text("Tier 1 Ships Upgrades (Need Score of 2000)", 130, 500, 210);
    }
    else if (highscore >= 2000 && highscore < 5000) {
        text("Tier 3 Ships and Tier 2 Ship Upgrades (Need Score of 5000)", 130, 500, 210);
    }
    else if (highscore >= 5000 && highscore < 8000) {
        text("Tier 3 Ship Upgrades (Need Score of 8000)", 130, 500, 210);
    }
    else if (highscore >= 8000 && highscore < 10000) {
        text("Tier 4 Ships (Need Score of 10000)", 130, 500, 210);
    }
    else if (highscore >= 10000 && highscore < 20000) {
        text("Tier 5 Ships (Need Score of 20000)", 130, 500, 210);
    }
    
    // Credits
    textSize(15);
    textFont(myFont);
    text("Created by Harrison and Sunny", 20, 575, 300);

    
};

// Hanger Scene
var unlockTier = 0;
var upgradeTier = 0;
var engineTier = 0;
var armorTier = 0;
var gunTier = 0;

var showUpgrades = function() {
    if(gunTier === 0) {
        image(holdingRack, 4, 408);
        image(holdingRack, 72, 408);
    }
    if(gunTier === 1) {
        image(gunT1, 4, 408);
        image(gunT1, 72, 408);
        if(scene === 32) {
            image(selected, 271, 548);
        }
    }
    if(gunTier === 2) {
        image(gunT2, 4, 408);
        image(gunT2, 72, 408);
        if(scene === 32) {
            image(selected, 309, 548);
        }
    }
    if(gunTier === 3) {
        image(gunT3, 4, 408);
        image(gunT3, 72, 408);
        if(scene === 32) {
            image(selected, 347, 548);
        }
    }
    if(armorTier === 0) {
        image(holdingRack, 316, 408);
    }
    if(armorTier === 1) {
        image(armorT1, 316, 408);
        if(scene === 32) {
            image(selected, 271, 511);
        }
    }
    if(armorTier === 2) {
        image(armorT2, 316, 408);
        if(scene === 32) {
            image(selected, 309, 511);
        }
    }
    if(armorTier === 3) {
        image(armorT3I, 316, 408);
        if(scene === 32) {
            image(selected, 347, 511);
        }
        if(mouseX >= 316 && mouseX <= 380 && mouseY >= 408 && mouseY <= 472) {
            image(armorT3II, 316, 408);
        }
    }
    if(engineTier === 0) {
        image(holdingRack, 248, 408);
    }
    if(engineTier === 1) {
        image(engineT1, 248, 408);
        if(scene === 32) {
            image(selected, 271, 474);
        }
    }
    if(engineTier === 2) {
        image(engineT2, 248, 408);
        if(scene === 32) {
            image(selected, 309, 474);
        }
    }
    if(engineTier === 3) {
        image(engineT3, 248, 408);
        if(scene === 32) {
            image(selected, 347, 474);
        }
    }
}
var showShipInHangar = function() {
    if(unlockTier >= 1) {
        image(t1Ship, 44, 358);
        image(t2Ship, 44, 312);
        image(t3Ship, 44, 266);
        image(t4Ship, 44, 220);
    }
    if(unlockTier >= 2) {
        image(t5Ship, 44, 157);
        image(t6Ship, 44, 111);
        image(t7Ship, 44, 65);
        image(t8Ship, 44, 19);
    }
    if(unlockTier >= 3) {
        image(t12Ship, 308, 157);
        image(t11Ship, 308, 111);
        image(t10Ship, 308, 65);
        image(t9Ship, 308, 19);
    }
    if(unlockTier >= 4) {
        image(tS4Ship, 308, 358);
        image(tS3Ship, 308, 312);
        image(tS2Ship, 308, 266);
        image(tS1Ship, 308, 220);
    }
    
    // God Mode
    if(admin === true) {
        image(tS3Ship, 176, 290);
    }
};
var shipUnlock = function() { // Higher score unlocks better ships
    if (highscore < 500) {
        unlockTier = 1;
        image(t1Ship, 44, 358);
        image(t2Ship, 44, 312);
        image(t3Ship, 44, 266);
        image(t4Ship, 44, 220);
        image(locked, 119, 511);
        image(locked, 157, 511);
        image(locked, 195, 511);
        image(locked, 233, 511);
        image(locked, 271, 511);
        image(locked, 309, 511);
        image(locked, 347, 511);
        image(locked, 119, 548);
        image(locked, 157, 548);
        image(locked, 195, 548);
        image(locked, 233, 548);
        image(locked, 271, 548);
        image(locked, 309, 548);
        image(locked, 347, 548);
    }
    else if (highscore >= 500 && highscore < 8000) {
        unlockTier = 2;
        image(locked, 271, 511);
        image(locked, 309, 511);
        image(locked, 347, 511);
        image(locked, 119, 548);
        image(locked, 157, 548);
        image(locked, 195, 548);
        image(locked, 233, 548);
        image(locked, 271, 548);
        image(locked, 309, 548);
        image(locked, 347, 548);
    }
    else if (highscore >= 8000 && highscore < 10000) {
        unlockTier = 3;
        image(locked, 157, 548);
        image(locked, 195, 548);
        image(locked, 233, 548);
        image(locked, 271, 548);
        image(locked, 309, 548);
        image(locked, 347, 548);
    }
    else if (highscore >= 10000 && highscore < 20000) {
        unlockTier = 4;
        image(locked, 309, 548);
        image(locked, 347, 548);
    }
    else if (highscore >= 20000) {
        unlockTier = 5;
    }
};
var allShips = function() { // Show ship pictures
    image(t1Ship, 119, 474);
    image(t2Ship, 157, 474);
    image(t3Ship, 309, 474);
    image(t4Ship, 347, 474);
    image(t5Ship, 119, 511);
    image(t6Ship, 157, 511);
    image(t7Ship, 195, 511);
    image(t8Ship, 233, 511);
    image(t9Ship, 271, 511);
    image(t10Ship, 309, 511);
    image(t11Ship, 347, 511);
    image(t12Ship, 119, 548);
    image(tS1Ship, 157, 548);
    image(tS2Ship, 195, 548);
    image(tS3Ship, 233, 548);
    image(tS4Ship, 271, 548);
    image(tSW2Ship, 309, 548);
    image(tSW1Ship, 347, 548);
};
var allUpgrades = function() { // Show upgrades for ship
    image(speedI, 271, 474);
    image(speedII, 309, 474);
    image(speedIII, 347, 474);
    image(armorI, 271, 511);
    image(armorII, 309, 511);
    image(armorIII, 347, 511);
    image(damageI, 271, 548);
    image(damageII, 309, 548);
    image(damageIII, 347, 548);
};
var showShips = function() { // Show ship on launch pad
        var launchX = 176;
        var launchY = 408;
        if(ship === 1) {
            image(t1Ship, launchX, launchY);
            if(scene === 31) {
                image(selected, 119, 474);
            }
        }
        if(ship === 2) {
            image(t2Ship, launchX, launchY);
            if(scene === 31) {
                image(selected, 157, 474);
            }
        }
        if(ship === 3) {
            image(t3Ship, launchX, launchY);
            if(scene === 31) {
                image(selected, 309, 474);
            }
        }
        if(ship === 4) {
            image(t4Ship, launchX, launchY);
            if(scene === 31) {
                image(selected, 347, 474);
            }
        }
        if(ship === 5) {
            image(t5Ship, launchX, launchY);
            if(scene === 31) {
                image(selected, 119, 511);
            }
        }
        if(ship === 6) {
            image(t6Ship, launchX, launchY);
            if(scene === 31) {
                image(selected, 157, 511);
            }
        }
        if(ship === 7) {
            image(t7Ship, launchX, launchY);
            if(scene === 31) {
                image(selected, 195, 511);
            }
        }
        if(ship === 8) {
            image(t8Ship, launchX, launchY);
            if(scene === 31) {
                image(selected, 233, 511);
            }
        }
        if(ship === 9) {
            image(t9Ship, launchX, launchY);
            if(scene === 31) {
                image(selected, 271, 511);
            }
        }
        if(ship === 10) {
            image(t10Ship, launchX, launchY);
            if(scene === 31) {
                image(selected, 309, 511);
            }
        }
        if(ship === 11) {
            image(t11Ship, launchX, launchY);
            if(scene === 31) {
                image(selected, 347, 511);
            }
        }
        if(ship === 12) {
            image(t12Ship, launchX, launchY);
            if(scene === 31) {
                image(selected, 119, 548);
            }
        }
        if(ship === 13) {
            image(tS1Ship, launchX, launchY);
            if(scene === 31) {
                image(selected, 157, 548);
            }
        }
        if(ship === 14) {
            image(tS2Ship, launchX, launchY);
            if(scene === 31) {
                image(selected, 195, 548);
            }
        }
        if(ship === 15) {
            image(tS3Ship, launchX, launchY);
            if(scene === 31) {
                image(selected, 233, 548);
            }
        }
        if(ship === 16) {
            image(tS4Ship, launchX, launchY);
            if(scene === 31) {
                image(selected, 271, 548);
            }
        }
        if(ship === 17) {
            image(tSW2Ship, launchX, launchY);
            if(scene === 31) {
                image(selected, 309, 548);
            }
        }
        if(ship === 18) {
            image(tSW1Ship, launchX, launchY);
            if(scene === 31) {
                image(selected, 347, 548);
            }
        }
        if(ship === 9999) {
            image(tS3Ship, launchX, launchY);
        }
};
var upgradesSelect = function() {
    if(highscore < 2000) {
        upgradeTier = 0;
        image(locked, 271, 474);
        image(locked, 309, 474);
        image(locked, 347, 474);
        image(locked, 271, 511);
        image(locked, 309, 511);
        image(locked, 347, 511);
        image(locked, 271, 548);
        image(locked, 309, 548);
        image(locked, 347, 548);
    }
    if(highscore >= 2000 && highscore < 5000) {
        upgradeTier = 1;
        image(locked, 309, 474);
        image(locked, 347, 474);
        image(locked, 309, 511);
        image(locked, 347, 511);
        image(locked, 309, 548);
        image(locked, 347, 548);
    }
    if(highscore >= 5000 && highscore < 8000) {
        upgradeTier = 2;
        image(locked, 347, 474);
        image(locked, 347, 511);
        image(locked, 347, 548);
    }
    if(highscore >= 8000) {
        upgradeTier = 3;
    }
};
var customization = function() { // Draw hanger scene buttons
    //Hangar Buttons
    image(hangar, 0, 0);
    image(shipsL, 9, 479);
    image(armoryL, 9, 514);
    image(menuL, 9, 549);
    showShips();
    showShipInHangar();
    showUpgrades();
    
    // Highlight buttons when mouse in area
    if(mouseX >= 9 && mouseX <= 101 && mouseY >= 479 && mouseY <= 505) {
        image(shipsD, 9, 479);
    }
    if(mouseX >= 9 && mouseX <= 101 && mouseY >= 514 && mouseY <= 540) {
        image(armoryD, 9, 514);
    }
    if(mouseX >= 9 && mouseX <= 101 && mouseY >= 549 && mouseY <= 575) {
        image(menuD, 9, 549);
    }
};
var shipSelectMenu = function() { // Draw ship selection scene
    // Hangar Buttons
    image(hangar, 0, 0);
    image(shipsL, 9, 479);
    image(shipSelect, 114, 470);
    image(backL, 9, 514);
    allShips();
    shipUnlock();
    showShips();
    showShipInHangar();
    showUpgrades();
    
    // Highlight buttons when mouse in area
    if(mouseX >= 9 && mouseX <= 101 && mouseY >= 479 && mouseY <= 505) {
        image(shipsD, 9, 479);
    }
    if(mouseX >= 9 && mouseX <= 101 && mouseY >= 514 && mouseY <= 540) {
        image(backD, 9, 514);
    }
};
var upgradesMenu = function() { // Draw ship upgrades scene
    //Hangar Buttons
    var armor3 = 0;
    image(hangar, 0, 0);
    image(armoryL, 9, 479);
    image(armory, 114, 470);
    image(backL, 9, 514); 
    allUpgrades();
    showShips();
    showShipInHangar();
    upgradesSelect();
    showUpgrades();
    
    // Highlight buttons when mouse in area
    if(mouseX >= 9 && mouseX <= 101 && mouseY >= 479 && mouseY <= 505) {
        image(armoryD, 9, 479);
    }
    if(mouseX >= 9 && mouseX <= 101 && mouseY >= 514 && mouseY <= 540) {
        image(backD, 9, 514);
    }
    if(mouseX >= 347 && mouseX <= 369 && mouseY >= 511 && mouseY <= 543) {
        if(upgradeTier >= 3) {
            image(armorIII2, 347, 511);
        }
    }
};

// Instruction Scene
var instructions1 = function() { // Instructions part 1
    // Background
    image(menuBackground, 0, 0);
    
    // Text
    fill(255, 255, 255);
    textAlign(LEFT);
    textFont(myFont);
    textSize(23);
    text("[W] to move forward" + "\n" + "\n" + "[S] to move backwards" + "\n" + "\n" + "[A] to move left" + "\n" + "\n" + "[D] to move right" + "\n" + "\n" + "[SPACE] to shoot lasers" + "\n" + "\n" + "\n" + "\n" + "[L SHIFT] to activate Aegis mode", 20, 50, 355);
    textSize(18);
    text("(Shooting depletes the amount of laser left. The less laser left, the longer it will regenerate)", 20, 305, 350);
    text("(Faster firerate, regeneration of health, increased movement speed, and increased armor for a limited time)", 20, 420, 350);
    
    // next instructions
    image(helpL, 250, 525);
    
    if (mouseX >= 250 && mouseX <= 342 && mouseY >= 525 && mouseY <= 551) {
        image(helpD, 250, 525);
    }
    
};
var instructions2 = function() { // Instructions part 2
    // Background
    image(menuBackground, 0, 0);
    
    // Text
    textAlign(LEFT);
    textFont(myFont);
    textSize(20);
    
    // Health
    fill(255, 0, 0);
    rect(0, 50, 130, 40);
    fill(255, 255, 255);
    text("Your health", 10, 120);
    
    // Laser
    fill(0, 255, 255);
    rect(135, 20, 30, 65);
    rect(220, 20, 30, 65);
    fill(255, 255, 255);
    rect(145, 110, 5, 40);
    triangle(140, 110, 147.5, 100, 155, 110)
    text("Amount of laser left", 100, 170, 120);
    
    // Score
    fill(255, 255, 255);
    text("Score", 165, 120);
    
    // Amount of powerup before aegis mode completed
    text("Amount of powerup", 250, 120, 150);
    textSize(18);
    text("(Aegis Mode)", 250, 175);
    
    // GUI
    image(playerGUI, 0, 20);
    
    // Other text
    textSize(23);
    text("Move your ship to dodge enemies' lasers and mines to stay alive", 20, 250, 350);
    text("Destroy enemies to get score and charge your powerup", 20, 350, 350);
    text("Getting a certain amount of score will unlock upgrades and better ships", 20, 420, 350);
    
    // instructions part 3
    image(helpL, 42, 525);
    
    if (mouseX >= 42 && mouseX <= 134 && mouseY >= 525 && mouseY <= 551) {
        image(helpD, 42, 525);
    }
};
var instructions3 = function() { // instructions part 3
    // Background
    image(menuBackground, 0, 0);
    
    // text
    textSize(20);
    text("Go to Hanger to upgrade your ship or choose better ships", 20, 50, 350);
    text("Hull armor in Armory (In Hanger), improves your armor so you can take more damage", 20, 115, 350);
    text("Ship Engine in Armory, increases the rate of powerup to get AegisMode faster", 20, 210, 350);
    text("FirePower in Armory, improves your ship laser damage", 20, 305, 350);
    text("Click on the upgrades and ship you want to equip", 20, 375, 350);
    text("Higher the tier, the better", 20, 440, 350);
    text("Your goal is to get the best ships, Tier 5 Ships", 20, 480, 350);
    
    // back to menu
    image(menuL, 250, 525);
    
    if (mouseX >= 250 && mouseX <= 342 && mouseY >= 525 && mouseY <= 551) {
        image(menuD, 250, 525);
    }
};

// Draw Gameplay Scene
var gameplay = function() {
    // Load background and player user interface
    image(map1, 0, 0);
    image(playerGUI, 0, 512);
};

// Mouse Click Check In Menu, Instruction, and Hanger Scenes
var mouseClicked = function() {
    // Menu to play
    if(mouseX >= 145 && mouseX <= 237 && mouseY >= 210 && mouseY <= 236) {
        if (scene === 1) {
            scene = 2;
        }
    }
    
    // Menu to hangar
    if(mouseX >= 145 && mouseX <= 237 && mouseY >= 260 && mouseY <= 286) {
        if (scene === 1) {
            scene = 3;
        }
    }
    
    // Hangar to ship select menu
    if(mouseX >= 9 && mouseX <= 101 && mouseY >= 479 && mouseY <= 505) {
        if(scene === 3) {
            scene = 31;
        }
    }
    
    // Hanger to ship upgrades menu
    if(mouseX >= 9 && mouseX <= 101 && mouseY >= 514 && mouseY <= 540) {
        if(scene === 3) {
            scene = 32;
        } else if(scene === 31) { // (BACK BUTTON) ship select menu to hanger
            scene = 3;
        } else if(scene === 32) { // (BACK BUTTON) ship upgrades menu to hanger
            scene = 3;
        }
    }
    
    // Hanger to menu
    if(mouseX >= 9 && mouseX <= 101 && mouseY >= 549 && mouseY <= 575) {
        if(scene === 3) {
            scene = 1;
        }
    }
    
    // In ship select menu, choose ship, if unlocked by highscore
    if(scene === 31) {
            if(mouseX >= 119 && mouseX <= 151 && mouseY >= 474 && mouseY <= 506) {
                if(unlockTier >= 1) {
                    ship = 1;
                }
            }
            if(mouseX >= 157 && mouseX <= 189 && mouseY >= 474 && mouseY <= 506) {
                if(unlockTier >= 1) {
                    ship = 2;
                }
            }
            if(mouseX >= 309 && mouseX <= 341 && mouseY >= 474 && mouseY <= 506) {
                if(unlockTier >= 1) {
                ship = 3;
                }
            }
            if(mouseX >= 347 && mouseX <= 379 && mouseY >= 474 && mouseY <= 506) {
                if(unlockTier >= 1) {
                    ship = 4;
                }
            }
            if(mouseX >= 119 && mouseX <= 151 && mouseY >= 511 && mouseY <= 543) {
                if(unlockTier >= 2) {
                    ship = 5;
                }
            }
            if(mouseX >= 157 && mouseX <= 189 && mouseY >= 511 && mouseY <= 543) {
                if(unlockTier >= 2) {
                    ship = 6;
                }
            }
            if(mouseX >= 195 && mouseX <= 227 && mouseY >= 511 && mouseY <= 543) {
                if(unlockTier >= 2) {
                    ship = 7;
                }
            }
            if(mouseX >= 233 && mouseX <= 265 && mouseY >= 511 && mouseY <= 543) {
                if(unlockTier >= 2) {
                    ship = 8;
                }
            }
            if(mouseX >= 271 && mouseX <= 303 && mouseY >= 511 && mouseY <= 543) {
                if(unlockTier >= 3) {
                    ship = 9;
                }
            }
            if(mouseX >= 309 && mouseX <= 341 && mouseY >= 511 && mouseY <= 543) {
                if(unlockTier >= 3) {
                    ship = 10;
                }
            }
            if(mouseX >= 347 && mouseX <= 379 && mouseY >= 511 && mouseY <= 543) {
                if(unlockTier >= 3) {
                    ship = 11;
                }
            }
            if(mouseX >= 119 && mouseX <= 151 && mouseY >= 548 && mouseY <= 580) {
                if(unlockTier >= 3) {
                    ship = 12;
                }
            }
            if(mouseX >= 157 && mouseX <= 189 && mouseY >= 548 && mouseY <= 580) {
                if(unlockTier >= 4) {
                    ship = 13;
                }
            }
            if(mouseX >= 195 && mouseX <= 227 && mouseY >= 548 && mouseY <= 580) {
                if(unlockTier >= 4) { 
                    ship = 14;
                }
            }
            if(mouseX >= 233 && mouseX <= 265 && mouseY >= 548 && mouseY <= 580) {
                if(unlockTier >= 4) {
                    ship = 15;
                }
            }
            if(mouseX >= 271 && mouseX <= 303 && mouseY >= 548 && mouseY <= 580) {
                if(unlockTier >= 4) {
                    ship = 16;
                }
            }
            if(mouseX >= 309 && mouseX <= 341 && mouseY >= 548 && mouseY <= 580) {
                if(unlockTier >= 5) {
                    ship = 17;
                }
            }
            if(mouseX >= 347 && mouseX <= 379 && mouseY >= 548 && mouseY <= 580) {
                if(unlockTier >= 5) {
                    ship = 18;
                }
            }
    }
    
    // In ship upgrades menu, choose upgrades for ship
    if(scene === 32) {
        if(mouseX >= 271 && mouseX <= 303 && mouseY >= 474 && mouseY <= 506) {
            if(upgradeTier >= 1) {
                engineTier = 1;
            }
        }
        if(mouseX >= 309 && mouseX <= 341 && mouseY >= 474 && mouseY <= 506) {
            if(upgradeTier >= 2) {
                engineTier = 2;
            }
        }
        if(mouseX >= 347 && mouseX <= 379 && mouseY >= 474 && mouseY <= 506) {
            if(upgradeTier >= 3) {
                engineTier = 3;
            }
        }
        if(mouseX >= 271 && mouseX <= 303 && mouseY >= 511 && mouseY <= 543) {
            if(upgradeTier >= 1) {
                armorTier = 1;
            }
        }
        if(mouseX >= 309 && mouseX <= 341 && mouseY >= 511 && mouseY <= 543) {
            if(upgradeTier >= 2) {
                armorTier = 2;
            }
        }
        if(mouseX >= 347 && mouseX <= 379 && mouseY >= 511 && mouseY <= 543) {
            if(upgradeTier >= 3) {
                armorTier = 3;
            }
        }
        if(mouseX >= 271 && mouseX <= 303 && mouseY >= 548 && mouseY <= 580) {
            if(upgradeTier >= 1) {
                gunTier = 1;
            }
        }
        if(mouseX >= 309 && mouseX <= 341 && mouseY >= 548 && mouseY <= 580) {
            if(upgradeTier >= 2) {
                gunTier = 2;
            }
        }
        if(mouseX >= 347 && mouseX <= 379 && mouseY >= 548 && mouseY <= 580) {
            if(upgradeTier >= 3) {
                gunTier = 3;
            }
        }
    }
    
    // Menu to Instructions part 1
    if(mouseX >= 145 && mouseX <= 237 && mouseY >= 310 && mouseY <= 336) {
        if(scene === 1) {
             scene = 4;
        }
    }
    
    // Instructions part 1 to instructions part 2
    if(mouseX >= 250 && mouseX <= 342 && mouseY >= 525 && mouseY <= 551) {
        if(scene === 4) {
             scene = 5;
        }
    }
    
    // Instructions part 2 to instructions part 3
    if(mouseX >= 42 && mouseX <= 134 && mouseY >= 525 && mouseY <= 551) {
        if (scene === 5) {
            scene = 6;
        }
    }
    
    // instructions part 3 to menu
    if(mouseX >= 250 && mouseX <= 342 && mouseY >= 525 && mouseY <= 551) {
        if(scene === 6) {
             scene = 1;
        }
    }
    
    // Reset button in gameover scene (gameover to menu)
    if(mouseX >= 145 && mouseX <= 237 && mouseY >= 350 && mouseY <= 376) {    
        if(scene === 9000) {
            scene = 1;
        }
    }
    
    /** Select God Mode Ship **/
    if(scene === 3 || scene === 31 || scene === 32) {
        if(mouseX >= 176 && mouseX <= 208 && mouseY >= 290 && mouseY <= 322) {
            if(admin === true) {
                ship = 9999;
            }
        }
    }
};

// Draw Game Over Scene
var gameover = function() {
    // Show background and reset button
    image(gameoverScene, 0, 0);
    image(resetL, 145, 350);
    
    // Highlight reset button when mouse hovers over
    if (mouseX >= 145 && mouseX <= 237 && mouseY >= 350 && mouseY <= 376) {
        image(resetD, 145, 350);
    }
};



/** PLAYER **/
var delayCounter = 0;
var fireDelay = 20;
var reloadCounter = 0;
var reload = 512;
var powerUpMeter = 0;
var aegisMode = false;
var score = 0;
var ship = 1;
var scores = [];
var highscore = 0;
var powerUpInterval = 2;
var powerDownInterval = 3;

// Player Variable
var player = function(x, y) {
    this.x = x;
    this.y = y;
    this.width = 32;
    this.speed;
    this.health = 130;
    this.armor;
    this.aegis;
    this.model;
};

// Player HUD
player.prototype.playerHud = function() {
    // Score box background
    fill(1, 39, 51);
    rect(165, 550, 50, 30);
    
    // Score in score box
    fill(255);
    textSize(13);
    textFont(myFont);
    text(score, 170, 556, 48, 28);
    
    // Health bar
    if (this.health > 0) {
        // Background of health bar
        fill(1, 39, 51);
        rect(9, 548, 121, 24);
        
        // Health bar
        fill(255, 0, 0);
        rect(0, 548, this.health, 24);
    }
    
    // If player is dead, show gameover scene
    if (this.health <= 0) {
        scene = 9000;
        this.health = 130; // refill health
    }


    // Background of the laser guage
    fill(1, 39, 51);
    rect(135, 513, 30, 100);
    rect(220, 513, 30, 100);
    
    // Amount of laser left in laser guage
    fill(0, 255, 255);
    rect(135, reload, 30, 100);
    rect(220, reload, 30, 100);
    
    // Laser depletion
    // Stops the bar when player can't shoot so reloadCounter can catch up
    if (keyIsDown(32) && reload < 575) { 
        reload += 0.1;
    }
    // Laser recovery
    if (delayCounter > fireDelay + 10 && reload > 512) { // Check if lasers are not firing
    
        // Wait time based on amount of shoot button spam (Percentages are rounded to nearest whole numbers)
        if (reload <= 520) { // If used less than about 12%
            reloadCounter += 50;
        }
        else if (reload <= 539) { // If used more than 12% and less than 43%
            reloadCounter += 40;
        }
        else if (reload <= 550) { // If used more than 43% and less than 60%
            reloadCounter += 30;
        }
        else if (reload <= 560) { // If used more than 60% and less than 76%
            reloadCounter += 20;
        }
        else if (reload > 560) { // If used more than 76%
            reloadCounter += 10;
        }
        
        // If reloadCounter passes a certain time point, refills the laser guage
        if (reloadCounter >= 1000) {
            reload = 512;
            reloadCounter = 0;
        }
    }
    
    
    // Background of powerup bar
    fill(1, 39, 51);
    rect(253, 542, 67, 20);
    
    // Powerup bar guage
    fill(0, 255, 255);
    rect(253, 542, powerUpMeter, 20);
    
    // Max powerup stored
    if (powerUpMeter > 67) {
        powerUpMeter = 67;
    }
    
     // Indicator that powerup is full or not full
    if (powerUpMeter < 67 && aegisMode === false) {
        image(powerUp1, 254, 564);
    }
    else if (aegisMode === true) {
        image(powerUp3, 254, 564);
    } else {
        image(powerUp2, 254, 564);
    }
};

// Update Player Movement and Controls
player.prototype.update = function() {
    // Control the player movement and set boundaries 
    if (keyIsDown(65) && this.x > 6 || keyIsDown(37) && this.x > 6) { // [A]
        this.x -= this.speed;
    }
    if (keyIsDown(68) && this.x < 345 || keyIsDown(39) && this.x < 345) { // [D]
        this.x += this.speed;
    }
    if (keyIsDown(87) && this.y > 9 || keyIsDown(38) && this.y > 9) { // [W]
        this.y -= this.speed;
    }
    if (keyIsDown(83) && this.y < 450 || keyIsDown(40) && this.y < 450) { // [S]
        this.y += this.speed;
    }
    
    // Control the player to activate aegis mode [SHIFT] (17 for ctrl if u want)
    if (keyIsDown(16) && powerUpMeter === 67) {
        aegisMode = true;
    }
    
    // Aegis mode activated
    if (aegisMode === true) {
        powerUpInterval = 0;
        fireDelay = 5; // decreases firedelay (x4 firerate) 
        this.width = 48; // changes width to match new ship image and shooting laser placement
        powerUpMeter -= powerDownInterval; // decreases powerupmeter so player does not have infinite supply
        // also increases speed and armor (seen in player.prototype.draw)
        if (this.health < 130) { // when in power up mode, the player's health regenerates at 0.2 hp per second
            this.health += 0.2;
        }
    }
    
    // // God Mode
    // if (ship === 9999) {
    //     if (this.health != 130) {
    //         this.health = 130;
    //     }
    // }
    
    // Player runs out of powerup
    if (powerUpMeter < 0.1) {
        aegisMode = false;
        fireDelay = 20;
        this.width = 32;
    }
    
    // Control the player to shoot [SPACE]
    if (keyIsDown(32) && delayCounter >= fireDelay && reload < 575) {
        bullets.push( new laser(this.x - 500, this.y, 0) ); // c9 glitch that first bullet pushed is slightly delayed
        bullets.push( new laser(this.x + this.width/4 - 1, this.y + 5, 0) );
        bullets.push( new laser(this.x + this.width - this.width/4 - 1, this.y + 5, 0) );
        if(aegisMode === true) { // aegis mode shoots diagonal bullets
            bullets.push( new laser(this.x + this.width/4 - 5, this.y + 5, -5) );
            bullets.push( new laser(this.x + this.width - this.width/4 - 5, this.y + 5, 5) );
            bullets.push( new laser(this.x + this.width/4 - 5, this.y + 5, -10) );
            bullets.push( new laser(this.x + this.width - this.width/4 - 5, this.y + 5, 10) );
        }
        delayCounter = 0;
    }
    // god mode shoots diagonal bullets
    if (keyIsDown(32) && ship === 9999) {
        bullets.push( new laser(this.x - 500, this.y, 0) ); // c9 glitch that first bullet pushed is slightly delayed
        bullets.push( new laser(this.x + this.width/4 - 0, this.y + 5, 0) );
        bullets.push( new laser(this.x + this.width - this.width/4 - 0, this.y + 5, 0) );
        bullets.push( new laser(this.x + this.width/4 - 0, this.y + 5, -1.5) );
        bullets.push( new laser(this.x + this.width - this.width/4 - 0, this.y + 5, 1.5) );
        bullets.push( new laser(this.x + this.width/4 - 0, this.y + 5, -3) );
        bullets.push( new laser(this.x + this.width - this.width/4 - 0, this.y + 5, 3) );
        bullets.push( new laser(this.x + this.width/4 - 0, this.y + 5, -5) );
        bullets.push( new laser(this.x + this.width - this.width/4 - 0, this.y + 5, 5) );
        bullets.push( new laser(this.x + this.width/4 - 0, this.y + 5, -7) );
        bullets.push( new laser(this.x + this.width - this.width/4 - 0, this.y + 5, 7) );
        bullets.push( new laser(this.x + this.width/4 - 0, this.y + 5, -9) );
        bullets.push( new laser(this.x + this.width - this.width/4 - 0, this.y + 5, 9) );
        bullets.push( new laser(this.x + this.width/4 - 0, this.y + 5, -11) );
        bullets.push( new laser(this.x + this.width - this.width/4 - 0, this.y + 5, 11) );
    delayCounter = 0;
    }
    delayCounter++;
    
    if (engineTier === 0) {
        powerUpInterval = 2;
        powerDownInterval = 0.5;
    }
    if(engineTier === 1) {
        powerUpInterval = 3.5;
        powerDownInterval = 0.3;
    }
    if(engineTier === 2) {
        powerUpInterval = 5;
        powerDownInterval = 0.2;
    }
    if(engineTier === 3) {
        powerUpInterval = 6.5;
        powerDownInterval = 0.1;
    }
};

// Draw Player
player.prototype.draw = function() {
    // Each ship has different model, armor, aegis model, and speed
    if(ship === 1) {
        this.model = t1Ship;
        this.armor = 100;
        this.aegis = t1ShipAegis;
        this.speed = 2.75;
    }   
    if(ship === 2) {
        this.model = t2Ship;
        this.armor = 80;
        this.aegis = t2ShipAegis;
        this.speed = 3.5;
    }
    if(ship === 3) {
        this.model = t3Ship;
        this.armor = 90;
        this.aegis = t3ShipAegis;
        this.speed = 3;
    }  
    if(ship === 4) {
        this.model = t4Ship;
        this.armor = 120;
        this.aegis = t4ShipAegis;
        this.speed = 2.7;
    }
    if(ship === 5) {
        this.model = t5Ship;
        this.armor = 310;
        this.aegis = t5ShipAegis;
        this.speed = 2.85;
    }   
    if(ship === 6) {
        this.model = t6Ship;
        this.armor = 340;
        this.aegis = t6ShipAegis;
        this.speed = 3.7;
    }
    if(ship === 7) {
        this.model = t7Ship;
        this.armor = 300;
        this.aegis = t7ShipAegis;
        this.speed = 3.1;
    }  
    if(ship === 8) {
        this.model = t8Ship;
        this.armor = 330;
        this.aegis = t8ShipAegis;
        this.speed = 2.7;
    }
    if(ship === 9) {
        this.model = t9Ship;
        this.armor = 525;
        this.aegis = t9ShipAegis;
        this.speed = 3.25;
    }   
    if(ship === 10) {
        this.model = t10Ship;
        this.armor = 535;
        this.aegis = t10ShipAegis;
        this.speed = 3;
    }
    if(ship === 11) {
        this.model = t11Ship;
        this.armor = 530;
        this.aegis = t11ShipAegis;
        this.speed = 2.75;
    }  
    if(ship === 12) {
        this.model = t12Ship;
        this.armor = 545;
        this.aegis = t12ShipAegis;
        this.speed = 2.6;
    }
    if(ship === 13) {
        this.model = tS1Ship;
        this.armor = 725;
        this.aegis = tS1ShipAegis;
        this.speed = 3.25;
    }   
    if(ship === 14) {
        this.model = tS2Ship;
        this.armor = 700;
        this.aegis = tS2ShipAegis;
        this.speed = 4;
    }
    if(ship === 15) {
        this.model = tS3Ship;
        this.armor = 725;
        this.aegis = tS3ShipAegis;
        this.speed = 3.75;
    }  
    if(ship === 16) {
        this.model = tS4Ship;
        this.armor = 750;
        this.aegis = tS4ShipAegis;
        this.speed = 3.5;
    }
    if(ship === 17) {
        this.model = tSW2Ship;
        this.armor = 900;
        this.aegis = tSWShipAegis;
        this.speed = 4.5;
    }
    if(ship === 18) {
        this.model = tSW1Ship;
        this.armor = 950;
        this.aegis = tSWShipAegis;
        this.speed = 4.5;
    }
    if(ship === 9999) { // hidden ship god mode (need pass)
        this.model = tS3Ship;
        this.aegis = tS3ShipAegis;
        this.armor = 99999999999;
        this.speed = 8;
    }
    
    // ship upgrades armor 
    if(armorTier === 1) {
        this.armor = this.armor * 1.2;
    }
    if(armorTier === 2) {
        this.armor = this.armor * 1.5;
    }
    if(armorTier === 3) {
        this.armor = this.armor * 2;
    }
    
    // When aegis mode is on, show aegis ship, increase armor and speed
    if (aegisMode === true) {
        image(this.aegis, this.x, this.y);
        this.armor = Math.pow(this.armor, 1.2);
        this.speed = this.speed * 2;
    } else { // otherwise show regular ship model
        image(this.model, this.x, this.y);
    }
};


/** PLAYER LASER **/
var bullets = [];

// Laser Variable
var laser = function(x, y, xSpeed) {
    this.x = x;
    this.y = y;
    this.damage;
    this.speed;
    this.xSpeed = xSpeed;
};

// Update Laser
laser.prototype.update = function() {
    // Moves the laser
    this.y -= this.speed;
    this.x += this.xSpeed;
    
    // Removes laser when out of game
    if (this.y < 0) { 
        for (var i in bullets) { // goes through all the player bullets
            if (bullets[i] === this) { // if it is that specific bullet,
                bullets.splice(i, 1); // remove it
            }
        }
    }
};

// Draw Laser
laser.prototype.draw = function() {
    // Laser's damage, speed, and colour 
    // changes based on ship
    if(ship === 1) {
        fill(0, 255, 0);
        this.damage = 1500;
        this.speed = 10;
    }
    if(ship === 2) {
        fill(0, 255, 0);
        this.damage = 1000;
        this.speed = 10;
    }
    if(ship === 3) {
        fill(0, 255, 0);
        this.damage = 1500;
        this.speed = 10;
    }  
    if(ship === 4) {
        fill(0, 255, 0);
        this.damage = 2000;
        this.speed = 10;
    }
    if(ship === 5) {
        fill(0, 0, 255);
        this.damage = 2500;
        this.speed = 12;
    }
    if(ship === 6) {
        fill(0, 255, 100);
        this.damage = 3000;
        this.speed = 12;
    }
    if(ship === 7) {
        fill(255, 0, 0);
        this.damage = 2500;
        this.speed = 12;
    }  
    if(ship === 8) {
        fill(0, 200, 255);
        this.damage = 3500;
        this.speed = 12;
    }
     if(ship === 9) {
        fill(255, 150, 255);
        this.damage = 3500;
        this.speed = 14;
    }
    if(ship === 10) {
        fill(255, 255, 200);
        this.damage = 4000;
        this.speed = 14;
    }
    if(ship === 11) {
        fill(255, 255, 255);
        this.damage = 3500;
        this.speed = 14;
    }  
    if(ship === 12) {
        fill(200, 100, 255);
        this.damage = 4500;
        this.speed = 14;
    }
    if(ship === 13) {
        fill(255, 255, 100);
        this.damage = 5500;
        this.speed = 16;
    }  
    if(ship === 14) {
        fill(255, 100, 100);
        this.damage = 5000;
        this.speed = 16;
    }
    if(ship === 15) {
        fill(100, 100, 255);
        this.damage = 5500;
        this.speed = 16;
    }
    if(ship === 16) {
        fill(255, 255, 255);
        this.damage = 6000;
        this.speed = 16;
    }
    if(ship === 17) {
        fill(0, 255, 0);
        this.damage = 8000;
        this.speed = 18;
    }  
    if(ship === 18) {
        fill(0, 255, 0);
        this.damage = 10000;
        this.speed = 18;
    }
    
    // Hidden ship
    if(ship === 9999) {
        fill(250, 250, 250);
        this.damage = 99999999;
        this.speed = 22;
    }
    
    // ship upgrades (Firepower in armory which is in hanger) improves laser damage
    if(gunTier === 1) {
        this.damage = this.damage * 1.2;
    }
    if(gunTier === 2) {
        this.damage = this.damage * 1.5;
    }
    if(gunTier === 3) {
        this.damage = this.damage * 2;
    }
    
    // Laser is a rectangle
    rect(this.x, this.y, 2, 10);
};


/** ENTITY - ASTEROID **/
var asteroids = [];

// Entity Asteroid Variable
var asteroidEntity = function(x, y) {
    this.x = x;
    this.y = y;
    this.width = 32;
    this.speed = -8;
    this.health = 32;
};

// Asteroid Movement
asteroidEntity.prototype.update = function() {
    // Asteroid movement
    this.y -= this.speed;
    
    // If it goes out of game
    if (this.y > 475) {
        this.y = Math.random() * -5000 - 1500; // spawns in random location
        this.x = Math.floor( Math.random()* 300 + 50);
        this.health = 32; // refills health
    }
};

// Draw Asteroid Entity
asteroidEntity.prototype.draw = function() {
    // Show image of asteroid
    image(asteroid1, this.x, this.y);
    
    // Draw health bar of asteroid
    if (this.health > 0) {
        // Background of health bar of asteroid
        fill(183, 28, 28);
        rect(this.x, this.y - 3, 32, 3);
    
        // Health bar of asteroid
        fill(0, 255, 0);
        rect(this.x, this.y - 3, this.health, 3);
    }
};

// Check for Asteroid Collision With Player (Asteroid hit ship)
player.prototype.collideAsteroid = function(a) {
    if (this.x >= a.x - this.width && this.x <= a.x + this.width && 
        this.y >= a.y - this.width && this.y <= a.y + this.width) {
        
        // Ship colliding with fast moving asteroid does 1/4 of max health
        this.health -= 130 / 4;  
        
        // Asteroid respawns
        a.x = Math.floor( Math.random()* 300 + 50);
        a.y = Math.random() * -5000 - 1500;
        a.health = 32;
    }
};

// Update Asteroid and Player Collisions
player.prototype.asteroidCollisionUpdate = function() {
    for (var i in asteroids) { // goes through the asteroids array
        this.collideAsteroid(asteroids[i]); // puts the asteroids from the array into the above prototype 
    }
};

// Check for Player's Laser Collisions with Asteroids
laser.prototype.collideAsteroid = function(a) {
    if (this.x >= a.x && this.x <= a.x + a.width && 
        this.y >= a.y - a.width && this.y <= a.y + a.width) {
            
        // When collided, removes bullets too
        for (var i in bullets) { 
            if (bullets[i] === this) {
                bullets.splice(i, 1);
            }
        }
        
        // Laser does damage to asteroid
        a.health -= this.damage;
        
        // If asteroid is destroyed, ...
        if (a.health <= 0) {
            powerUpMeter += powerUpInterval;
            score += 10;
            explosions(a.x, a.y);

            a.x = Math.floor( Math.random()* 300 + 50);
            a.y = Math.random() * -5000 - 1500;
            a.health = 32;
        }
    }
};

// Update Player's Laser and Asteroid Collisions
laser.prototype.asteroidCollisionUpdate = function() {
    for (var i in asteroids) { // goes through asteroids array
        this.collideAsteroid(asteroids[i]); // puts the asteroids from the array into the above prototype
    }
};


/** ENTITY #1 - HEAVY ATTACKER **/
var enemies1 = [];
var e1Bullets = [];

// Entity Enemy1 Variable
var enemyEntity1 = function(x, y) {
    this.x = x;
    this.y = y;
    this.width = 64;
    this.ySpeed = 0.2;
    this.xSpeed = 1.25;
    this.health = 64;
    this.armour = 1500;
    this.counter = 0;
    this.delay = 150;
};

// Entity Enemy1 Laser Variable
var enemyEntity1Laser = function(x, y) { 
    this.x = x;
    this.y = y;
    this.width = 32;
    this.damage = 2000;
    this.speed = 2.5;
};

// Update Enemy1 Laser
enemyEntity1Laser.prototype.update = function() {
    // Moves the laser
    this.y += this.speed;
    
    // Removes laser when out of game
    if (this.y > 490) {
        for (var i in e1Bullets) {
            if (e1Bullets[i] === this) {
                e1Bullets.splice(i, 1);
            }
        }
    }
};

// Draw Enemy1 Laser
enemyEntity1Laser.prototype.draw = function() {
    fill(255, 0, 0);
    rect(this.x, this.y, 2, 20);
};

// Update Enemy1 Ship
enemyEntity1.prototype.update = function() {
    // Frequency of shots
    if (this.counter >= this.delay) {
        e1Bullets.push( new enemyEntity1Laser(this.x - 500, this.y) ); //c9 glitch that the first bullet pushed is slightly delayed sometimes
        e1Bullets.push( new enemyEntity1Laser(this.x + 18, this.y + 30) );
        e1Bullets.push( new enemyEntity1Laser(this.x + 41, this.y + 30) );
        this.counter = 0;
    }
    this.counter++;
};

// Draw Enemy1 Ship
enemyEntity1.prototype.draw = function() {
    // Show image of enemy1
    image(enemyA1, this.x, this.y);
    
    // Draw health bar of enemy 1
    if (this.health > 0) {
        fill(183, 28, 28);
        rect(this.x, this.y - 3, 64, 3);
    
        fill(0, 255, 0);
        rect(this.x, this.y - 3, this.health, 3);
    }
};

// Check Enemy1 Follow Player (Enemy1 Movement)
player.prototype.followEnemy1 = function(e1) {
    // see if player is left or right of the enemy
    var direction = this.x - e1.x - 16;
    var distance = Math.sqrt(direction * direction + 1);
    direction = direction / distance;
    
    // moves enemy the same x axis of player
    e1.x += direction * e1.xSpeed;
    
    if (e1.y < 50) { // stops moving past 50pixels
        e1.y += e1.ySpeed;
    }
};

// Check Enemy1 Collision With Player (Ship hit ship)
player.prototype.collideEnemy1 = function(e1) {
    // if player hits enemy1
    if (this.x >= e1.x - this.width + 10 && this.x <= e1.x + e1.width - 10 && 
        this.y >= e1.y - this.width + 15 && this.y <= e1.y + e1.width - 25 ||
        this.x >= e1.x - this.width + 20 && this.x <= e1.x + e1.width - 20 &&
        this.y >= e1.y - this.width + 15 && this.y <= e1.y + e1.width - 2) {
        
        // Damages player    
        this.health -= 130 / 10;
        
        // Enemy pushes player
        if (this.y > 470 && this.x > 176) { // if on the left side, push left
            this.x -= 20;
        }
        if (this.y > 470 && this.x < 176) { // if on the right side, push right
            this.x += 20;
        } 
        else {
            this.y += 20; // otherwise pushes down
        }
    }
};

// Check Enemy1's Laser Collision With Player (Laser hit ship)
player.prototype.collideLaserEnemy1 = function(e1Laser) {
    // if enemy1 laser hit player
    if (e1Laser.x >= this.x && e1Laser.x <= this.x + this.width &&
        e1Laser.y >= this.y && e1Laser.y <= this.y + this.width) { 
        
        // Player takes damage    
        this.health -= e1Laser.damage / this.armor;

        // When collided, removes bullets too
        for (var i in e1Bullets) { // goes through all of enemy1 bullets
            if (e1Bullets[i] === e1Laser) { // if it is that specific bullet that hit player
                e1Bullets.splice(i, 1); // removes it
            }
        }        
    }
};

// Update all Enemy1 and Player prototypes
player.prototype.enemy1CollisionUpdate = function() {
    // Enemy1 follows player
    for (var i in enemies1) {
        this.followEnemy1(enemies1[i]); // puts enemies1 array into enemy1 follow player prototype
    }
    
    // Enemy1 hit player
    for (var i in enemies1) {
        this.collideEnemy1(enemies1[i]); // puts enemies 1 array into enemy1 hit player prototype
    }
    
    // Enemy1 laser hit player
    for (var i in e1Bullets) {
        this.collideLaserEnemy1(e1Bullets[i]); // put enemies1 bullets array into enemy1 laser hit player prototype
    }
};

// Check Player's Laser Collision With Enemy1
laser.prototype.collideEnemy1 = function(e1) {
    // enemy1's hitbox split into 2 (the back and the head) for more accurate damage
    if (this.x >= e1.x && this.x <= e1.x + e1.width && 
        this.y >= e1.y && this.y <= e1.y + e1.width - 25 ||
        this.x >= e1.x + 10 && this.x <= e1.x + e1.width - 20 &&
        this.y >= e1.y && this.y <= e1.y + e1.width - 10) {
            
        // When collided, removes bullets too
        for (var i in bullets) { 
            if (bullets[i] === this) {
                bullets.splice(i, 1);
            }
        }
        
        // Laser does damage to enemy
        e1.health -= this.damage / e1.armour;
        
        // If enemy1 is destroyed, ...
        if (e1.health <= 0) {
            powerUpMeter += powerUpInterval;
            score += 100;
            explosions(e1.x, e1.y);
            
            for (var i in enemies1) {
                if (enemies1[i] === e1) {
                    enemies1.splice(i, 1);
                }
            }
        }
    }
};

// Update Player's Laser and Enemy1 Collision
laser.prototype.enemy1CollisionUpdate = function() {
    for (var i in enemies1) {
        this.collideEnemy1(enemies1[i]);// puts enemies1 into the above prototype
    }
};

/** ENTITY #2 - MEDIUM STRIKER **/ 
var enemies2 = [];
var e2Bullets = [];
var e2Mine = [];
var e2MineCount = 0;
var e2MineMax = 3;

// Entity Enemy2 Variable
var enemyEntity2 = function(x, y) {
    this.x = x;
    this.y = y;
    this.width = 32;
    this.speed = 1;
    this.health = 32;
    this.armour = 100;
    this.counter = 0;
    this.delay = 100;
};

// Entity Enemy2 Laser Variable
var enemyEntity2Laser = function(x, y) {
    this.x = x;
    this.y = y;
    this.damage = 500;
    this.speed = 2.5;
};

// Update Enemy2 Laser Movement
enemyEntity2Laser.prototype.update = function() {
    // Moves the laser
    this.y += this.speed;
    
    // Removes laser when out of game
    if (this.y > 490) {
        for (var i in e2Bullets) {
            if (e2Bullets[i] === this) {
                e2Bullets.splice(i, 1);
            }
        }
    }
};

// Draw Enemy2 Laser
enemyEntity2Laser.prototype.draw = function() {
    fill(255, 235, 59);
    rect(this.x, this.y, 2, 10);
};

// Entity Enemy2 Mine Variable
var enemyEntity2Mine = function(x, y) {
    this.x = x;
    this.y = y;
    this.width = 32;
    this.damage = 50;
    this.timer = 0;
};

// Draw Enemy2 Mine
enemyEntity2Mine.prototype.draw = function() {
    fill(255);
    image(mine, this.x - 15, this.y);
};

// Update Enemy2 Ship (Shoot lasers and drop mines and movement)
enemyEntity2.prototype.update = function() {
    // Shoot lasers
    if (this.y > 150 && this.counter >= this.delay) {
        e2Bullets.push( new enemyEntity2Laser(this.x - 500, this.y) ); //c9 glitch that the first bullet is slightly delayed
        e2Bullets.push( new enemyEntity2Laser(this.x + 6, this.y + 15) );
        e2Bullets.push( new enemyEntity2Laser(this.x + 24, this.y + 15) );
        this.counter = 0;
    }
    this.counter++; // counter counts
     
    // Drop Mines if in area and less than max number of mine
    if (this.y > 250 && this.y < 450 && e2MineCount < e2MineMax) {
        if ( Math.floor( Math.random() * 600) + 1 === 1 ) { // 1 in 600 chance
            e2MineCount++;
            e2Mine.push( new enemyEntity2Mine(this.x + 12, this.y) ); //pushes mine out
        }
    }
    
    // Movement
    this.y += this.speed;
    
    // If it goes out of the game, remove it 
    if (this.y > 465) {
        for (var i in enemies2) { // goes through all enemies2 in the array
            if (enemies2[i] === this) { // if it is that certain one
                enemies2.splice(i, 1); // remove it
            }
        }     
    }
};

// Draw Enemy2 Ship
enemyEntity2.prototype.draw = function() {
    // Show image of enemy2
    image(enemyA2, this.x, this.y);
    
    // Draw health bar of enemy2
    if (this.health > 0) {
        // background of health bar
        fill(183, 28, 28);
        rect(this.x, this.y - 3, 32, 3);
        
        // actual health bar
        fill(0, 255, 0);
        rect(this.x, this.y - 3, this.health, 3);
    }
};

// Check Enemy2 Collision With Player (Ship hit ship)
player.prototype.collideEnemy2 = function(e2) {
    // if player hits enemy 2
    if (this.x >= e2.x - this.width + 10 && this.x <= e2.x + e2.width - 10 && 
        this.y >= e2.y - this.width + 15 && this.y <= e2.y + e2.width - 25 ||
        this.x >= e2.x - this.width + 20 && this.x <= e2.x + e2.width - 20 &&
        this.y >= e2.y - this.width + 15 && this.y <= e2.y + e2.width - 2) {
        
        // Damages player    
        this.health -= 130 / 10;
        
        // Enemy is destroyed by collision and respawns
        for (var i in enemies2) { 
            if (enemies2[i] === e2) {
                enemies2.splice(i, 1);
            }
        }
    }
};

// Check Enemy2's Laser Collision With Player (Laser hit ship)
player.prototype.collideLaserEnemy2 = function(e2Laser) {
    // if enemy2 laser hit player
    if (e2Laser.x >= this.x && e2Laser.x <= this.x + this.width &&
        e2Laser.y >= this.y && e2Laser.y <= this.y + this.width) {
        
        // Damages player    
        this.health -= e2Laser.damage / this.armor;

        // When collided, removes bullets too
        for (var i in e2Bullets) {
            if (e2Bullets[i] === e2Laser) {
                e2Bullets.splice(i, 1);
            }
        }        
    }
};

// Update all Enemy2 and Player prototypes
player.prototype.enemy2CollisionUpdate = function() {
    // Enemy2 ship hit player
    for (var i in enemies2) {
        this.collideEnemy2(enemies2[i]); // puts enemies2 array in the prototypes
    }
    
    // Enemy2 laser hit player
    for (var i in e2Bullets) {
        this.collideLaserEnemy2(e2Bullets[i]); // puts enemies2 bullets array in the prortyueps
    }
};

// Check Player's Laser Collision With Enemy2
laser.prototype.collideEnemy2 = function(e2) {
    // if player'slaser hit enemy2
    if (this.x >= e2.x && this.x <= e2.x + e2.width &&
        this.y >= e2.y && this.y <= e2.y + e2.width) {

        // When collided, removes bullets too
        for (var i in bullets) { 
            if (bullets[i] === this) {
                bullets.splice(i, 1);
            }
        }
        
        // Laser does damage to enemy
        e2.health -= this.damage / e2.armour;
        
        // If enemy2 is destroyed, ...
        if (e2.health <= 0) {
            powerUpMeter += powerUpInterval;
            score += 10;
            explosions(e2.x, e2.y);
            
            for (var i in enemies2) { // goes through all enemies2
                if (enemies2[i] === e2) { // if it is the one that got hit
                    enemies2.splice(i, 1); // remove it
            }
        }
        }
    }
};

// Update Player's Laser and Enemy2 Collision
laser.prototype.enemy2CollisionUpdate = function() {
    for (var i in enemies2) {
        this.collideEnemy2(enemies2[i]); // puts enemies2 array in the above prototype
    }
};

// Check Enemy2's Mine Collision With Player
player.prototype.collideMineEnemy2 = function(mine) {     
    // Ship hits mine
    if (this.x >= mine.x - 48 && this.x <= mine.x + 16 &&
        this.y >= mine.y - 32 && this.y <= mine.y + 16) {
        
        // For that specific mine
        for (var i in e2Mine) {
            if (e2Mine[i] === mine) {
                // Removes it
                mine.timer = 0;
                e2MineCount--;
                e2Mine.splice(i, 1);
                
                // damages player
                this.health -= mine.damage;
                
                // shows explosion
                explosions(mine.x - 145, mine.y - 140);
                
            }
        } 
    }
    
    // When mine timer reaches a certain point, that specific mine does...
    for (var i in e2Mine) {
        if (e2Mine[i] === mine && mine.timer > 500) { 
            
            // shows explosion
            image(explosion4, mine.x - 145, mine.y - 140, 320, 320);
            
            // Use equation of ellipse to see if player is in explosion radius 
            // (x-h)^2 / (x's radius)^2 + (y-h)^2 / (y's radius)^2
            if (Math.pow(this.x - mine.x + 16, 2) / 8256 + 
                Math.pow(this.y - mine.y + 8, 2) / 8324 <= 1) {
                    
                this.health -= mine.damage; // damages player
            }
            
            // removes the mine 
            mine.timer = 0;
            e2MineCount--;
            e2Mine.splice(i, 1); 
        }
    }
    mine.timer++;
};

// Update Enemy2's Mine and Player Collision
player.prototype.enemy2MineCollisionUpdate = function() {
    for (var i in e2Mine) {
        this.collideMineEnemy2(e2Mine[i]); // puts mine array in the above prototype
    }
};

// Check Player's Laser Collision With Enemy2's Mine
laser.prototype.collideMineEnemy2 = function(mine) {
    if ( Math.pow(this.x - mine.x, 2) + Math.pow(this.y - mine.y, 2) <= Math.pow(mine.width/2, 2) ) {
        for (var i in bullets) { 
            if (bullets[i] === this) {
                bullets.splice(i, 1);
            }
        }
    }
};

// Update Player's Laser Collision With Enemy2's Mine
laser.prototype.enemy2MineCollisionUpdate = function() {
    for (var i in e2Mine) {
        this.collideMineEnemy2(e2Mine[i]); // puts mine array in the above prottype
    }
};

/** ENTITY #3 - GROUP ATTACKER **/
var enemies3 = [];
var e3Bullets = [];

// Entity Enemy3 Variable
var enemyEntity3 = function(x, y) {
    this.x = x;
    this.y = y;
    this.width = 32;
    this.speed = 0.75;
    this.health = 32;
    this.armour = 650;
    this.counter = 0;
    this.delay = 80;
};

// Entity Enemy3 Laser Variable
var enemyEntity3Laser = function(x, y) {
    this.x = x;
    this.y = y;
    this.width2 = 4;
    this.damage = 500;
    this.speed = 2;
};

// Update Enemy3 Laser
enemyEntity3Laser.prototype.update = function() {
    // Moves the laser
    this.y += this.speed;
    
    // Removes laser when out of game
    if (this.y > 490) {
        for (var i in e3Bullets) {
            if (e3Bullets[i] === this) {
                e3Bullets.splice(i, 1);
            }
        }
    }
};

// Draw Enemy3 Laser
enemyEntity3Laser.prototype.draw = function() {
    fill(255, 0, 0);
    rect(this.x, this.y, 2, 10);
};

// Update Enemy3 Ship
enemyEntity3.prototype.update = function() {
    // Frequency of shots
    if (this.y > 50 && this.counter >= this.delay) {
        e3Bullets.push( new enemyEntity3Laser(this.x - 500, this.y) ); ///c9 glitch that the first bullet is slightly delayed
        e3Bullets.push( new enemyEntity3Laser(this.x + 5, this.y + 5) );
        e3Bullets.push( new enemyEntity3Laser(this.x + 25, this.y + 5) );
        this.counter = 0;
    }
    this.counter++;
    
    // Movement
    this.y += this.speed;
    if (this.y > 325) { // If enemies past certain point, exit the game
        if (this.x < 192) { 
            this.x -= this.speed + 5; // If enemies are on the left side of the game, go left
        } else {
            this.x += this.speed + 5; // If enemies are on the right side of the game, go right
        }
    }
    
    // If enemies are out of the game
    if (this.x < -100 || this.x > 484) {
        for (var i in enemies3) {
            if (enemies3[i] === this) { // remove them from the array
                enemies3.splice(i, 1);
            }
        }
    }
    
};

// Draw Enemy3 Ship
enemyEntity3.prototype.draw = function() {
    // Show image
    image(enemyA3, this.x, this.y);

    
    // Draw health bar 
    if (this.health > 0) {
        fill(183, 28, 28);
        rect(this.x, this.y - 5, 32, 3);
    
        fill(0, 255, 0);
        rect(this.x, this.y - 5, this.health, 3);
    }
};

// Check Enemy3 Collision With Player (Ship hit ship)
player.prototype.collideEnemy3 = function(e3) {
    if (this.x >= e3.x - e3.width + 10 && this.x <= e3.x + e3.width - 10 && 
        this.y >= e3.y - e3.width && this.y <= e3.y + e3.width) {
        
        // Damages player    
        this.health -= 130 / 20;
        
        for (var i in enemies3) {
            if (enemies3[i] === e3) {
                enemies3.splice(i, 1);
            }
        }
    }
};

// Check Enemy3's Laser Collision With Player (Laser hit ship)
player.prototype.collideLaserEnemy3 = function(e3Laser) {
    if (e3Laser.x >= this.x && e3Laser.x <= this.x + this.width &&
        e3Laser.y >= this.y && e3Laser.y <= this.y + this.width) { 
        
        // Player takes damage    
        this.health -= e3Laser.damage / this.armor;
        
        // When collided, removes bullets too
        for (var i in e3Bullets) { 
            if (e3Bullets[i] === e3Laser) {
                e3Bullets.splice(i, 1);
            }
        }        
    }
};

// Update all Enemy3 and Player Collisions
player.prototype.enemy3CollisionUpdate = function() {
    // Enemy3 hit player
    for (var i in enemies3) {
        this.collideEnemy3(enemies3[i]);
    }
    
    // Enemy3 laser hit player
    for (var i in e3Bullets) {
        this.collideLaserEnemy3(e3Bullets[i]);
    }
};

// Check Player's Laser Collision With Enemy1
laser.prototype.collideEnemy3 = function(e3) {
    if (this.x >= e3.x && this.x <= e3.x + e3.width && 
        this.y >= e3.y && this.y <= e3.y + e3.width) {
            
        // When collided, removes bullets too
        for (var i in bullets) { 
            if (bullets[i] === this) {
                bullets.splice(i, 1);
            }
        }
        
        // Laser does damage to enemy
        e3.health -= this.damage / e3.armour;
        
        // If enemy3 is destroyed, ...
        if (e3.health <= 0) {
            powerUpMeter += powerUpInterval;
            score += 25;
            explosions(e3.x, e3.y);
            
            for (var i in enemies3) {
                if (enemies3[i] === e3) {
                    enemies3.splice(i, 1);
                }
            }
        }
    }
};

// Update Player's Laser and Enemy3 Collision
laser.prototype.enemy3CollisionUpdate = function() {
    for (var i in enemies3) {
        this.collideEnemy3(enemies3[i]);
    }
};


/** ENTITY #4 - ELITE INTERCEPTOR (SUICIDE SHOOTER) **/
var enemies4 = [];
var e4Bullets = [];

// Entity Enemy4 Variable
var enemyEntity4 = function(x, y) {
    this.x = x;
    this.y = y;
    this.width = 32;
    this.ySpeed = 1;
    this.xSpeed = 1.5;
    this.health = 32;
    this.armour = 500;
    this.counter = 0;
    this.delay = 75;
};

// Entity Enemy4 Laser Variable
var enemyEntity4Laser = function(x, y) {
    this.x = x;
    this.y = y;
    this.width2 = 4;
    this.damage = 1000;
    this.speed = 3;
};

// Update Enemy4 Laser
enemyEntity4Laser.prototype.update = function() {
    // Moves the laser
    this.y += this.speed;
    
    // Removes laser when out of game
    if (this.y > 490) {
        for (var i in e4Bullets) {
            if (e4Bullets[i] === this) {
                e4Bullets.splice(i, 1);
            }
        }
    }
};

// Draw Enemy4 Laser
enemyEntity4Laser.prototype.draw = function() {
    fill(255, 0, 0);
    rect(this.x, this.y, 2, 10);
};

// Update Enemy4 Ship
enemyEntity4.prototype.update = function() {
    // Frequency of shots
    if (this.counter >= this.delay) {
        e4Bullets.push( new enemyEntity4Laser(this.x - 500, this.y) );// c9 glitch that the first pushed bullet is slightly delayed
        e4Bullets.push( new enemyEntity4Laser(this.x + 5, this.y + 5) );
        e4Bullets.push( new enemyEntity4Laser(this.x + 25, this.y + 5) );
        
        // will keep pushing bullets until this.counter surpasses this.delay plus a while
        if (this.counter >= this.delay + 5) { 
            this.counter = 0;
        }
    }
    this.counter++; //counter counts

};

// Draw Enemy4 Ship
enemyEntity4.prototype.draw = function() {
    // Show image
    image(enemyA4, this.x, this.y);
    
    // Draw health bar 
    if (this.health > 0) {
        fill(183, 28, 28);
        rect(this.x, this.y - 5, 32, 3);
    
        fill(0, 255, 0);
        rect(this.x, this.y - 5, this.health, 3);
    }
};

// Check Enemy4 Follow Player (Enemy4 Movement)
player.prototype.followEnemy4 = function(e4) {
    // see if player is left or right of enemy
    var direction = this.x - e4.x;
    var distance = Math.sqrt(direction * direction + 1);
    direction = direction / distance;
    
    // moves enemy to the same x axis as the player
    e4.x += direction * e4.xSpeed;
    
    // moves enemy down
    e4.y += e4.ySpeed;
    
    // If it goes out of the game
    if (e4.y > 400) {
        for (var i in enemies4) {
            if (enemies4[i] === e4) {
                enemies4.splice(i, 1);
            }
        }
    }

};

// Check Enemy4 Collision With Player (Ship hit ship)
player.prototype.collideEnemy4 = function(e4) {
    if (this.x >= e4.x - e4.width + 10 && this.x <= e4.x + e4.width - 10 && 
        this.y >= e4.y - e4.width && this.y <= e4.y + e4.width) {
        
        // Damages player    
        this.health -= 130 / 10;
        e4.health -= 8;

        // Enemy respawns
        if (e4.health <= 0) {
            powerUpMeter += powerUpInterval;
            score += 30;
            explosions(e4.x, e4.y);
            
            for (var i in enemies4) {
                if (enemies4[i] === e4) {
                    enemies4.splice(i, 1);
                }
            }
        }
    }
};

// Check Enemy4's Laser Collision With Player (Laser hit ship)
player.prototype.collideLaserEnemy4 = function(e4Laser) {
    if (e4Laser.x >= this.x && e4Laser.x <= this.x + this.width &&
        e4Laser.y >= this.y && e4Laser.y <= this.y + this.width) { 
        
        // Player takes damage    
        this.health -= e4Laser.damage / this.armor;
        
        // When collided, removes bullets too
        for (var i in e4Bullets) { 
            if (e4Bullets[i] === e4Laser) {
                e4Bullets.splice(i, 1);
            }
        }        
    }
};

// Update all Enemy4 and Player Collisions
player.prototype.enemy4CollisionUpdate = function() {
    // Enemy4 Follow player
    for (var i in enemies4) {
        this.followEnemy4(enemies4[i]);
    }
    
    // Enemy4 hit player
    for (var i in enemies4) {
        this.collideEnemy4(enemies4[i]);
    }
    
    // Enemy4 laser hit player
    for (var i in e4Bullets) {
        this.collideLaserEnemy4(e4Bullets[i]);
    }
};

// Check Player's Laser Collision With Enemy4
laser.prototype.collideEnemy4 = function(e4) {
    if (this.x >= e4.x && this.x <= e4.x + e4.width && 
        this.y >= e4.y && this.y <= e4.y + e4.width) {
            
        // When collided, removes bullets too
        for (var i in bullets) { 
            if (bullets[i] === this) {
                bullets.splice(i, 1);
            }
        }
        
        // Laser does damage to enemy
        e4.health -= this.damage / e4.armour;
        
        // If enemy4 is destroyed, ...
        if (e4.health <= 0) {
            powerUpMeter += powerUpInterval;
            score += 30;
            
            for (var i in enemies4) {
                if (enemies4[i] === e4) {
                    enemies4.splice(i, 1);
                }
            }
        }
    }
};

// Update Player's Laser and Enemy4 Collision
laser.prototype.enemy4CollisionUpdate = function() {
    for (var i in enemies4) {
        this.collideEnemy4(enemies4[i]);
    }
};


/** SPAWN STUFF (LEVELS) **/ 
spawn = new player(176, 450);

// Wave type
var mayDeathRainUponThem = function() {
    // the better the ship is, the more asteroid spawns to add difficulty
    if (ship <= 5) {
        asteroids.push( new asteroidEntity( Math.random() * 300 + 50, -100) );
        asteroids.push( new asteroidEntity( Math.random() * 300 + 50, -500) );
    }
    else if (ship > 5 && ship <= 10) {
        asteroids.push( new asteroidEntity( Math.random() * 300 + 50, -1000) );
        asteroids.push( new asteroidEntity( Math.random() * 300 + 50, -500) );
        asteroids.push( new asteroidEntity( Math.random() * 300 + 50, -1000) );
        asteroids.push( new asteroidEntity( Math.random() * 300 + 50, -500) );
    }
    else if (ship > 10) {
        asteroids.push( new asteroidEntity( Math.random() * 300 + 50, -500) );
        asteroids.push( new asteroidEntity( Math.random() * 300 + 50, -50) );
        asteroids.push( new asteroidEntity( Math.random() * 300 + 50, -1000) );
        asteroids.push( new asteroidEntity( Math.random() * 300 + 50, -1000) );
        asteroids.push( new asteroidEntity( Math.random() * 300 + 50, -500) );
        asteroids.push( new asteroidEntity( Math.random() * 300 + 50, -1000) );
        asteroids.push( new asteroidEntity( Math.random() * 300 + 50, -500) );
    }
};

var formationA = function() {
    enemies2.push(new enemyEntity2(178, -200));
    enemies2.push(new enemyEntity2(32, -50));
    enemies2.push(new enemyEntity2(64, -150));
    enemies2.push(new enemyEntity2(128, -50));
    enemies2.push(new enemyEntity2(224, -150));
    enemies2.push(new enemyEntity2(288, -50));
    enemies2.push(new enemyEntity2(352, -150));
    enemies2.push(new enemyEntity2(100, -50));
    enemies2.push(new enemyEntity2(32, -150));
    enemies2.push(new enemyEntity2(64, -150));
    enemies2.push(new enemyEntity2(128, -150));
    enemies2.push(new enemyEntity2(224, -250));
    enemies2.push(new enemyEntity2(288, -250));
    enemies2.push(new enemyEntity2(352, -250));
    enemies2.push(new enemyEntity2(100, -250));
};

var formationB = function() {
    enemies3.push(new enemyEntity3(0, -50) );
    enemies3.push(new enemyEntity3(32, -25) );
    enemies3.push(new enemyEntity3(64, -50) );
    enemies3.push(new enemyEntity3(288, -100) );
    enemies3.push(new enemyEntity3(320, -75) );
    enemies3.push(new enemyEntity3(352, -100) );
    enemies3.push(new enemyEntity3(192, -200) );
    enemies3.push(new enemyEntity3(224, -175) );
    enemies3.push(new enemyEntity3(256, -200) );
    enemies3.push(new enemyEntity3(96, -300) );
    enemies3.push(new enemyEntity3(128, -275) );
    enemies3.push(new enemyEntity3(160, -300) );
};

var formationC = function() {
    enemies4.push( new enemyEntity4(32, -50) );
    enemies4.push( new enemyEntity4(96, -75) );
    enemies4.push( new enemyEntity4(128, -100) );
};

var formationD = function() {
    enemies1.push( new enemyEntity1(150, -50) );
    enemies2.push(new enemyEntity2(40, -250) );
    enemies2.push(new enemyEntity2(100, -50) );
    enemies2.push(new enemyEntity2(150, -150) );
    enemies2.push(new enemyEntity2(200, -50) );
    enemies2.push(new enemyEntity2(80, -150) );
    enemies2.push(new enemyEntity2(140, -50) );
    enemies2.push(new enemyEntity2(280, -50) );
    enemies2.push(new enemyEntity2(150, -150) );
    enemies2.push(new enemyEntity2(200, -200) );
    enemies2.push(new enemyEntity2(100, -200) );
    enemies3.push(new enemyEntity3(288, -250) );
    enemies3.push(new enemyEntity3(320, -200) );
    enemies3.push(new enemyEntity3(352, -250) );
    enemies3.push(new enemyEntity3(150, -300) );
    enemies3.push(new enemyEntity3(182, -350) );
    enemies3.push(new enemyEntity3(216, -300) );
    enemies3.push(new enemyEntity3(50, -275) );
    enemies3.push(new enemyEntity3(82, -225) );
    enemies3.push(new enemyEntity3(114, -275) );
    enemies4.push( new enemyEntity4(-50, -200) );
    enemies4.push( new enemyEntity4(434, -232) );

};

var formationE = function() {
    enemies1.push(new enemyEntity1(288, -100));
    enemies2.push(new enemyEntity2(32, -50));
    enemies2.push(new enemyEntity2(64, -150));
    enemies2.push(new enemyEntity2(128, -50));
    enemies2.push(new enemyEntity2(224, -150));
    enemies2.push(new enemyEntity2(288, -50));
    enemies2.push(new enemyEntity2(352, -150));
    enemies2.push(new enemyEntity2(100, -50));
};

// Spawn waves
var waveTimer = 0;
var waveLoop = 0;

var spawnWaves = function() { //for loops count too fast
    // wave 1
    if (waveTimer === 100) {
        formationA();
        mayDeathRainUponThem();
    }
    
    if (waveTimer === 1000) {
        formationA();
    }
    
    if (waveTimer === 2000) {
        formationA();
    }
    
    if (waveTimer === 3000) {
        formationE();
    }

    if (waveTimer === 4000) {
        formationB();
    }
    
    // wave 2
    if (waveTimer === 5300) {
        formationC();
    }
    
    // wave 3
    if (waveTimer === 6300) {
        formationA();
        formationB();
    }
    
    // wave 4
    if (waveTimer === 7000) {
        formationC();
    }
    
    // wave 5
    if (waveTimer === 7500) {
        formationE();
        formationC();
    }
    
    // wave 6
    if (waveTimer === 8000) {
        formationD();
    }
    
    // wave 7
    if (waveTimer === 9000) {
        formationB();
    }
    if (waveTimer === 9300) {
        formationD();
    }
    
    // goes back to wave 1
    if (waveTimer === 10000) {
        waveTimer = 0;
        waveLoop += 1;
    }
    
    // Difficulty increases as they win more
    if (waveLoop === 0) {
        waveTimer += 2;
    }
    if (waveLoop === 1) {
        waveTimer += 4;
    }
    if (waveLoop === 2) {
        waveTimer += 5;
    }
    if (waveLoop === 3) {
        waveTimer += 8;
    }
};



// update and loop everything
draw = function() {
    if(battleSong.isPlaying() === false) {
        battleSong.play();
    } 
    
    // Hidden ship access
    if(systemLoginId === "Asuna") {
        admin = true;
        println("Access Granted m8");
    }
    
    // Menu
    if(scene === 1) {
        menu();
        
        // pushes the new score  
        scores.push(score);
        
        // finds highest score in the scores array using a for loop
        for (var i = 0; i < scores.length; i++) {
            if (scores[i] > highscore) {
                highscore = scores[i];
            }
        }
        
        //highscore = Math.max.apply(Math, scores);
        
        // Resets everything except scores
        score = 0;
        delayCounter = 0;
        reloadCounter = 0;
        reload = 512;
        powerUpMeter = 0;
        aegisMode = false;
        
        // clears the arrays which clears enemies and lasers
        bullets = [];
        asteroids = []; 
        enemies1 = [];
        e1Bullets = [];
        enemies2 = [];
        e2Bullets = [];
        e2Mine = [];
        e2MineCount = 0;
        enemies3 = [];
        e3Bullets = [];
        enemies4 = [];
        e4Bullets = [];
        waveTimer = 0;
        waveLoop = 0;
        spawn = new player(176, 450); //respawns player
    }
    
    // Instructions part 1
    if (scene === 4) {
        instructions1();
    }
    // Instructions part 2
    if (scene === 5) {
        instructions2();
    }
    
    // instructions part 3
    if (scene === 6) {
        instructions3();
    }
    
    //Hangar
    if (scene === 3) {
        customization();
    }
    if (scene === 31) {
        shipSelectMenu();
    }
    if (scene === 32) {
        upgradesMenu();
    }
    
    //Gameover
    if (scene === 9000) {
        gameover();
    }

    // Gameplay
    if(scene === 2) {
        spawn.playerHud();
        gameplay();
        spawnWaves();
        
        //Draw the player
        spawn.update();
        spawn.draw();
        
        // Draw Player Lasers
        for (var i in bullets) {
            bullets[i].draw();
            bullets[i].update();
        }  
        
        // Asteroid
        for (var i in asteroids) { // draw the asteroid
            asteroids[i].draw();
            asteroids[i].update();
        }
        for (var i in bullets) { // asteroid and player's laser collision
            bullets[i].asteroidCollisionUpdate();
        }        
        spawn.asteroidCollisionUpdate(); // asteroid collide with player
        
        // Enemy1
        for (var i in enemies1) { // draw enemy1
            enemies1[i].draw();
            enemies1[i].update();
        }
        for (var i in e1Bullets) { // draw enemy1's lasers
            e1Bullets[i].draw();
            e1Bullets[i].update();
        }
        for (var i in bullets) { // enemy1 and player's laser collision
            bullets[i].enemy1CollisionUpdate();
        }
        spawn.enemy1CollisionUpdate(); // enemy1 and its laser collide with player
        
        //Draw enemy2
        for (var i in enemies2) { // draw enemy2
            enemies2[i].draw();
            enemies2[i].update();
        }
        for (var i in e2Bullets) { // draw enemy2's lasers
            e2Bullets[i].draw();
            e2Bullets[i].update();
        }
        for (var i in e2Mine) { // draw enemy2's mines
            e2Mine[i].draw();
        }
        for (var i in bullets) { // enemy2 and player's laser collision
            bullets[i].enemy2CollisionUpdate();
        }
        for (var i in bullets) {
            bullets[i].enemy2MineCollisionUpdate();
        }
        spawn.enemy2CollisionUpdate(); // enemy2 and its laser collide with player
        spawn.enemy2MineCollisionUpdate(); // enemy2's mine and its collision with player
        
        // enemy3
        for (var i in enemies3) {
            enemies3[i].draw();
            enemies3[i].update();
        }
        for (var i in e3Bullets) {
            e3Bullets[i].draw();
            e3Bullets[i].update();
        }
        for (var i in bullets) {
            bullets[i].enemy3CollisionUpdate();
        }
        spawn.enemy3CollisionUpdate();
        
        // enemy4
        for (var i in enemies4) {
            enemies4[i].draw();
            enemies4[i].update();
        }
        for (var i in e4Bullets) {
            e4Bullets[i].draw();
            e4Bullets[i].update();
        }
        for (var i in bullets) {
            bullets[i].enemy4CollisionUpdate();
        }
        spawn.enemy4CollisionUpdate();
    }
    // text(waveTimer + " " + waveLoop, 100, 100);
    // text(scene, mouseX, mouseY);
};