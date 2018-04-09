from operator import attrgetter


class Person:

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age


def main():
    people = get_people_input()
    print_people(people)


def get_people_input():
    people = []
    first_name = input("First name (empty value to quit): ")
    while first_name != "":
        last_name = input("Last name: ")
        age = int(input("Age: "))
        person = Person(first_name, last_name, age)
        people.append(person)

        first_name = input("First name (empty value to quit): ")

    return people


def print_people(people):
    for person in sorted(people, key=attrgetter("age")):
        print("{self.first_name:15} {self.last_name:15} {self.age:3}".format(self=person))


main()
