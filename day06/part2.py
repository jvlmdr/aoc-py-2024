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
    free = (arr != '#')
    direction = (-1, 0)
    _, _, candidates = traverse(free, pos, direction)
    candidates.remove(pos)

    count = 0
    for x in candidates:
        tmp = np.array(free)
        tmp[x[0], x[1]] = False
        loop, _, _ = traverse(tmp, pos, direction)
        if loop:
            print(x)
            count += 1
    print(count)


def traverse(free, pos, direction):
    visited_pos = set()
    visited_state = set()
    exit = False
    loop = False
    shape = np.array(free.shape)
    while not exit and not loop:
        if (pos, direction) in visited_state:
            loop = True
        visited_pos.add(pos)
        visited_state.add((pos, direction))
        next_pos = (pos[0] + direction[0], pos[1] + direction[1])
        if not (np.all(0 <= np.array(next_pos)) and np.all(np.array(next_pos) < shape)):
            exit = True
        else:
            if not free[next_pos[0], next_pos[1]]:
                direction = next_dir[direction]
            else:
                pos = next_pos
    return loop, exit, visited_pos


if __name__ == '__main__':
    main()
