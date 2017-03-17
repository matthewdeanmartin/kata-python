# coding=utf-8
"""
Create a text adventure map with three rooms.

Navigation is done with N, S, E, W.

Describe rooms on entry.

Prevent attempting to leave a room by an impossible route.

There are many ways to implement this.
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
import collections


# level 1
def run():
    Compass = collections.namedtuple("Compass", "N S E W")
    N, S, E, W = 0, 1, 2, 3
    room_map = {
        "room1": Compass(N=None, S=None, E=None, W="room2"),
        "room2": Compass(N=None, S="room3", E="room1", W=None),
        "room3": Compass(N="room3", S=None, E="room1", W=None)
    }
    print(room_map["room1"].W)
    command = ""
    current_room = "room1"
    while command != "exit":
        command = input("Where to?")
        if command in "NSEW" and len(command) == 1:
            directions = room_map[current_room]
            what = directions[eval(command)]
            if what:
                current_room = what
                print(what)
            else:
                print("You can't go that way")
    print("Game over man")

def run2():
    Compass = collections.namedtuple("Compass", "N S E W")
    N, S, E, W = 0, 1, 2, 3
    room_map = {
        "room1": Compass(N=None, S=None, E=None, W="room2"),
        "room2": Compass(N=None, S="room3", E="room1", W=None),
        "room3": Compass(N="room3", S=None, E="room1", W=None)
    }
    print(room_map["room1"].W)
    command = ""
    current_room = "room1"
    while command != "exit":
        command = input("Where to?")
        if command in "NSEW" and len(command) == 1:
            process_direction(command, current_room, room_map)
    print("Game over man")

def process_direction(command, current_room, room_map):
    directions = room_map[current_room]
    what = directions[eval(command)]
    if what:
        current_room = what
        print(what)
    else:
        print("You can't go that way")


run2()
