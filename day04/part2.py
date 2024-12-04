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
    grid = np.array(list(map(list, lines)))
    m, n = grid.shape
    shape = np.array([m, n])
    inds = []
    p = np.array(list('MAS'))
    rp = p[::-1]
    total = 0
    for i in range(1, m - 1):
        for j in range(1, n - 1):
            subgrid = grid[i-1:i+2, j-1:j+2]
            d1 = np.diag(subgrid)
            d2 = np.diag(np.fliplr(subgrid))
            if (np.all(d1 == p) or np.all(d1 == rp)) and (np.all(d2 == p) or np.all(d2 == rp)):
                total += 1
    print(total)


if __name__ == '__main__':
    main()
