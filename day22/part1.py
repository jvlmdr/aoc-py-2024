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
    init_codes = [int(s) for s in lines]
    total = 0
    for code in tqdm(init_codes):
        for _ in range(2000):
            code = evolve(code)
        total += code
    print(total)


def evolve(x):
    x = ((x * 64) ^ x) % 16777216
    x = ((x // 32) ^ x) % 16777216
    x = ((x * 2048) ^ x) % 16777216
    return x


if __name__ == '__main__':
    main()
