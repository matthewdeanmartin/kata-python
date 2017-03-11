# coding=utf-8
"""
Unit tests
"""

import kata.life_ring.main as lr
import unittest

class RingTest(unittest.TestCase):
    def test_main(self):
        lr.run()
