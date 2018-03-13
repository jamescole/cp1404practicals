"""
CP1404/CP5632 - Practical
Random word generator - based on format of words

Another way to get just consonants would be to use string.ascii_lowercase
(all letters) and remove the vowels.
"""
import random

VOWELS = "aeiou"
CONSONANTS = "bcdfghjklmnpqrstvwxyz"
VOWELS_AND_CONSONANTS = VOWELS + CONSONANTS

# word_format = raw_input("Enter word format string, consisting of the following kinds of characters\n" +
#                         "\tlowercase letters from a-z - representing that letter\n" +
#                         "\t# - representing a vowel\n" +
#                         "\t% - representing a consonant\n" +
#                         "\t* - representing a vowel or consonant\n" +
#                         ">>> ").lower()

# randomly generate the word format
WORD_FORMAT_CHARACTERS = VOWELS_AND_CONSONANTS + "#%*"
MAX_WORD_FORMAT_STRING_LENGTH = 20
word_format_string_length = random.randint(1, MAX_WORD_FORMAT_STRING_LENGTH)




def main():

    word_format = generate_random_word_format_string(word_format_string_length)

    print("Generated word format string {} of length {}".format(word_format, word_format_string_length))

    word = generate_word(word_format)

    print(word)


def generate_word(word_format):
    word = ""
    for kind in word_format:
        if kind == "#":
            word += random.choice(VOWELS)
        elif kind == "%":
            word += random.choice(CONSONANTS)
        elif kind == "*":
            word += random.choice(VOWELS_AND_CONSONANTS)
        else:
            word += kind
    return word


def generate_random_word_format_string(word_format_string_length):
    word_format = ""
    for i in range(word_format_string_length):
        word_format += random.choice(WORD_FORMAT_CHARACTERS)
    return word_format


main()
