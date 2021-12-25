from xml.dom import minidom


def size_constant():
    return 29


def max_questions():
    return 174


class Test:

    def __init__(self):
        self.counters = [0] * size_constant()
        self.questionCounter = 0
        self.xmldoc = minidom.parse('fixture/test1.xml')
        self.condText = 'В своём ответе на вопрос выберите вариант, который наиболее точно описывает ваше отношение к тому, что там написано.'

    def __del__(self):
        self.xmldoc.unlink()

    def getcounters(self):
        return self.counters

    def getquestion(self):
        if self.questionCounter < max_questions():
            exercises = self.xmldoc.getElementsByTagName('exercise')
            number = exercises[self.questionCounter].getAttribute('n')
            itemlist = self.xmldoc.getElementsByTagName('question')
            question = itemlist[self.questionCounter].firstChild.nodeValue
            return '' + number + '. ' + question
        else:
            raise ValueError('Question number out of bounds!')

    def answerquestion(self, answer):
        exercises = self.xmldoc.getElementsByTagName('exercise')
        coln = int(exercises[self.questionCounter].getAttribute('col_n')) - 1
        self.questionCounter += 1
        self.counters[coln] += answer

    def getresult(self):
        return self.counters.index(max(self.counters))


class Answers:
    def __init__(self):
        self.xmldoc = minidom.parse('fixture/answer1.xml')
        self.xmldoc.normalize()
        self.startText = 'Вам подходят следующие специальности:\n'
        self.emptyText = 'К сожалению в данный момент в Политехническом университете нет подходящих для Вас специальностей.'
        self.warText = 'У Вас есть склонность к военным специальностям, поступайте на военную кафедру.'
        self.http = 'https://dep.spbstu.ru/edu/'


    def getanswer(self, number):
        if number >= 29:
            raise ValueError("Number of option can\'t be bigger than 29")
        else:
            if number == 14:
                return self.warText
            specials = self.xmldoc.getElementsByTagName('special')

            if not specials[number].childNodes:
                return self.emptyText

            answer = self.startText

            numbers_list = specials[number].getElementsByTagName('number')
            names_list = specials[number].getElementsByTagName('name')

            numsize = len(numbers_list)

            for index in range(0, numsize):
                numb = numbers_list[index].firstChild.nodeValue
                answer += numb
                name = names_list[index].firstChild.nodeValue
                answer = answer + ' ' + name + ' '
                answer = answer + self.http + numb + '/\n'

        return answer


# т.к. в питоне нет switch, то приходится пользоваться словарями
button_to_value = {
    'Да': 2,
    'Скорее да, чем нет': 1,
    'Не знаю': 0,
    'Скорее нет, чем да': -1,
    'Нет': -2,
}
