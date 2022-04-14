import unittest
import Basic_Class


class Testing(unittest.TestCase):
    def test_adding_numbers(self):
        basic_class = Basic_Class.Basic_Class()
        a = 9
        b = -1
        self.assertEqual(8, basic_class.addNumbers(a,b))

    def test_leetSpeak(self):
        basic_class = Basic_Class.Basic_Class()
        text = 'TEST'
        expected_leet_speak = '+35+'
        self.assertEqual(expected_leet_speak, basic_class.generateLeetSpeak(text))

if __name__ == '__main__':
    unittest.main()