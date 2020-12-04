#!/usr/bin/python3
import re

path = 'puzzleinputs/day2.txt'

lines = open(path, 'r').read().splitlines()
linesCount = len(lines)


def valid_password(line):
    splitted = re.split(' ', line.replace(':', ''))
    numbers = list(map(int, re.split('-', splitted[0])))
    char = splitted[1]
    pw = splitted[2]
    count = sum(map(lambda x: 1 if char in x else 0, pw))
    return numbers[0] <= count <= numbers[1]


def part_one():
    return sum(map(lambda l: 1 if valid_password(l) else 0, lines))


print("Part 1:", part_one())
