# coding=utf-8
"""
You are on an infinite grid of squares, sort of like New York City.

Walk in any direction, N, S, E, W. At intersections, pick a route at random, but not doubling back.

On average how long will it take to get back to the starting point?

How often does it fail to return to the starting point after x iterations?
"""

import random
import pprint


def run():
    """
    Entry point.

    Return value is not the os return value!
    :return:
    """
    N, S, E, W = (0, 1, 2, 3)
    names=  {N:"N",S:"S",E:"E",W:"W"}
    counts = {N: 0, S: 0, E: 0, W:0}
    spot = [0,0]
    first = True
    last_direction  = -1
    turns = 0

    while spot != [0,0] or first:
        first = False
        direction = random.randint(0, 3)
        if last_direction == N and direction == S:
            continue
        if last_direction == S and direction == N:
            continue
        if last_direction == E and direction == W:
            continue
        if last_direction == W and direction == E:
            continue
        print(spot)
        if direction == N:
            spot[0] += 1
        elif direction == S:
            spot[0] += -1
        elif direction == W:
            spot[1] += -1
        elif direction == E:
            spot[1] += 1

        counts[direction] += 1

        turns +=1
        if turns > 100000:
            print("")
            print("Failed to return to 0,0 in < 100000 turns")
            pprint.pprint(counts)
            exit(0)
        print(names[direction], end="")

if __name__ == "__main__":
    # Executes when called from python file_name.py
    run()
