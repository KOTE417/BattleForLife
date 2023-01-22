import random

import object.player as pl
import object.skills as sk

def agility(agility, power):
    i=random.randint(0,100)
    print("random i "+str(i))
    if i < agility:
        return power
    else:
        return 0

##### FIGHTING ######

def fighting(enemy, skill_p):
    for items in enemy.items:
        print("ОРужие врага: "+items.name)
    
    for skill in enemy.skills:
        print("Скилл врага: "+skill.name)

    

    print("Ваше оружие: "+str(pl.id.weapon)+" "+str(pl.id.weapon_p))
    
    power_p = pl.id.power+pl.id.weapon_p+random.randint(pl.id.weapon.damage_m, pl.id.weapon.damage)+skill_p.power
    print(" "+str(pl.id.power)+" "+str(pl.id.weapon_p)+" "+str(pl.id.weapon.damage_m)+" "+str(pl.id.weapon.damage))

    print("Ваша сила с оружием: "+str(power_p))
    
    power_e = enemy.power
    +items.buf
    +skill.power

    print("ваши силы: "+str(power_p))
    print("Enemy: "+str(power_e))

    print("Выбранный скилл"+str(skill_p.name))

    agil_p = pl.id.agility+skill_p.agility

    print("player_agility со скиллом: "+str(agil_p))
    print("enemy: "+str(enemy.agility))

    agility_sum = enemy.agility+skill.agility+agil_p
    
    agil_per_p = (agil_p/agility_sum)*100
    agil_per_e = ((enemy.agility+skill.agility)/agility_sum)*100
    
    print("sum: "+str(agility_sum))
    print("player: "+str(agil_per_p))
    print("enemy: "+str(agil_per_e))

    print("power_p"+str(power_p))
    print("power_e"+str(power_e))

    pw_p = agility(agil_per_p, power_p)
    pw_e = agility(agil_per_e, power_e)

    print("pw_p"+str(pw_p))
    print("pw_e"+str(pw_e))

    pl.id.hp -= pw_e
    enemy.hp -= pw_p

    print("Player HP: "+str(pl.id.hp))
    print("Enemy HP: "+str(enemy.hp))

    if enemy.hp<=0:
        return 1

    if pl.id.hp<=0:
        return 2

    return 0

def debuf(enemy, skill):
    enemy.hp -= skill.poison
    print("хп противника  "+str(enemy.hp))

#######  FIGHT   #########

def fight(enemy):                                                      ### Рандом врагов
        
    i=0

    pl.id.stamina -= 10
    print("Ваша стамина: "+str(pl.id.stamina))
    print("Ваш противник: "+str(enemy.name))
    print("Ваши силы: "+str(pl.id.power))

    x=0
    while x<1:
        choice = input("Биться или убежать? ")
        if str(choice)=="":
            x +=1
            while i<1 :
                z=0
                while z<1:
                    print("Ваши доступные скилы:")
                    print("Skill_1: "+str(pl.id.skill_1.name))
                    print("Skill_2: "+str(pl.id.skill_2.name))
                    print("Skill_3: "+str(pl.id.skill_3.name))
                    skill_c = input("Выберите скил: ")
                    if skill_c == pl.id.skill_1.name:
                        z=1
                        skill = pl.id.skill_1
                    if skill_c == pl.id.skill_2.name:
                        z=1
                        skill = pl.id.skill_2
                    if skill_c == pl.id.skill_3.name:
                        z=1
                        skill = pl.id.skill_3
                    if skill_c == "":
                        z=1
                        skill = sk.none

                atak = input("атака")
                if str(atak)=="":
                    debuf(enemy, skill)
                    i=fighting(enemy, skill)
            if i==1:
                print("вы победили!!!!")
                money = random.randint(10,50)
                pl.id.money +=money
                if enemy.level<6:
                    pl.id.xp += +5
                elif enemy.level>6 and enemy.level<11:
                    pl.id.xp += +15
                print("xp: "+str(pl.id.xp)+" Money+ "+str(money))
            else:
                print("вы проиграли(((")
            i-=1
            print("i: "+str(i))
            return i

        if str(choice)=="убежать":
            x=1
            print("вы убежали")
            return 0