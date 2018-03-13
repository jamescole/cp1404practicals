"""
CP1404/CP5632 - Practical
Pseudocode for temperature conversion
"""


def get_fahrenheit_from_celsius(celsius):
    return celsius * 9.0 / 5 + 32


def get_celsius_from_fahrenheit(fahrenheit):
    return 5.0 / 9.0 * (fahrenheit - 32)


def main():
    MENU = """C - Convert Celsius to Fahrenheit
    F - Convert Fahrenheit to Celsius
    Q - Quit"""
    print(MENU)

    choice = input(">>> ").upper()

    while choice != "Q":
        if choice == "C":
            celsius = float(input("Celsius: "))
            fahrenheit = get_fahrenheit_from_celsius(celsius)
            print("Result: {:.2f} F".format(fahrenheit))
        elif choice == "F":
            fahrenheit = float(input("Fahrenheit: "))
            celsius = get_celsius_from_fahrenheit(fahrenheit)
            print("Result: {:.2f} C".format(celsius))
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you.")


main()
