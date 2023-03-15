"""
多项式GF(2)[x]运算（系数仅包含有限域的0与1）
0+0=0，0+1=1+0=1，1+1=0
0*0=0，0*1=1*0=0，1*1=1
使用整数代表多项式
0b101 -> x^2 + 1
------------------------------------
Polynomial GF (2) [x] operation (coefficients only contain 0 and 1 of finite fields)
"""


def add(a: int, b: int) -> int:
    return a ^ b


def sub(a: int, b: int) -> int:
    return a ^ b


def mul(a: int, b: int, poly: int = None) -> int:
    """
    :param a: 被乘数
    :param b: 乘数
    :param poly: 不可约多项式
    :return: 积
    """
    ans = 0
    if poly is None:
        digit_1 = None
    else:
        digit_1 = poly.bit_length() - 1
        a = divmod(a, poly)[1]
    while b:
        if b & 1:
            ans = ans ^ a
        a, b = a << 1, b >> 1
        if digit_1 is not None and a >> digit_1:  # 取出 a 的最高位
            a = a ^ poly
    return ans


def pow(a: int, n: int, mod: int = None) -> int:
    res = 1
    while n:
        if n & 1:
            res = mul(res, a, mod)
        a = mul(a, a, mod)
        n >>= 1
    return res


def divmod(a: int, b: int) -> (int, int):
    """
    :param a: 被除数
    :param b: 除数
    :return: 商, 余数
    """
    if b == 0:  # 除数不能为 0
        raise ZeroDivisionError
    ans = 0
    digit_a, digit_b = a.bit_length(), b.bit_length()
    while not a < b:
        rec = digit_a - digit_b
        a = a ^ (b << rec)
        ans = ans | (1 << rec)
        digit_a = a.bit_length()
    return ans, a


def inverse(a: int, poly: int):
    """求逆"""
    a, b = a, poly
    u1, u2 = 1, 0  # 初始化u1,u2
    while b:
        q, r = divmod(a, b)
        a, b = b, r
        u1, u2 = u2, u1 ^ mul(q, u2)
    return u1


class GF2Poly:
    def __init__(self, value: int, ir_poly: int = None):
        """多项式GF(2)[x] = value"""
        self.value = value
        self.ir_poly = ir_poly

    def __add__(self, other):
        """GF(2)[x]加法"""
        assert self.ir_poly == other.ir_poly, ""
        res = add(self.value, other.value)
        return GF2Poly(res, self.ir_poly)

    def __sub__(self, other):
        """GF(2)[x]减法"""
        assert self.ir_poly == other.ir_poly, ""
        res = sub(self.value, other.value)
        return GF2Poly(res, self.ir_poly)

    def __mul__(self, other):
        """GF(2)[x]乘法"""
        assert self.ir_poly == other.ir_poly, ""
        res = mul(self.value, other.value, self.ir_poly)
        return GF2Poly(res, self.ir_poly)

    def __truediv__(self, other):
        """GF(2)[x]除法"""
        assert self.ir_poly == other.ir_poly, ""
        q, r = divmod(self.value, other.value)
        return GF2Poly(q, self.ir_poly)

    def __mod__(self, other):
        """GF(2)[x]取模"""
        assert self.ir_poly == other.ir_poly, ""
        q, r = divmod(self.value, other.value)
        return GF2Poly(r, self.ir_poly)

    def __pow__(self, n: int):
        """GF(2)[x]幂"""
        res = pow(self.value, n, self.ir_poly)
        return GF2Poly(res, self.ir_poly)

    def inverse(self):
        """GF(2)[x]求逆"""
        assert self.ir_poly is not None, ""
        u = inverse(self.value, self.ir_poly)
        return GF2Poly(u, self.ir_poly)

    def __str__(self):
        return bin(self.value)

    def __eq__(self, other):
        assert self.ir_poly == other.ir_poly
        return self.value == other.value
