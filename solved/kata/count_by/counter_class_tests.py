# coding=utf-8
"""
Write the class that makes these tests pass or consider this a solved example of how to write tests.
"""#
#
# THIS IS A SOLVED SOLUTION. DON'T EDIT.
#
# If this is an interview, don't read this until you've solved your version.
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
import unittest
from .counter_class import Counter

class CounterTest(unittest.TestCase):
    def test_advance_default_counter(self):
        counter = Counter()
        counter.advance()
        assert counter.current == 1

    def test_advance_count_by_two(self):
        counter = Counter(count_by=2)
        counter.advance()
        assert counter.current == 2

    def test_type_error_on_exceed_maximum(self):
        counter = Counter()
        i = 0
        try:
            while True:
                counter.advance()
                i+=1
                if i>101:
                    assert False, "Default limit should be 100, we are past that."
        except TypeError:
            assert True
        assert counter.current == 2