
class ITEM:
    def __init__(self, name, buf, demage_m, demage):
        self.name = name
        self.buf = buf
        self.demage_m = demage_m
        self.demage = demage

claws = ITEM("claws", 3, 0, 0)
teeth = ITEM("teeth", 1, 0, 0)
tentacles = ITEM("tentacles", 3, 0 ,0)

sword = ITEM("sword", 0, 4, 6)
dagger = ITEM("dagger", 0, 3, 4)

punch = ITEM("punch", 0, 1, 3)
bite = ITEM("bite", 0, 1, 3)

aqua_punch = ITEM("aqua_punch", 0, 1, 3)

shield = ITEM("shield", -4, 0, 0)

claws_gul = ITEM("claws_gul", 0, 6, 8)