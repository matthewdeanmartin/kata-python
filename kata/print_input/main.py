# coding=utf-8
"""
The code under test is already written. This is intentially written to make it difficult to test.

You may need to monkey patch, add a fake or a spy or dependency injection.

Write automated tests to test these two functions.

The automated tests must not halt on the input() as the build scripts run unattended, on a server far 
away with no one sitting infront of it to type.
"""
from __future__ import print_function, unicode_literals, absolute_import

def hello_world():
    print("hello world")

def how_are_you():
    return input("How are you?")


def exercise():
    """
    This exercises the above methods.
    :return: 
    """
    hello_world()
    print(how_are_you())