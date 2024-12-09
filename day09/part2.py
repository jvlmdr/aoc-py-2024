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
    # Walk backwards through the disk.
    i = len(disk) - 1
    while i > 0:
        pos_i, size_i, name_i = disk[i]
        # Walk forwards through the disk.
        for j in range(i):
            pos_j, size_j, index_j = disk[j]
            pos_k, _, _ = disk[j + 1]
            if pos_j + size_j + size_i <= pos_k:
                disk.pop(i)
                disk.insert(j + 1, (pos_j + size_j, size_i, name_i))
                i += 1
                break
            j += 1
        i -= 1

    print(sum([
        index * sum(range(pos, pos + size)) for pos, size, index in disk
    ]))


def parse_sections(sizes):
    pos = 0
    index = 0
    is_file = True
    for size in sizes:
        if is_file:
            yield (pos, size, index)
            index += 1
        pos += size
        is_file = not is_file


if __name__ == '__main__':
    main()
