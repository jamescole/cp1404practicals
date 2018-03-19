def main():
    print("Enter empty string to end getting input")

    input_strings = get_input_strings()
    repeated_strings = get_repeated_strings(input_strings)
    if len(repeated_strings) > 0:
        print("Strings repeated: {}.".format(", ".join(repeated_strings)))
    else:
        print("No repeated strings entered")


def get_input_strings():
    input_strings = []
    input_string = input("Enter string: ")
    while input_string != "":
        input_strings.append(input_string)
        input_string = input("Enter string: ")
    return input_strings


def get_repeated_strings(list_of_strings):
    return [string for i, string in enumerate(list_of_strings) if list_of_strings.count(string) > 1 and i == list_of_strings.index(string)]


main()
