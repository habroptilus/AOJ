def getInput():
    N = int(input())
    numbers = []
    for i in range(N):
        numbers.append(int(input()))
    return numbers


R = getInput()
min = 10000000000
max = -10000000000
for i in range(len(R)):
    if R[i] - min > max:
        max = R[i] - min
    if min > R[i]:
        min = R[i]
print(max)
