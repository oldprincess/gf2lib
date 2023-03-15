"""
GF2矩阵运算（元素仅包含0与1）
0+0=0，0+1=1+0=1，1+1=0
0*0=0，0*1=1*0=0，1*1=1
-------------------------------------------------------
GF2 matrix operation (elements only contain 0 and 1)
"""

from typing import List, Optional, Tuple
import copy


def identity(n: int) -> List[List[int]]:
    """n维单位阵"""
    return [[0 if c != r else 1 for c in range(n)] for r in range(n)]


def from_int(n: int, size: int = None) -> List[List[int]]:
    """整数转列向量, 0b100 -> [[1], [0], [0]]

    :param n: 整数
    :param size: 列向量长度
    """
    size = size if size is not None else n.bit_length()
    b_str = bin(n)[2::].rjust(size, '0')  # 构建01字符串
    return [[i] for i in list(map(int, b_str))]


def to_int(m: List[List[int]]) -> int:
    """列向量转整数, [[0], [1], [1]] -> 0b011"""
    assert len(m[0]) == 1, ""  # 列向量
    t = list(map(str, [i[0] for i in m]))
    t = ''.join(t)  # 转成01字符串
    return int(t, 2)


def equal(m1: List[List[int]], m2: List[List[int]]) -> bool:
    """矩阵判等"""
    row1, col1 = len(m1), len(m1[0])
    row2, col2 = len(m2), len(m2[0])
    assert row1 == row2 and col1 == col2, ""
    for r in range(row1):
        for c in range(col1):
            if m1[r][c] != m2[r][c]:
                return False
    return True


def h_stack(m1: List[List[int]], m2: List[List[int]]) -> List[List[int]]:
    """矩阵水平拼接(hstack)"""
    row1, col1 = len(m1), len(m1[0])
    row2 = len(m2)
    assert row1 == row2, ""
    return [copy.deepcopy(m1[r]) + copy.deepcopy(m2[r]) for r in range(row1)]


def h_slice(matrix: List[List[int]], start: int = None, stop: int = None, step: int = 1) -> List[List[int]]:
    """矩阵水平切片"""
    row = len(matrix)
    return [copy.deepcopy(matrix[r][start: stop: step]) for r in range(row)]


def v_stack(m1: List[List[int]], m2: List[List[int]]) -> List[List[int]]:
    """矩阵垂直拼接(vstack)"""
    col1 = len(m1[0])
    col2 = len(m2[0])
    assert col1 == col2, ""
    return copy.deepcopy(m1) + copy.deepcopy(m2)


def v_slice(matrix: List[List[int]], start: int = None, stop: int = None, step: int = 1) -> List[List[int]]:
    """矩阵垂直切片"""
    return copy.deepcopy(matrix[start: stop: step])


def transpose(matrix: List[List[int]]) -> List[List[int]]:
    """转置"""
    row, col = len(matrix), len(matrix[0])
    return [[matrix[r][c] for r in range(row)] for c in range(col)]


def inverse(matrix: List[List[int]]) -> Optional[List[List[int]]]:
    """矩阵求逆, 若无逆矩阵则返回None"""
    row, col = len(matrix), len(matrix[0])  # 矩阵的行列
    if row != col:
        return None
    t_matrix = [[matrix[r][c] for c in range(col)] for r in range(row)]  # 拷贝
    e_matrix = identity(row)  # 扩展矩阵

    for i in range(row):
        # 寻找第i列不为0的行
        for r in range(i, row):
            if t_matrix[r][i] != 0:
                if i != r:
                    # 交换两行
                    t_matrix[i], t_matrix[r] = t_matrix[r], t_matrix[i]
                    e_matrix[i], e_matrix[r] = e_matrix[r], e_matrix[i]
                break
        else:  # 找不到对应的行，没有逆矩阵
            return None

        # 对其它行的变换
        for r in range(row):
            if r != i:
                temp = t_matrix[r][i]
                for c in range(col):
                    e_matrix[r][c] = e_matrix[r][c] ^ (e_matrix[i][c] & temp)
                    t_matrix[r][c] = t_matrix[r][c] ^ (t_matrix[i][c] & temp)
    return e_matrix


def mul(m1: List[List[int]], m2: List[List[int]]) -> List[List[int]]:
    """矩阵乘法"""
    row1, col1 = len(m1), len(m1[0])
    row2, col2 = len(m2), len(m2[0])
    assert col1 == row2, ""
    res = [[0 for _ in range(col2)] for _ in range(row1)]
    for row in range(row1):
        for col in range(col2):
            res[row][col] = sum([m1[row][k] & m2[k][col] for k in range(col1)]) & 1
    return res


def add(m1: List[List[int]], m2: List[List[int]]) -> List[List[int]]:
    """矩阵加法"""
    row1, col1 = len(m1), len(m1[0])
    row2, col2 = len(m2), len(m2[0])
    assert row1 == row2 and col1 == col2, ""
    return [[m1[r][c] ^ m2[r][c] for c in range(col1)] for r in range(row1)]


class GF2Matrix:
    @staticmethod
    def identity(n: int):
        """创建n维单位矩阵"""
        return GF2Matrix(identity(n))

    @staticmethod
    def from_int(n: int, size: int = None):
        return GF2Matrix(from_int(n, size))

    def to_int(self):
        return to_int(self.matrix)

    def transpose(self):
        """矩阵转置"""
        return GF2Matrix(transpose(self.matrix))

    def inverse(self):
        return GF2Matrix(inverse(self.matrix))

    def __init__(self, matrix: List[List[int]]):
        self.matrix = copy.deepcopy(matrix)

    def __add__(self, other):
        return GF2Matrix(add(self.matrix, other.matrix))

    def __mul__(self, other):
        return GF2Matrix(mul(self.matrix, other.matrix))

    def __eq__(self, other):
        return equal(self.matrix, other.matrix)

    def __or__(self, other):
        """水平拼接"""
        return GF2Matrix(h_stack(self.matrix, other.matrix))

    def h_stack(self, other):
        return GF2Matrix(h_stack(self.matrix, other.matrix))

    def h_slice(self, start: int = None, stop: int = None, step: int = 1):
        return GF2Matrix(h_slice(self.matrix, start, stop, step))

    def v_stack(self, other):
        return GF2Matrix(v_stack(self.matrix, other.matrix))

    def v_slice(self, start: int = None, stop: int = None, step: int = 1):
        return GF2Matrix(v_slice(self.matrix, start, stop, step))

    def __getitem__(self, r_c: Tuple[int, int]):
        """获取r行c列的元素"""
        assert isinstance(r_c[0], int) and isinstance(r_c[1], int)
        return self.matrix[r_c[0]][r_c[1]]

    def __setitem__(self, r_c: Tuple[int, int], value: int):
        """设置r行c列的元素"""
        assert isinstance(r_c[0], int) and isinstance(r_c[1], int) and isinstance(value, int)
        self.matrix[r_c[0]][r_c[1]] = value

    def __str__(self):
        return str(self.matrix)
