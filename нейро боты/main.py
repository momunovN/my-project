from aiogram import Bot, Dispatcher, types, executor
from neiro.bottt import generate_image
from neiro.neiro_assistent import get_response
from    neiro.neiro_consultant import get_sovet


Api = '7389563455:AAHuVhbamX6RumY9e7bYk7xIRxj-mt2-NpE'
bot = Bot(token= Api)
dp = Dispatcher(bot)


@dp.message_handler(commands= 'start')
async def start(message: types.Message):
    await message.answer('Привет, я бот шедеврум от Яндекс. Я сгенерирую картинку по вашему запросу')




@dp.message_handler(commands='sovet')
async def analize_message(message: types.Message):
    user = message.get_args()
    response_text = await get_sovet(user)
    await message.answer(response_text)


@dp.message_handler(commands='generate_image')
async def handler_message(message: types.Message):
    user = message.get_args()
    response_text = await get_response(user)
    user_text = response_text
    await message.reply(f"Вот твой улучшенный промпт {user_text}")
    print(user_text)
    await message.reply('Ожидайте, идет генерация изображения ')

    try:
        image_data = generate_image(user_text)
        await message.reply_photo(photo=image_data)
    except Exception as e:
        await message.reply(f"Уфы, ошибка: {e}")




if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)