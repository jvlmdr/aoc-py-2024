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

DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0)]


def main():
    min_gain = int(sys.argv[2])
    max_len = int(sys.argv[3])
    with open(sys.argv[1]) as f:
        lines = [s.rstrip('\n') for s in f]
    arr = np.array([list(s) for s in lines])
    path = set(map(tuple, np.array(np.where(arr != '#')).T.tolist()))
    end, = map(tuple, np.array(np.where(arr == 'E')).T.tolist())
    dist = compute_distances(path, end)

    count = 0
    for a, dist_a in tqdm(dist.items()):
        for b, dist_b in dist.items():
            if not dist_a > dist_b:
                continue
            shortcut_len = abs(a[0] - b[0]) + abs(a[1] - b[1])
            if not shortcut_len <= max_len:
                continue
            gain = dist_a - (dist_b + shortcut_len)
            if gain >= min_gain:
                count += 1
    print(count)


def compute_distances(path, goal):
    dist = {}
    pos, prev = goal, None
    for i in itertools.count():
        dist[pos] = i
        neighbors = [
            x for x in [(pos[0] + d[0], pos[1] + d[1]) for d in DIRECTIONS]
            if x in path and x != prev
        ]
        if len(neighbors) == 0:
            break
        prev = pos
        pos, = neighbors
    return dist


if __name__ == '__main__':
    main()
