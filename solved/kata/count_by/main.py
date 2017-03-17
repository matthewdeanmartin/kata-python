"""
Count by n.
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
