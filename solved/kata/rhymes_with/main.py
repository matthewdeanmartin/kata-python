# coding=utf-8
"""
Generate all the possible rhyming words given an example.

A word rhymes if it has the same vowel plus consonants, but different beginning.

Some examples:

cat rhymes with hat
tear rhymes with bear

Nonsense words are fine, e.g.

torrie rhymes with zorrie

Schematically, a rhyme is something like this:
[something][vowels][consonants]

vowels = "aeiou"
consonants = "bcdfghjklmnpqrstvwxyz"

This won't work perfectly without an English dictionary and phonetic representation. Do as well as can be done with a
dozen or two lines of code.
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
    word = "fart"
    vowels = "aeiou"
    consonants = "bcdfghjklmnpqrstvwxyz"

    last_vowel = 0
    for spot, letter in enumerate(word):
        if letter in vowels:
            last_vowel = spot
        print(letter, spot)
    end_of_word = word[last_vowel:]

    for consonant in consonants:
        if consonant != word[0]:
            print(consonant + end_of_word)
        print(end_of_word)

run()
