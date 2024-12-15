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

DIRECTIONS = {
    '^': (-1, 0),
    'v': (1, 0),
    '<': (0, -1),
    '>': (0, 1),
}

def main():
    with open(sys.argv[1]) as f:
        lines = [s.rstrip('\n') for s in f]
    m = lines.index("")
    grid = lines[:m]
    steps = list(itertools.chain.from_iterable(lines[m + 1:]))

    arr = np.array(list(map(list, grid)))
    is_box = arr == "O"
    is_wall = arr == "#"
    start_i, start_j = np.squeeze(np.array(np.where(arr == "@")))
    pos = (start_i, start_j)

    for step in steps:
        # print()
        # print("step:", step)
        # print(render(is_wall, is_box, pos))
        direction = DIRECTIONS[step]
        pos, is_box, _ = attempt_move(is_wall, pos, is_box, direction)

    print(checksum(is_box))


def render(is_wall, is_box, pos):
    m, n = is_wall.shape
    lines = [
        ["O" if is_box[i, j] else "#" if is_wall[i, j] else " "
            for j in range(n)]
        for i in range(m)
    ]
    if pos is not None:
        lines[pos[0]][pos[1]] = "@"
    return "\n".join("".join(line) for line in lines)


def attempt_move(is_wall, pos, is_box, direction):
    new_pos = (pos[0] + direction[0], pos[1] + direction[1])
    if is_wall[new_pos]:
        if is_box[pos]:
            # Cannot push further.
            return pos, is_box, False
        else:
            # No change. Could return true or false.
            return pos, is_box, False
    if not is_box[new_pos]:
        # Found a free space!
        # If we are pushing a box, move it.
        is_box = np.array(is_box)
        is_box[new_pos] = is_box[pos]
        return new_pos, is_box, True
    # We have run into a box.
    # Try to move it.
    _, is_box, success = attempt_move(is_wall, new_pos, is_box, direction)
    if success:
        # We moved it! Move ourselves.
        is_box = np.array(is_box)
        is_box[new_pos] = is_box[pos]
        return new_pos, is_box, True
    else:
        # We couldn't move it.
        return pos, is_box, False


def checksum(is_box):
    m, n = is_box.shape
    i, j = np.meshgrid(np.arange(m), np.arange(n), indexing='ij')
    return np.sum((100 * i + j) * np.astype(is_box, int))


if __name__ == '__main__':
    main()
