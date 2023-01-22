from tkinter import *

W























 
import object.weapon as wp

def store():
    store = Tk()
    store.title("BATTLE FOR LIFE")  
    store.geometry('400x250')
    mass=[wp.dagger, wp.serp, wp.short_bow, wp.coudgel, wp.trindent, wp.skimitar, wp.mace]
    i=1
    for x in mass:
        i += 1
        name = Label(store, text="Оружие")
        power = Label(store, text="Сила")
        price = Label(store, text="Цена")
        btn = Button(store, text=str(x.name))  
        rewie = Label(store, text=str(x.power))
        price_x = Label(store, text=str(x.price))

        name.grid(column=0, row=0)
        power.grid(column=1, row=0)
        price.grid(column=2, row=0)
        btn.grid(column=0, row=i)
        rewie.grid(column=1, row=i)
        price_x.grid(column=2, row=i)