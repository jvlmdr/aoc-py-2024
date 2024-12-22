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
    init_codes = [int(s) for s in lines]
    prices = collections.defaultdict(dict)
    for i, code in enumerate(tqdm(init_codes)):
        code_seq = list(itertools.accumulate(range(2000), lambda x, _: evolve(x), initial=code))
        price_seq = np.asarray(code_seq) % 10
        for t in range(len(price_seq)):
            hist = tuple(np.diff(price_seq[:t+1][-5:]))
            if len(hist) != 4:
                continue
            if i not in prices[hist]:
                prices[hist][i] = price_seq[t]
    print(max((sum(v.values()), k) for k, v in prices.items()))


def evolve(x):
    x = ((x * 64) ^ x) % 16777216
    x = ((x // 32) ^ x) % 16777216
    x = ((x * 2048) ^ x) % 16777216
    return x


if __name__ == '__main__':
    main()
