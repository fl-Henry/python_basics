"""
### Задача: Шкаф в люк

Определить, пройдет ли прямоугольный параллелепипед с ребрами A, B, C
через круглое окно с заданной площадью.

"""
from math import sqrt, pi

S = 55
A, B, C = 6, 9, 3.1
print(A, B, C)

R = sqrt(S / pi)
D = 2 * R
print(f'R = {R} ; D = {D}')

# 0 <= alf <= math.pi / 2)
# a == R * sin(...)
#
# A == 2 * a
# A == 2 * R * sin(alf)

# sin(alf) == A / (2 * R)
#
# B == 2 * R * cos(alf)
#
# 1 == sin(alf) ** 2 + cos(alf) ** 2
# cos(alf) == sqrt(1 - (sin(alf) ** 2))
# cos(alf) == sqrt(1 - (A / (2 * R)) ** 2)
# B_max == 2 * R * sqrt(1 - A / R)

# A x B
# B x C
# A x C
B_max, C_max, A_max = 0, 0, 0

if D > max(A, C):
    A_max = D * sqrt(1 - (C / D) ** 2)
if D > max(A, B):
    B_max = D * sqrt(1 - (A / D) ** 2)
if D > max(C, B):
    C_max = D * sqrt(1 - (B / D) ** 2)

print(A_max, B_max, C_max)
if A_max >= A or B_max >= B or C_max >= C:
    print(True)
else:
    print(False)
