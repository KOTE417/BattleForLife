
from tkinter import *
import random

import object.weapon as wp
import object.player as pl
import object.enemy as en
import function.check as ch
import store
  
#def clicked():  
#    res = "Привет {}".format(txt.get())  
#    lbl.configure(text=res)  

def stats():
    stats = Tk()
    stats.title("BATTLE FOR LIFE")  
    stats.geometry('400x250')

    mass_name = ["name", "level", "hp", "xp", "agility", "power", "money", "weapon", "weapon_p", "skill_1", "skill_2", "skill_3", "stamina"]
    i=0
    z=0
    for x in mass_name:  
        x = Label(stats, text=x, font=("", 16)) ####колонка с названиями
        if i>7:
            z=2
            i=0
        i+=1
        x.grid(column=z, row=i)

    mass_pl = [pl.id.name, pl.id.level, pl.id.hp, pl.id.xp, 
    pl.id.agility, pl.id.power, pl.id.money, pl.id.weapon.name, 
    pl.id.weapon.power, pl.id.skill_1.name, pl.id.skill_2.name, 
    pl.id.skill_3.name, pl.id.stamina]
    i=0
    z=1
    for p in mass_pl:
        p = Label(stats, text=p, font=("", 16)) ###КОЛОНКА С ЗНАЧЕНИЯМИ
        if i>7:
            z=3
            i=0
        i+=1
        p.grid(column=z, row=i)

def fight():
    mass_en = ch.check_enemy()
    x=random(0,3)


    

    

def chill():
    print("xd")

def hub():
    hub_wnd = Tk()
    hub_wnd.title("BATTLE FOR LIFE")
    hub_wnd.geometry('400x250')
    home_text = Label(hub_wnd, text="Вы дома, куда хотите сходить?")
    home_text.grid(column=0, row=0)
    store_btn = Button(hub_wnd, text="Магазин", command=store.store)
    store_btn.grid(column=0, row=1)
    chill_btn = Button(hub_wnd, text="Отдых", command=chill)
    chill_btn.grid(column=0, row=2)
    arena_btn = Button(hub_wnd, text="Арена", command=fight)
    arena_btn.grid(column=0, row=3)
    equip_btn = Button(hub_wnd, text="Экип", command=store)
    equip_btn.grid(column=0, row=4)
    stats_btn = Button(hub_wnd, text="Статы", command=stats)
    stats_btn.grid(column=0, row=5)

window = Tk()
window.title("BATTLE FOR LIFE")
window.geometry('400x250')
hub()
window.mainloop()
