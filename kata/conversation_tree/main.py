# coding=utf-8
"""
Implement a conversation tree, e.g.

User says Hello, and gets in response one of the following.
User picks from numbered items, eg. U1,U2
U:Hello ->
    C:How are you?
        U1: Fine
            C: Me too!
                U1: What's happening today?
                U2: Where is the library?
        U2: I'm sick
            C: Sorry to hear that.
                U1: Where is a pharmacy?
                U2: Where is the hospital?
        U3: Oh well
            C: You sound disinterested.
                U1: No, at at all.
                U2: You got that right

Level 1 - data is mixed with code
Level 2 - data is neatly segregated from code.
Level 3 - re-use paths, e.g. if another part of a tree has "I'm fine" then transition to that node.
"""

def run():
    pass