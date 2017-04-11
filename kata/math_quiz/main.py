# coding=utf-8
"""
Goals
Ask user randomly generated questions for each of the 4 operations.
exit on q
Keep score.

Advanced
- Use lambdas
- Deal with divide by 0 (i.e. don't let the game end, instead do a suitable recovery)
- Limit division to questions with whole number answers
- Deal with q, Q, Quit, "", quit, etc.
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