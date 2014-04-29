# from sys import argv
from os.path import exists
import re
vowel_pattern = re.compile('[aeiou]')
seed_dictionary_path = '/usr/share/dict/words'
# seed_dictionary_path = 'toydict.txt'

def free_vowels(word):
    key = ''
    for char in word:
        # replace all vowels with free character '_'
        if vowel_pattern.match(char):
            char = '_'
        key += char
    return key

def create_key(word):
    def remove_consecutive_duplicate_characters(word):
        out = ''
        for i in range(len(word) - 1):
            if word[i] != word[i+1]:
                out += word[i]
        # append last character
        out += word[-1]
        return out    

    return remove_consecutive_duplicate_characters(free_vowels(word))

def seed_dict():
    # script, input_file = argv
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
            word = in_file.readline().strip()
            if word == '':
                in_file_ended = True
                in_file.close()
                break

            key = create_key(word)
            add_to_dictionary(key, word)
            add_correctly_spelled_word_as_key(word)

        return dictionary

def give_suggestion(user_input):
    if dictionary.get(user_input):
        return dictionary[user_input][0]
    key = create_key(user_input)
    if dictionary.get(key):
        potential = dictionary[key][0]
        # conect should produce connect as suggestion
        def is_valid_spellcheck(raw, potential):
            raw = free_vowels(raw)
            potential = free_vowels(potential)
            # print raw, potential
            i = 0
            j = 0
            while i < len(potential)-1:
                # print i, j
                if potential[i] == raw[j]:
                    i += 1
                    j += 1
                    continue
                # the characters don't match; check for duplication in raw
                while raw[j] == raw[j-1]:
                    j += 1
                # if at this point there is still no match, the suggesion is invalid
                if potential[i] != raw[j]:
                    return False
            return True

        if is_valid_spellcheck(free_vowels(user_input), potential):
            return potential
    return "NO SUGGESTION"

dictionary = seed_dict()
# print dictionary

while True: 
    user_input = raw_input("> ").strip().lower() # case insensitive
    if not user_input:
        continue
    suggesion = give_suggestion(user_input)
    print suggesion
