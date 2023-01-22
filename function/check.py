import object.player as pl
import object.enemy as en
import object.skills as sk

def chek():

    if pl.id.xp >= 20 and pl.id.level<1:
        pl.id.level = 1
        pl.id.skills += [sk.undercut]
        pl.id.power += 1
        pl.id.agility += 1
        pl.id.hp_def += 10
        pl.id.xp = 0
    elif pl.id.xp >= 30 and pl.id.level<2:
        pl.id.level = 2
        pl.id.xp = 0
    elif pl.id.xp >= 40 and pl.id.level<3:
        pl.id.level = 3
        pl.id.xp = 0
    elif pl.id.xp >= 50 and pl.id.level<4:
        pl.id.level = 4
        pl.id.xp = 0
    elif pl.id.xp >= 60 and pl.id.level<5:
        pl.id.level = 5
        pl.id.xp = 0
        print("  #####   !!!  ")
        print("  ##      !!!  ")
        print("   ####   !!!  ")
        print("      ##  !!!  ")
        print("      ##  !!!  ")
        print("  #####   !!!  ")
    elif pl.id.xp >= 80 and pl.id.level<6:
        pl.id.level = 6
        pl.id.xp = 0
    elif pl.id.xp >= 100 and pl.id.level<7:
        pl.id.level = 7
        pl.id.xp = 0
    elif pl.id.xp >= 120 and pl.id.level<8:
        pl.id.level = 8
        pl.id.xp = 0
    elif pl.id.xp >= 140 and pl.id.level<9:
        pl.id.level = 9
        pl.id.xp = 0
    elif pl.id.xp >= 160 and pl.id.level<10:
        pl.id.level = 10
        pl.id.xp = 0

def check_enemy():
    if pl.id.level<6:
        mass = [en.Wolf, en.Rat, en.Slime, en.Borow]
        return mass
    
    elif pl.id.level<11:
        mass = [en.Mature_Wolf, en.Blue_Slime, en.Mature_Rat, en.Wild_boar]
        return mass

    elif pl.id.level<16:
        mass = [en.Skelet, en.Goblin, en.Zombie, en.Aqua_man]
        return mass

    elif pl.id.level<21:
        mass = [en.SKelet_Warrior, en.Goblin_Scout, en.Gul, en.Death_man]
        return mass
    
    elif pl.id.level<26:
        mass = [en.Retary, en.Myrmilion, en.Sekutor, en.Sammit]
        return mass