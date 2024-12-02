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
    count = 0
    for row in arr:
        for i in range(len(row)):
            tmp = row[:i] + row[i + 1:]
            delta = np.diff(tmp)
            if (np.all(delta > 0) or np.all(delta < 0)) and all(np.abs(delta) <= 3):
                count += 1
                break
    print(count)


if __name__ == '__main__':
    main()
