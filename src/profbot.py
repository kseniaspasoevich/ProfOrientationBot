import asyncio
from tkinter.tix import Form

import dp
import telebot
from aiogram import Bot, Dispatcher, types
from aiogram.bot import bot
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import Dispatcher, FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.types import BotCommand, message

import aiogram.utils.markdown as md
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ParseMode
from aiogram.utils import executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from aiogram import Dispatcher
from aiogram.dispatcher.filters.state import StatesGroup
from aiogram.types import message

from choice1 import register_handlers_basic_commands
from choice2 import register_handlers_command_two
from test1 import  button_to_value

from config import cfs

bot = Bot(token=cfs)
dp = Dispatcher(bot, storage=MemoryStorage())


async def set_commands(bot: Bot):
    commands = [
        BotCommand(command='/start', description='Добро пожаловать в бот Профориентатор!'),
        BotCommand(command='/help', description='Узнать больше'),
        BotCommand(command='/2', description='Политех в соцсетях'),
        BotCommand(command='/test', description='Начать тест'),
        BotCommand(command='/cancel', description='Отменить текущее действие'),
    ]
    await bot.set_my_commands(commands)


# здесь вызываем бота
async def main():
    register_handlers_command_two(dp)
    register_handlers_basic_commands(dp)
    #dp.register_message_handler(commands='help1',state='*')
    from test import cmd_start, process_answer_invalid, process_answer,cmd_help, Form
    dp.register_message_handler(cmd_help,commands='helptest',state='*')
    dp.register_message_handler(cmd_start, commands="starttest")
    dp.register_message_handler(process_answer,lambda message: message.text in button_to_value,state=Form.answer)
    dp.register_message_handler(process_answer_invalid,lambda message: message.text not in button_to_value, state=Form.answer)

    await set_commands(bot)

    await dp.start_polling()


if __name__ == '__main__':
    asyncio.run(main())
