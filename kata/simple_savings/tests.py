# coding=utf-8
"""
Exercise code under test
"""
import unittest

import kata.simple_savings.main as main


class Tests(unittest.TestCase):
    def test_main(self):
        main.run()
