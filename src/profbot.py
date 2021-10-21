"""
this is out main
coding starts here
"""
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

from config import cfs

bot = Bot(token=cfs)
dp = Dispatcher(bot)


@dp.message_handler(commands='start')
async def process_start_command(message: types.Message):
    await message.reply('Привет! Что бы Вы хотели проделать с нашим ботом?\n'
                        'Тест профориентации (1)\n'
                        'Просто узнать больше о Политехе(2)')


@dp.message_handler(commands='1')
async def process_command_one(message: types.Message):
    await message.reply('Хорошо!\nДавайте проведем тест!')


@dp.message_handler(commands='2')
async def process_command_two(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ['Обучение', 'Студенческие отряды', 'Общежития', 'Преподаватели', 'Баллы ЕГЭ']
    keyboard.add(*buttons)
    await message.answer('Выберите категорию, пожалуйста.', reply_markup=keyboard)


@dp.message_handler(commands='help')
async def process_help_command(message: types.Message):
    await message.reply('Напиши мне что-нибудь, и я отправлю этот текст тебе в ответ! '
                        'Пока не расписали логику бота(')


@dp.message_handler(lambda message: message.text == 'Обучение')
async def education_button(message: types.Message):
    await message.reply('Отличный выбор университета!')


@dp.message_handler(lambda message: message.text == 'Студенческие отряды')
async def stud_organisations_button(message: types.Message):
    await message.reply('Их очень много. Можем расписать подробно, '
                        'если заинтересованы')


@dp.message_handler(lambda message: message.text == 'Общежития')
async def dorms_button(message: types.Message):
    await message.reply('Не отлично, но и не ужасно')


@dp.message_handler(lambda message: message.text == 'Преподаватели')
async def teachers_button(message: types.Message):
    await message.reply('В основном, хорошие')


@dp.message_handler(lambda message: message.text == 'Баллы ЕГЭ')
async def ege_button(message: types.Message):
    await message.reply('Зависит уже от направления')


@dp.message_handler()
async def echo_message(msg: types.Message):
    await bot.send_message(msg.from_user.id, msg.text)


if __name__ == '__main__':
    executor.start_polling(dp)

