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
    shape = np.array(arr.shape)
    antinodes = set()
    for k in tokens:
        # shape: (2, n)
        locs = np.array(np.where(arr == k))
        _, n = locs.shape
        for i in range(n):
            for j in range(i + 1, n):
                a = locs[:, i]
                b = locs[:, j]
                c = a
                while np.all(0 <= c) and np.all(c < shape):
                    antinodes.add(tuple(c))
                    c = c + (a - b)
                c = b
                while np.all(0 <= c) and np.all(c < shape):
                    antinodes.add(tuple(c))
                    c = c + (b - a)
    print(len(antinodes))


if __name__ == '__main__':
    main()
