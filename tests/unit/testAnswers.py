
import unittest

import sys
sys.path.append(".")
from src.test1 import Answers, SIZE_CONSTANT





class TestAnswers(unittest.TestCase):
    # setUp method is overridden from the parent class TestCase
    def setUp(self):
        self.answers = Answers()

    def tearDown(self):
        del self.answers

    # Each test method starts with the keyword test_
    def test_War_text(self):
        self.assertEqual(self.answers.getAnswer(14), self.answers.warText)

    def test_getAnswerThrow(self):
        self.assertRaises(ValueError, self.answers.getAnswer, SIZE_CONSTANT())


# Executing the te in the above test case class
if __name__ == "__main__":
    unittest.main()