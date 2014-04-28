# from sys import argv
from os.path import exists
import re
vowel_pattern = re.compile('[aeiou]')
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

def seed_dict():
    # script, input_file = argv
    input_file = "toydict.txt"
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

        while not in_file_ended:
            word = in_file.readline().strip()
            if word == '':
                in_file_ended = True
                break

            key = create_key(word)
            add_to_dictionary(key, word)

        return dictionary

def is_valid_spellcheck(raw, potential):
    if len(raw) < len(potential):
        return False
    return True
    # for i in range(len(potential)):
    #     if potential[i]

def give_suggestion(user_input):
    key = create_key(user_input)
    if dictionary.get(key):
        potential = dictionary[key][0]
        if is_valid_spellcheck(user_input, potential):
            return potential
    return "NO SUGGESTION"

dictionary = seed_dict()
print dictionary

while True: 
    user_input = raw_input("> ").strip().lower() # case insensitive
    if not user_input:
        continue
    suggesion = give_suggestion(user_input)
    print suggesion
