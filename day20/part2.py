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
    max_dist = int(sys.argv[3])
    with open(sys.argv[1]) as f:
        lines = [s.rstrip('\n') for s in f]
    arr = np.array([list(s) for s in lines])
    bounds = arr.shape
    path = set(map(tuple, np.array(np.where(arr != '#')).T.tolist()))
    end, = map(tuple, np.array(np.where(arr == 'E')).T.tolist())
    dist = compute_distances(path, end)

    shortcuts = {}
    for a in tqdm(dist.keys()):
        for b, gain in find_shortcuts_from(bounds, dist, a, max_dist):
            if not gain >= min_gain:
                continue
            shortcuts[a, b] = max(shortcuts.get((a, b), 0), gain)
    print(len(shortcuts))


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


def find_shortcuts_from(bounds, dist, start, max_depth):
    q = collections.deque([(start, 0)])
    visited = set()
    while q:
        pos, depth = q.popleft()
        if pos in visited:
            continue
        visited.add(pos)
        if pos in dist:
            gain = dist[pos] - dist[start] - depth
            if gain > 0:
                yield (pos, int(gain))
        if not depth < max_depth:
            continue
        for d in DIRECTIONS:
            new_pos = (pos[0] + d[0], pos[1] + d[1])
            if not (0 <= new_pos[0] < bounds[0] and 0 <= new_pos[1] < bounds[1]):
                continue
            q.append((new_pos, depth + 1))


if __name__ == '__main__':
    main()
