#!/usr/bin/python3

def list_to_dictionary(ll):
    d = {}
    for t in ll:
        d[t[0]] = t[1]
    return d


def is_valid(p):
    return {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'} <= p.keys()


puzzle_input_raw = open('puzzleinputs/day4.txt', 'r').read()

passports = list(
    map(list_to_dictionary,
        map(lambda _: map(lambda _: _.split(':'), _),
            map(lambda _: _.replace('\n', ' ').split(' '), puzzle_input_raw.split('\n\n')))))

number_of_valid = list(map(is_valid, passports)).count(True)
print("Number of valid passports:", number_of_valid)
