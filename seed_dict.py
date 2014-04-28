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

    def remove_duplicate_letters(s):
        out = ''
        for i in range(len(s) - 1):
            if s[i] != s[i+1]:
                out += s[i]
        # append last character
        out += s[-1]
        return out        

    while not in_file_ended:
        word = in_file.readline()
        if word == '':
            in_file_ended = True
            break

        # create key
        key = ''
        print 'making key'
        word = remove_duplicate_letters(word)
        for char in word:
            # replace all vowels with free character '?'
            if vowel_pattern.match(char):
                char = '?'
            key += char
        print key    


