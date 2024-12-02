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

    nums = [[int(s) for s in line.split()] for line in lines]
    first = [x[0] for x in nums]
    second = [x[1] for x in nums]
    counts = dict(collections.Counter(second))
    dist = [a * counts.get(a, 0) for a in first]
    print(sum(dist))


if __name__ == '__main__':
    main()
