import unittest

import kata.print_input.main as cb

class Tests(unittest.TestCase):
    def test_hello(self):
        # This test needs to determine that "hello world" really was written to the console.
        # A human verification system (even mechanical turk!) is not good enough.
        # Should assert "hello world" indeed is sent to standard out.
        # remember, we are testing hello_world, not print, which presumably works fine.
        pass

    def test_how_are_you(self):
        # This test must pass without you typing anything.
        # It should assert something like, When input receives "fine", method returns fine.
        # remember, we are testing how_are_you(), not input, which presumably works fine.
        pass

    def test_integration_test_both(self):
        # Test exercise(), which calls both.
        pass