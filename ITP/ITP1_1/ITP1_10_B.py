import math
a,b,C=map(int,input().split())
C=math.radians(C)
S=a*b*math.sin(C)/2
L=math.sqrt(a**2+b**2-2*a*b*math.cos(C))+a+b
h=b*math.sin(C)
print(S)
print(L)
print(h)
