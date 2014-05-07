from os.path import exists
import re, sys
VOWEL_PATTERN = re.compile('[aeiou]')
SEED_DICTIONARY_PATH = '/usr/share/dict/words'
SEED_DICTIONARY_PATH = 'toydict.txt'
INCORRECT_WORDS_PATH = 'misspelled_words.txt'

# replace all vowels in word with wildcard character '_'
def free_vowels(word):
    key = ''
    for char in word:
        if VOWEL_PATTERN.match(char):
            char = '_'
        key += char
    return key

def remove_consecutive_duplicate_characters(word):
    out = ''
    for i in range(len(word) - 1):
        if word[i] != word[i+1]: 
            out += word[i]
    # append last character
    out += word[-1]
    return out    

# create keys: Aachen -> _ch_n
def create_key(word): 
    # key = free_vowels(remove_consecutive_duplicate_characters(word.lower()))
    key = remove_consecutive_duplicate_characters(free_vowels(word.lower()))
    return key

def seed_dict():
    input_file = SEED_DICTIONARY_PATH
    isValid = True

    if not exists(input_file):
        print "%r does not exist!" % input_file
        isValid = False

    if isValid:
        in_file = open(input_file)
        in_file_ended = False # Is cursor at the end of the file? 
        dictionary = {}

        def add_to_dictionary(key, value):
            if dictionary.get(key):
                dictionary[key].append(value)
            else:
                dictionary[key] = [value]

        # account for correct raw input -- simply return the same string
        def add_correctly_spelled_word_as_key(value):
            if dictionary.get(value):
                pass
            dictionary[value] = [value]

        while not in_file_ended:
            word = in_file.readline().strip()
            if word == '':
                in_file_ended = True
                in_file.close()
                break
            else:
                key = create_key(word)
                add_to_dictionary(key, word)
                add_correctly_spelled_word_as_key(word)

        return dictionary

# 'conect' should NOT produce 'connect' as suggestion
def is_valid_spellcheck(raw, potential):
    if len(raw) < len(potential):
        return False
    raw = free_vowels(raw.lower()).strip()
    potential = free_vowels(potential.lower())
    # print 'potential word with free vowels is ', potential
    # print 'user_input with free vowels is ', raw
    i = 0 # potential word index
    j = 0 # raw word index

    while j < len(raw) and i < len(potential):
        # print i, j
        if potential[i] == raw[j]:
            i += 1
            j += 1
            # 'caat' should NOT produce 'Catt' as suggestion
            # we've reached the end of raw, 
            # but there are remaining chars in potential to check
            if j == len(raw) and i < len(potential):
                return False
        else:
            # the characters don't match; check for duplication in raw
            while raw[j] == raw[j-1] and j < len(raw):
                j += 1
            # if at this point there is still no match, the suggesion is invalid
            if potential[i] != raw[j]:
                return False
    return True

# provide a correctly spelled word for user input
def spellcheck(user_input):
    if dictionary.get(user_input): # correctly spelled word entered
        return dictionary[user_input][0] # this will be a single element list

    key = create_key(user_input)
    suggestion = "NO SUGGESTION"
    # print ''
    # print 'word is', user_input
    # print 'key is ', key
    if dictionary.get(key):
        potentials = dictionary[key]
        # print 'key maps to value', potentials
    
        for potential in potentials:
            if is_valid_spellcheck(user_input, potential):
                suggestion = potential
                break
    return suggestion

# test from a .txt file of misspelled words
def test_generated_misspellings():
    input_file = INCORRECT_WORDS_PATH
    isValid = True

    if not exists(input_file):
        print "%r does not exist!" % input_file
        isValid = False

    if isValid:
        in_file = open(input_file)
        in_file_ended = False # Is cursor at the end of the file? 
        while not in_file_ended:
            word = in_file.readline().strip()
            if word == '':
                in_file_ended = True
                in_file.close()
            else:
                suggestion = spellcheck(word)
                if suggestion == "NO SUGGESTION":
                    print "%s has no suggested correction." % word
                    return
    print "All test cases passed."

# test via piping: $ python incorrect_word_generator.py | python spellchecker.py
def test_piped_input():
    lines = sys.stdin.read().split()
    for word in lines:
        suggestion = spellcheck(word)
        if suggestion == "NO SUGGESTION":
            print "%s has no suggested correction." % word
            return
    print "All test cases passed."

# test from raw user input on console
def continuous_loop():
    while True: 
        user_input = raw_input("> ").strip()
        if not user_input:
            continue
        print spellcheck(user_input)

def main():
    continuous_loop()
    # test_generated_misspellings()
    # test_piped_input()

if __name__ == "__main__":
    dictionary = seed_dict()
    # print dictionary
    main()