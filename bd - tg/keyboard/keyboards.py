from aiogram.types import  ReplyKeyboardMarkup, KeyboardButton

def get_keyboard_1():

    keyboard = ReplyKeyboardMarkup(resize_keyboard= True)
    btn1 = KeyboardButton('Отправь фото природы')
    btn2 = KeyboardButton('след. клава')
    keyboard.add(btn1, btn2)
    return keyboard

def get_keyboard_2():
    keyboard_2 = ReplyKeyboardMarkup(resize_keyboard= True)
    btn1_2 = KeyboardButton('отправь фото из космоса')
    btn2_2 = KeyboardButton('вернуться назад')
    keyboard_2.add(btn1_2, btn2_2)
    return keyboard_2