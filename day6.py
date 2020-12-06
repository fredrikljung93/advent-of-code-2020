#!/usr/bin/python3

def unique(list1): return list(set(list1))


def common_elements_helper(common_set, lists): return common_set if len(lists) == 0 \
    else common_elements_helper(common_set.intersection(lists[0]), lists[1:])


def common_elements(lists): return common_elements_helper(set(lists[0]), lists[1:])


groups = [s.replace('\n', ' ') for s in open('puzzleinputs/day6.txt', 'r').read().split('\n\n')]

first_commons = list(common_elements(groups[1].split(' ')))

print("Part 1:", sum([len(unique(g.replace(' ', ''))) for g in groups]))
print("Part 2:", sum([len(common_elements(g.split(' '))) for g in groups]))
