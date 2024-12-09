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
    sizes = list(map(int, line))
    disk = list(parse_sections(sizes))

    # Try to move each file to the left.
    i = len(disk) - 1
    while i > 0:
        pos_i, size_i, index_i = disk[i]
        if index_i is None:
            disk.pop(i)
            i -= 1
            continue
        # Look for a free space to the left.
        for j in range(i):
            pos_j, size_j, index_j = disk[j]
            if index_j is not None:
                continue
            delta = size_j - size_i
            if delta < 0:
                continue
            # Replace the empty space with the object.
            disk.pop(i)
            disk[j] = (pos_j, size_i, index_i)
            # Insert remaining empty space between this object and the next.
            if delta > 0:
                disk.insert(j + 1, (pos_j + size_i, delta, None))
                i += 1
            break
        i -= 1

    print(sum([
        index * sum(range(pos, pos + size)) for pos, size, index in disk
        if index is not None
    ]))


def parse_sections(sizes):
    pos = 0
    index = 0
    is_file = True
    for size in sizes:
        yield (pos, size, index if is_file else None)
        if is_file:
            index += 1
        pos += size
        is_file = not is_file


if __name__ == '__main__':
    main()
