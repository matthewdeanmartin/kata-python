# coding=utf-8
"""
Life ring game or Searching a list of bits for the on bit.

An ocean x units wide has a man overboard, drawn with a Y.

You must throw a life ring to resuce them, by guessing their coordinate. The diagram is drawn on screen, so
the user only needs to guestimate how much white space they see.

A shark (or sharks) is swimming on the grid according to some sort of search pattern. You have to find the
swimmer before the shark does.

Each shark can either do a scan, binary search, random search. The shark can remember what it did previously
and gets clues from the environment, such as "too high/too low", "found/not found", the bounds of the ocean,
"warmer/colder", i.e. warmer if closer to the swimmer. A good shark finds the swimmer the fastest with the fewest
clues.

"""
from __future__ import print_function, unicode_literals, absolute_import

# configure logging for file and console output.
import logging
import os.path
if os.path.isfile("log.txt"):
    os.remove("log.txt")
logging.basicConfig(filename='log.txt',level=logging.DEBUG)
logging.getLogger().addHandler(logging.StreamHandler())

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