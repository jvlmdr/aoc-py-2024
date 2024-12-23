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
import networkx as nx


def main():
    with open(sys.argv[1]) as f:
        lines = [s.rstrip('\n') for s in f]
    edges = [l.split('-') for l in lines]

    neighbors = collections.defaultdict(set)
    for a, b in edges:
        neighbors[a].add(b)
        neighbors[b].add(a)

    triples = set()
    for a in neighbors:
        for b in neighbors[a]:
            if not a < b:
                continue
            common = neighbors[a].intersection(neighbors[b])
            for c in common:
                if not b < c:
                    continue
                triples.add((a, b, c))

    print(sum(1 for triple in triples if any(map(lambda x: x.startswith('t'), triple))))


if __name__ == '__main__':
    main()
