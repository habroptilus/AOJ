def inputInline():
    N = int(input())
    numbers = list(map(int, input().split(" ")))
    return numbers


def bubbleSort(numbers):
    N = len(numbers)
    count = 0
    flag = True
    while flag:
        flag = False
        for i in range(N - 1):
            if numbers[i] > numbers[i + 1]:
                temp = numbers[i]
                numbers[i] = numbers[i + 1]
                numbers[i + 1] = temp
                flag = True
                count += 1
    return (" ".join(list(map(str, numbers))), count)


result = bubbleSort(inputInline())
print(result[0])
print(result[1])
