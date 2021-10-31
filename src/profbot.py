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
    await message.reply('Привет! Что бы Вы хотели проделать с нашим ботом?\n')


@dp.message_handler(commands='1')
async def process_command_one(message: types.Message):
    await message.reply('Давайте проведем тест!')


@dp.message_handler(commands='2')
async def process_command_two(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ['Обучение', 'Студенческие отряды']
    keyboard.add(*buttons)
    await message.answer('Выберите категорию', reply_markup=keyboard)


@dp.message_handler(commands='help')
async def process_help_command(message: types.Message):
    await message.reply('Напиши мне что-нибудь')


@dp.message_handler()
async def echo_message(msg: types.Message):
    await bot.send_message(msg.from_user.id, msg.text)


if __name__ == '__main__':
    executor.start_polling(dp)
