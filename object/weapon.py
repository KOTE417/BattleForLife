
class ITEM:
    def __init__(self, name, power, damage_m, damage, type, price):
        self.name = name
        self.power = power
        self.damage_m = damage_m
        self.damage = damage
        self.type = type
        self.price = price

none = ITEM("none", 0, 0, 1, "-", 0)
dagger = ITEM("Кинжал", 12, 1, 3, "колющий", 80)
spear = ITEM("Копье", 22, 2, 5, "колющий", 200)
mace = ITEM("Палица", 24, 1, 6, "дробящий", 300)
serp = ITEM("Серп", 15, 1, 4, "рубящий", 200)
short_bow = ITEM("Короткий лук", 18, 0, 6, "Колющий", 160)
short_sword = ITEM("Короткий меч", 24, 1, 6, "рубящий", 300)
trindent = ITEM("Трезубец", 18, 3, 6, "колющий", 200)
coudgel = ITEM("Дубина", 12, 1, 3, "дробящий", 80)
skimitar = ITEM("Скимитар", 24, 3, 6, "рубящий", 300)