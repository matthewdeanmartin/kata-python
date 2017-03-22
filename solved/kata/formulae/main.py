# coding=utf-8
"""
Offer a menu to solve a variety of problems.

Any of these could be a stand alone Kata, but the overhead of writing a kata makes it easier to batch them up.

Caculate your age given current year and birth year. Do same given exact dates.

Caculate gas mileate/fuel efficiency given starting mileate, ending mileage, amount to fill the tank.

Calculate weight on planet X given gravity ratio and your weight.


Feature set 1 -  
"""
#
#
# THIS IS A SOLVED SOLUTION. DON'T EDIT.
#
# If this is an interview, don't read this until you've solved your version.
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
import datetime

def age_in_years(birth_day, reference_day):
    """

    :type birth_day: datetime.date
    :type reference_day: datetime.date
    :rtype: int
    """
    delta = reference_day - birth_day
    return delta.days/365

def age_in_days(birth_day, reference_day):
    """

    :type birth_day: datetime.date
    :type reference_day: datetime.date
    :rtype: int
    """
    delta = reference_day - birth_day
    return delta


def run():
    years = age_in_years(datetime.date(1973, 6, 5), datetime.date.today())
    print(years)


if __name__ == "__main__":
    run()