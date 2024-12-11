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
    for _ in range(25):
        stones = list(itertools.chain.from_iterable(blink(s) for s in stones))
    print(len(stones))


def blink(s):
    if s == '0':
        return ['1']
    n = len(s)
    m = n // 2
    if n == 2 * m:
        return [s[:m], str(int(s[m:]))]
    return [str(2024 * int(s))]


if __name__ == '__main__':
    main()
