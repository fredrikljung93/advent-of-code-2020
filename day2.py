#!/usr/bin/python3
import re

path = 'puzzleinputs/day2.txt'

lines = open(path, 'r').read().splitlines()


def valid_password_1(line):
    splitted = re.split(' ', line.replace(':', ''))
    numbers = list(map(int, re.split('-', splitted[0])))
    char = splitted[1]
    pw = splitted[2]
    count = sum(map(lambda x: 1 if char in x else 0, pw))
    return numbers[0] <= count <= numbers[1]


def valid_password_2(line):
    splitted = re.split(' ', line.replace(':', ''))
    numbers = list(map(int, re.split('-', splitted[0])))
    char = splitted[1]
    pw = splitted[2]
    return (pw[numbers[0] - 1] == char) != (pw[numbers[1] - 1] == char)


def part_one():
    return sum(map(lambda l: 1 if valid_password_1(l) else 0, lines))


def part_two():
    return sum(map(lambda l: 1 if valid_password_2(l) else 0, lines))


print("Part 1:", part_one())
print("Part 2:", part_two())
