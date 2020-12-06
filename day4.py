#!/usr/bin/python3
import string


def list_to_dictionary(ll):
    d = {}
    for t in ll:
        d[t[0]] = t[1]
    return d


def is_valid_1(p):
    return {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'} <= p.keys()


def is_valid_2(p):
    if not is_valid_1(p):
        return False
    return valid_byr(p) and valid_iyr(p) and valid_eyr(p) and valid_hgt(p) and valid_hcl(p) and valid_ecl(
        p) and valid_pid(p)


def valid_byr(p): return numeric_between_values(p.get('byr'), 1920, 2002)


def valid_iyr(p): return numeric_between_values(p.get('iyr'), 2010, 2020)


def valid_eyr(p): return numeric_between_values(p.get('eyr'), 2020, 2030)


def valid_pid(p):
    s = p.get('pid')
    return len(s) == 9 and s.isdigit()


def valid_hgt(p):
    if p.get('hgt').endswith('cm'):
        return numeric_between_values(p.get('hgt')[:3], 150, 193)
    if p.get('hgt').endswith('in'):
        return numeric_between_values(p.get('hgt')[:2], 59, 76)
    return False


def valid_hcl(p):
    s = p.get('hcl')
    return s[0] == '#' and len(s) == 7 and all(c in string.hexdigits for c in s[1:])


def valid_ecl(p):
    return p.get('ecl') in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']


def numeric_between_values(s, min_i, max_i): return (min_i <= int(s) <= max_i) if s.isdigit() else False


puzzle_input_raw = open('puzzleinputs/day4.txt', 'r').read()

passports = list(
    map(list_to_dictionary,
        map(lambda _: map(lambda _: _.split(':'), _),
            map(lambda _: _.replace('\n', ' ').split(' '), puzzle_input_raw.split('\n\n')))))

print("Part 1:", list(map(is_valid_1, passports)).count(True))
print("Part 2:", list(map(is_valid_2, passports)).count(True))
