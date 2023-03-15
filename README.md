# gf2lib

gf2lib是一个操作有限域GF(2)多项式和GF(2)矩阵的库

* gf2lib.gf2poly：GF(2)多项式
* gf2lib.gf2matrix：GF(2)矩阵

## 一、 快速开始

* （1） 通过pip安装

```bash
pip install gf2lib
```

* （2）直接拷贝位于src中的源代码

## 二、 demo

更多参考样例见GitHub中的example文件夹，[gf2lib](https://github.com/oldprincess/gf2lib)

* （1） gf2poly

```python
from gf2lib.gf2poly import GF2Poly

ir_poly = 0x11b  # p(x)=x^8+x^4+x^3+x+1

a = GF2Poly(0b101, ir_poly)  # x^2+1
b = GF2Poly(0b010, ir_poly)  # x

print(a.value)  # 0b101
print(a.ir_poly)  # 0b100011011
print(a)  # 0b101

c = a + b  # 加法
d = a * b  # 乘法
e = a ** 4  # 幂
f = a / b  # 除法
g = a % b  # 模
h = a.inverse()  # 求逆
```

* （2） gf2matrix

```python
from gf2lib.gf2matrix import GF2Matrix

M = GF2Matrix([[0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1], [1, 0, 0, 0]])
M = M * M  # 乘法
M = M.inverse()  # 求逆
print(M)  # [[0, 0, 1, 0], [0, 0, 0, 1], [1, 0, 0, 0], [0, 1, 0, 0]]
```

---

# gf2lib
gf2lib is a library for manipulating GF (2) polynomials and GF (2) matrices over finite fields

* gf2lib.gf2poly: GF (2) polynomial
* gf2lib.gf2matrix: GF (2) matrix

## 1. Quick Start

* (1) Install via pip

```bash
pip install gf2lib
```

* (2) Directly copy the source code in src

## 2. Demo

For more reference examples, see the example folder in GitHub. [gf2lib](https://github.com/oldprincess/gf2lib)
