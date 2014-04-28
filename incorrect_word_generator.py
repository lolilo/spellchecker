from os.path import exists
import random
seed_dictionary_path = 'toydict.txt'
vowels = ['a', 'e', 'i', 'o', 'u']

def create_word_list():
    input_file = seed_dictionary_path
    if not exists(input_file):
        print "%r does not exist!" % input_file
    else: 
        # create list of all words
        words = open(input_file).read().splitlines()
        return words

def select_random_word(word_list):
    random_word = random.choice(word_list)
    return random_word

words = create_word_list()
word = select_random_word(words)

def generate_mistake(word):
    mispelled_word = ''
    for i in range(len(word)):
        char = word[i]
        if char in vowels:
            random_vowel = random.choice(vowels)
            char = random_vowel
        duplication_amount = random.randint(1, 6) # duplicate some random amount between one and six, inclusive
        mispelled_word += char * duplication_amount
    out = ''
    for i in range(len(mispelled_word)):
        make_capital = random.choice([True, False])
        if make_capital:
            out += mispelled_word[i].upper()
        out += mispelled_word[i]
    return out

print generate_mistake('noise')
