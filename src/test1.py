from xml.dom import minidom

# в  питоне констант нет поэтому можно делать так
from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import state
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.types import message


def SIZE_CONSTANT():
    return 29


def MAX_QUESTIONS():
    return 174


class Test:

    def __init__(self):
        self.counters = [0] * SIZE_CONSTANT()
        self.questionCounter = 0
        self.xmldoc = minidom.parse('test1.xml')
        self.condText = "Если Вам очень нравится то, о чем спрашивается в вопросе, в бланке ответов рядом с его " \
                        "номером " \
                        "поставьте два плюса (++), если просто нравится - один плюс (+), если не знаете, сомневаетесь " \
                        "- " \
                        "ноль (0), если не нравится - один минус (-), а если очень не нравиться - два минуса (--). " \
                        " Исправим это позже. НАЧИНАЕМ ТЕСТ: Нажмите команду /begin"
        self.startText = "Любите ли Вы? Нравится ли Вам? Хотели бы Вы "
        pass

    def __del__(self):
        self.xmldoc.unlink()
        pass

    def getcounters(self):
        return self.counters

    def getquestion(self):
        if self.questionCounter < MAX_QUESTIONS():
            # вызываем здесь minidom и получаем тест вопроса по question counter
            exercises = self.xmldoc.getElementsByTagName('exercise')
            number = exercises[self.questionCounter].getAttribute("n")
            itemlist = self.xmldoc.getElementsByTagName('question')
            question = itemlist[self.questionCounter].firstChild.nodeValue
            return "" + number + ". " + question
        else:
            raise ValueError('Represents a hidden bug, do not catch this')
        pass

    def answerquestion(self, answer):

        # Здесь получаем тескт(а может быть и число раз кнопок 5) вопроса и далее увеличваем нужный счётчик(как я не знаю)
        exercises = self.xmldoc.getElementsByTagName('exercise')
        number = exercises[self.questionCounter].getAttribute("n")
        colN = int(exercises[self.questionCounter].getAttribute("col_n")) - 1
        self.questionCounter += 1
        self.counters[colN] += answer

        # кинуть исключение или написать, что пользователь не то сделал

    def getresult(self):
        # пусть пока получаем в качестве результата максимум counters
        return self.counters.index(max(self.counters))


class Answers:
    xmldoc = minidom.parse('answer1.xml')
    xmldoc.normalize()
    startText = "Вам подходят следующие специальности:\n"
    emptyText = "К сожалению в данный момент в Политехническом университете нет подходящих для Вас специальностей."
    warText = "У Вас есть склонность к военным специальностям, поступайте на военную кафедру."
    http = "https://dep.spbstu.ru/edu/"

    def getAnswer(self, number):  # number - это максимальный counters
        if number == 14:
            return self.warText
        specials = self.xmldoc.getElementsByTagName('special')

        if not specials[number].childNodes:
            return self.emptyText

        answer = self.startText

        numbersList = specials[number].getElementsByTagName('number')
        namesList = specials[number].getElementsByTagName('name')

        for i in range(0, len(numbersList)):
            numb = numbersList[i].firstChild.nodeValue
            answer = answer + numb
            name = namesList[i].firstChild.nodeValue
            answer = answer + " " + name + " "
            answer = answer + self.http + numb + "/\n"

        return answer


# т.к. в питоне нет switch, то приходится пользоваться словарями
button_to_value = {
    'Да': 2,
    'Скорее да, чем нет': 1,
    'Не знаю': 0,
    'Скорее нет, чем да': -1,
    'Нет': -2
}

a = Test()


# ответы из словаря выше
class GetAnswer(StatesGroup):
    answer = State()


# здесь создаем кнопки с ответами
async def set_answers_to_keyboards(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    for response in button_to_value:
        keyboard.add(response)
    await GetAnswer.answer.set()
    await message.answer(a.condText, reply_markup=keyboard)


# здесь начинаем тест
async def begin_test(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    for response in button_to_value:
        keyboard.add(response)
    await GetAnswer.answer.set()
    await message.answer(a.getquestion())


async def process_chosen_answers(message: types.Message, state: FSMContext):
    await state.update_data(chosen_answer=message.text.lower())
    # Для последовательных шагов можно не указывать название состояния, обходясь next()
    await GetAnswer.next()
    await message.answer(Answers.getAnswer(Answers, a.getresult()))


def register_handlers_test(dp: Dispatcher):
    dp.register_message_handler(set_answers_to_keyboards, commands="test", state="*")  # ok
    dp.register_message_handler(begin_test, commands="begin", state="*")  # ok
    dp.register_message_handler(process_chosen_answers, state=GetAnswer.answer)
