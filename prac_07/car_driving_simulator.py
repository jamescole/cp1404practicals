from prac_07.car import Car


def main():
    print("Let's drive!")
    name = input("Enter your car name: ")
    car = Car(name, 100)

    print(car)
    print_menu()
    menu_choice = input("").upper()
    while menu_choice != "Q":
        if menu_choice == "D":
            drive(car)
        elif menu_choice == "R":
            refuel(car)
        else:
            print("Invalid choice")

        print()
        print(car)
        print_menu()
        menu_choice = input("").upper()

    print()
    print("Good bye {}'s driver.".format(car.name))


def print_menu():
    menu = """Menu:
d) drive
r) refuel
q) quit
Enter your choice: """
    print(menu, end='')


def drive(car):
    kms_to_drive = int(input("How many km do you wish to drive? "))
    if kms_to_drive < 0:
        print("Distance must be >= 0")

    kms_driven = car.drive(kms_to_drive)
    if kms_driven == kms_to_drive:
        print("The car drove {}km.".format(kms_driven))
    else:
        print("The car drove {}km and ran out of fuel.".format(kms_driven))


def refuel(car):
    fuel_prompt = "How many units of fuel do you want to add to the car? "
    fuel_units = int(input(fuel_prompt))
    while fuel_units < 0:
        print("Fuel amount must be >= 0")
        fuel_units = int(input(fuel_prompt))
    car.add_fuel(fuel_units)
    print("Added {} units of fuel".format(fuel_units))


main()
