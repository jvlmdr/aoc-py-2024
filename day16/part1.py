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

TURNS = {
    (1, 0): ((0, 1), (0, -1)),
    (-1, 0): ((0, 1), (0, -1)),
    (0, 1): ((1, 0), (-1, 0)),
    (0, -1): ((1, 0), (-1, 0)),
}


def main():
    with open(sys.argv[1]) as f:
        lines = [s.rstrip('\n') for s in f]
    grid = np.array(list(map(list, lines)))
    start = tuple(map(int, np.squeeze(np.asarray(np.where(grid == 'S')))))
    goal = tuple(map(int, np.squeeze(np.asarray(np.where(grid == 'E')))))
    is_free = grid != '#'

    pos, dpos = start, (0, 1)
    q = [(0, pos, dpos)]
    visited = set()
    while q:
        cost, pos, dpos = heapq.heappop(q)
        if pos == goal:
            print(cost)
            return

        if (pos, dpos) in visited:
            # Already visited this state with a lower cost. Do not extend.
            continue
        visited.add((pos, dpos))

        # Move forward.
        pos_ = tuple(map(lambda a, b: a + b, pos, dpos))
        if is_free[pos_]:
            cost_ = cost + 1
            heapq.heappush(q, (cost_, pos_, dpos))
        # Turn on the spot.
        for dpos_ in TURNS[dpos]:
            cost_ = cost + 1000
            heapq.heappush(q, (cost_, pos, dpos_))

    print('not reachable')


if __name__ == '__main__':
    main()
