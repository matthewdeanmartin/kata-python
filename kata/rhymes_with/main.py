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

This won't work perfectly without an english dictionary and phonetic representation. Do as well as can be done with a
dozen or two lines of code.
"""
from __future__ import print_function, unicode_literals, absolute_import

# configure logging for file and console output.
import logging
import os.path
if os.path.isfile("log.txt"):
    os.remove("log.txt")
logging.basicConfig(filename='log.txt',level=logging.DEBUG)
logging.getLogger().addHandler(logging.StreamHandler())

# strongly discourage using console input and output.
# You can make testable code full of input and print statements, but it introduces
# unnecessary complexity. See kata on testing input and print with fakes and spies.
def input(*args, **kwargs):
    raise TypeError("Don't use input, log or get input from function arguments.")
def raw_input(*args, **kwargs):
    raise TypeError("Don't use raw_input, either, log or get input from function arguments.")

def run():
    """
    Main entry point for your application.  
    """
    pass

# the functions/classes you write here should have no print or input statements.

if __name__ == "__main__" or __name__ == "builtins":
    # Need an environment to run this?
    # https://repl.it/languages/python3
    logging.info("The application is starting.")
    run()