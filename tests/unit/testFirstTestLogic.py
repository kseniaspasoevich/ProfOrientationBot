import unittest

from random import randint


import sys
sys.path.append('.')
from src.test1 import Test, max_questions


class TestFirstTest(unittest.TestCase):
    def setUp(self):
        self.test = Test()
        pass

    def tearDown(self):
        del self.test
        pass

    def test_init(self):
        cond = True
        for index in range(len(self.test.counters)):
            if self.test.counters[index] != 0:
                cond = False
                break

        self.assertEqual(cond, True, 'Error! All counters must be initialized with zeroes!')
        self.assertEqual(self.test.questionCounter, 0)

    def test_getRandomQuestion(self):

        self.test.questionCounter = randint(0, max_questions() - 1)

        exercises = self.test.xmldoc.getElementsByTagName('exercise')
        number = exercises[self.test.questionCounter].getAttribute("n")
        itemlist = self.test.xmldoc.getElementsByTagName('question')
        question = itemlist[self.test.questionCounter].firstChild.nodeValue

        self.assertEqual(self.test.getquestion(), '' + number + '. ' + question,'Error! Get question returned '+self.test.getquestion()+" expected: "+'' + number + '. ' + question)

    def test_RaiseError(self):

        self.test.questionCounter = max_questions()
        self.assertRaises(ValueError, self.test.getquestion)

    def test_incrementSuitableCounter(self):
        exercises = self.test.xmldoc.getElementsByTagName('exercise')
        number = exercises[self.test.questionCounter].getAttribute('n')
        coln = int(exercises[self.test.questionCounter].getAttribute('col_n')) - 1

        prevquestionCounter = self.test.questionCounter

        prevCounterVal = self.test.counters[coln]

        answ = randint(-2, 2)

        self.test.answerquestion(answ)
        self.assertEqual(self.test.questionCounter, prevquestionCounter + 1)
        self.assertEqual(self.test.counters[coln], prevCounterVal + answ)

    def test_getResult(self):
        self.assertEqual(self.test.getresult(), self.test.counters.index(max(self.test.counters)))


if __name__ == "__main__":
    unittest.main()
