from random import randrange

MIN_RANDOM_NUMBER_INCLUSIVE = 1
MAX_RANDOM_NUMBER_INCLUSIVE = 45
NUMBERS_PER_PICK = 6


def main():
    number_of_quick_pics = int(input("How many quick picks? "))
    for quick_pick_index in range(number_of_quick_pics):
        quick_pick_list = generate_quick_pics()
        quick_pick_list.sort()
        print_quick_pick_list(quick_pick_list)


def generate_quick_pics():
    """
    Return a list of NUMBERS_PER_PICK randomly-generated, unique integers.
    Numbers between MIN_RANDOM_NUMBER_INCLUSIVE and MAX_RANDOM_NUMBER_INCLUSIVE.
    """
    quick_pics = []
    random_number = 0
    for number_index in range(NUMBERS_PER_PICK):
        found_unique_number = False
        while not found_unique_number:
            random_number = randrange(MIN_RANDOM_NUMBER_INCLUSIVE, MAX_RANDOM_NUMBER_INCLUSIVE + 1)
            found_unique_number = random_number not in quick_pics
            # if not found_unique_number:
            #     print("{} : {}".format(quick_pics, random_number))
        quick_pics.append(random_number)

    return quick_pics


def print_quick_pick_list(quick_pick_list):
    for number in quick_pick_list:
        print("{:3}".format(number), end='')
    print()


main()
