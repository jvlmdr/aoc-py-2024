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

ops = {
    'AND': lambda a, b: a & b,
    'OR': lambda a, b: a | b,
    'XOR': lambda a, b: a ^ b,
}


def main():
    with open(sys.argv[1]) as f:
        lines = [s.rstrip('\n') for s in f]
    m = lines.index('')
    values_lines = lines[:m]
    gate_lines = lines[m + 1:]
    values = dict(parse_value(l) for l in values_lines)
    gates = [parse_gate(l) for l in gate_lines]
    z_names = sorted([c for c, _, _, _ in gates if c.startswith('z')])
    while not all(k in values for k in z_names):
        for c_name, op_name, a_name, b_name in gates:
            if a_name in values and b_name in values:
                values[c_name] = ops[op_name](values[a_name], values[b_name])
    zs = [(int(k[1:]), values[k]) for k in z_names]
    print(sum(b * (2 ** a) for a, b in zs))


def parse_value(l):
    a, b = l.split(': ')
    return a, int(b)


def parse_gate(l):
    m = re.match(r'(\w+) (AND|OR|XOR) (\w+) -> (\w+)', l)
    a, op, b, c = m.groups()
    return c, op, a, b


if __name__ == '__main__':
    main()
