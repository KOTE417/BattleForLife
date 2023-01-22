import object.player as pl

def equipment():
    print("Ваши оружия: ")
    for x in pl.id.inventory:
        print(str(x.name)+" power: "+str(x.power)+" damage: "
        +str(x.damage_m)+"-"+str(x.damage)+" type: "+str(x.type)+"\n")

    print("Выбранное: "+str(pl.id.weapon)+" "+str(pl.id.weapon_p)+"\n")

    choice = input("Какое оружие хотите экипировать: ")
    for x in pl.id.inventory:
        if str(choice) == str(x.name):
            pl.id.weapon = x
            pl.id.weapon_p = x.power

    print("Ваша экипировка: ")
    print(str(pl.id.weapon.name)+" ---- "+str(pl.id.weapon.power))

    return 0

def eq_skills():
    print("Ваши имеющиеся скиллы: ")
    for x in pl.id.skills:
        print(str(x.name)
        +" || power: "+str(x.power)
        +" || agility: "+str(x.agility)
        +" || hp"+str(x.hp)
        +" || poison: "+str(x.poison)
        +" || bloodes: "+str(x.bloodes)
        +" || shield: "+str(x.shield))

    print("\nВыбранные скиллы:\nSkills_1: "+str(pl.id.skill_1.name)+
    " || Skills_2:  "+str(pl.id.skill_2.name)+" || Skills_3: "+str(pl.id.skill_3.name))
    
    choice = input("Какое скилл хотите экипировать 1: ")
    for x in pl.id.skills:
        if str(choice) == str(x.name):
            pl.id.skill_1 = x
        else:
            print("Такого скилла нет")
                

    b=0
    while b<1:
        choice_2 = input("Какое скилл хотите экипировать 2: ")
        for x in pl.id.skills:
            if str(choice_2) == str(x.name):
                if str(choice_2) != str(choice) or str(choice) == "none":
                    pl.id.skill_2 = x
                    b=1
                else:
                    ("Этот скилл уже выбран")
            else:
                print("Такого скилла нет")

    b=0
    while b<1:
        choice_3 = input("Какое скилл хотите экипировать 3: ")
        for x in pl.id.skills:
            if str(choice_3) == str(x.name):
                if str(choice_3) != str(choice) or str(choice_3) != str(choice_2) or str(choice) == "none":
                    pl.id.skill_3 = x
                    b=1
                else:
                    ("Этот скилл уже выбран")
            else:
                print("Такого скилла нет")

    print("Ваша экипировка скиллов: \n")
    print("Skill_1: ")
    print(str(pl.id.skill_1.name)
    +" || power: "+str(pl.id.skill_1.power)
    +" || agility: "+str(pl.id.skill_1.agility)
    +" || hp"+str(pl.id.skill_1.hp)
    +" || poison: "+str(pl.id.skill_1.poison)
    +" || bloodes: "+str(pl.id.skill_1.bloodes)
    +" || shield: "+str(pl.id.skill_2.shield))

    print("Skill_2: ")
    print(str(pl.id.skill_2.name)
    +" || power: "+str(pl.id.skill_2.power)
    +" || agility: "+str(pl.id.skill_2.agility)
    +" || hp"+str(pl.id.skill_2.hp)
    +" || poison: "+str(pl.id.skill_2.poison)
    +" || bloodes: "+str(pl.id.skill_2.bloodes)
    +" || shield: "+str(pl.id.skill_2.shield))

    print("Skill_3: ")
    print(str(pl.id.skill_3.name)
    +" || power: "+str(pl.id.skill_3.power)
    +" || agility: "+str(pl.id.skill_3.agility)
    +" || hp"+str(pl.id.skill_3.hp)
    +" || poison: "+str(pl.id.skill_3.poison)
    +" || bloodes: "+str(pl.id.skill_3.bloodes)
    +" || shield: "+str(pl.id.skill_3.shield))

    return 0