w=eval(input())
n=eval(input())
edge=[]
for i in range(n):
    edge.append(tuple(map(int,input().split(','))))
for i in range(1,w+1):
    temp=i
    for j in range(n):
        if temp in edge[n-j-1]:
            temp=edge[n-j-1][edge[n-j-1].index(temp)-1]
    print(temp)
