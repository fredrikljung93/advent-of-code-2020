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


def seat(s): return [helper(0, 127, 'F', s[0:7]), helper(0, 7, 'L', s[-3:])]


def seat_id(s): return s[0] * 8 + s[1]


taken_seats = list(map(lambda l: seat(l), lines))
taken_seatids = list(map(seat_id, taken_seats))
max_seat_id = max(taken_seatids)
min_seat_id = min(taken_seatids)
all_seats = list(range(min_seat_id, max_seat_id + 1))

free_seats = [x for x in all_seats if x not in taken_seatids]

print(max_seat_id)
print(free_seats[0])
