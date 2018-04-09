from prac_07.guitar import Guitar


def main():
    guitar = Guitar("Gibson L-5 CES", 1922, 16035.40)
    print(guitar)
    print("age: {}".format(guitar.get_age()))
    print("is vintage: {}".format(guitar.is_vintage()))

    print()
    guitar = Guitar("Strummy strum", 1988, 160)
    print(guitar)
    print("age: {}".format(guitar.get_age()))
    print("is vintage: {}".format(guitar.is_vintage()))


main()
