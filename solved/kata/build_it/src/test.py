# coding=utf-8
"""
The application is already written and is buildable, as you can see, it is Hello World

See README for description of kata
"""
import unittest

import hello.main


class HelloTest(unittest.TestCase):
    def test_main(self):
        assert hello.main.say_hello() == "Hello World"
