import object.skills as sk
import object.weapon as wp

class PLAYER:

        def __init__(self, name, level, hp, hp_def, xp, power, agility, money, inventory,
        skills, skill_1, skill_2, skill_3, weapon, weapon_p, shield, stamina):
                self.name = name
                self.level = level
                self.hp = hp
                self.hp_def = hp_def
                self.xp = xp
                self.power = power
                self.agility = agility
                self.money = money     
                self.inventory = inventory
                self.skills = skills
                self.skill_1 = skill_1          
                self.skill_2 = skill_2
                self.skill_3 = skill_3
                self.weapon = weapon
                self.weapon_p = weapon_p
                self.shield = shield
                self.stamina = stamina

name = "Player"
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
id = PLAYER(name, level, hp, hp_def, xp, power, agility,
money, inventory, skills, skill_1, skill_2, skill_3, weapon, weapon_p, shield, stamina)