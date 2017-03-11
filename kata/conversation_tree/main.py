# coding=utf-8
"""
Implement a conversation tree, e.g.

User says, and gets in response one of the following.
Hello -> (How are you?, Hello, Go Away)

User now must pick next utterance from list
How are you? -> (Me too!, I'm sick, Oh well)

If the user picked, say "Me too!", the computer responds with
Me too! -> (See you!, Oh well, That's great!)

Level 1 - data is mixed with code
Level 2 - data is neatly segregated from code.
Level 3 - re-use paths, e.g. if another part of a tree has "I'm fine" then transition to that node.
"""

def run():
    pass