count = [0 for i in range(100)]
while True:
    try:
        count[int(input()) - 1] += 1
    except:
        break
max_e = 0
max_i = []
for i in range(100):
    temp = max_e
    max_e = max(count[i], max_e)
    if temp == max_e and count[i] == max_e:
        max_i.append(i + 1)
    elif temp != max_e:
        max_i = [i + 1]
for i in max_i:
    print(i)
