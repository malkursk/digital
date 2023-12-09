import math
import os
import numpy as np


def build_dictionary(form, keys=['extern_id', 'direction', 'width_bytes', 'key']):
    dct = {}
    for k in keys:
        dct.update({k: form.get(k)})
    return {key: v for key, v in dct.items() if v}


def check_file(file_name, max_file_size=1024 * 1024 * 10):  # проверка доступности и размера файла
    if not os.path.isfile(file_name):
        return False
    if (os.stat(file_name)).st_size > max_file_size:
        return False
    return True


def file_to_matrix(pth, width_bytes, bump_value=True):  # файл в матрицу
    def int_to_reverse_bin(num, min_len=8):  # перевод int в бинарный массив старшими битами вправо
        v = int(num)
        s = []
        while v > 0:
            s.append(v % 2)
            v = v // 2
        for i in range(0, min_len - len(s)):
            s.append(False)
        return s

    file_size = (os.stat(pth)).st_size
    buf = open(pth, "rb").read(file_size)
    arr = []
    for v in buf:
        arr.append(int_to_reverse_bin(v))

    matrix_rows = math.ceil(file_size / width_bytes)
    add = (matrix_rows * width_bytes - file_size) * 8
    if add % 8:
        arr.append(int_to_reverse_bin(0, add))
    for i in range(0, add // 8):
        arr.append(int_to_reverse_bin(0))

    matrix = np.matrix(arr).reshape(matrix_rows, width_bytes * 8)
    return np.pad(matrix, 1, 'constant', constant_values=bump_value)


def get_rule(v):
    alpha = 'ABCDEFGH'
    d = [[-1, -1], [0, -1], [1, -1], [1, 0], [1, 1], [0, 1], [-1, 1], [-1, 0]]
    return d[alpha.find(v)]


def calc_matrix(m, key_abc, is_fwd):
    row, col = m.shape

    f = [[1, row - 1, 1], [1, col - 1, 1]] if is_fwd else [[row - 2, 0, -1], [col - 2, 0, -1]]

    for i in range(f[0][0], f[0][1], f[0][2]):
        for j in range(f[1][0], f[1][1], f[1][2]):
            for v in key_abc:
                n = get_rule(v)
                m[i, j] ^= m[i + n[1], j + n[0]]

    return m.astype(int)


def matrix_to_file(m, file_name, file_size):
    def reverse_bin8_to_int(arr):
        r = int(arr[0])
        for i in range(1, 8):
            r += arr[i] << i
        return r

    row, col = m.shape
    m = m.reshape(1, row * col)
    tail = row * col % 8 - 1
    r = np.array(m[0::-tail])
    r = r.reshape((row * col // 8, 8))
    res = []
    for i in range(0, file_size):
        res.append(reverse_bin8_to_int(r[i]))

    f = open(file_name, 'wb')
    f.write(bytearray(res))
    return True


def crypto_cell(input_path, d={}):
    if check_file(input_path):
        if not ('direction' in d):  # порядок обхода: forward, reverse
            d.update({'direction': 'forward'})
        if not ('width_bytes' in d):  # ширина матрицы, байт: 1..9999
            d.update({'width_bytes': 4})
        if not ('key' in d):  # окрестность элемента: ABCDEFGH
            d.update({'key': 'AB'})

        fwd = d['direction'] == 'forward'  # используем прямой обход?
        mtr = file_to_matrix(input_path, int(d['width_bytes']))
        mtr = calc_matrix(mtr.astype(bool), d['key'], fwd)  # шифруем
        o_path = input_path + f'.{str(fwd)}-{str(d["width_bytes"])}-{d["key"]}.dat'
        matrix_to_file(mtr[1:-1, 1:-1], o_path, (os.stat(input_path)).st_size)  # сохраняем в файл без рамки
        return o_path
    else:
        return 'ОШИБКА: проверьте корректность исходных данных'