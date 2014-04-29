# import sys # for piping capability
from os.path import exists
import re
vowel_pattern = re.compile('[aeiou]')
seed_dictionary_path = '/usr/share/dict/words'
# seed_dictionary_path = 'toydict.txt'
incorrect_words_path = 'misspelled_words.txt'

def free_vowels(word):
    key = ''
    for char in word:
        # replace all vowels with free character '_'
        if vowel_pattern.match(char):
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

def create_key(word):
    return remove_consecutive_duplicate_characters(free_vowels(word))

def seed_dict():
    input_file = seed_dictionary_path
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
            word = in_file.readline().strip().lower()
            if word == '':
                in_file_ended = True
                in_file.close()
                break
            else:
                key = create_key(word)
                add_to_dictionary(key, word)
                add_correctly_spelled_word_as_key(word)

        return dictionary

def give_suggestion(user_input):
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
        # 'conect' should NOT produce 'connect' as suggestion
        def is_valid_spellcheck(raw, potential):
            if len(raw) < len(potential):
                return False
            raw = free_vowels(raw)
            # AchhHhhHhheiiiiIiAiNnNnNn
            # TODO: breaking for AchhHhhHhheiiiiIiAiNnNnNn
            potential = free_vowels(potential)
            # print 'user_input with free vowels is ', raw
            # print 'potential word with free vowels is ', potential
            i = 0
            j = 0
            while i < len(potential)-1 and j < len(raw)-1:
                # print i, j
                if potential[i] == raw[j]:
                    i += 1
                    j += 1
                    continue
                # the characters don't match; check for duplication in raw
                while raw[j] == raw[j-1] and j < len(raw)-1:
                    j += 1
                # if at this point there is still no match, the suggesion is invalid
                if potential[i] != raw[j]:
                    return False
            return True
    
        for potential in potentials:
            if is_valid_spellcheck(user_input, potential):
                suggestion = potential
                break
    return suggestion

def spellcheck(user_input):
    user_input = user_input.lower() # case insensitive
    if not user_input:
        return
    suggesion = give_suggestion(user_input)
    return suggesion

def test_generated_misspellings():
    input_file = incorrect_words_path
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
                    break
    print "All test cases passed."

def continuous_loop():
    while True: 
        user_input = raw_input("> ").strip()
        # user_input = sys.stdin.read()
        print spellcheck(user_input)

def main():
    """In case we need this for something"""
    pass

if __name__ == "__main__":
    dictionary = seed_dict()
    continuous_loop()
    # test_generated_misspellings()
