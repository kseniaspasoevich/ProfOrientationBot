import unittest
import os.path
import xml
from xml.dom import minidom


class FileIntegrityTests(unittest.TestCase):
    def setUp(self):
        self.str1 = 'fixture/answer1.xml'
        self.str2 = 'fixture/test1.xml'
        pass

    def tearDown(self):
        pass

    def test_file_exists(self):
        self.assertTrue(os.path.isfile(self.str1), self.str1 + " does not exist!")
        self.assertTrue(os.path.isfile(self.str2), self.str2 + " does not exist!")

    def test_valid_XMLs(self):

        state = True
        try:
            minidom.parse(self.str1)

        except xml.parsers.expat.ExpatError:
            state = False
        finally:
            self.assertTrue(state, self.str1 + " is not a valid xml!")
            pass

        try:
            minidom.parse(self.str2)

        except xml.parsers.expat.ExpatError:
            state = False
        finally:
            self.assertTrue(state, self.str2 + " is not a valid xml!")
            pass


if __name__ == '__main__':
    unittest.main()
