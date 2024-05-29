from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def get_keyboard_inline_1():
    keyboard_inline = InlineKeyboardMarkup(row_width=2)
    btn_inline = InlineKeyboardButton('Горы', url='https://ru.freepik.com/search?ai=excluded&format=search&last_filter=query&last_value=%D0%B3%D0%BE%D1%80%D1%8B&query=%D0%B3%D0%BE%D1%80%D1%8B&type=photo')
    btn_inline_1_2 = InlineKeyboardButton('Море', url='https://ru.freepik.com/search?ai=excluded&format=search&last_filter=query&last_value=%D0%BC%D0%BE%D1%80%D0%B5&query=%D0%BC%D0%BE%D1%80%D0%B5&type=photo')
    btn_inline_1_3 = InlineKeyboardButton('Пустыня', url='https://ru.freepik.com/search?ai=excluded&format=search&last_filter=query&last_value=%D0%BF%D1%83%D1%81%D1%82%D1%8B%D0%BD%D1%8F&query=%D0%BF%D1%83%D1%81%D1%82%D1%8B%D0%BD%D1%8F&type=photo')
    btn_inline_1_4 = InlineKeyboardButton('Как беречь природу', url='https://foxford.ru/wiki/okruzhayuschiy-mir/ohrana-givoy-prirodi?utm_referrer=https%3A%2F%2Fyandex.ru%2F')

    keyboard_inline.add(btn_inline, btn_inline_1_2, btn_inline_1_3, btn_inline_1_4)

    return keyboard_inline


def get_keyboard_inline_2():
    keyboard_inline_2 = InlineKeyboardMarkup(row_width=2)
    btn_inline_2 = InlineKeyboardButton('Космос', url='https://ru.freepik.com/search?ai=excluded&format=search&last_filter=query&last_value=%D0%BA%D0%BE%D1%81%D0%BC%D0%BE%D1%81&query=%D0%BA%D0%BE%D1%81%D0%BC%D0%BE%D1%81&type=photo')
    btn_inline_3 = InlineKeyboardButton('Статья о космосе', url='https://starwalk.space/ru/news/what-is-space')
    keyboard_inline_2.add(btn_inline_2, btn_inline_3)
    return keyboard_inline_2


