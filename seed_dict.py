from sys import argv
from os.path import exists
import re

script, input_file = argv
isValid = True
vowel_pattern = re.compile('[aeiou]')

if not exists(input_file):
    print "%r does not exist!" % input_file
    isValid = False

if isValid:
    in_file = open(input_file)

    # Is cursor at the end of the file? 
    in_file_ended = False
    dictionary = {}
    def create_key(word):
        def remove_duplicate_letters(word):
            out = ''
            for i in range(len(word) - 1):
                if word[i] != word[i+1]:
                    out += word[i]
            # append last character
            out += word[-1]
            return out    

        def free_vowels(word):
            key = ''
            for char in word:
                # replace all vowels with free character '_'
                if vowel_pattern.match(char):
                    char = '_'
                key += char
            return key

        return free_vowels(remove_duplicate_letters(word))
    def add_to_dictionary(key, value):
        if dictionary.get(key):
            dictionary[key].append(value)
        else:
            dictionary[key] = [value]

    while not in_file_ended:
        word = in_file.readline().strip()
        if word == '':
            in_file_ended = True
            break

        key = create_key(word)
        add_to_dictionary(key, word)

    print dictionary


