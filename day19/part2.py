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
    towels = lines[0].split(", ")
    designs = lines[2:]

    @functools.cache
    def num_ways(design):
        if design == "":
            return 1
        count = 0
        for towel in towels:
            if design.startswith(towel):
                count += num_ways(design[len(towel):])
        return count

    print(sum(num_ways(design) for design in designs))


if __name__ == '__main__':
    main()
