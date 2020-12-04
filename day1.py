#!/usr/bin/python3
path = 'puzzleinputs/day1.txt'

numbers = list(map(int, open(path, 'r').read().splitlines()))
numbersCount = range(len(numbers))


def part_one():
    for x in numbersCount:
        for y in numbersCount:
            xn = numbers[x]
            xy = numbers[y]
            if xn + xy == 2020:
                return xn * xy
    return -1


print(part_one())
