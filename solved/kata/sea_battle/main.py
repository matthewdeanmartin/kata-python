# coding=utf-8
"""
Ocean is a n1 x n2 grid.

Goals:
    Print the grid of the ocean using ^ for empty cells
    Add the ships and print them as X's
    Let the user fire shots at coordinates and mark on map
    Determin if a shot hit a ship
    Determine if entire ship has been shot.
    Determine if all ships have been shot.

User enters coordinate and finds out if they hit a ship and sank it.
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
# level 1
def run():
    ocean = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    ships = [[(0, 0), (0, 1)], [(2, 2), (2, 3)]]
    some_ship = []
    for ship in ships:
        for coordinate in ship:
            some_ship.append(coordinate)
    for row_id, row in enumerate(ocean):
        for column_id, column in enumerate(row):
            if (row_id, column_id) in some_ship:
                print("X", end="")
            else:
                print("^", end="")
        print()

# level 2


run()
