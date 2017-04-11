# coding=utf-8
"""
Create a text adventure map with three rooms.

Navigation is done with N, S, E, W.

Describe rooms on entry.

Prevent attempting to leave a room by an impossible route.

There are many ways to implement this. A way that makes it easy to completely swap out a new map without
changing all lines of code is a superior solution.
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