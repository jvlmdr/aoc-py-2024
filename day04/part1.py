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

# shape: (8, 2)
DIRECTIONS = np.array([
    (0, 1), (1, 0), (0, -1), (-1, 0),
    (1, 1), (1, -1), (-1, 1), (-1, -1),
])


def main():
    with open(sys.argv[1]) as f:
        lines = [s.rstrip('\n') for s in f]
    grid = np.array(list(map(list, lines)))
    m, n = grid.shape
    shape = np.array([m, n])
    inds = []
    for i in range(m):
        for j in range(n):
            steps = np.arange(4)
            # shape: (8, 4, 2)
            inds_ij = np.array([i, j]) + steps[None, :, None] * DIRECTIONS[:, None, :]
            inds.append(inds_ij)
    inds = np.concatenate(inds, axis=0)
    valid = np.all((0 <= inds) & (inds < shape), axis=(1, 2))
    inds = inds[valid]
    words = grid[inds[:, :, 0], inds[:, :, 1]]
    match = np.all(words == np.array(list('XMAS')), axis=-1)
    print(np.count_nonzero(match))


if __name__ == '__main__':
    main()
