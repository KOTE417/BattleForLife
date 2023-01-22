import random
import time
import os

import object.player as pl
import object.enemy as en
import object.weapon as wp
import object.skills as sk
import function.fight as fg
import function.shop as sp
import function.equip as eq
import function.check as ch
import function.show as sh

def choise_name():
        name = input("Введите своё имя: ")
        level = 0
        hp = 100
        hp_def = 100
        xp = 0
        power = 5
        agility = 10
        money = 100
        inventory = []
        skills = [sk.none, sk.undercut]
        skill_1 =sk.undercut
        skill_2 =sk.none
        skill_3 =sk.none        
        weapon = wp.none
        weapon_p = 0
        shield = "none"
        stamina = 100
        pl.id = pl.PLAYER(name, level, hp, hp_def, xp, power, agility,
        money, inventory, skills, skill_1, skill_2, skill_3, weapon, weapon_p, shield, stamina)
        text = "Привет, "+str(pl.id.name)
        return text


def main():
        ##x=0
        ##while x<1:
        print("\n")
        print("#######          ###       #########   #########   ##        #####   ")
        print("##    ##        ## ##         ###         ###      ##        ##      ")
        print("##    ##       ##   ##        ###         ###      ##        ##      ")
        print("#######       ##     ##       ###         ###      ##        #####   ")
        print("##    ##     ###########      ###         ###      ##        ##      ")
        print("##    ##    ##         ##     ###         ###      ##        ##      ")
        print("#######    ##           ##    ###         ###      #######   ######  ")
        ##time.sleep(0.1)
        ##os.system('cls')
        print("\n")
        print("#######    ###      ######            ##        ##   #######  #####  ")
        print("##        ## ##     ##   ##           ##             ##       ##     ")
        print("#####    ##   ##    ######            ##        ##   #####    ##     ")
        print("##      ##     ##   ####              ##        ##   ##       #####  ")
        print("##       ##   ##    ## ##             ##        ##   ##       ##     ")
        print("##        ## ##     ##  ##            ##        ##   ##       ##     ")
        print("##         ###      ##   ##           #######   ##   ##       #####  ")
        print("\n")
        ##time.sleep(0.01)
        ##os.system('cls')
        

        choise_name()
        i=0
        while i<1:
                ch.chek()
                print("Вы дома, куда хотите сходить?")
                choice = input("Магазин, Арена, Отдых, Статы, Инвентарь, Экип, скилл ")
                if str(choice)=="магазин":
                        print("\n")
                        print("############################################")
                        print("##             #############              ##")
                        print("##                 SHOP                   ##")
                        print("##               #########                ##")
                        print("##          |#      --->            ####  ##")
                        print("##    #     | #              |      ####  ##")
                        print("##    #     |  #    --->     |       ||   ##")
                        print("##   ###    | #             ---      ||   ##")
                        print("##    #     |#      --->     |       ||   ##")
                        print("############################################")
                        print("##                                        ##")
                        print("############################################")
                        print("\n######")
                        i = sp.shop()
                        choice = "default"
                        print("######\n")
                elif str(choice)=="арена":
                        print("\n######")
                        mass=ch.check_enemy()
                        x=random.randint(0,3)
                        i=fg.fight(mass[x])
                        choice = "default"
                        print("######\n")
                elif str(choice)=="отдых":
                        print("\n######")
                        pl.id.stamina = 100
                        pl.id.hp = pl.id.hp_def
                        print("Вы отдохнули и набрались сил, поздравляю!")
                        print("######\n")
                elif str(choice)=="статы":
                        print("\n######")
                        sh.stats()
                elif str(choice)=="инвентарь":
                        print("Ваш инвентарь: ")
                        for x in pl.id.inventory:
                                print(str(x.name)+" "+str(x.power))
                        print("######\n")
                elif str(choice)=="экип":
                        i=eq.equipment()
                elif str(choice)=="скилл":
                        sh.skills()
                        skill = input("Хотите изменить ваш сет скиллов?")
                        if str(skill) == "да":
                                i=eq.eq_skills()
                        elif str(skill) == "нет":
                                print("Оставляем всё на своем месте)")

main()