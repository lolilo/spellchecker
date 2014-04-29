from os.path import exists
from sys import argv
import random
SEED_DICTIONARY_PATH = '/usr/share/dict/words'
# SEED_DICTIONARY_PATH = 'toydict.txt'
VOWEL_LIST = ['a', 'e', 'i', 'o', 'u']

# returns True if path to dictionary exists
def seed_dictionary_exists(path):
    if not exists(path):
        print "%r does not exist!" % SEED_DICTIONARY_PATH
        return False
    return True

# create list of all words from input file
def create_word_list(input_file):
    words = open(input_file).read().splitlines()
    return words

# generates a mispelling of word
def generate_mistake(word):

    def randomize_vowel(char):
        if char in VOWEL_LIST:
            return random.choice(VOWEL_LIST)
        return char

    def randomize_capitalization(char):
        make_capital = random.choice([True, False])
        if make_capital:
            return char.upper()
        return char

    def random_duplication(char):
        duplication_amount = random.randint(1, 6) # duplicate some random amount between one and six, inclusive
        return char * duplication_amount
            
    misspelled_word = ''
    for char in word:
        misspelled_word += random_duplication(randomize_capitalization(randomize_vowel(char)))
    return misspelled_word

def generate_txt_file_of_misspelled_words():
    script, output_file = argv
    if seed_dictionary_exists(SEED_DICTIONARY_PATH):
        print "Writing list of misspelled words to %s." % output_file
        target = open(output_file, 'w')
        target.truncate()

        words = create_word_list(SEED_DICTIONARY_PATH)

        for word in words:
            misspelled_word = generate_mistake(word)
            target.write(misspelled_word + '\n')
        print 'Complete.'
        target.close()

# print misepelled words to console for testing via piping
# $ python incorrect_word_generator.py | python spellchecker.py 
def print_mispelled_words():
    if seed_dictionary_exists(SEED_DICTIONARY_PATH):
        words = create_word_list(SEED_DICTIONARY_PATH)

        for word in words:
            misspelled_word = generate_mistake(word)
            print misspelled_word

def main():
    # generate_txt_file_of_misspelled_words()
    print_mispelled_words()

if __name__ == "__main__":
    main()
