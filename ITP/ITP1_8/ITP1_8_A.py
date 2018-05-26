a=raw_input().split(',')
b=[]
c=[]
for i in range(len(a)):
    for j in range(len(a[i])):
        if a[i][j].isalpha():
            if a[i][j].islower():
                b.append(a[i][j].upper())
            else:
                b.append(a[i][j].lower())
        else:
            b.append(a[i][j])
    c.append(''.join(b))
    b=[]
print(','.join(c))
