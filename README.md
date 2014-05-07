Spellchecker
============

Overview
------------------
To run on your machine, choose either a full dictionary or a toy dictionary in [spellchecker.py](https://github.com/lolilo/spellchecker/blob/master/spellchecker.py#L4) and [incorrect_word_generator.py](https://github.com/lolilo/spellchecker/blob/master/incorrect_word_generator.py#L4). 

An English dictionary is [seeded](https://github.com/lolilo/spellchecker/blob/master/spellchecker.py#L32) by the following [rules](https://github.com/lolilo/spellchecker/blob/master/spellchecker.py#L27), 

Keys

* [all lower-case](https://github.com/lolilo/spellchecker/blob/master/spellchecker.py#L29)
* [adjacent duplicated letters removed](https://github.com/lolilo/spellchecker/blob/master/spellchecker.py#L17)
* [vowels replaced with '_', an arbitrary wildcard character](https://github.com/lolilo/spellchecker/blob/master/spellchecker.py#L9)

[Values](https://github.com/lolilo/spellchecker/blob/master/spellchecker.py#L65) are directly mapped from raw strings taken from seed file. For example, the words 'Aachen' and 'Achaean' will both produce the key '_ch_n'. The key-value pair will then be 

    '_ch_n': ['Aachen', 'Achaean']

To account for user input that is already spelled correctly, we also populate the dictionary with [correctly spelled words as both key and value in their respective key-value pairs](https://github.com/lolilo/spellchecker/blob/master/spellchecker.py#L66).

When spellchecking the input 'AchhHhhHhheiiiiIiAiNnNnNn', we [transform this input](https://github.com/lolilo/spellchecker/blob/master/spellchecker.py#L79) into the key '_ch_n' with the same functions used in populating our dictionary. The key '_ch_n' maps to ['Aachen', 'Achaean']. However, according to our rules, 'Aachen' will be a false match for 'AchhHhhHhheiiiiIiAiNnNnNn'. We must [check the validity of the returned value against the raw user input](https://github.com/lolilo/spellchecker/blob/master/spellchecker.py#L88) before displaying the suggestion to the user. We loop through the list of potential suggestions and return a suggestion that passes our validity check. If we exhaust the list (or if the key created from the user's input does not map to any values), we return ["NO SUGGESTION"](https://github.com/lolilo/spellchecker/blob/master/spellchecker.py#L108). 

    word is achhhhhhhheiiiiiiainnnnnn
    key is  _ch_n
    key maps to value ['Aachen', 'Achaean']
    user_input with free vowels is  _chhhhhhhh_________nnnnnn
    potential word with free vowels is  __ch_n -- this does not pass our validity checker
    user_input with free vowels is  _chhhhhhhh_________nnnnnn
    potential word with free vowels is  _ch___n
    For _ch_n, spellchecker produces 'Achaean' and not 'Aachen'

Another example, 'conect', should not produce a suggestion according to our rules. 

    word is conect
    key is  c_n_ct
    key maps to value ['connect']
    user_input with free vowels is  c_n_ct
    potential word with free vowels is c_nn_ct
    c_n_ct does not have the minimum number of 'n' characters, so the spellchecker produces NO SUGGESTION

In the event that we reach the end of the raw word, but there are still remaining potential characters to check, we know the potential word is [not valid](https://github.com/lolilo/spellchecker/blob/master/spellchecker.py#L89). i.e. spellchecking 'caat' does not return 'Catt'

Test Cases
------------------
incorrect_word_generator.py produces misspellings of words in our dictionary in order for us to test the integrity of spellchecker.py. We can pipe the output from the word generator to the spellchecker program with the correct [main function](https://github.com/lolilo/spellchecker/blob/master/spellchecker.py#L163) selected in spellchecker.py.
    
    $ python incorrect_word_generator.py | python spellchecker.py

The [program will stop if it meets an input that does not produce a suggestion](https://github.com/lolilo/spellchecker/blob/master/spellchecker.py#L150). If all test cases pass, a [success message displays](https://github.com/lolilo/spellchecker/blob/master/spellchecker.py#L152).

Time Complexity
------------------
To spellcheck a raw input string of length m, we first change each character to lowercase with Python's string.lower method, which is around O(m). There is then another pass to remove duplicate characters and then change vowels to '_', each of which is O(m). There is probably a way to reduce this O(3*m) to O(m), which I may look into in the future. Once we have our transformed input string, lookup to the dictionary is on average O(1). Checking the validity of a suggested word is again some constant time. 

Overall, the time complexity is O(k*m), where k > 0 and m is the length of the input string. This aligns with the restriction of this program being faster than O(n) per word checked, where n is the length of the dictionary.
