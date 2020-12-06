#!/usr/bin/python3

lines = open('puzzleinputs/day5.txt', 'r').read().splitlines()


def helper(mi, ma, lower_half_char, s):
    range_width = ma - mi
    if len(s) == 0:
        return mi
    if s[0] == lower_half_char:
        return helper(mi, (ma - range_width // 2 - 1), lower_half_char, s[1:])
    else:
        return helper((mi + range_width // 2 + 1), ma, lower_half_char, s[1:])


def seat_id(s):
    return [helper(0, 127, 'F', s[0:7]) * 8 + helper(0, 7, 'L', s[-3:])]


seat_ids = map(lambda l: seat_id(l), lines)

print(max(seat_ids))
