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

directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
next_dir = {
    a: b for a, b in zip(directions, directions[1:] + directions[:1])
}

def main():
    with open(sys.argv[1]) as f:
        lines = [s.rstrip('\n') for s in f]
    arr = np.array([list(line) for line in lines])
    (pos_i,), (pos_j,) = np.where(arr == '^')
    pos = (pos_i, pos_j)
    pos = np.array(pos)
    shape = np.array(arr.shape)
    free = (arr != '#')
    direction = (-1, 0)
    visited = np.zeros(arr.shape, dtype=bool)
    while True:
        visited[pos[0], pos[1]] = True
        next_pos = pos + direction
        if not (np.all(0 <= next_pos) and np.all(next_pos < shape)):
            break
        if not free[next_pos[0], next_pos[1]]:
            direction = next_dir[direction]
        else:
            pos = next_pos
        print(visited)
    print(np.sum(visited))


if __name__ == '__main__':
    main()
