#!/usr/bin/python3

def parsed_line(s):
    split = s.split(' bags contain ')
    return split[0], [] if split[1] == 'no other bags.' else [s.split(' bag')[0].split(' ', 1) for s in
                                                              split[1].split(', ')]


lines = open('puzzleinputs/day7.txt', 'r').read().splitlines()

parsed_lines = [parsed_line(l) for l in lines]


def parsed_line_from_color(color):
    next_color = next(p for p in parsed_lines if p[0] == color)
    return next_color


def can_contain_gold(p):
    other_bags_colors = [c[1] for c in p[1]]
    if not other_bags_colors:
        return False
    if 'shiny gold' in other_bags_colors:
        return True
    return any([can_contain_gold(parsed_line_from_color(c)) for c in other_bags_colors])


print("Part 1:", sum([can_contain_gold(p) for p in parsed_lines]))
