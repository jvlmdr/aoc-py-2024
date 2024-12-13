import collections
import functools
import heapq
import itertools
import math
from pprint import pprint
import re
import sys

import numpy as np
from tqdm import tqdm


def main():
    with open(sys.argv[1]) as f:
        lines = [s.rstrip('\n') for s in f]
    game_lines = '\n'.join(lines).split('\n\n')
    games = list(map(parse_game, game_lines))

    results = []
    for game in games:
        (a1, a2), (b1, b2), (g1, g2) = game
        # u * a1 + v * b1 = g1
        # u * a2 + v * b2 = g2
        # solution:
        # v = (a1 * g2 - a2 * g1) / (a1 * b2 - a2 * b1)
        # u = (g1 - b1 * v) / a1
        v = (a1 * g2 - a2 * g1) // (a1 * b2 - a2 * b1)
        u = (g1 - b1 * v) // a1
        if a1 * u + b1 * v == g1 and a2 * u + b2 * v == g2:
            results.append(3 * u + v)

    print(sum(results))


p_button = re.compile(r'Button .: X\+(\d+), Y\+(\d+)')
p_goal = re.compile(r'Prize: X=(\d+), Y=(\d+)')

def parse_button(line):
    m = p_button.match(line)
    return (int(m[1]), int(m[2]))

def parse_goal(line):
    m = p_goal.match(line)
    return (10000000000000 + int(m[1]), 10000000000000 + int(m[2]))

def parse_game(text):
    a, b, c = text.split('\n')
    return (parse_button(a), parse_button(b), parse_goal(c))


if __name__ == '__main__':
    main()
