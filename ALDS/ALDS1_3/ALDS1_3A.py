comands = input().split()
stack = []
for command in comands:
    if command == "+":
        stack = stack[:-2] + [stack[-1] + stack[-2]]
    elif command == "-":
        stack = stack[:-2] + [stack[-2] - stack[-1]]
    elif command == "*":
        stack = stack[:-2] + [stack[-1] * stack[-2]]
    else:
        stack.append(int(command))
assert len(stack) == 1
print(stack[0])
