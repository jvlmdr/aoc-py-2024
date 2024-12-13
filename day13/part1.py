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
    for (ai, aj), (bi, bj), (gi, gj) in games:
        wins = []
        for u in range(101):
            (pi, pj) = (u * ai, u * aj)
            v = (gi - pi) // bi
            if not 0 <= v <= 100:
                continue
            if (gi, gj) == (pi + v * bi, pj + v * bj):
                wins.append(3 * u + v)
        if wins:
            results.append(min(wins))

    print('feasible:', len(results), 'of', len(games))
    print(results)
    print(sum(results))


p_button = re.compile(r'Button .: X\+(\d+), Y\+(\d+)')
p_goal = re.compile(r'Prize: X=(\d+), Y=(\d+)')

def parse_button(line):
    m = p_button.match(line)
    return (int(m[1]), int(m[2]))

def parse_goal(line):
    m = p_goal.match(line)
    return (int(m[1]), int(m[2]))

def parse_game(text):
    a, b, c = text.split('\n')
    return (parse_button(a), parse_button(b), parse_goal(c))


if __name__ == '__main__':
    main()
