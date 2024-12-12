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
    arr = np.array(list(map(list, lines)))

    group = np.zeros_like(arr, dtype=int)

    def walk(pos, num):
        if group[pos]:
            return
        group[pos] = num
        for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            new_pos = (pos[0] + di, pos[1] + dj)
            if not (0 <= new_pos[0] < arr.shape[0] and 0 <= new_pos[1] < arr.shape[1]):
                continue
            if arr[new_pos] == arr[pos]:
                walk(new_pos, num)

    counter = 1
    for i in range(arr.shape[0]):
        for j in range(arr.shape[1]):
            if not group[i, j]:
                walk((i, j), counter)
                counter += 1

    group_ids = set(group.flatten())
    total = 0
    for group_id in group_ids:
        mask = group == group_id
        area = np.sum(mask)
        perim = calcPerim(mask)
        print(area, perim)
        total += area * perim
    print(total)


def calcPerim(mask):
    mask = np.pad(mask, ((1, 1), (1, 1)), 'constant', constant_values=0)
    return np.sum(np.diff(mask, axis=1) != 0) + np.sum(np.diff(mask, axis=0) != 0)


if __name__ == '__main__':
    main()
