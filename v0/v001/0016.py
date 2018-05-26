from math import *

x = 0
y = 0
D = []
A = []
sum_a = -90
while True:
    d, a = map(int, input().split(","))
    if a == 0 and d == 0:
        break
    else:
        D.append(d)
        A.append(a)
for i in range(len(A)):
    x = x + D[i] * cos(sum_a * pi / 180)
    y = y - D[i] * sin(sum_a * pi / 180)
    if abs(x-round(x))<10**(-7):
        x=round(x)
    if abs(y - round(y)) < 10 ** (-7):
        y=round(y)
    sum_a += A[i]
if x >= 0:
    print(floor(x))
else:
    print(floor(x)+1)
if y >= 0:
    print(floor(y))
else:
    print(floor(y)+1)

