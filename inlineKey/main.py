from aiogram import Bot, Dispatcher, types, executor
from config import TELEGRAM_TOKEN
from keyboard.keyboards import  get_keyboard_1, get_keyboard_2
from keyboard.key_inline import get_keyboard_inline_1, get_keyboard_inline_2
bot = Bot(token= TELEGRAM_TOKEN)
dp = Dispatcher(bot)



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
    await message.reply('Привет я эхо бот' , reply_markup=get_keyboard_1())


@dp.message_handler(lambda message: message.text == 'отправь фото кота')
async def btn_1_click(message: types.Message):
    await bot.send_photo(message.chat.id,
                         photo='https://trikky.ru/wp-content/blogs.dir/1/files/2021/06/25/img-20210625-wa0008.jpg', caption='Вот тебе кот', reply_markup=get_keyboard_inline_1())






@dp.message_handler(lambda message: message.text == 'след. клава')
async def btn_2_click(message: types.Message):
    await message.answer('Тут попросить фото собаки', reply_markup=get_keyboard_2())




@dp.message_handler(lambda message: message.text == 'отправь фото собаки')
async def btn_3_click(message: types.Message):
    await bot.send_photo(message.chat.id, photo='https://pichold.ru/wp-content/uploads/2019/07/animals.jpg', caption='Вот тебе собака', reply_markup=get_keyboard_inline_2())



@dp.message_handler(lambda message: message.text == 'вернуться назад')
async def back_1(message: types.Message):
    await message.answer('Тут попросить фото кота', reply_markup=get_keyboard_1())



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