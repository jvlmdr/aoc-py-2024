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
    text = '\n'.join(lines)
    blocks = [block.split('\n') for block in text.split('\n\n')]

    locks = [b for b in blocks if is_lock(b)]
    keys = [b for b in blocks if not is_lock(b)]

    total = 0
    for lock in locks:
        for key in keys:
            if compare(lock, key):
                total += 1
    print(total)


def is_lock(block):
    return all(x == '#' for x in block[0])


def compare(lock, key):
    lock = np.array(list(map(list, lock))) == '#'
    key = np.array(list(map(list, key))) == '#'
    return not np.any(lock & key)


if __name__ == '__main__':
    main()
