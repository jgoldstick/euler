#!/usr/bin/env python
"""
You are given the following information, but you may prefer to do some research for yourself.

    1 Jan 1900 was a Monday.
    Thirty days has September,
    April, June and November.
    All the rest have thirty-one,
    Saving February alone,
    Which has twenty-eight, rain or shine.
    And on leap years, twenty-nine.
    A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.

How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
"""
NORMAL_YR = 0
LEAP_YR = 1

# Sunday is 0, Saturday is 7

# days_added for normal year, leap year for each month.  So if Jan 1 was
# sunday, Feb 1 would be Wednesday, etc.
days_added = ((3, 3),
              (0, 1),
              (3, 3),
              (2, 2),
              (3, 3),
              (2, 2),
              (3, 3),
              (3, 3),
              (2, 2),
              (3, 3),
              (2, 2),
              (3, 3)
              )

# Translation tables -- numbers to names for days and months
DAY = ("Sunday", "Monday", "Tuesday", "Wednesday",
       "Thursday", "Friday", "Saturday")
MONTH = ("January", "February", "March", "April", "May", "June",
         "July", "August", "September", "October", "November", "December")


def is_leapyear(year):
    """
    Leap year is year divisible by 4 but not by 100 unless divisible by 400
    returns True or False
    """
    it_is = False
    if not year % 4:
        it_is = True
    if not year % 100:
        it_is = False
    if not year % 400:
        it_is = True
    return it_is


if __name__ == '__main__':
    starting_sunday_count = 0
    starting_day = 1
    for y in xrange(1900, 2001):
        year_type = is_leapyear(y)
        for m in xrange(12):
            print "%s, %d starts on %s" % (MONTH[m], y, DAY[starting_day])
            starting_day = (starting_day + days_added[m][int(year_type)]) % 7
            if starting_day == 0 and y > 1900:
                starting_sunday_count += 1
                print "Months that started on Sunday: ", starting_sunday_count
    print starting_sunday_count
