from gf2lib import gf2poly
from gf2lib.gf2poly import GF2Poly

a = 0b101  # x^2+1
b = 0b010  # x

c = gf2poly.add(a, b)  # 加法
c = gf2poly.mul(a, b)  # 乘法
c = gf2poly.pow(a, 4)  # 幂
q, r = gf2poly.divmod(a, b)  # 除法

ir_poly = 0x11b  # p(x)=x^8+x^4+x^3+x+1

c = gf2poly.mul(a, b, ir_poly)  # 模乘
c = gf2poly.pow(a, 4, ir_poly)  # 模幂
c = gf2poly.inverse(a, ir_poly)  # 逆(a^-1 mod ir_poly)

# =======================================================

a = GF2Poly(0b101)  # 未设置不可约多项式
b = GF2Poly(0b010)  # 未设置不可约多项式

c = a + b  # 加法
c = a * b  # 乘法
c = a ** 4  # 幂
c = a / b  # 除法
c = a % b  # 模
cmp = (a * b == b * a)  # 比较

# ==========================================================

a = GF2Poly(0b101, ir_poly)  # 设置不可约多项式
b = GF2Poly(0b010, ir_poly)  # 设置不可约多项式

c = a.inverse()  # a^-1 mod ir_poly
