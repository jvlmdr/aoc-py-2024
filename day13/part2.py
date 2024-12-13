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
        (ai, aj), (bi, bj), (gi, gj) = game
        # Need:
        # u * ai + v * bi = gi
        # u * aj + v * bj = gj
        # There may be many such solutions?
        (_, s, _) = np.linalg.svd([[ai, bi], [aj, bj]])
        if abs(s[1]) < 1e-6:
            raise ValueError('ambiguous')
        (u, v) = np.linalg.solve([[ai, bi], [aj, bj]], [gi, gj])
        u, v = int(round(u)), int(round(v))
        if u < 0 or v < 0:
            continue
        if ai * u + bi * v == gi and aj * u + bj * v == gj:
            results.append(3 * u + v)

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
    return (10000000000000 + int(m[1]), 10000000000000 + int(m[2]))

def parse_game(text):
    a, b, c = text.split('\n')
    return (parse_button(a), parse_button(b), parse_goal(c))


if __name__ == '__main__':
    main()
