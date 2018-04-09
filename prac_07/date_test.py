
from prac_07.date import Date


def main():
    date = Date(26,12,1978)
    print(date)
    print("Is leap year? {}".format(date.is_leap_year()))

    print(date._DAYS_IN_NON_LEAP_YEAR_MONTH)
    print(date._DAYS_IN_LEAP_YEAR_MONTH)

    date.add_days(37)
    print(date)


main()
