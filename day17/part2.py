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
    program_line = lines[4]
    instructions = list(map(int, program_line.split(': ')[1].split(',')))
    print(next(solutions(instructions)))


def calc_output(a):
    b = a % 8
    b = b ^ 5
    c = a // (2 ** b)
    b = b ^ 6
    a = a // 8
    b = b ^ c
    return b % 8


def solutions(instructions):
    if len(instructions) == 1:
        want, = instructions
        # Consider a such that a // 8 == 0.
        for a in range(1, 8):
            if calc_output(a) == want:
                yield a
    else:
        want, *rest = instructions
        # Consider a such that a // 8 is valid for next step.
        for next_a in solutions(rest):
            for i in range(8):
                a = next_a * 8 + i
                if calc_output(a) == want:
                    yield a


def execute(a):
    out = []
    while a != 0:
        _, y = calc_output(a)
        out.append(y)
        a = a // 8
    return out


if __name__ == '__main__':
    main()
