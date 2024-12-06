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
    pos = np.squeeze(np.where(arr == '^'))
    shape = np.array(arr.shape)
    free = (arr != '#')
    direction = (-1, 0)
    visited = set()
    while True:
        visited.add(tuple(pos))
        next_pos = pos + direction
        if not np.all(next_pos % shape == next_pos):
            break
        if not free[next_pos[0], next_pos[1]]:
            direction = next_dir[direction]
        else:
            pos = next_pos
    print(len(visited))


if __name__ == '__main__':
    main()
