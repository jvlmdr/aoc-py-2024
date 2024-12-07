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
        if can_reach(y, xs[::-1]):
            total += y
    print(total)


def parse_line(s):
    result, xs = s.split(': ')
    return int(result), tuple(map(int, xs.split(' ')))


def can_reach(y, xs):
    if not xs:
        return y == 0
    x, xs = xs[0], xs[1:]
    if y - x >= 0 and can_reach(y - x, xs):
        return True
    if y % x == 0 and can_reach(y // x, xs):
        return True
    y_str = str(y)
    x_str = str(x)
    n = len(x_str)
    if len(y_str) > n and y_str[-n:] == x_str and can_reach(int(y_str[:-n]), xs):
        return True
    return False


if __name__ == '__main__':
    main()
