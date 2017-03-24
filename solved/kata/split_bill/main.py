# coding=utf-8
"""
Three people go out to a restaurant together.

A orders something for $15
B orders something for $10
C orders something for $18

Tax is 10%
Tip is 15%, at the moment, assume everyone wants to tip 15%

Divide up the check

exactly, i.e. each person pays the same as if they'd eaten alone.
evenly, showing amount of subsidy as an even split will favor people who ordered expensive dishes

Round to penny and assign rounding error to largest check.
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
def run():
    check = 100
    people = 2
    tip = 0.15
    print(check*(1+tip)/people)

def exact():
    people = [10.75, 12.37]
    tip = 0.15
    total = 0
    for amount in people:
        total += amount
    total_with_tip = total * (1+tip)
    print(total_with_tip)
    shares =[]
    for i in range(0,len(people)):
        shares.append(total_with_tip * (people[i]/total))
    for share in shares:
        print(share)
    print(sum(shares))


exact()