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
    tokens = set(itertools.chain.from_iterable(lines))
    tokens.remove('.')
    arr = np.array(list(map(list, lines)))
    antinodes = set()
    for k in tokens:
        # shape: (2, n)
        locs = np.array(np.where(arr == k))
        _, n = locs.shape
        for i in range(n):
            for j in range(i + 1, n):
                a = locs[:, i]
                b = locs[:, j]
                c = b + (b - a)
                d = a + (a - b)
                antinodes.add(tuple(c))
                antinodes.add(tuple(d))
    m, n = arr.shape
    antinodes = {(i, j) for i, j in antinodes if 0 <= i < m and 0 <= j < n}
    print(len(antinodes))


if __name__ == '__main__':
    main()
