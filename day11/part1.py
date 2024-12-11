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
    for i in range(25):
        stones = list(blink(stones))
    print(len(stones))


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


if __name__ == '__main__':
    main()
