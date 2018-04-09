class Date:
    _DAYS_IN_NON_LEAP_YEAR_MONTH = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    _DAYS_IN_LEAP_YEAR_MONTH = _DAYS_IN_NON_LEAP_YEAR_MONTH[:]
    _DAYS_IN_LEAP_YEAR_MONTH[1] = 28

    def __init__(self, day, month, year):
        """day, month and year are all ints"""
        self.day = day
        self.month = month
        self.year = year

    def __str__(self):
        return "{}/{}/{}".format(self.day, self.month, self.year)

    def add_days(self, n):
        """Add n days to the stored date."""
        curr_day = self.day
        curr_month = self.month
        curr_year = self.year

        while n != 0:

            if self.is_leap_year():
                days_in_curr_month = self._DAYS_IN_LEAP_YEAR_MONTH[curr_month - 1]
            else:
                days_in_curr_month = self._DAYS_IN_NON_LEAP_YEAR_MONTH[curr_month - 1]

            days_remaining_in_curr_month = days_in_curr_month - curr_day
            if days_remaining_in_curr_month < n:
                n -= days_remaining_in_curr_month + 1
                curr_day = 1
                curr_month += 1
                if curr_month == 13:
                    curr_month = 1
                    curr_year += 1
            else:
                curr_day += n
                n = 0

        self.day = curr_day
        self.month = curr_month
        self.year = curr_year

    def is_leap_year(self):
        if self.year % 4 == 0:
            if self.year % 100 == 0:
                if self.year % 400 == 0:
                    return True
                else:
                    return False
            else:
                return True
        else:
            return False
