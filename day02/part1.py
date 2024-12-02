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

    arr = [list(map(int, line.split())) for line in lines]
    deltas = [np.diff(row) for row in arr]
    const_sign = [np.all(delta > 0) | np.all(delta < 0) for delta in deltas]
    moderate = [np.all(np.abs(delta) <= 3) for delta in deltas]
    print(np.count_nonzero(np.logical_and(const_sign, moderate)))


if __name__ == '__main__':
    main()
