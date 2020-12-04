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


def part_two():
    for x in numbersCount:
        for y in numbersCount:
            for z in numbersCount:
                xn = numbers[x]
                xy = numbers[y]
                xz = numbers[z]
                if xn + xy + xz == 2020:
                    return xn * xy * xz
    return -1


print("Part 1:", part_one())
print("Part 2:", part_two())
