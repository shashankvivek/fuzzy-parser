import unittest
from main.engine.tokenizer import Tokenizer


class TestTokenizer(unittest.TestCase):

    def test_get_parsed_data(self):
        token = Tokenizer('../../data/input.txt')
        lines = token.get_parsed_data()
        self.assertEqual(len(lines), 7)
