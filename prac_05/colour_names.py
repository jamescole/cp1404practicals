COLOUR_NAMES = {"AliceBlue": "#f0f8ff", "AntiqueWhite": "#faebd7", "AntiqueWhite1": "#ffefdb",
                "AntiqueWhite2": "#eedfcc",
                "AntiqueWhite3": "#cdc0b0", "AntiqueWhite4": "#8b8378", "aquamarine1": "#7fffd4",
                "aquamarine2": "#76eec6",
                "aquamarine4": "#458b74"}

WIDTH_OF_COLOUR_NAME_COLUMN = 15


def main():
    print_colour_abbreviations_and_names()
    print()

    colour_name = get_colour_name()
    while colour_name != "":
        if is_valid_colour_name(colour_name):
            print_colour_value(colour_name)
        else:
            print("Invalid colour name")
        colour_name = get_colour_name()


def print_colour_abbreviations_and_names():
    for abbreviation in COLOUR_NAMES:
        print("{:{}} is {}".format(abbreviation, WIDTH_OF_COLOUR_NAME_COLUMN, COLOUR_NAMES[abbreviation]))


def get_colour_name():
    return input("Enter colour name: ")


def is_valid_colour_name(colour_name):
    return colour_name.upper() in [colour_name.upper() for colour_name in COLOUR_NAMES]


def print_colour_value(colour_name):
    for colour in COLOUR_NAMES:
        if colour_name.upper() == colour.upper():
            print(colour, "is", COLOUR_NAMES[colour])
            break


main()
