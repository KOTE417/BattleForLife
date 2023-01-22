import telebot
import random
import pymysql
import re

import object.player as pl
import object.enemy as en
import object.weapon as wp
import object.skills as sk
import function.fight as fg
import function.shop as sp
import function.equip as eq
import function.check as ch
import function.show as sh

from telebot import types



bot = telebot.TeleBot("5921193873:AAFtVwAzegmN6G9USoetSEVV7NoSW-BFJRM")

###try:
###        db = pymysql.connect(
###        host=config.host,
###        port=3306,
###        user=config.user,
###        password=config.password,
###        database=config.db_name,
###        cursorclass=pymysql.cursors.DictCursor
###)
###        print("connected")
###except Exception as ex:
###        print("no")
###        print(ex)
###

def choise_name(name_p):
        name = name_p
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
        pl.id = pl.PLAYER(name, level, hp, hp_def, xp, power, agility,
        money, inventory, skills, skill_1, skill_2, skill_3, weapon, weapon_p, shield, stamina)
        text = "Привет, "+str(pl.id.name)
        return text

@bot.message_handler(commands=['start'])
def welcome(message):
        bot.send_message(message.chat.id, text="Введите ваш никнейм")
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Арена")
        btn2 = types.KeyboardButton("Магазин")
        btn3 = types.KeyboardButton("Отдых")
        btn4 = types.KeyboardButton("Статы")
        markup.add(btn1, btn2, btn3, btn4)
        @bot.message_handler(content_types=['text'])
        def choice_name(message):
                bot.send_message(message.chat.id, text=str(), reply_markup=markup)

@bot.message_handler(content_types=['text'])
def func(message):
        if(message.text == "Магазин"):
                shop = sp.shop()
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                btn1 = types.KeyboardButton("Арена")
                btn2 = types.KeyboardButton("Магазин")
                btn3 = types.KeyboardButton("Отдых")
                btn4 = types.KeyboardButton("Статы")
                markup.add(btn1, btn2, btn3, btn4)
                bot.send_message(message.chat.id, text=str)

        


bot.infinity_polling()