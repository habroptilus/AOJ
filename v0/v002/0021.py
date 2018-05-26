ABs=[]
CDs=[]
n = int(input())
for i in range(n):
    x_1, y_1, x_2, y_2, x_3, y_3, x_4, y_4, = map(float, input().split())
    AB = [x_2 - x_1, y_2 - y_1]
    CD = [x_4 - x_3, y_4 - y_3]
    ABs.append(AB)
    CDs.append(CD)
for i in range(n):
    if abs(ABs[i][0]*CDs[i][1]-ABs[i][1]*CDs[i][0])<10**(-10):
        print("YES")
    else:
        print("NO")