from prac_07.guitar import Guitar


def main():
    print("My guitars!")

    guitars = []
    # name = input("Name: ")
    # while name != "":
    #     year = int(input("Year: "))
    #     cost = input("Cost: $")
    #     guitar = Guitar(name, year, cost)
    #     guitars.append(guitar)
    #     print("{} added".format(guitar))
    #     name = input("Name: ")

    guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))

    print("These are my guitars:")
    for i, guitar in enumerate(guitars):
        format_str = "Guitar {}: {self.name:>20} ({self.year}), worth ${self.cost} {}"
        print(format_str.format(i + 1, "(vintage)" if guitar.is_vintage() else "", self=guitar))


main()
