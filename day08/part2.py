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
        # shape: (n, 2)
        locs = np.array(np.where(arr == k)).T
        for i, a in enumerate(locs):
            for b in locs[i+1:]:
                c = a
                while np.all(c % shape == c):
                    antinodes.add(tuple(c))
                    c = c + (a - b)
                c = b
                while np.all(c % shape == c):
                    antinodes.add(tuple(c))
                    c = c + (b - a)
    print(len(antinodes))


if __name__ == '__main__':
    main()
