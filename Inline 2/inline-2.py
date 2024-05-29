from aiogram import Dispatcher, Bot, types, executor
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
import random
from datetime import datetime


TOKEN_API = '7447805026:AAEwdeQ9Tdgwt2wlh0EN7tfqqShb9BPjfHI'
bot = Bot(token=TOKEN_API)
dp = Dispatcher(bot)

keyboard1 = InlineKeyboardMarkup(row_width=1)
btn1 = InlineKeyboardButton('Переключиться на клавиатиру 2', callback_data='go_to_2')
btn1_2 = InlineKeyboardButton('Отправь случайное число', callback_data= 'send_random_number')
keyboard1.add(btn1, btn1_2)



keyboard2 = InlineKeyboardMarkup(row_width=1)
btn2 = InlineKeyboardButton('Переключиться на клавиатиру 1', callback_data='go_to_1')
btn2_2 = InlineKeyboardButton('Текущее время', callback_data='send_datetime')
keyboard2.add(btn2, btn2_2)






@dp.message_handler(commands='start')
async def start (message: types.Message):
    await message.reply('Ты на клавиатуре 1, нажми на кнопку,чтобы перейти на 2 клавиатуру', reply_markup=keyboard1)


@dp.callback_query_handler(lambda c: c.data == 'send_random_number')
async def random_number(callback_query: types.CallbackQuery):
    random_number = random.randint(1, 100)
    await callback_query.message.answer(f'Ваше случайное число:{random_number}')


@dp.callback_query_handler(lambda c: c.data == 'send_datetime')
async def send_datetime(callback_query: types.CallbackQuery):
    curent_time = datetime.now().strftime("%H:%M:%S")
    await callback_query.message.answer(f'Текущее время:{curent_time}')



@dp.callback_query_handler(lambda c: c.data == 'go_to_2')
async def go_to_2(callback_query: types.CallbackQuery):
    await callback_query.message.edit_text('Ты перешёл на 2 клавиатуру, нажми на кнопку, чтобы перейти на 1 клавиатуру',
                                           reply_markup=keyboard2)



@dp.callback_query_handler(lambda c: c.data == 'go_to_1')
async def go_to_1(callback_query: types.CallbackQuery):
    await callback_query.message.edit_text('Ты перешёл на 1 клавиатуру, нажми на кнопку, чтобы перейти на 2 клавиатуру',
                                           reply_markup=keyboard1)



if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)