from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State

available_ege_disciplines = ['информатика', 'биология', 'физика'
    , 'химия', 'обществознание', 'иностранный язык'
    , 'базовая математика', 'профильная математика', 'литература'
    , 'история']


class ChooseDiscipline(StatesGroup):
    waiting_for_discipline_name = State()


async def choose_disciplines2(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    for name in available_ege_disciplines:
        keyboard.add(name)
    await message.answer('Выберите предметы, которые бы хотели сдавать\n'
                         'НАПОМИНАНИЕ: Русский язык уже включён!', reply_markup=keyboard)
    await ChooseDiscipline.waiting_for_discipline_name.set()


async def discipline_chosen(message: types.Message, state: FSMContext):
    if message.text.lower() not in available_ege_disciplines:
        await message.answer('Пожалуйста, выберите предмет из списка ниже!')
        return
    await state.update_data(chosen_disc=message.text.lower())

    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    for size in available_ege_disciplines:
        keyboard.add(size)
    # Для простых шагов можно не указывать название состояния, обходясь next()
    await ChooseDiscipline.next()
    await message.answer('Теперь выберите 3 предмет:', reply_markup=keyboard)


'''
async def all_disciplines_chosen(message: types.Message, state: FSMContext):
    if message.text.lower() not in available_ege_disciplines:
        await message.answer('Пожалуйста, выберите предмет из списка ниже.')
        return
    user_data = await state.get_data()
    await message.answer(f'Вы выбрали предметы:' {message.text.lower()} +{user_data['chosen_disc']}.'\n',
                         reply_markup=types.ReplyKeyboardRemove())
    await state.finish()
'''


def register_handlers_ege(dp: Dispatcher):
    dp.register_message_handler(choose_disciplines2, commands="test", state="*")
    dp.register_message_handler(discipline_chosen, state=ChooseDiscipline.waiting_for_discipline_name)
    # dp.register_message_handler(all_disciplines_chosen, state=ChooseDiscipline.waiting_for_discipline_name)
