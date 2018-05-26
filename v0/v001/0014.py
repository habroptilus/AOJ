import sys
D=[]
for line in sys.stdin:
    D.append(int(line))
for d in D:
    print(sum([(((i+1)*d)**2)*d for i in range(int(600/d)-1)]))
