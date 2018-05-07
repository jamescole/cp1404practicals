"""
CP1404/CP5632 Practical
File renaming and os examples
"""
import shutil
import os

LOWERCASE_LETTERS = "abcdefghijklmnopqrstuvwxyz"
UPPERCASE_LETTERS = LOWERCASE_LETTERS.upper()
ALL_LETTERS = LOWERCASE_LETTERS + UPPERCASE_LETTERS


def main():
    """Demo file renaming with the os module."""
    print("Current directory is", os.getcwd())

    # change to desired directory
    os.chdir('Lyrics/Christmas')
    # print a list of all files (test)
    print(os.listdir('.'))

    # make a new directory
    # os.mkdir('temp')

    # loop through each file in the (original) directory
    for filename in os.listdir('.'):
        # ignore directories, just process files
        if not os.path.isdir(filename):
            new_name = get_fixed_filename(filename)

            # NOTE: These options won't just work...
            # they show you ways of renaming and moving files,
            # but you need to have valid filenames. You can't make a file with
            # a blank name, and on Windows you can't have files with the same
            # characters but different case (e.g. a.TXT and A.txt)
            # So, you need to get valid filenames before you can use these.

            # Option 1: rename file to new name - in place
            os.rename(filename, new_name)

            # Option 2: move file to new place, with new name
            # shutil.move(filename, 'temp/' + new_name)

            # Processing subdirectories using os.walk()

            # os.chdir('..')  # .. means "up" one directory
            # for dir_name, subdir_list, file_list in os.walk('.'):
            #     print("In", dir_name)
            #     print("\tcontains subdirectories:", subdir_list)
            #     print("\tand files:", file_list)


def get_fixed_filename(filename):
    """Return a 'fixed' version of filename."""
    # First, replace the spaces and .TXT (the easy part)

    filename = filename.replace(" ", "_").replace(".TXT", ".txt")

    filename_base, filename_extension = os.path.splitext(filename)

    new_filename_base = insert_underscores_before_capital_letters(filename_base)

    new_filename_base = capitalise_first_letters_of_words(new_filename_base)

    new_name = new_filename_base + filename_extension

    return new_name


def insert_underscores_before_capital_letters(string):
    """
    Returns a modified copy of string in which underscores have been inserted before capital letters that follow other
    letters (so excluding a capital that is the first character in the string, or one that follows whitespace or a
    symbol like '(').
    """
    new_name = ""

    previous_letter = ""
    for letter_pos, letter in enumerate(string):
        if letter_pos != 0:
            previous_letter = string[letter_pos - 1]
            if letter.isupper() and previous_letter in ALL_LETTERS:
                new_name += "_"
        new_name += letter

    return new_name


def capitalise_first_letters_of_words(string):
    """
    Capitalise the first letters of words in string.
    Assumes that the start of words are either the first character in the string or characters that immediately follow
    a non-letter (e.g. whitespace, or a symbol like an underscore or bracket)
    """

    # Capitalise the first character and any characters following underscores.
    new_string = ""
    previous_letter = ""
    for letter_pos, letter in enumerate(string):
        if letter_pos != 0:
            previous_letter = string[letter_pos - 1]
        if previous_letter not in ALL_LETTERS:
            letter = letter.upper()
        new_string += letter
    return new_string


main()
