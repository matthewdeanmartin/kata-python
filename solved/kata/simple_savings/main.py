# coding=utf-8
"""
How long will it take to save up to buy a bike?
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

# Level 1
def run():
    bike_cost = 100.0
    monthly_savings = 12
    months_to_save = bike_cost / monthly_savings
    print(months_to_save)


# Level 2
def run2():
    bike_cost = 100.0
    monthly_savings = 12
    months = months_to_save(bike_cost, monthly_savings)
    print(months)


def months_to_save(cost, rate):
    """

    :type cost: float|int
    :type rate:  float|int
    :rtype: float
    """
    if rate == 0:
        raise TypeError("Can't calculate with zero rate")
    if rate < 0:
        raise TypeError("Monthly rate should be a positive number, negative savings not meaningful here")
    if cost < 0:
        raise TypeError("Negative cost not meaningful here.")
    return cost / rate


# level 3
def run3():
    savings = Savings(100, 10)
    print(savings.months())

class Savings(object):
    def __init__(self, cost, rate):
        self.cost = cost
        self.rate = rate
        if not self.validate():
            self.cost = None
            self.rate = None

    def months(self):
        return self.cost / self.rate

    def validate(self):
        if self.rate == 0:
            raise TypeError("Can't calculate with zero rate")
        if self.rate < 0:
            raise TypeError("Monthly rate should be a positive number, negative savings not meaningful here")
        if self.cost < 0:
            raise TypeError("Negative cost not meaningful here.")
