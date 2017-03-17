"""
Assuming known meal prices for 2 or more people, and a 15% tip, split a check:

exactly
evenly, showing amount of subsidy

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