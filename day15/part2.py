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

DIRECTIONS = {'^': (-1, 0), 'v': (1, 0), '<': (0, -1), '>': (0, 1)}


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

    is_wall, pos, is_box = expand(is_wall, pos, is_box)
    for step in steps:
        print()
        print("step:", step)
        print(render(is_wall, is_box, pos))
        pos, is_box = move(is_wall, pos, is_box, DIRECTIONS[step])

    print(checksum(is_box))


def expand(is_wall, start, is_box):
    m, n = is_wall.shape
    new_is_wall = np.tile(np.expand_dims(is_wall, axis=-1), (1, 1, 2))
    new_is_wall = np.reshape(new_is_wall, (m, 2 * n))
    new_pos = (start[0], 2 * start[1])
    # Use a tri-map (0, 1, 2) for the box occupancy.
    new_is_box = np.zeros((m, 2 * n), dtype=int)
    i, j = np.where(is_box)
    new_is_box[i, 2 * j] = 1
    new_is_box[i, 2 * j + 1] = 2
    return new_is_wall, new_pos, new_is_box


def pos_to_start(is_box, x):
    if is_box[x] == 1:
        return x
    elif is_box[x] == 2:
        return (x[0], x[1] - 1)
    return None


def move(is_wall, x, is_box, direction):
    new_x = (x[0] + direction[0], x[1] + direction[1])
    if is_wall[new_x]:
        return x, is_box
    pushed_start = pos_to_start(is_box, new_x)
    if pushed_start is None:
        # No box to push.
        return new_x, is_box
    # There is a box. Attempt to push it.
    is_box, success = attempt_push(is_wall, pushed_start, is_box, direction)
    return new_x if success else x, is_box


def attempt_push(is_wall, start, is_box, direction):
    # Positions occupied by this box.
    xs = (start, (start[0], start[1] + 1))
    # New putative position of box.
    new_start = (start[0] + direction[0], start[1] + direction[1])
    # New positions occupied by box.
    new_xs = (new_start, (new_start[0], new_start[1] + 1))
    if any(is_wall[x] for x in new_xs):
        return is_box, False
    pushed_starts = set(pos_to_start(is_box, x) for x in new_xs)
    pushed_starts = pushed_starts - {None} - {start}
    # Make a copy in case we fail.
    backup = np.array(is_box)
    # Attempt to move all boxes.
    for pushed_start in pushed_starts:
        is_box, success = attempt_push(is_wall, pushed_start, is_box, direction)
        if not success:
            return backup, False
    # Update position.
    is_box[xs[0]] = 0
    is_box[xs[1]] = 0
    is_box[new_xs[0]] = 1
    is_box[new_xs[1]] = 2
    return is_box, True


def checksum(is_box):
    m, n = is_box.shape
    i, j = np.meshgrid(np.arange(m), np.arange(n), indexing='ij')
    return np.sum((100 * i + j) * np.astype(is_box == 1, int))


def render(is_wall, is_box, start):
    m, n = is_wall.shape
    lines = [
        ["[" if is_box[i, j] == 1 else "]" if is_box[i, j] == 2
            else "#" if is_wall[i, j] else " " for j in range(n)]
        for i in range(m)
    ]
    if start is not None:
        lines[start[0]][start[1]] = "@"
    return "\n".join("".join(line) for line in lines)


if __name__ == '__main__':
    main()
