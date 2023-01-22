import object.player as pl
import object.weapon as wp

from tkinter import *

def shop(window, lbl):
        lbl.configure(text="Полюбуйтесь на наши предметы:")
        mass=[wp.dagger, wp.coudgel, wp.short_bow, wp.spear,
         wp.trindent, wp.serp, wp.mace, wp.short_bow, wp.skimitar] ###Предметы из shop
        for x in mass:
                lbl = Label(window, str(x.name)+" power:"+str(x.power)+" damage_min: "
                +str(x.damage_m)+" damage: "+str(x.damage)+"\ntype: "
                +str(x.type)+" Цена: "+str(x.price)+"\n########", font=("Arial", 14))
                i=0
        while i<1:
                print("Ваш кошелек: "+str(pl.id.money))
                choice = input("Что берете? \nИли выход ")
                for x in mass:
                        if choice == str(x.name):
                                if pl.id.money<x.price:
                                        print("you don`t have money(((")

                                pl.id.money-=x.price
                                pl.id.weapon = x
                                pl.id.weapon_p = x.power
                                pl.id.inventory += [x]
                                print("Вашь инвентарь: ")
                                for x in pl.id.inventory:
                                        print(str(x.name)+" "+str(x.power))
                                print(str(pl.id.money))
                                print("ОО, отличный выбор! "+str(choice))
                if choice == "выход":
                        return 0