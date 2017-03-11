# coding=utf-8
"""
Exercise code under test
"""
import unittest

import blanks.template.main as cb


class CounterTest(unittest.TestCase):
    def test_main(self):
        cb.run()
        raise TypeError("Not implemented")
