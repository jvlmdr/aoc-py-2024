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

    def parse_line(s):
        result, inputs = s.split(': ')
        result = int(result)
        inputs = list(map(int, inputs.split(' ')))
        return result, inputs

    lines = list(map(parse_line, lines))
    total = 0
    for output, inputs in lines:
        if can_reach(output, inputs[::-1]):
            total += output
    print(total)


def can_reach(output, inputs):
    if not inputs:
        return False
    x, xs = inputs[0], inputs[1:]
    if not xs:
        return x == output
    if output - x >= 0 and can_reach(output - x, xs):
        return True
    if output % x == 0 and can_reach(output // x, xs):
        return True
    return False


if __name__ == '__main__':
    main()
