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
    stones = line.split()
    print(sum(num_stones(s, 75) for s in stones))


def blink(stones):
    for s in stones:
        n = len(s)
        if s == '0':
            yield '1'
            continue
        if n % 2 == 0:
            yield str(int(s[:n//2]))
            yield str(int(s[n//2:]))
            continue
        else:
            yield str(2024 * int(s))


@functools.lru_cache(maxsize=None)
def num_stones(stone, repeat):
    if repeat == 0:
        return 1
    children = list(blink([stone]))
    return sum(num_stones(c, repeat - 1) for c in children)


if __name__ == '__main__':
    main()
