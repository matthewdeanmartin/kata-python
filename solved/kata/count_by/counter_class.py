# coding=utf-8
"""
OOP Counter. This could be a gratuitious use of OOP in real world code.
"""
#
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
class Counter(object):
    def __init__(self, count_by=1,start_at=0, end_at=100):
        self.count_by=count_by
        self.start_at = start_at
        self.end_at = end_at
        self.current = self.start_at

    def advance(self):
        self.current += self.count_by
        return self.current

    def move_back(self):
        self.current -= self.count_by


