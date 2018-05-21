N=int(input())
x_a=[0]*N
y_a=[0]*N
r_a=[0]*N
x_b=[0]*N
y_b=[0]*N
r_b=[0]*N
for i in range(N):
    x_a[i],y_a[i],r_a[i],x_b[i],y_b[i],r_b[i]=map(float,input().split())
for i in range(N):
    AB=((x_a[i]-x_b[i])**2+(y_a[i]-y_b[i])**2)**(1/2)
    r_diff=abs(r_a[i]-r_b[i])
    if AB > r_a[i]+r_b[i]:
        print(0)
    elif r_a[i]+r_b[i] >= AB and AB >= r_diff:
        print(1)
    else:
        if r_a[i] > r_b[i]:
            print(2)
        else:
            print(-2)
