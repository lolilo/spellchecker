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


    while not in_file_ended:
        word = in_file.readline()
        if word == '':
            in_file_ended = True
            break

        # create key
        word = remove_duplicate_letters(word)
        key = free_vowels(word)
        print key



