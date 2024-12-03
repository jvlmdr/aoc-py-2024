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
    p = re.compile(r'mul\((\d+),(\d+)\)')
    total = 0
    for line in lines:
        ms = p.findall(line)
        for m in ms:
            a, b = map(int, m)
            total += a * b
    print(total)


if __name__ == '__main__':
    main()
