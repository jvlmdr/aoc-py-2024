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
    robots = [parse_line(s) for s in lines]

    nx, ny = 101, 103
    for t in range(100):
        robots = [
            (((px + vx) % nx, (py + vy) % ny), (vx, vy)) for (px, py), (vx, vy) in robots
        ]
        pprint(robots)

    # Count number in each quadrant.
    mx, my = nx // 2, ny // 2
    print(mx, my)
    quadrants = [0, 0, 0, 0]
    for (px, py), _ in robots:
        if px == mx or py == my:
            continue
        if px < mx and py < my:
            quadrants[0] += 1
        elif px < mx and py > my:
            quadrants[1] += 1
        elif px > mx and py < my:
            quadrants[2] += 1
        elif px > mx and py > my:
            quadrants[3] += 1
    print(quadrants)
    print(math.prod(quadrants))


p = re.compile(r'p=(\d+),(\d+) v=(-?\d+),(-?\d+)')

def parse_line(s):
    m = p.match(s)
    px, py, vx, vy = map(int, m.groups())
    return (px, py), (vx, vy)




if __name__ == '__main__':
    main()
