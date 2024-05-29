from aiogram import Bot, Dispatcher, types, executor
from config import TELEGRAM_TOKEN
from keyboard.keyboards import  get_keyboard_1, get_keyboard_2
from keyboard.key_inline import get_keyboard_inline_1, get_keyboard_inline_2
from database.database import initialize_db, add_user, get_user

bot = Bot(token= TELEGRAM_TOKEN)
dp = Dispatcher(bot)

initialize_db()



async def set_commands(bot: Bot):
    commands = [
        types.BotCommand(command='/start', description='Запустить'),
        types.BotCommand(command='/help', description='Помощь'),
        types.BotCommand(command='/about', description='О нас'),
        types.BotCommand(command='/hi', description='Hi'),
        types.BotCommand(command='/iecho', description='Эхо')
    ]
    await bot.set_my_commands(commands)


@dp.message_handler(commands= 'start')
async def start(message: types.Message):
    user = get_user(message.from_user.id)
    if user is None:
        add_user(message.from_user.id, message.from_user.username, message.from_user.first_name, message.from_user.last_name)
        await message.reply('Привет я эхо бот' , reply_markup=get_keyboard_1())
    else:
        await message.reply('Привет я эхо бот', reply_markup=get_keyboard_1())

@dp.message_handler(lambda message: message.text == 'Отправь фото природы')
async def btn_1_click(message: types.Message):
    await bot.send_photo(message.chat.id,
                         photo='https://mykaleidoscope.ru/x/uploads/posts/2022-10/1666361538_47-mykaleidoscope-ru-p-peizazhi-prirodi-krasivo-52.jpg',
                         caption='Вот природа', reply_markup=get_keyboard_inline_1())






@dp.message_handler(lambda message: message.text == 'след. клава')
async def btn_2_click(message: types.Message):
    await message.answer('Тут попросить фото космоса', reply_markup=get_keyboard_2())




@dp.message_handler(lambda message: message.text == 'отправь фото из космоса')
async def btn_3_click(message: types.Message):
    await bot.send_photo(message.chat.id, photo='https://w-dog.ru/wallpapers/4/3/304282222858937/vselennaya-nebo-tumannost-planeta.jpg',
                         caption='Вот тебе космос', reply_markup=get_keyboard_inline_2())



@dp.message_handler(lambda message: message.text == 'вернуться назад')
async def back_1(message: types.Message):
    await message.answer('Тут попросять фото природы', reply_markup=get_keyboard_1())



@dp.message_handler(commands= 'help')
async def help(message: types.Message):
    await message.reply('Чем я могу тебе помочь?' )

@dp.message_handler(commands= 'about')
async def about (message: types.Message):
    await message.reply('Я эхо-бот ......')

@dp.message_handler(commands= 'hi')
async def hi (message: types.Message):
    await message.reply('Привееееееетттик.....')

@dp.message_handler(commands= 'I-echo')
async def iecho (message: types.Message):
    await message.reply('Привееееееетттик.....')


@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(message.text)




async def on_startup(dispatcher):
    await set_commands(dispatcher.bot)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup )