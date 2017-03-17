# coding=utf-8
"""
Calculate how many descendents you will have after n generations if each of your descendents has n children
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