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

from networkx.drawing.nx_pydot import write_dot

ops = {
    'AND': lambda a, b: a & b,
    'OR': lambda a, b: a | b,
    'XOR': lambda a, b: a ^ b,
}


def main():
    with open(sys.argv[1]) as f:
        lines = [s.rstrip('\n') for s in f]
    m = lines.index('')
    gate_lines = lines[m + 1:]
    gates = [parse_gate(l) for l in gate_lines]
    z_names = sorted([c for c, _, _, _ in gates if c.startswith('z')])
    n = len(z_names)
    gate_op = {c: op for c, op, _, _ in gates}

    g = nx.DiGraph(itertools.chain.from_iterable([(a, c), (b, c)] for c, _, a, b in gates))
    suspect = set()
    for i in range(n - 1):
        # Expect single AND between x{i}, y{i} and z{i}.
        x = f'x{i:02d}'
        y = f'y{i:02d}'
        z = f'z{i:02d}'
        anc_z = set(nx.ancestors(g, z))
        desc_x = set(nx.descendants(g, x))
        desc_y = set(nx.descendants(g, y))
        inter = desc_x.union(desc_y).intersection(anc_z)
        inter_op = sorted([gate_op[k] for k in inter])
        if inter_op != ['XOR']:
            print('suspect:', (x, y), z, inter_op)
            suspect |= inter | {z}

        # Expect 2x AND, 1x OR, 1x XOR between x{i}, y{i} and z{i+1}.
        z = f'z{i + 1:02d}'
        anc_z = set(nx.ancestors(g, z))
        inter = desc_x.union(desc_y).intersection(anc_z)
        inter_op = sorted([gate_op[k] for k in inter])
        if inter_op != ['AND', 'AND', 'OR', 'XOR']:
            print('suspect:', (x, y), z, inter_op)
            suspect |= inter | {z}

    print('num suspect:', len(suspect))
    print('suspect:', suspect)

    h = nx.relabel_nodes(g, {c: f'{c}_{gate_op[c]}' for c in g.nodes if c in gate_op}, copy=True)
    write_dot(h, 'graph.dot')


def parse_value(l):
    a, b = l.split(': ')
    return a, int(b)


def parse_gate(l):
    m = re.match(r'(\w+) (AND|OR|XOR) (\w+) -> (\w+)', l)
    a, op, b, c = m.groups()
    return c, op, a, b


if __name__ == '__main__':
    main()
