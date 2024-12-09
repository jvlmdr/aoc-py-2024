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
    line, = lines
    ns = list(map(int, line))
    usage = [-1 for _ in range(sum(ns))]
    cursor = 0
    index = 0
    is_file = True
    objs = []
    for n in ns:
        objs.append((is_file, cursor, n, index if is_file else None))
        for _ in range(n):
            if is_file:
                usage[cursor] = index
            cursor += 1
        if is_file:
            index += 1
        is_file = not is_file

    # Try to move each file to the left.
    i = len(objs) - 1
    while i > 0:
        # Attempt to move each file back to the left.
        is_file_i, cursor_i, size_i, index_i = objs[i]
        if not is_file_i:
            i -= 1
            continue
        # Look for a free space to the left.
        for j in range(i):
            is_file_j, cursor_j, size_j, index_j = objs[j]
            if is_file_j:
                continue
            delta = size_j - size_i
            if delta < 0:
                continue
            # Replace the space.
            del objs[i]
            objs[j] = (is_file_i, cursor_j, size_i, index_i)
            if delta > 0:
                objs.insert(j + 1, (False, cursor_j + size_i, delta, None))
                i += 1
            break
        i -= 1

    usage = [-1 for _ in range(sum(ns))]
    cursor = 0
    for is_file, cursor, size, index in objs:
        if is_file:
            for _ in range(size):
                usage[cursor] = index
                cursor += 1
    print(sum([i * x for i, x in enumerate(usage) if x >= 0]))


if __name__ == '__main__':
    main()
