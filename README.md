spellchecker
============

An English dictionary is seeded by the following rules, 

Keys, 
1. all lower-case
2. adjacent duplicated letters removed
3. vowels replaced with '_'

Values, 

To account for user input that is already spelled correct, we also populate the dictionary with [correctly spelled words as idential keys and values](https://github.com/lolilo/spellchecker/blob/master/spellchecker.py#L50).



The input 'AchhHhhHhheiiiiIiAiNnNnNn' will transform to key _ch_n. In our dictionary, this maps to ['aachen', 'achaean'].


user_input with free vowels is  _chhhhhhhh_________nnnnnn
potential word is  __ch_n
user_input with free vowels is  _chhhhhhhh_________nnnnnn
potential word is  _ch___n


word is conect
key is  c_n_ct
['connect']
user_input with free vowels is  c_n_ct
potential word is  c_nn_ct
NO SUGGESTION
