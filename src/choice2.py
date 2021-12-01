from aiogram import types, Dispatcher


async def process_command_two(message: types.Message):
    buttons = [
        types.InlineKeyboardButton(text='Вконтакте', url='https://vk.com/polytech_petra'),
        types.InlineKeyboardButton(text='Telegram', url='https://t.me/polytech_petra'),
        types.InlineKeyboardButton(text='Instagram', url='https://www.instagram.com/polytech_petra/'),
        types.InlineKeyboardButton(text='Facebook', url='https://www.facebook.com/spbstu.official'),
    ]
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    keyboard.add(*buttons)
    await message.answer('Выберите сервис: ', reply_markup=keyboard)


def register_handlers_command_two(dp: Dispatcher):
    dp.register_message_handler(process_command_two, commands='2', state='*')
