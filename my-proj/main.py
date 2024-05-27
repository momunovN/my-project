from aiogram import Bot, Dispatcher, types, executor

from config import TELEGRAM_TOKEN

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
    await message.reply('Привет я эхо бот')


@dp.message_handler(commands= 'help')
async def help(message: types.Message):
    await message.reply('Чем я могу тебе помочь?')

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