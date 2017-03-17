# coding=utf-8
"""
Write a limerick generator that puts words into a template.

Extend to generate all possible limericks with various lists of words, madlib style.

Extend to use functions and generators (i.e. the yeild keyword)
"""
"""
There was a Young [Person of Crete],
Whose toilette was far from [complete];
She dressed in a [sack],
Spickle-speckled with [black],
That ombliferous [person of Crete].”
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

# level 1
def run():
    place_names = ["nantucket", "boston"]
    nouns = ["luck", "duck"]
    rude_verbs = ["fuck it", "drink some tea"]
    template = """
    There once was a man from {0}
    who something something {1}
    He something something {2}
    """
    for place in place_names:
        for noun in nouns:
            for rude in rude_verbs:
                print(template.format(place, noun, rude))

def run2():
    place_names = ["nantucket", "boston"]
    nouns = ["luck", "duck"]
    rude_verbs = ["fuck it", "drink some tea"]
    template = """
       There once was a man from {0}
       who something something {1}
       He something something {2}
       """
    for poem in limerick(place_names, nouns, rude_verbs,template):
        print(poem)

def limerick(place_names, nouns, rude_verbs, template):
    for place in place_names:
        for noun in nouns:
            for rude in rude_verbs:
                yield template.format(place, noun, rude)
run2()