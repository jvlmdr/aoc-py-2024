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
    disk = [None for _ in range(sum(sizes))]
    pos = 0
    index = 0
    is_file = True
    for size in sizes:
        for _ in range(size):
            if is_file:
                disk[pos] = index
            pos += 1
        if is_file:
            index += 1
        is_file = not is_file

    a = 0
    b = len(disk) - 1
    while a < b:
        if disk[a] is not None:
            a += 1
        elif disk[b] is None:
            b -= 1
        else:
            disk[a] = disk[b]
            disk[b] = None
            a += 1
            b -= 1

    print(sum([i * x for i, x in enumerate(disk) if x is not None]))


if __name__ == '__main__':
    main()
