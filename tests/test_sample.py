import unittest
from unittest.mock import mock_open, patch
from scr import clearword, starter

class MyTestCase(unittest.TestCase):
    def test_answer1(self):
        self.assertEqual(starter(['-s', '1234']), 4)
    
    def test_answer3(self):
        m = mock_open(read_data='qwerty\nddsdsd')
        with patch('builtins.open', m):
            with open('foo') as mock_file:
                file = mock_file.readlines()
                self.assertEqual([clearword(string.strip()) for string in file], [6, 2])