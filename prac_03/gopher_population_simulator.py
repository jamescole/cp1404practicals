import random
import math

MIN_PERCENTAGE_GOPHERS_BORN_YEARLY = 10
MAX_PERCENTAGE_GOPHERS_BORN_YEARLY = 20

MIN_PERCENTAGE_GOPHERS_DIE_YEARLY = 5
MAX_PERCENTAGE_GOPHERS_DIE_YEARLY = 25


def main():
    print("Welcome to the Gopher Population Simulator!")

    population = 1000

    print("Starting population {}\n".format(population))

    number_of_years = 10

    for year in range(1, number_of_years + 1):
        percentage_gophers_born = random.randint(MIN_PERCENTAGE_GOPHERS_BORN_YEARLY, MAX_PERCENTAGE_GOPHERS_BORN_YEARLY)
        number_gophers_born = math.floor(population * (percentage_gophers_born / 100))
        percentage_gophers_die = random.randint(MIN_PERCENTAGE_GOPHERS_DIE_YEARLY, MAX_PERCENTAGE_GOPHERS_DIE_YEARLY)
        number_gophers_die = math.floor(population * (percentage_gophers_die / 100))

        population += number_gophers_born - number_gophers_die

        print("Year {}\n*****".format(year))
        print("{} gophers were born.  {} died".format(number_gophers_born, number_gophers_die))
        print("Population: {}".format(population))
        print()


main()
