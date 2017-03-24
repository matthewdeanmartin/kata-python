# coding=utf-8
""""
Count by n.

Print to the screen numbers 1, 2, 3, but also 2, 4, 6 (counting by 2), etc.

Be explicit about when the code should start and stop counting.

Make memory efficient if possible.
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

import logging
logging.basicConfig(filename='log.txt',level=logging.DEBUG)

def run():
    counter(10)


# level 1
def counter(by):
    amount = 0
    for i in range(0, 100):
        amount += by
        print(amount)

# level 1
def counter_efficient(by, start=0, times=100):
    amount = 0
    for i in range(start, times):
        amount += by
        yield amount

if __name__ == "__main__":
    run()
