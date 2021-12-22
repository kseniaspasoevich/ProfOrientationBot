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

from src.choice1 import register_handlers_basic_commands
from src.choice2 import register_handlers_command_two
from src.config import cfs
from src.test1 import *

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


class GetAnswer(StatesGroup):
    answer = State()


# здесь вызываем бота
async def main():
    register_handlers_command_two(dp)
    register_handlers_basic_commands(dp)
    register_handlers_test(dp)

    await set_commands(bot)

    await dp.start_polling()


if __name__ == '__main__':
    asyncio.run(main())
