#!/usr/bin/python3

def unique(list1): return list(set(list1))


groups = [unique(s.replace('\n', '')) for s in open('puzzleinputs/day6.txt', 'r').read().split('\n\n')]

print("Part 1:", sum([len(g) for g in groups]))
