from profbot import *


@dp.message_handler(lambda message: message.text == 'Обучение')
async def education_button(message: types.Message):
    await message.reply('Отличный выбор университета!')


@dp.message_handler(lambda message: message.text == 'Студенческие отряды')
async def stud_organisations_button(message: types.Message):
    await message.reply('Их очень много. Можем расписать подробно')
