# coding=utf-8
"""
Implement a conversation tree, e.g.

User says Hello, and gets in response one of the following.
User picks from numbered items, eg. U1,U2
U:Hello ->
    C:How are you?
        U1: Fine
            C: Me too!
                U1: What's happening today?
                U2: Where is the library?
        U2: I'm sick
            C: Sorry to hear that.
                U1: Where is a pharmacy?
                U2: Where is the hospital?
        U3: Oh well
            C: You sound disinterested.
                U1: No, at at all.
                U2: You got that right

OK - data is mixed with code
Better - data is neatly segregated from code.
Best - re-use paths, e.g. if another part of a tree has "I'm fine" then transition to that node.
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