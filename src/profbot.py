import asyncio

from aiogram import Bot
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import Dispatcher
from aiogram.types import BotCommand

from startCommands import register_handlers_basic_commands
from mediaCommand import register_handlers_command_two
from test1 import button_to_value
from config import cfs

bot = Bot(token=cfs)
dp = Dispatcher(bot, storage=MemoryStorage())


async def set_commands(bot: Bot):
    commands = [
        BotCommand(command='/start', description='Добро пожаловать в бот Профориентатор!'),
        BotCommand(command='/help', description='Узнать больше о боте'),
        BotCommand(command='/media', description='Политех в соцсетях'),
        BotCommand(command='/starttest', description='Начать тест'),
        BotCommand(command='/helptest', description='Как решать тест'),
        BotCommand(command='/cancel', description='Отменить текущее действие'),
    ]
    await bot.set_my_commands(commands)


async def main():
    register_handlers_command_two(dp)
    register_handlers_basic_commands(dp)
    from test import cmd_start, process_answer_invalid, process_answer, cmd_help, Form
    dp.register_message_handler(cmd_help, commands='helptest', state='*')
    dp.register_message_handler(cmd_start, commands='starttest')
    dp.register_message_handler(process_answer, lambda message: message.text in button_to_value, state=Form.answer)
    dp.register_message_handler(process_answer_invalid, lambda message: message.text not in button_to_value, state=Form.answer)

    await set_commands(bot)

    await dp.start_polling()


if __name__ == '__main__':
    asyncio.run(main())
