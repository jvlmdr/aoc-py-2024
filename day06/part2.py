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
    free = (arr != '#')
    direction = (-1, 0)
    _, _, candidates = traverse(free, pos, direction)
    candidates.remove(tuple(pos))

    count = 0
    for x in tqdm(candidates):
        tmp = np.array(free)
        tmp[x[0], x[1]] = False
        loop, _, _ = traverse(tmp, pos, direction)
        if loop:
            count += 1
    print(count)


def traverse(free, pos, direction):
    visited_pos = set()
    visited_state = set()
    exit = False
    loop = False
    shape = np.array(free.shape)
    while not exit and not loop:
        state = (tuple(pos), direction)
        if state in visited_state:
            loop = True
        visited_pos.add(tuple(pos))
        visited_state.add(state)
        next_pos = pos + direction
        if not np.all(next_pos % shape == next_pos):
            exit = True
        else:
            if not free[next_pos[0], next_pos[1]]:
                direction = next_dir[direction]
            else:
                pos = next_pos
    return loop, exit, visited_pos


if __name__ == '__main__':
    main()
