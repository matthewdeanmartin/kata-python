import unittest

import kata.count_by.main as cb


class CounterTest(unittest.TestCase):
    def test_main(self):
        cb.run()

    def test_short_list_by_two(self):
        result = [x for x in cb.counter_efficient(by=2, start=0, times=6)]
        print(result)
        assert result == [2, 4, 6, 8, 10, 12]
