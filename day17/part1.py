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
    register_lines = lines[:3]
    program_line = lines[4]
    registers = tuple([int(s.split(': ')[1]) for s in register_lines])
    instructions = list(map(int, program_line.split(': ')[1].split(',')))
    print(','.join(map(str, execute(instructions, registers))))


def execute(instructions, registers):
    counter = 0
    while 0 <= counter < len(instructions):
        registers, counter, out = step(instructions, registers, counter)
        if out is not None:
            yield out


def step(instructions, registers, counter):
    instr = instructions[counter]
    lit_val = instructions[counter + 1]
    combo_val = combo_operand(registers, lit_val)
    step = True
    out = None
    if instr == 0:
        y = registers[0] // (2 ** combo_val)
        registers = (y, registers[1], registers[2])
    elif instr == 1:
        y = registers[1] ^ lit_val
        registers = (registers[0], y, registers[2])
    elif instr == 2:
        y = combo_val % 8
        registers = (registers[0], y, registers[2])
    elif instr == 3:
        if registers[0] != 0:
            counter = lit_val
            step = False
    elif instr == 4:
        y = registers[1] ^ registers[2]
        registers = (registers[0], y, registers[2])
    elif instr == 5:
        y = combo_val % 8
        out = y
    elif instr == 6:
        y = registers[0] // (2 ** combo_val)
        registers = (registers[0], y, registers[2])
    elif instr == 7:
        y = registers[0] // (2 ** combo_val)
        registers = (registers[0], registers[1], y)
    else:
        raise ValueError('invalid instruction', instr)
    if step:
        counter = counter + 2
    return registers, counter, out


def combo_operand(registers, raw):
    if not 0 <= raw < 7:
        raise ValueError('invalid', raw)
    if raw < 4:
        return raw
    return registers[raw - 4]


if __name__ == '__main__':
    main()
