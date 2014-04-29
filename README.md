spellchecker
============

An English dictionary is seeded by the following rules, 

Keys, 
1. all lower-case
2. adjacent duplicated letters removed
3. vowels replaced with '_'

Values are directly mapped from raw strings taken from seed file. For example, the words 'Aachen' and 'Achaean' will both produce the key '_ch_n'. The key value pair will then be '_ch_n' : ['aachen', 'achaean'].

To account for user input that is already spelled correctly, we also populate the dictionary with [correctly spelled words as idential keys and values](https://github.com/lolilo/spellchecker/blob/master/spellchecker.py#L50).

When spellchecking the input 'AchhHhhHhheiiiiIiAiNnNnNn', we transform this input into the key _ch_n with the same functions used in populating our dictionary. This maps to ['aachen', 'achaean']. However, according to our rules, 'aachen' will be a false match for 'AchhHhhHhheiiiiIiAiNnNnNn'. We must check the validity of the returned value before displaying the suggestion to the user. 




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
