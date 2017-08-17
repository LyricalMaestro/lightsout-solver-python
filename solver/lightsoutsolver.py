#coding: utf-8

from solver import f2matrixanalyzer
import f2

def __put_value_as_matrix(array, size, i, j, value):
    array[i * size + j] = value

def __count_non_zero_vector(f2_vector):
    count = 0
    for f in f2_vector:
        if f == f2.F2(1):
            count += 1
    return count

"""
指定したライトアウトをときます。
"""
def solve_lightsout(lights, size):
    array = [ 0 for i in range(size * size * size * size)]

    "タップ操作行列作成"
    for i in range(size):
        for j in range(size):
            target = i * size + j
            __put_value_as_matrix(array, size * size, target, target, 1)
            if i > 0:
                __put_value_as_matrix(array, size * size, target, (i - 1) * size + j, 1)
            if i < size - 1:
                __put_value_as_matrix(array, size * size, target, (i + 1) * size + j, 1)
            if j > 0:
                __put_value_as_matrix(array, size * size, target, i * size + j - 1, 1)
            if j < size - 1:
                __put_value_as_matrix(array, size * size, target, i * size + j + 1, 1)

    "行列分析"
    analyzer = f2matrixanalyzer.F2MatrixAnalyzer(array=array, size=size * size)
    analyzer.analyze()

    "このライツアウトが解けるかどうか"
    if analyzer.in_image(lights):
        "解ける場合最小の解を探る"
        coimage_list = analyzer.get_coimage_list(lights)
        val = None
        min_count = 9999999
        for coimage_vec in coimage_list:
            count = __count_non_zero_vector(coimage_vec)
            if val is None or count < min_count:
                val = coimage_vec
                min_count = count
        return val
    else:
        return None

"""
指定したサイズが「任意の初期状態のライト」でも解けるかどうかを判定します。
"""
def is_all_solvable_size(size):
    array = [ 0 for i in range(size * size * size * size)]

    "タップ操作行列作成"
    for i in range(size):
        for j in range(size):
            target = i * size + j
            __put_value_as_matrix(array, size * size, target, target, 1)
            if i > 0:
                __put_value_as_matrix(array, size * size, target, (i - 1) * size + j, 1)
            if i < size - 1:
                __put_value_as_matrix(array, size * size, target, (i + 1) * size + j, 1)
            if j > 0:
                __put_value_as_matrix(array, size * size, target, i * size + j - 1, 1)
            if j < size - 1:
                __put_value_as_matrix(array, size * size, target, i * size + j + 1, 1)

    "行列分析"
    analyzer = f2matrixanalyzer.F2MatrixAnalyzer(array=array, size=size * size)
    analyzer.analyze()
    return analyzer.has_inverse()

if __name__ == '__main__':
    solve_lightsout([1,0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1], 4)
