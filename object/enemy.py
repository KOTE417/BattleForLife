import object.items as it
import object.skills as sk
import object.weapon as wp

class ENEMY:
    def __init__(self, name, level, hp, power, agility, items, skills):
        self.name = name
        self.level = level
        self.hp = hp
        self.power = power
        self.agility = agility
        self.items = items
        self.skills = skills

Rat = ENEMY("Крыса", 5, 15, 5, 10, [it.claws],[sk.none])
Wolf = ENEMY("Волк", 5, 20, 5, 6, [it.claws, it.teeth], [sk.none])
Slime = ENEMY("Слизь", 5, 10, 4, 4, [it.tentacles], [sk.none])
Borow = ENEMY("Боров", 5, 20, 5, 6, [it.claws], [sk.jerk])
 
Mature_Wolf = ENEMY("Матёрый волк", 10, 35, 10, 9, [it.teeth, it.claws], [sk.howl])
Blue_Slime = ENEMY("Голубая слизь", 10, 20, 8, 10, [it.tentacles], [sk.none])
Mature_Rat = ENEMY("Матёрый крыск", 10, 25, 10, 15, [it.claws], [sk.none])
Wild_boar = ENEMY("Дикий кабан", 10, 30, 10, 12, [it.claws], [sk.jerk])

Skelet = ENEMY("Скелет", 15, 50, 15, 10, [it.sword], [sk.none])
Goblin = ENEMY("Гоблин", 15, 35, 15, 20, [it.dagger], [sk.none])
Zombie = ENEMY("Зомби", 15, 80, 10, 10, [it.punch, it.bite], [sk.none])
Aqua_man = ENEMY("Водяной", 15, 40, 15, 15, [it.aqua_punch], [sk.none])

SKelet_Warrior = ENEMY("Скелет-воитель", 20, 50, 20, 10, [it.sword, it.shield], [sk.none])
Goblin_Scout = ENEMY("Гоблин-развдечик", 20, 35, 15, 20, [it.dagger], [sk.none])
Gul = ENEMY("Гуль", 20, 40, 15, 1000, [it.claws_gul], [sk.none])
Death_man = ENEMY("Умертвий", 20, 80, 15, 15000, [it.sword],[sk.none])

Retary = ENEMY("Ретарий", 25, 100, 100, 100, [it.sword, it.shield], [sk.none])
Myrmilion = ENEMY("Мурмиллион", 25, 100, 100, 100, [it.sword], [sk.none])
Sekutor = ENEMY("Секутор", 25, 100, 100, 100, [it.sword], [sk.none])
Sammit = ENEMY("Самнит", 25, 100, 100, 100, [it.sword], [sk.none])


