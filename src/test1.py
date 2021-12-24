from xml.dom import minidom

# в  питоне констант нет поэтому можно делать так


def SIZE_CONSTANT():
    return 29


def MAX_QUESTIONS():
    return 174


class Test:

    def __init__(self):
        self.counters = [0] * SIZE_CONSTANT()
        self.questionCounter = 0
        self.xmldoc = minidom.parse('src/test1.xml')
        self.condText = "Если Вам очень нравится то, о чем спрашивается в вопросе, в своём ответе выберите вариант " \
                        ", который  " \
                        "наиболее точно описывает ваше отношение."
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
    xmldoc = minidom.parse('src/answer1.xml')
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


