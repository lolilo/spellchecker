spellchecker
============

An English dictionary is [seeded](https://github.com/lolilo/spellchecker/blob/master/spellchecker.py#L30) by the following [rules](https://github.com/lolilo/spellchecker/blob/master/spellchecker.py#L27), 

Keys

* [all lower-case](https://github.com/lolilo/spellchecker/blob/master/spellchecker.py#L56)
* [adjacent duplicated letters removed](https://github.com/lolilo/spellchecker/blob/master/spellchecker.py#L18)
* [vowels replaced with '_'](https://github.com/lolilo/spellchecker/blob/master/spellchecker.py#L9)

[Values](https://github.com/lolilo/spellchecker/blob/master/spellchecker.py#L43) are directly mapped from raw strings taken from seed file. For example, the words 'Aachen' and 'Achaean' will both produce the key '_ch_n'. The key value pair will then be '_ch_n' : ['aachen', 'achaean'].

To account for user input that is already spelled correctly, we also populate the dictionary with [correctly spelled words as idential keys and values](https://github.com/lolilo/spellchecker/blob/master/spellchecker.py#L50).

When spellchecking the input 'AchhHhhHhheiiiiIiAiNnNnNn', we [transform this input](https://github.com/lolilo/spellchecker/blob/master/spellchecker.py#L72) into the key _ch_n with the same functions used in populating our dictionary. The key _ch_n maps to ['aachen', 'achaean']. However, according to our rules, 'aachen' will be a false match for 'AchhHhhHhheiiiiIiAiNnNnNn'. We must [check the validity of the returned value](https://github.com/lolilo/spellchecker/blob/master/spellchecker.py#L80) before displaying the suggestion to the user. We loop through the list of potential suggestions and return a suggestion that passes our validity check. If we exhaust the list (or if the key created from the user's input does not map to any values), we return ["NO SUGGESTION"](https://github.com/lolilo/spellchecker/blob/master/spellchecker.py#L103). 

    word is achhhhhhhheiiiiiiainnnnnn
    key is  _ch_n
    key maps to value ['aachen', 'achaean']
    user_input with free vowels is  _chhhhhhhh_________nnnnnn
    potential word with free vowels is  __ch_n -- this does not pass our validity checker
    user_input with free vowels is  _chhhhhhhh_________nnnnnn
    potential word with free vowels is  _ch___n
    For _ch_n, spellchecker produces 'achaean' and not 'aachen'.

Another example, conect should not produce a suggestion according to our rules. 

    word is conect
    key is  c_n_ct
    key maps to value ['connect']
    user_input with free vowels is  c_n_ct
    potential word with free vowels is c_nn_ct
    c_n_ct does not have the minimum number of 'n' characters, so the spellchecker produces NO SUGGESTION

incorrect_word_generator.py produces misspellings of words in our dictionary in order for us to test the integrity of spellchecker.py.
    
    $ python incorrect_word_generator.py | python spellchecker.py
