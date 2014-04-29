from os.path import exists
from sys import argv
import random
seed_dictionary_path = '/usr/share/dict/words'
# seed_dictionary_path = 'toydict.txt'
vowels = ['a', 'e', 'i', 'o', 'u']

script, output_file = argv
isValid = True
if not exists(seed_dictionary_path):
    print "%r does not exist!" % seed_dictionary_path
    isValid = False

if isValid:
    print "Writing list of misspelled words to %s." % output_file
    target = open(output_file, 'w')
    target.truncate()

    def create_word_list():
        input_file = seed_dictionary_path
        # create list of all words
        words = open(input_file).read().splitlines()
        return words

    def select_random_word(word_list):
        random_word = random.choice(word_list)
        return random_word

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
            char = mispelled_word[i]
            # random vowels
            if char in vowels:
                random_vowel = random.choice(vowels)
                char = random_vowel
            # random capitalization
            make_capital = random.choice([True, False])
            if make_capital:
                out += char.upper()
            out += mispelled_word[i]
        return out

    words = create_word_list()
    word = select_random_word(words)

    for word in words:
        misspelled_word = generate_mistake(word)
        target.write(misspelled_word + '\n')
        # print misspelled_word
    print 'Complete.'
    target.close()

