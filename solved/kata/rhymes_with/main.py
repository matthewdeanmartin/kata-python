# coding=utf-8
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
