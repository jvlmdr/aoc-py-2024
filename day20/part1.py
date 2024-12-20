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
    with open(sys.argv[1]) as f:
        lines = [s.rstrip('\n') for s in f]
    arr = np.array([list(s) for s in lines])
    is_open = arr != '#'
    start = tuple(map(int, np.squeeze(np.asarray(np.where(arr == 'S')))))
    end = tuple(map(int, np.squeeze(np.asarray(np.where(arr == 'E')))))
    dist = compute_distances(is_open, start, end)

    path_i, path_j = np.where(is_open)
    path_i = list(map(int, path_i))
    path_j = list(map(int, path_j))
    total = 0
    for i, j in zip(path_i, path_j):
        total += sum(1 for x in find_shortcuts_from(dist, (i, j)) if x >= 100)
    print(total)


def find_shortcuts_from(dist, start):
    assert np.isfinite(dist[start])
    shape = dist.shape
    q = [(start, 0)]
    while q:
        pos, depth = q.pop()
        assert depth <= 2
        if np.isfinite(dist[pos]):
            gain = dist[pos] - dist[start] - depth
            if gain > 0:
                yield int(gain)
        if depth == 2:
            continue
        for d in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            new_pos = (pos[0] + d[0], pos[1] + d[1])
            if not (0 <= new_pos[0] < shape[0] and 0 <= new_pos[1] < shape[1]):
                continue
            q.append((new_pos, depth + 1))


def compute_distances(is_open, start, end):
    dist = np.full(is_open.shape, np.inf)
    q = [(0, end)]
    visited = set()
    while q:
        path_len, pos = heapq.heappop(q)
        visited.add(pos)
        assert dist[pos] == np.inf, dist[pos]
        dist[pos] = path_len
        for d in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            new_pos = (pos[0] + d[0], pos[1] + d[1])
            if new_pos in visited:
                continue
            if is_open[new_pos]:
                heapq.heappush(q, (path_len + 1, new_pos))
    return dist


if __name__ == '__main__':
    main()
