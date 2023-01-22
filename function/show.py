import object.player as pl
import object.skills as sk

def stats():
    print("Name: "+str(pl.id.name)
    +" || Level: "+str(pl.id.level)
    +" || HP: "+str(pl.id.hp)
    +" || XP: "+str(pl.id.xp)
    +" || agility: "+str(pl.id.agility)
    +" || Power: "+str(pl.id.power)
    +"\nMoney: "+str(pl.id.money)
    +" || Weapon: "+str(pl.id.weapon.name)
    +" || weapon_p: "+str(pl.id.weapon.power)
    +"\nSkill_1: "+str(pl.id.skill_1.name)
    +" || Skill_2: "+str(pl.id.skill_2.name)
    +" || Skill_3: "+str(pl.id.skill_3.name)
    +"\nShield: "+str(pl.id.shield)
    +" || Stamina: "+str(pl.id.stamina))

def skills():
    print ("Ваши экиппированные скиллы:\n")
    print (str(pl.id.skill_1.name)
    +"\nPOWER: "+ str(pl.id.skill_1.power)
    +" || AGILITY "+str(pl.id.skill_1.agility)
    +" || HP "+str(pl.id.skill_1.hp)
    +" || POISON "+str(pl.id.skill_1.poison)
    +" || BLOODES "+str(pl.id.skill_1.bloodes)
    +" || SHIELD "+str(pl.id.skill_1.shield))

    print ("\n"+str(pl.id.skill_2.name)+
    "\nPOWER: "+str(pl.id.skill_2.power)
    +" || AGILITY "+str(pl.id.skill_2.agility)
    +" || HP "+str(pl.id.skill_2.hp)
    +" || POISON "+str(pl.id.skill_2.poison)
    +" || BLOODES "+str(pl.id.skill_2.bloodes)
    +" || SHIELD "+str(pl.id.skill_2.shield))

    print ("\n"+str(pl.id.skill_3.name)+
    "\nPOWER: "+str(pl.id.skill_3.power)
    +" || AGILITY "+str(pl.id.skill_3.agility)
    +" || HP "+str(pl.id.skill_3.hp)
    +" || POISON "+str(pl.id.skill_3.poison)
    +" || BLOODES "+str(pl.id.skill_3.bloodes)
    +" || SHIELD "+str(pl.id.skill_3.shield))