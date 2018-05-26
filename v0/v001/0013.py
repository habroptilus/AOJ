import sys
a=[]
stack=[]
for line in sys.stdin:
    a.append(int(line))
for i in range(len(a)):
    if a[i]==0:
        print(stack[-1])
        del stack[-1]
    else:stack.append(a[i])
