# TLEになる。O(n)になっていない？

n, q = map(int, input().split())
queue = []
for i in range(n):
    name, time = input().split()
    queue.append({"name": name, "time": int(time)})
t = 0
while len(queue) != 0:
    #print([queue[i]["time"] for i in range(len(queue))])
    if queue[0]["time"] <= q:
        t += queue[0]["time"]
        name = queue[0]["name"]
        queue.remove(queue[0])
        print("{} {}".format(name, t))
    else:
        queue = queue[1:] + \
            [{"name": queue[0]["name"], "time":queue[0]["time"] - q}]
        t += q
