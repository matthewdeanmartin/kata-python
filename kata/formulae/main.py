# coding=utf-8
"""
Offer a menu to solve a variety of problems.

Any of these could be a stand alone Kata, but the overhead of writing a kata makes it easier to batch them up.

Caculate your age given current year and birth year. Do same given exact dates.

Caculate gas mileate/fuel efficiency given starting mileate, ending mileage, amount to fill the tank.

Calculate weight on planet X given gravity ratio and your weight.

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
def print(*args, **kwargs):
    raise TypeError("Don't use print, return values from functions or callables.")

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