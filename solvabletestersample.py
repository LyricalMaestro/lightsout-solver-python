#coding: utf-8

import argparse
import os
from solver import lightsoutsolver
from solver import f2

class range_check(object):
    def __init__(self, low_limit=None, high_limit=None, vtype="integer"):
        self.min = low_limit
        self.max = high_limit
        self.type = vtype

    def __contains__(self, val):
        ret = True
        if self.min is not None:
            ret = ret and (val >= self.min)
        if self.max is not None:
            ret = ret and (val <= self.max)
        return ret

    def __iter__(self):
        low = self.min
        if low is None:
            low = "-inf"
        high = self.max
        if high is None:
            high = "+inf"
        L1 = self.type
        L2 = " {} <= x <= {}".format(low, high)
        return iter((L1, L2))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='LightsOut Solver')
    parser.add_argument('-s', type=int, choices=range_check(low_limit=2), help='LightsOut Size')
    argv_values = parser.parse_args()
    size = argv_values.s

    always_solvable = lightsoutsolver.is_all_solvable_size(size)
    if always_solvable:
        print "size %d lightsout is always solvable." % size
    else:
        print "size %d lightsout is *not* always solvable." % size
