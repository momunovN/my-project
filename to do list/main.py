
from aiogram import Dispatcher, executor, Bot, types
from config import API_KEY
import database


bot = Bot(token=API_KEY)
dp = Dispatcher(bot)

database.init_db()


async def set_commands(bot: Bot):
    commands = [
        types.BotCommand(command='/start', description='Запустить'),
        types.BotCommand(command='/help', description='Помощь'),
        types.BotCommand(command='/list', description='Список'),

    ]
    await bot.set_my_commands(commands)




@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.reply('Привет, я твой TO DO list\n '
                        'Нажми на команду /help для информации')

@dp.message_handler(commands=['help'])
async def help(message: types.Message):
    await message.reply('Команды - /add + Текст - командай для добавление задач\n '
                        '/list - список задач\n'
                        '/delete + <Номер задачи> -Команда для удаление')


@dp.message_handler(commands=['add'])
async def add(message: types.Message):
    task = message.get_args()
    if task == True:
        user_id = message.from_user.id
        username = message.from_user.username
        database.add_task(user_id, username, task)
        await message.reply(f"Задача {task} добавлена")
    else:
        await message.reply('Задача не может быть пустой. Пожалуйста, укажите задачу через команду /add')
    print(task)

# @dp.message_handler(commands=['add'])
# async def add(message: types.Message):
#     task = message.get_args()
#     if task:
#         user_id = message.from_user.id
#         username = message.from_user.username
#         if not database.task_exists(user_id, task):
#             database.add_task(user_id, username, task)
#             await message.reply(f"Задача {task} добавлена")
#         else:
#             await message.reply('Задача уже существует')
#     else:
#         await message.reply('Задача не может быть пустой. Пожалуйста, укажите задачу через команду /add')
#     print(task)


@dp.message_handler(commands=['list'])
async def listt(message: types.Message):
    tasks = database.get_task()
    if tasks:
        tasks_list = "\n".join([f"{task[0]}. {task[3]} (Добавлена пользователем @{task[2]})" for task in tasks])
        await message.reply(f"Ваши задачи: \n{tasks_list}")
    else:
        await message.reply('Ваш список задач пуст')
    print(tasks)

@dp.message_handler(commands=['delete'])
async def delete(message: types.Message):
    task_id = message.get_args()
    if task_id.isdigit():
        database.delete_tasks(int(task_id))
        tasks = database.get_task()
        for i, task in enumerate(tasks):
            database.update_task_id(task[0], i + 1)
        await message.reply(f"Задача {task_id} удалена")
    else:
        await message.reply('Укажите корректный id задачи ')
    print(task_id)



# @dp.message_handler(commands=['delete'])
# async def delete(message: types.Message):
#     task_id = message.get_args()
#     if task_id.isdigit():
#         user_id = message.from_user.id
#         if database.task_exists(user_id, task_id):
#             database.delete_tasks(int(task_id))
#             tasks = database.get_tasks(user_id)
#             for i, task in enumerate(tasks):
#                 database.update_task_id(task[0], i + 1)
#             await message.reply(f"Задача {task_id} удалена")
#         else:
#             await message.reply('Задача не существует')
#     else:
#         await message.reply('Укажите корректный id задачи ')
#     print(task_id)

async def on_startup(dp: Dispatcher):
    await set_commands(dp.bot)




if __name__ == '__main__':
    executor.start_polling(dp, skip_updates= True, on_startup=on_startup)