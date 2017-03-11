# coding=utf-8
"""
Life ring game,

works on https://repl.it/languages/python3
"""
from __future__ import print_function

import random


def run():
    """
    An ocean x units wide has a man overboard, drawn with a Y.

    You must throw a life ring to resuce them, by guessing their coordinate. The diagram is drawn on screen, so
    the user only needs to guestimate how much white space they see.

    A shark (or sharks) is swimming on the grid according to some sort of search pattern. You have to find the
    swimmer before the shark does.

    Each shark can either do a scan, binary search, random search. The shark can remember what it did previously
    and gets clues from the environment, such as "too high/too low", "found/not found", the bounds of the ocean,
    "warmer/colder", i.e. warmer if closer to the swimmer. A good shark finds the swimmer the fastest with the fewest
    clues.
    :return:
    """
    ocean = sized_ocean(20)
    ocean, person_location = drop_in_ocean(ocean)
    show_ocean(ocean)
    shark_location = -1
    high_low = "high"
    bounds = None
    while True:
        try:
            location = int(input("Enter location to throw life ring: "))
        except SyntaxError:
            print("Enter a number 0 to what you think the ocean size is.")
            continue

        try:
            if location < 0:
                raise IndexError()
            if ocean[location]:
                print("The swimmer is saved!")
                break
        except IndexError:
            print('Out of bounds. The ring fails to land in the water.')
        honest_map = [0 for _ in range(len(ocean))]
        if shark_location > person_location:
            high_low = "high"
        else:
            high_low = "low"

        # shark gets history + clues
        # namely, high low? size of ocean?
        # TODO: add multiple sharks
        shark_location, bounds = shark(honest_map, bounds, shark_location, high_low)
        if ocean[shark_location] == 1:
            print("Shark ate 'em. Sorry")
            break
        show_ocean(ocean, location, shark_location)


def sized_ocean(size):
    return [0 for _ in range(size)]


def drop_in_ocean(ocean):
    location = random.randint(0, len(ocean)-1)
    ocean[location] = 1
    return ocean, location

def random_shark(ocean, bounds=None, last_guess=-1, last_high_low="N/A"):
    """
    Random, but doesn't guess same twice. Respects boundaries.
    """
    if bounds is None:
        bounds =[]
    while True:
        location = random.randint(0, len(ocean) - 1)
        if location not in bounds:
            break
    bounds.append(location)
    return location, bounds

def scan_shark(ocean, bounds=None, last_guess=-1, last_high_low="N/A"):
    """
    Only moves left and right. Doesn't go out of bounds.
    """
    if bounds is None:
        bounds = (True, False)
    up, down = bounds
    if up:
        guess = last_guess +1
    if down:
        guess = guess -1
    if guess == len(ocean):
        down = True
        up = not down
    if guess == 0:
        down = False
        up = not down
    return guess, (up, down)

def shark(ocean, bounds=None, last_guess=0, last_high_low="N/A"):
    """
    Efficiently use clues about too high/too low
    Remembers past guesses
    """
    if bounds is None:
        bounds = (0, len(ocean))
    if last_guess < 0:
        guess = bounds[1] / 2
    else:
        print(bounds)
        if last_high_low == "high":
            bounds = (bounds[0], last_guess)
            guess = bounds[0] + (bounds[1] - bounds[0]) / 2
            assert bounds[0] < guess < bounds[1]
            # bounds = (last_guess, bounds[1])
        else:
            bounds = (last_guess, bounds[1])
            guess = bounds[1] - ((bounds[1] - bounds[0]) / 2)
            assert bounds[0] < guess < bounds[1]
            # bounds = (bounds[0], last_guess)

    print("that last one was too " + last_high_low)
    print(bounds)
    assert bounds[1] > bounds[0]
    return int(round(guess, 0)), bounds


def show_ocean(model, ring_location=-1, shark_location=-1):
    print("[", end='')
    for position, item in enumerate(model):
        if position == ring_location:
            print("o", end='')
        elif position == shark_location:
            print("^", end='')
        else:
            print("Y" if item == 1 else " ", end='')
    print("]")


if __name__ == "__main__" or __name__ == "builtins":
    run()
