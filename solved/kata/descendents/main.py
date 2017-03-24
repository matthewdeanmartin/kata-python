# coding=utf-8
"""
Calculate how many descendents you will have after n generations if each of your descendents has x children

So just to make clear who is included or not:

   A marries B, generation one has two people.
   A & B have 2 kids, generation two has four people
   The 2 kids have two kids each, generation three has 8 people.
And so on.
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
    pop = 2
    kids = 2
    generation = 1
    while generation<10:
        print(generation, kids)
        more_kids = kids * 2
        generation += 1
        kids += more_kids


if __name__ == "__main__":
    run()