from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def get_keyboard_inline_1():
    keyboard_inline = InlineKeyboardMarkup(row_width=1)
    btn_inline = InlineKeyboardButton('Посмотреть', url='https://cattish.ru/breed/')

    keyboard_inline.add(btn_inline, btn_inline_2)

    return keyboard_inline


def get_keyboard_inline_2():
    keyboard_inline_2 = InlineKeyboardMarkup(row_width=1)
    btn_inline_2 = InlineKeyboardButton('Посмотреть', url='https://lapkins.ru/dog/')
    keyboard_inline_2.add(btn_inline_2)
    return keyboard_inline_2
