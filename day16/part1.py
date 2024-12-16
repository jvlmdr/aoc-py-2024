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

    def heur(pos, dpos):
        rel = tuple(map(lambda a, b: a - b, goal, pos))
        return sum(map(abs, rel))

    pos, dpos = start, (0, 1)
    q = [(heur(pos, dpos), 0, pos, dpos)]
    min_cost_seen = {}
    while q:
        _, cost, pos, dpos = heapq.heappop(q)
        if pos == goal:
            print(cost)
            return

        if (pos, dpos) in min_cost_seen and min_cost_seen[pos, dpos] < cost:
            # Already visited this state with a lower cost. Do not extend.
            continue
        min_cost_seen[pos, dpos] = cost

        # Move forward.
        pos_ = tuple(map(lambda a, b: a + b, pos, dpos))
        if is_free[pos_]:
            cost_ = cost + 1
            heapq.heappush(q, (cost_ + heur(pos_, dpos), cost_, pos_, dpos))
        # Turn on the spot.
        for dpos_ in TURNS[dpos]:
            cost_ = cost + 1000
            heapq.heappush(q, (cost_ + heur(pos, dpos_), cost_, pos, dpos_))

    print('not reachable')


if __name__ == '__main__':
    main()
