accum = [0, 31, 60, 91, 121, 152, 182, 213, 244, 274, 305, 335]
youbi = ["Wednesday", "Thursday", "Friday", "Saturday",
         "Sunday", "Monday", "Tuesday", ]


def getYoubi(month, day):
    total = accum[month - 1] + day
    return youbi[total % 7]


month = 13
day = 32

while True:
    month, day = map(int, input().split())
    if month == 0:
        break
    print(getYoubi(month, day))
