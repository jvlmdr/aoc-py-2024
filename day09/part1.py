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
    for n in ns:
        for _ in range(n):
            if is_file:
                usage[cursor] = index
            cursor += 1
        if is_file:
            index += 1
        is_file = not is_file
    print(usage)

    a = 0
    b = len(usage) - 1
    while a < b:
        if usage[a] >= 0:
            a += 1
        elif usage[b] < 0:
            b -= 1
        else:
            assert usage[a] == -1
            assert usage[b] != -1
            usage[a] = usage[b]
            usage[b] = -1
            a += 1
            b -= 1

    print(sum([i * x for i, x in enumerate(usage) if x >= 0]))


if __name__ == '__main__':
    main()
