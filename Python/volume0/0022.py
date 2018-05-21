
def partial_max(L):
    n=len(L)
    max=-100000000000
    max_i=0
    for i in range(n):
       if max < sum(L[:i+1]):
           max=sum(L[:i+1])
           max_i=i
    max = -100000000000
    max_j=0
    for j in range(n):
       if max < sum(L[j:]):
           max=sum(L[j:])
           max_j=j

    if max_i >= max_j:
        return sum(L[max_j:max_i+1])
    elif sum(L[max_j:])>sum(L[:max_i+1]):
        return sum(L[max_j:])
    else:
        return sum(L[:max_i+1])
n=int(input())
A=[]
while n!=0:
    A.append([int(input()) for i in range(n)])
    n=int(input())
for i in range(len(A)):
    print(partial_max(A[i]))