class SKILL:
    def __init__(self, name, power, agility, hp, poison, bloodes, shield):
        self.name = name
        self.power = power
        self.agility = agility
        self.hp = hp
        self.poison = poison
        self.bloodes = bloodes
        self.shield = shield


none = SKILL("none", 0, 0, 0, 0, 0, 0)
jerk = SKILL("jerk", 3, -1, 0, 0, 0, 0)
howl = SKILL("howl", 0, -1, 0, 0, 0, 0)

slime = SKILL("slime", 0, 0, 10, 0, 0, 0)

wather_region = SKILL("Водяной регион", 2, 0, 0, 0, 0, 0)

#### FOR PLAYERS ####

undercut = SKILL("подсечка", 0, 4, 0,10,0,0)
furios_roar = SKILL("Яростный рёв", 5, 0,0,0,0,0)
none = SKILL("none", 0, 0, 0, 0, 0, 0)