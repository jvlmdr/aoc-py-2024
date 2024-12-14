import collections
import functools
import heapq
import itertools
import math
from pprint import pprint
import re
import sys
import time

import numpy as np
from tqdm import tqdm


def main():
    with open(sys.argv[1]) as f:
        lines = [s.rstrip('\n') for s in f]
    robots = [parse_line(s) for s in lines]

    best = 2 * len(robots)
    nx, ny = 101, 103
    for t in tqdm(itertools.count(1)):
        robots = [
            (((px + vx) % nx, (py + vy) % ny), (vx, vy)) for (px, py), (vx, vy) in robots
        ]
        # Count the number of corners.
        arr = np.zeros((ny, nx), dtype=int)
        for (px, py), _ in robots:
            arr[py, px] += 1
        num_corners = np.sum(np.abs(np.diff(np.diff(arr, axis=1), axis=0)))

        if num_corners < best:
            best = num_corners
            print("best", best)
            print("TIME:", t)
            text = [[' ' for _ in range(nx)] for _ in range(ny)]
            for (px, py), _ in robots:
                text[py][px] = '#'
            print('\n'.join(''.join(row) for row in text))


p = re.compile(r'p=(\d+),(\d+) v=(-?\d+),(-?\d+)')

def parse_line(s):
    m = p.match(s)
    px, py, vx, vy = map(int, m.groups())
    return (px, py), (vx, vy)


if __name__ == '__main__':
    main()
