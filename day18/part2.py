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
    grid_size = int(sys.argv[1])
    with open(sys.argv[2]) as f:
        lines = [s.rstrip('\n') for s in f]
    coords = [tuple(map(int, line.split(','))) for line in lines]

    is_blocked = np.zeros((grid_size, grid_size), dtype=bool)
    for i, x in enumerate(coords):
        if not path_exists(grid_size, is_blocked):
            print('no path exists')
            break
        is_blocked[x] = True
        print(i, 'add:', ','.join(map(str, x)))


def path_exists(grid_size, is_blocked):
    goal = (grid_size - 1, grid_size - 1)
    q = [(0, (0, 0))]
    visited = set()
    while q:
        dist, (i, j) = heapq.heappop(q)
        if (i, j) == goal:
            return True
        if (i, j) in visited:
            continue
        visited.add((i, j))

        for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            ni, nj = i + di, j + dj
            if 0 <= ni < grid_size and 0 <= nj < grid_size and not is_blocked[ni, nj]:
                heapq.heappush(q, (dist + 1, (ni, nj)))
    return False


if __name__ == '__main__':
    main()
