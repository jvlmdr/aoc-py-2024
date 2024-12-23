import collections
import functools
import heapq
import itertools
import math
from pprint import pprint
import re
import sys

import networkx as nx
import numpy as np
from tqdm import tqdm


def main():
    with open(sys.argv[1]) as f:
        lines = [s.rstrip('\n') for s in f]
    edges = [l.split('-') for l in lines]
    g = nx.Graph(edges)
    max_clique = max(nx.find_cliques(g), key=len)
    print(','.join(sorted(max_clique)))


if __name__ == '__main__':
    main()
