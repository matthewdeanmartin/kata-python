# coding=utf-8
"""
Write a limerick generator that puts a collection words into a template.

Extend to generate all possible limericks with various lists of words, madlib style.

Extend to use functions and generators (i.e. the yeild keyword)

There was a Young [Person of Crete],
Whose toilette was far from [complete];
She dressed in a [sack],
Spickle-speckled with [black],
That ombliferous [person of Crete].

For example [Lady of York, town, gown, brown, Lady of York], [A, B, C, D, A], etc

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