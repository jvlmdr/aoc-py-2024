import collections
import functools
import heapq
import itertools
import math
from pprint import pprint
import re
import sys

import numpy as np
from sortedcontainers import SortedDict
from tqdm import tqdm


def main():
    with open(sys.argv[1]) as f:
        lines = [s.rstrip('\n') for s in f]
    line, = lines
    sizes = list(map(int, line))

    init_disk = list(parse_sections(sizes))
    curr_disk = SortedDict({pos: (size, index) for pos, size, index in init_disk})
    # Walk backwards through the objects.
    for pos, size, index in reversed(init_disk):
        if index is None:
            continue
        assert pos in curr_disk
        for pos_, (size_, index_) in curr_disk.items():
            if pos_ >= pos:
                break
            if index_ is not None:
                continue
            leftover = size_ - size
            if leftover < 0:
                continue
            # We've found our spot!
            del curr_disk[pos]
            curr_disk[pos_] = (size, index)
            if leftover > 0:
                curr_disk[pos_ + size] = (leftover, None)
            break

    print(sum([
        index * sum(range(pos, pos + size))
        for pos, (size, index) in curr_disk.items()
        if index is not None
    ]))


def parse_sections(sizes):
    pos = 0
    index = 0
    is_file = True
    for size in sizes:
        yield (pos, size, index if is_file else None)
        pos += size
        if is_file:
            index += 1
        is_file = not is_file


if __name__ == '__main__':
    main()
