import asyncio

from aiogram import Bot
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import Dispatcher
from aiogram.types import BotCommand

from choice1 import register_handlers_basic_commands
from choice2 import register_handlers_command_two
from config import cfs
from test import register_handlers_ege


async def set_commands(bot: Bot):
    commands = [
        BotCommand(command='/start', description='Добро пожаловать в бот Профориентатор!'),
        BotCommand(command='/help', description='Узнать больше'),
        BotCommand(command='/2', description='Политех в соцсетях'),
        BotCommand(command='/test', description='Начать тест'),
        BotCommand(command='/cancel', description='Отменить текущее действие'),
    ]
    await bot.set_my_commands(commands)


async def main():

    bot = Bot(token=cfs)
    dp = Dispatcher(bot, storage=MemoryStorage())

    register_handlers_command_two(dp)
    register_handlers_basic_commands(dp)
    register_handlers_ege(dp)

    await set_commands(bot)

    await dp.start_polling()


if __name__ == '__main__':
    asyncio.run(main())
