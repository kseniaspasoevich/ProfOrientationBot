import aiogram.utils.markdown as md
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ParseMode
from test1 import Test, Answers, MAX_QUESTIONS, button_to_value
from profbot import bot

test11 = Test()


class Form(StatesGroup):
    answer = State()



async def cmd_help(message: types.Message):

    global test11
    await bot.send_message(message.chat.id,md.text(test11.condText))

async def cmd_start(message: types.Message):
    global test11
    test11 = Test()
    await Form.answer.set()
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, selective=True)
    for nameb in button_to_value:
        markup.add(nameb)

    await  bot.send_message(message.chat.id,
                               md.text(test11.getquestion()), reply_markup=markup)



async def process_answer(message: types.Message, state: FSMContext):

    global test11
    async with state.proxy() as data:
        data['answer'] = message.text
        name1 = button_to_value[data['answer']]
        test11.answerquestion(name1)
    global counter
    if test11.questionCounter < MAX_QUESTIONS()/40:#потом верну 174 сейчас не буду

        await bot.send_message(message.chat.id,
                               md.text(test11.getquestion()))
        await Form.first()
    else:
        await Form.next()
        markup = types.ReplyKeyboardRemove()
        await bot.send_message(message.chat.id,md.text("Тест завершён, рекомендуемые специальности приведены ниже!"), reply_markup=markup, parse_mode=ParseMode.MARKDOWN)
        await state.finish()
        answr = Answers()
        await bot.send_message(message.chat.id,md.text(answr.getAnswer(test11.getresult())))
        del test11
        del answr




async def process_answer_invalid(message: types.Message):
    return await message.reply("Неверный ответ, выберите допустимый среди имеющихся кнопок")

