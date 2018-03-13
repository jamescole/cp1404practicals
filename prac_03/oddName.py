"""
Asks the user for their name, checks it isn't blank, then prints every second letter in the name.

James Cole
"""


def main():
    name = get_name()
    step = 2
    print(get_every_nth_letter(name, step))


def get_name():
    """
    get user's name, repeatedly asking for input until a non-empty string is entered
    """
    name = input("Enter your name: ")
    while name == "":
        print("Error, empty name string")
        name = input("Enter your name: ")
    return name


def get_every_nth_letter(string, step):
    """
    return a string containing every Nth letter (where N is indicated by 'step') of string
    """
    return string[step - 1::step]


main()
