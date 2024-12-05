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

    lt_than = set(pairs)

    def compare(a, b):
        if (a, b) in lt_than:
            return -1
        elif (b, a) in lt_than:
            return 1
        return 0

    total = 0
    for row in orders:
        assert len(row) == len(set(row))
        out = sorted(row, key=functools.cmp_to_key(compare))
        m = (len(row) - 1) // 2
        if out != row:
            total += out[m]
    print(total)


if __name__ == '__main__':
    main()
