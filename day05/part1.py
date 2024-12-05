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

    total = 0
    for row in orders:
        assert len(row) == len(set(row))
        lookup = {x: i for i, x in enumerate(row)}
        valid = all(a not in lookup or b not in lookup or lookup[a] < lookup[b] for a, b in pairs)
        if valid:
            total += row[(len(row) - 1) // 2]
    print(total)


if __name__ == '__main__':
    main()
