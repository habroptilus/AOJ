x=[]
y=[]
while True:
    i,j=map(int,raw_input().split())
    if(i==0)and(j==0):
        break;
    x.append(i)
    y.append(j)
X=iter(x)
Y=iter(y)

for a in X:
    b=Y.next()
    if a<b:
        print('%d %d'%(a,b))
    else:
        print('%d %d'%(b,a))
