
import unittest

import sys
sys.path.append('.')
from src.test1 import Answers, size_constant


class TestAnswers(unittest.TestCase):
    def setUp(self):
        self.answers = Answers()

    def tearDown(self):
        del self.answers

    def test_War_text(self):
        self.assertEqual(self.answers.getanswer(14), self.answers.warText,"Error! Special case war doesn't work!")

    def test_getAnswerThrow(self):
        self.assertRaises(ValueError, self.answers.getanswer, size_constant())


# Executing the te in the above test case class
if __name__ == "__main__":
    unittest.main()
