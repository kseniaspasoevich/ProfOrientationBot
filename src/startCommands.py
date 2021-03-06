from aiogram import types, Dispatcher


async def process_start_command(message: types.Message):
    await message.reply('Привет! Что бы Вы хотели проделать с нашим ботом?\n'
                        '/starttest-Тест профориентации\n'
                        '/media-Политех в соцсетях\n'
                        '/help-Помочь с ботом')


async def process_help_command(message: types.Message):
    await message.reply('Абитуриенты не всегда понимают куда лучше всего поступать. Большое количество иногда схожих '
                        'направлений,вызывает путаницу и студент не может выбрать направление подходящее к его '
                        'запросам. Наш бот предоставляет возможность абитуриенту получить информацию о направлениях, '
                        'которые могут ему подойти лучше всего.')


def register_handlers_basic_commands(dp: Dispatcher):
    dp.register_message_handler(process_start_command, commands='start', state='*')
    dp.register_message_handler(process_help_command, commands='help', state='*')
