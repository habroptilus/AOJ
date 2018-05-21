
x=[]
while True:
    i=int(raw_input())
    if i==0:
        break;
    x.append(i)
X=iter(x)
i=1
for a in X:
    print('Case %d: %d'%(i,a))
    i+=1
