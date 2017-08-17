#coding: utf-8

import argparse
import os
from solver import lightsoutsolver
from solver import f2
from utils import validator

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='LightsOut Solver')
    parser.add_argument('-s', type=int, choices=validator.range_check(low_limit=2), help='LightsOut Size')
    argv_values = parser.parse_args()
    size = argv_values.s

    always_solvable = lightsoutsolver.is_all_solvable_size(size)
    if always_solvable:
        print "size %d lightsout is always solvable." % size
    else:
        print "size %d lightsout is *not* always solvable." % size
