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


numeric_keypad = [['7', '8', '9'], ['4', '5', '6'], ['1', '2', '3'], [None, '0', 'A']]
arrow_keypad = [[None, '^', 'A'], ['<', 'v', '>']]

numeric_to_pos = {
    s: (i, j) for i, row in enumerate(numeric_keypad) for j, s in enumerate(row) if s
}
arrow_to_pos = {
    s: (i, j) for i, row in enumerate(arrow_keypad) for j, s in enumerate(row) if s
}


def main():
    num_levels = int(sys.argv[2])
    with open(sys.argv[1]) as f:
        seqs = [s.rstrip('\n') for s in f]

    @functools.cache
    def min_cost(level, a, b):
        if level == 0:
            return 1
        avoid = (3, 0) if level == num_levels else (0, 0)
        candidates = [x + 'A' for x in paths_between(avoid, a, b)]
        best_cost, _ = min((min_seq_cost(level - 1, x), x) for x in candidates)
        return best_cost

    def min_seq_cost(level, seq):
        to_pos = numeric_to_pos if level == num_levels else arrow_to_pos
        return sum(min_cost(level, to_pos[a], to_pos[b]) for a, b in zip('A' + seq, seq))

    print(sum(int(seq[:-1]) * min_seq_cost(num_levels, seq) for seq in seqs))


def paths_between(avoid, a, b):
    if a == avoid or b == avoid:
        return []
    if a == b:
        return ['']
    ai, aj = a
    bi, bj = b
    sign = lambda x: -1 if x < 0 else 1 if x > 0 else 0
    di = sign(bi - ai)
    dj = sign(bj - aj)

    results = []
    if abs(di):
        results.extend(('^' if di < 0 else 'v') + x for x in paths_between(avoid, (ai + di, aj), b))
    if abs(dj):
        results.extend(('<' if dj < 0 else '>') + x for x in paths_between(avoid, (ai, aj + dj), b))
    return results


if __name__ == '__main__':
    main()
