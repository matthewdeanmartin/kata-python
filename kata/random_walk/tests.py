# coding=utf-8
"""
Exercise code under test
"""
import unittest

import kata.random_walk.main as main


class Tests(unittest.TestCase):
    def test_main(self):
        main.run()
