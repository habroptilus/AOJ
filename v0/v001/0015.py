N = int(input())
A = []
B = []
for i in range(N):
    a = int(input())
    b = int(input())
    A.append(a)
    B.append(b)

for i in range(N):
    if A[i] >= 10 ** 80 or B[i] >= 10 ** 80:
        print("overflow")
    elif A[i] + B[i] >= 10 ** 80:
        print("overflow")
    else:
        print(str(A[i] + B[i]))
