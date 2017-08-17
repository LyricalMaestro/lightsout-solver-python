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

def split_to_intarray(mat):
    array_string = mat.split(",")
    return [ int(s) for s in array_string]

def print_input_lightsout(mat_array, size):
    print "-------      INPUT LIGHTSOUT  --------"
    for i in range(size):
        msg = " "
        for j in range(size):
            panel = ""
            if mat_array[i * size + j] % 2 == 1:
                panel = "■"
            else:
                panel = "□"
            msg += " " + panel
        print msg

def print_output_lightsout(mat_array, size):
    print "-------      OUTPUT LIGHTSOUT  --------"
    for i in range(size):
        msg = " "
        for j in range(size):
            panel = ""
            if mat_array[i * size + j] == f2.F2(1):
                panel = "■"
            else:
                panel = "□"
            msg += " " + panel
        print msg

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='LightsOut Solver')
    parser.add_argument('-s', type=int, choices=range_check(low_limit=2), help='LightsOut Size')
    parser.add_argument('-mat', help='LightsOut Init Matrix')
    argv_values = parser.parse_args()

    size = argv_values.s
    mat_array = split_to_intarray(argv_values.mat)
    need_min = argv_values.min
    if len(mat_array) !=  size * size:
        print "Error! -matに指定する値の数は-sで指定する値の自乗と同じにしてください。"

    print_input_lightsout(mat_array=mat_array, size=size)

    answer = lightsoutsolver.solve_lightsout(mat_array, size)
    if answer is None:
        print "-------      OUTPUT LIGHTSOUT  --------"
        print "not solvable."
    else:
        print_output_lightsout(mat_array=answer, size=size)
