NUMBER_OF_PEOPLE = 5
DAY_POS = 0
MONTH_POS = 1
YEAR_POS = 2


def main():
    date_of_births = get_date_of_births()
    print_date_of_births(date_of_births)

    names = ["Jack", "Jill", "Harry"]
    dobs = [(12, 4, 1999), (1, 1, 2000), (27, 3, 1982)]
    print(create_dict_from_parallel_lists(names, dobs))


def get_date_of_births():
    date_of_births = {}
    # we assume each person's name is unique
    for i in range(NUMBER_OF_PEOPLE):
        name = input("Person's name: ")
        date_of_birth_string = input("Person's date of birth (dd/mm/yyyy): ")
        date_of_birth_tuple = tuple([int(number) for number in date_of_birth_string.split("/")])
        date_of_births[name] = date_of_birth_tuple
    return date_of_births


def print_date_of_births(date_of_births):
    for name in date_of_births:
        dob_tuple = date_of_births[name]
        print("{} was born on {}/{}/{}".format(name, dob_tuple[DAY_POS], dob_tuple[MONTH_POS], dob_tuple[YEAR_POS]))


def create_dict_from_parallel_lists(key_list, value_list):
    return dict(zip(key_list, value_list))


main()
