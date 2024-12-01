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
    if len(sys.argv) < 2:
        print(f'Usage: {sys.argv[0]} data.txt')
        return
    with open(sys.argv[1]) as f:
        lines = [s.rstrip() for s in f]

    nums = [[int(s) for s in line.split()] for line in lines]
    first = [x[0] for x in nums]
    second = [x[1] for x in nums]
    first = np.sort(first)
    second = np.sort(second)
    print(np.sum(np.abs(first - second)))


if __name__ == '__main__':
    main()
