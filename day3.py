#!/usr/bin/python3
from functools import reduce

path = 'puzzleinputs/day3.txt'

lines = open(path, 'r').read().splitlines()
linesCount = len(lines)
width = len(lines[0])


def travel(count, x, y, dx, dy):
    if y >= linesCount:
        return count
    else:
        return travel(
            count + (1 if lines[y][x] == '#' else 0),
            (x + dx) % width,
            y + dy,
            dx,
            dy)


print("Part 1:", travel(0, 0, 0, 3, 1))

print("Part2:", reduce((lambda x, y: x * y), [travel(0, 0, 0, 1, 1),
                                              travel(0, 0, 0, 3, 1),
                                              travel(0, 0, 0, 5, 1),
                                              travel(0, 0, 0, 7, 1),
                                              travel(0, 0, 0, 1, 2)
                                              ]))
