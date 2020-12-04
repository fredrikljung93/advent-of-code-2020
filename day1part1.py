#!/usr/bin/python3
path = 'puzzleinputs/day1.txt'

numbers = list(map(int, open(path, 'r').read().splitlines()))
numbersCount = range(len(numbers))

for x in numbersCount:
    for y in numbersCount:
        xn = numbers[x]
        xy = numbers[y]
        if xn + xy == 2020:
            print(xn * xy)
            exit()
