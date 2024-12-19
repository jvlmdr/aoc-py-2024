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
    def can_make(design):
        if design == "":
            return True
        for towel in towels:
            if design.startswith(towel) and can_make(design[len(towel):]):
                return True
        return False

    print(sum(1 for design in designs if can_make(design)))


if __name__ == '__main__':
    main()
