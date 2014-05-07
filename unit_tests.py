import unittest
from spellchecker import *

class TestListOperations(unittest.TestCase):

    def setUp(self):
        self.word1 = 'conspiracy'
        self.word2 = 'Achaean'
        self.word3 = 'HHHAAAoAiiIPPppPPyyYYYYy'
        self.word4 = 'conect'
        self.dictionary = { 'c_n_ct' : ['connect']}

    def test_create_key(self):
        self.assertEqual(create_key(self.word1), 'c_nsp_r_cy')
        self.assertEqual(create_key(self.word2), '_ch_n')
        self.assertEqual(create_key(self.word3), 'h_py')

# ['Catt', 'cat', 'coat', 'coot', 'cot', 'cut']

# 'conect' should NOT produce 'connect' as suggestion
# 'caat' should NOT produce 'Catt' as suggestion

    def test_is_valid_spellcheck(self):
        self.assertEqual(is_valid_spellcheck('conect', 'connect'), False) 
        self.assertEqual(is_valid_spellcheck('cOOnnnnnneaaact', 'connect'), True)
        self.assertEqual(is_valid_spellcheck('CUNsperrICY', 'conspiracy'), True)
        self.assertEqual(is_valid_spellcheck('inSIDE  ', 'inside'), True)
        self.assertEqual(is_valid_spellcheck('   jjoobbb', 'job'), True)
        self.assertEqual(is_valid_spellcheck('AchhHhhHhheiiiiIiAiNnNnNn', 'Aachen'), False) 
        self.assertEqual(is_valid_spellcheck('AchhHhhHhheiiiiIiAiNnNnNn', 'Achaean'), True)
        self.assertEqual(is_valid_spellcheck('caaat', 'Catt'), False) 
        self.assertEqual(is_valid_spellcheck('caaat', 'cat'), True) 

if __name__ == '__main__':
    unittest.main()