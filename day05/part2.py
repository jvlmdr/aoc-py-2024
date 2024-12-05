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

    split = lines.index('')
    pair_lines = lines[:split]
    order_lines = lines[split+1:]
    pairs = [tuple(map(int, s.split('|'))) for s in pair_lines]
    orders = [list(map(int, s.split(','))) for s in order_lines]

    lt_than = collections.defaultdict(set)
    for a, b in pairs:
        lt_than[a].add(b)
    lt_than = dict(lt_than)

    total = 0
    for row in orders:
        assert len(row) == len(set(row))
        m = (len(row) - 1) // 2
        out = topological_sort(lt_than, row)
        if out != row:
            print(row)
            print(out)
            print()
            total += out[m]
    print(total)


def topological_sort(lt, xs):
    xs = list(xs)
    i = 0
    while i < len(xs):
        j = i + 1
        valid = True
        while j < len(xs) and valid:
            if xs[j] in lt and xs[i] in lt[xs[j]]:
                xs[i], xs[j] = xs[j], xs[i]
                valid = False
            j += 1
        if valid:
            i += 1
    return xs


if __name__ == '__main__':
    main()
