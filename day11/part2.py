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


def blink(s):
    if s == '0':
        return ['1']
    n = len(s)
    m = n // 2
    if n == 2 * m:
        return [s[:m], str(int(s[m:]))]
    return [str(2024 * int(s))]


@functools.lru_cache(maxsize=None)
def num_stones(stone, repeat):
    if repeat == 0:
        return 1
    return sum(num_stones(c, repeat - 1) for c in blink(stone))


if __name__ == '__main__':
    main()
