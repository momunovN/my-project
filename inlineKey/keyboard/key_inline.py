from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def get_keyboard_inline_1():
    keyboard_inline = InlineKeyboardMarkup(row_width=2)
    btn_inline = InlineKeyboardButton('Породы кошек', url='https://cattish.ru/breed/')
    btn_inline_1_2 = InlineKeyboardButton('Фотки кошек', url='https://ru.freepik.com/photos/%D0%BA%D0%BE%D1%88%D0%BA%D0%B8')
    keyboard_inline.add(btn_inline, btn_inline_1_2)

    return keyboard_inline


def get_keyboard_inline_2():
    keyboard_inline_2 = InlineKeyboardMarkup(row_width=2)
    btn_inline_2 = InlineKeyboardButton('Порода собак', url='https://lapkins.ru/dog/')
    btn_inline_3 = InlineKeyboardButton('Фотки собак', url='https://lapkins.ru/dog/')
    keyboard_inline_2.add(btn_inline_2, btn_inline_3)
    return keyboard_inline_2


