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
    lines = list(map(parse_line, lines))
    total = 0
    for y, xs in lines:
        if can_reach(y, xs):
            total += y
    print(total)


def parse_line(s):
    result, xs = s.split(': ')
    return int(result), tuple(map(int, xs.split(' ')))


def can_reach(y, xs):
    if not xs:
        return y == 0
    xs, x = xs[:-1], xs[-1]
    # y = ... + x ?
    if y - x >= 0 and can_reach(y - x, xs):
        return True
    # y = ... * x ?
    if y % x == 0 and can_reach(y // x, xs):
        return True
    return False


if __name__ == '__main__':
    main()
