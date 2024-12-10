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

DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def main():
    with open(sys.argv[1]) as f:
        lines = [s.rstrip('\n') for s in f]
    heights = np.array([list(map(int, line)) for line in lines])
    heads = list(map(tuple, np.array(np.where(heights == 0)).T))
    size = heights.shape

    @functools.lru_cache(maxsize=None)
    def peaks_from(pos) -> int:
        if heights[pos] == 9:
            return 1
        peaks = 0
        for d in DIRECTIONS:
            next_pos = (pos[0] + d[0], pos[1] + d[1])
            if not (0 <= next_pos[0] < size[0] and 0 <= next_pos[1] < size[1]):
                continue
            if heights[next_pos] == heights[pos] + 1:
                peaks += peaks_from(next_pos)
        return peaks

    print(sum(map(peaks_from, heads)))

if __name__ == '__main__':
    main()
