from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils import executor
import requests
import base64
import time
from random import randint

API_TOKEN = '7389563455:AAHuVhbamX6RumY9e7bYk7xIRxj-mt2-NpE'
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    keyboard = InlineKeyboardMarkup()
    keyboard.add(InlineKeyboardButton("Сгенерировать картинку", callback_data='generate_image'))
    await message.answer('Привет, я бот шедеврум от Яндекс, генерирую картинки по запросу. Нажмите кнопку ниже для генерации картинки:',
                         reply_markup=keyboard)

@dp.callback_query_handler(lambda query: query.data == 'generate_image')
async def button_pressed(query: types.CallbackQuery):
    await query.message.answer("Напиши запрос для генерации изображения")

@dp.message_handler(lambda message: message.text)
async def generate_image_from_text(message: types.Message):
    prompt_text = message.text
    await message.answer('Ожидайте, идет генерация изображения...')  # Add this line
    image_data = generate_image(prompt_text)
    await bot.send_photo(message.from_user.id, photo=image_data, caption=f"Вот ваш запрос: {prompt_text}")


def generate_image(prompt_text):
    prompt = {
        "modelUri": "art://b1gvhp2b702b3kvoqti3/yandex-art/latest",
        "generationOptions": {
            "seed": randint(10000, 2000000)
        },
        "messages": [
            {
                "weight": 1,
                "text": prompt_text
            }
        ]
    }


    url = "https://llm.api.cloud.yandex.net/foundationModels/v1/imageGenerationAsync"
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Api-Key AQVNwJ0beANsfkeszeGmC7BPmiqLB9uPpJuYGFtj"
    }
    print()
    response = requests.post(url=url, headers=headers, json=prompt)
    result = response.json()

    operation_id = result['id']
    operation_url = f"https://llm.api.cloud.yandex.net:443/operations/{operation_id}"
    while True:
        operation_response = requests.get(url=operation_url, headers=headers)
        operation_result = operation_response.json()
        if 'response' in operation_result:
            image_base64 = operation_result['response']['image']
            image_data = base64.b64decode(image_base64)
            return image_data
        else:
            print('Ожидайте, изображение не готово')
            time.sleep(5)

@dp.message_handler()
async def handler_message(message: types.Message):
    user_text = message.text
    await message.reply('Ожидайте, идет генерация изображения ')

    try:
        image_data = generate_image(user_text)
        await message.reply_photo(photo=image_data)
    except Exception as e:
        await message.reply(f"Уфы, ошибка: {e}")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
