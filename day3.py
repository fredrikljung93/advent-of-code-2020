#!/usr/bin/python3

path = 'puzzleinputs/day3.txt'

lines = open(path, 'r').read().splitlines()
linesCount = len(lines)
width = len(lines[0])


def part_1(count, x, y):
    if y == linesCount:
        return count
    else:
        return part_1(
            count + (1 if lines[y][x] == '#' else 0),
            (x + 3) % width,
            y + 1)


print(part_1(0, 0, 0))
