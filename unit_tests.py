import unittest
from spellchecker import *

class TestListOperations(unittest.TestCase):

    def setUp(self):
        self.word1 = 'conspiracy'
        self.word2 = 'Achaean'
        self.word3 = 'HHHAAAoAiiIPPppPPyyYYYYy'

    def test_free_vowels(self):
        self.assertEqual(create_key(self.word1), 'c_nsp_r_cy')
        self.assertEqual(create_key(self.word2), '_ch_n')
        self.assertEqual(create_key(self.word3), 'h_py')

if __name__ == '__main__':
    unittest.main()