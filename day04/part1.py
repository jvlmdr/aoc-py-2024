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
    ii, jj = np.meshgrid(np.arange(m), np.arange(n), indexing='ij')
    # shape: (m, n, 2)
    start = np.stack([ii, jj], axis=2)
    steps = np.arange(4)
    # shape: (m, n, 8, 4, 2)
    inds = start[:, :, None, None, :] + steps[:, None] * DIRECTIONS[:, None, :]
    inds = np.reshape(inds, (-1, 4, 2))
    valid = np.all(inds % np.array([m, n]) == inds, axis=(1, 2))
    inds = inds[valid]
    words = grid[inds[:, :, 0], inds[:, :, 1]]
    match = np.all(words == np.array(list('XMAS')), axis=-1)
    print(np.count_nonzero(match))


if __name__ == '__main__':
    main()
