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
    p = re.compile(r'(mul\((\d+),(\d+)\)|do\(\)|don\'t\(\))')
    total = 0
    enabled = True
    for line in lines:
        ms = p.findall(line)
        for m in ms:
            if m[0] == 'do()':
                enabled = True
            elif m[0] == 'don\'t()':
                enabled = False
            else:
                a, b = int(m[1]), int(m[2])
                if enabled:
                    total += a * b
    print(total)


if __name__ == '__main__':
    main()
