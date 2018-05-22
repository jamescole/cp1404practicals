

def main():


    print_string_from_outside_in("Programming")  # should print "Pgrnoigmrma"
    print()
    print_string_from_outside_in("123456")  # should print "162534"
    print()
    print_string_from_outside_in("a")  # should print "a"


def print_string_from_outside_in(string):
    """
    Prints string from the outside in, using recursion.
    E.g. if string is "Programming", prints: "P g r n o i g m r m a".
    Another example: 123456 -> 162534
    """

    if len(string) <= 1:
        print(string, end="")
    else:
        print(string[0], end="")
        print(string[-1], end="")
        print_string_from_outside_in(string[1:-1])


main()
